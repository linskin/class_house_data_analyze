def get_region_data(house_data, city_get):
    import pandas as pd

    house_data_temp = house_data[house_data['城市拼音'] == city_get]
    regions = house_data_temp['地区'].unique()
    region_get_data = []
    city_name = house_data_temp['城市'].values[0]

    lon_lat_data = pd.read_csv('static/data/shandong_data.csv')
    lon_lat_data_city = lon_lat_data[lon_lat_data['城市'] == city_name]
    count_region = []
    price_region = []
    geoCoordMap_region = {}
    region_info = {}

    for region in regions:
        house_data_region = house_data_temp[house_data_temp['地区'] == region]
        region_data_dict = {'region': region, 'list_link': city_get + '/' + house_data_region['地区拼音'].values[0]}
        region_get_data.append(region_data_dict)
        lon_lat_data_region = lon_lat_data_city[lon_lat_data_city['地区'] == region]
        region_adjust = lon_lat_data_region['地图中的地区'].values[0]
        count_region_dict = {'name': region_adjust, 'value': len(house_data_region)}
        price_region_dict = {'name': region_adjust, 'value': round(house_data_region['房价'].mean())}
        count_region.append(count_region_dict)
        price_region.append(price_region_dict)
        geoCoordMap_region[region_adjust] = [lon_lat_data_region['经度'].values[0],
                                             lon_lat_data_region['纬度'].values[0]]
        region_info[region_adjust] = house_data_region['地区拼音'].values[0]

    data = {
        'region_get_data': region_get_data,
        'city_name': city_name,
        'count_region': count_region,
        'price_region': price_region,
        'geoCoordMap_region': geoCoordMap_region,
        'region_info': region_info,
        'regions': list(regions)
    }
    return data
