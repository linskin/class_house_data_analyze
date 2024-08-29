def get_city_data(house_data):
    import pandas as pd
    lon_lat_data = pd.read_csv('static/data/shandong_data.csv')
    citys=list(house_data['城市'].unique())
    city_and_pinyin=[]
    count_city = []
    price_city = []
    geoCoordMap_city = {}
    citys_info = {}
    citys_info1 = {}
    for city in citys:
        house_data_temp=house_data[house_data['城市']==city]
        city_and_pinyin.append({'city':city,'pinyin':house_data_temp['城市拼音'].values[0]})
        count_city.append({'name':city,'value':len(house_data_temp)})
        price_city.append({'name': city, 'value': round(house_data_temp['房价'].mean())})
        citys_info[house_data_temp['城市拼音'].values[0]]=city
        citys_info1[city]=house_data_temp['城市拼音'].values[0]
        lon_lat_city=lon_lat_data[lon_lat_data['地区']==city]
        lon_lat_temp=[lon_lat_city['经度'].values[0],lon_lat_city['纬度'].values[0]]
        geoCoordMap_city[city]=lon_lat_temp
    data={'city_and_pinyin': city_and_pinyin,
          'citys':citys,
          'lon_lat_data': lon_lat_data,
          'count_city': count_city,
          'price_city': price_city,
          'geoCoordMap_city': geoCoordMap_city,
          'citys_info': citys_info,
          'citys_info1': citys_info1,
         }
    return data

