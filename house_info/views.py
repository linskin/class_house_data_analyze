import pandas as pd
from django import forms
from django.shortcuts import render
from django.utils.safestring import mark_safe
from pmdarima import auto_arima  # 导入自动ARIMA选择方法
from django.shortcuts import render
from .forms import ARIMAForm
from data_processing.city_show_data import get_city_data
from data_processing.get_data import get_sql_data
from data_processing.index_data import get_index_data
from data_processing.region_show_data import get_region_data
from data_processing.regionlist_data import get_regionlist_data

# from statsmodels.tsa.arima_model import ARIMA

# Create your views here.

house_data = get_sql_data()


def login(request):
    big_screen_data = get_index_data(house_data)
    return render(request, 'index.html', {
        "all_map_data": mark_safe(big_screen_data['all_map_data']),
        "second_map_data": mark_safe(big_screen_data['second_map_data']),
        "price_mean": mark_safe(big_screen_data['price_mean']),
        "all_data": mark_safe(big_screen_data['all_data']),
        "year_data": mark_safe(big_screen_data['year_data']),
        "word_data": mark_safe(big_screen_data['word_data']),
    })


def map_sample(request):
    return render(request, 'map_refer.html')


def word_sample(request):
    return render(request, 'wordcloud_refer.html')


def city_show(request):
    city_data = get_city_data(house_data)
    return render(request, 'city_show.html', {
        "city_and_pinyin": city_data['city_and_pinyin'],
        "citys": mark_safe(city_data['citys']),
        "count_city": mark_safe(city_data['count_city']),
        "price_city": mark_safe(city_data['price_city']),
        "geoCoordMap_city": mark_safe(city_data['geoCoordMap_city']),
        "citys_info1": mark_safe(city_data['citys_info1']),
    })


def region_show(request, city):
    region_data = get_region_data(house_data, city)
    return render(request, 'region_show.html', {
        "regions_data": region_data['region_get_data'],
        "city": city,
        "city_name": region_data['city_name'],
        "count_region": mark_safe(region_data['count_region']),
        "price_region": mark_safe(region_data['price_region']),
        "geoCoordMap_region": mark_safe(region_data['geoCoordMap_region']),
        "regions": mark_safe(region_data['regions']),
        "region_info": mark_safe(region_data['region_info'])

    })


def region_list(request, region_select):
    select_list = request.GET.getlist("select_list")
    regionlist_get_data = get_regionlist_data(house_data, region_select, select_list)
    return render(request, 'region_list.html', {
        "city_pinyin": regionlist_get_data['city_pinyin'],
        "city_name": regionlist_get_data['city_name'],
        "region_name": regionlist_get_data['region_name'],
        "region_select": regionlist_get_data['region_select'],
        "select_data": regionlist_get_data['select_data'],
        "house_list_dict": mark_safe(regionlist_get_data['house_list_dict']),
        "show_counts": regionlist_get_data['show_counts'],
        "select_list": list(regionlist_get_data['select_list']),
    })


def table_demo(request):
    return render(request, 'table_refer.html')


def detail_show(request):
    detail_select = request.GET.get('detail')
    house_data.fillna('未知', inplace=True)
    detail_data_temp = house_data[house_data['链接'] == detail_select]
    detail_data = detail_data_temp.to_dict(orient='records')[0]
    up_link = detail_data['城市拼音'] + '/' + detail_data['地区拼音']
    return render(request, 'detail.html',
                  {'detail_data': detail_data,
                   'up_link': up_link,
                   })

def plot_arima_forecast(request):
    """
    处理用户上传的文件，使用自动选择的ARIMA模型对时间序列数据进行拟合和预测，并将数据传递给前端进行可视化。
    """
    if request.method == 'POST':
        form = ARIMAForm(request.POST, request.FILES)
        if form.is_valid():
            # 获取上传的文件和预测步数
            uploaded_file = request.FILES['file']
            steps = form.cleaned_data['steps']

            try:
                # 读取数据
                data = pd.read_csv(uploaded_file, index_col='日期', parse_dates=True)

                # 只取‘房屋单价’
                data = data[['房屋单价']]

                # data = data['房屋单价']

                data.columns = ['数值']

                # 设置索引频率为月初（MS）
                data.index.freq = 'MS'

                # 使用 auto_arima 自动选择最佳 ARIMA 模型
                model = auto_arima(data['数值'], seasonal=False, trace=True, stepwise=True, error_action='ignore')

                # 预测未来steps个时间点
                forecast = model.predict(n_periods=steps)

                fitted_values = model.predict_in_sample()  # 获取拟合值
                fitted_values.iloc[0] = data['数值'].iloc[0]
                fitted_values.iloc[1] = data['数值'].iloc[1]
                fitted_values.iloc[2] = data['数值'].iloc[2]

                fitted_values = pd.Series(fitted_values, index=data.index)  # 将拟合值转换为时间序列

                # 创建预测值的索引并转换为Series
                forecast_index = pd.date_range(start=fitted_values.index[-1], periods=steps + 1, freq='MS')
                forecast_series = pd.Series(forecast, index=forecast_index[1:])  # 跳过重叠部分

                # 将数据转换为字典格式，传递给前端
                context = {
                    'dates': list(data.index.strftime('%Y-%m')),  # 日期
                    'actual_values': list(data['数值']),  # 实际值
                    'fitted_values': list(fitted_values),  # 拟合值
                    'forecast_dates': list(forecast_series.index.strftime('%Y-%m')),  # 预测的日期
                    'forecast_values': list(forecast_series),  # 预测值
                }

                return render(request, 'arima_forecast.html', context)

            except Exception:
                # 处理其他异常并将其传递到前端
                return render(request, 'arima_form.html', {'form': form,
                                                           'message': ['发生错误：文件不符合标准格式','标准格式：表数据须含有‘日期’和‘房屋单价‘两列','文件大小不超过5MB']})
    else:
        form = ARIMAForm()

    return render(request, 'arima_form.html', {'form': form})