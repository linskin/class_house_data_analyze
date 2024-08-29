from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.utils.safestring import mark_safe
from data_processing.index_data import get_index_data
from data_processing.get_data import get_sql_data
from data_processing.city_show_data import get_city_data
from data_processing.region_show_data import get_region_data
from data_processing.regionlist_data import get_regionlist_data

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
