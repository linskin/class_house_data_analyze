def get_index_data(house_data):
    import numpy as np
    import pandas as pd

    #map_data & treemap_data
    province_data = pd.read_csv('static/data/province_data.csv')
    province_data.fillna(0, inplace=True)
    province_data['总房源'] = province_data['二手房'] + province_data['新房'] + province_data['租房']
    provinces = province_data['省份'].unique()
    all_map_data = []
    second_map_data = []
    all_data = []
    for province in provinces:
        province_data_temp = province_data[province_data['省份'] == province]
        all_map_data.append({'name': province, 'value': np.sum(province_data_temp['总房源'])})
        second_map_data.append({'name': province, 'value': np.sum(province_data_temp['二手房'])})
        citys_temp = province_data_temp['城市'].unique()
        children = []
        for city in citys_temp:
            house_data_temp = province_data_temp[province_data_temp['城市'] == city]
            city_temp_dict = {'name': city, 'value': np.sum(house_data_temp['总房源'])}
            children.append(city_temp_dict)
        province_dict = {'name': province, 'value': np.sum(province_data_temp['总房源']), 'children': children}
        all_data.append(province_dict)
    # bar_data
    price_mean_group = house_data.groupby('城市')['房价'].mean()
    price_mean = [list(price_mean_group.index), list(np.round(price_mean_group.values))]
    #line_data
    house_data['挂牌年份'] = house_data['挂牌时间'].apply(lambda x: x[:4] + "年")
    year_group = house_data.groupby('挂牌年份')['城市'].count()
    year_data = {'year': list(year_group.index), 'house_count': list(year_group.values)}

    #cloud_data
    important_data = pd.read_csv('static/data/feat_importances.csv', encoding='utf-8')
    important_data.columns = ['features', 'importance']
    feat_dict = {'city': '城市',
                 'region': '地区',
                 'huxing': '房屋户型',
                 'louceng': '所在楼层',
                 'mianji': '建筑面积',
                 'huxingjiegou': '户型结构',
                 'chaoxiang': '房屋朝向',
                 'jianzhujiegou': '建筑结构',
                 'zhuangxiu': '装修情况',
                 'tihu': '梯户比例',
                 'quanshu': '交易权属',
                 'chanquan': '产权所属',
                 'diya': '抵押信息'}
    important_data['features'] = important_data['features'].map(feat_dict)
    word_data = []
    for i in range(len(important_data)):
        word_data_temp = {}
        word_data_temp['name'] = important_data.iloc[i, 0]
        word_data_temp['value'] = important_data.iloc[i, 1]
        word_data.append(word_data_temp)

    data = {'all_map_data': all_map_data,
            'second_map_data': second_map_data,
            'price_mean': price_mean,
            'all_data': all_data,
            'year_data': year_data,
            'word_data': word_data,

            }
    return data
