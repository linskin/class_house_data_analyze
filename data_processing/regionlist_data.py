def get_regionlist_data(house_data, region_select, select_list):
    import numpy as np
    city_pinyin = region_select.split('/')[0]
    region_pinyin = region_select.split('/')[1]
    house_data.fillna('未知', inplace=True)
    house_data_temp = house_data[(house_data['城市拼音'] == city_pinyin) & (house_data['地区拼音'] == region_pinyin)]
    city_name = house_data_temp['城市'].values[0]
    region_name = house_data_temp['地区'].values[0]
    select_data = {"装修情况": house_data_temp['装修情况'].unique(),
                   "楼层分类": house_data_temp['楼层分类'].unique(),
                   "产权所属": house_data_temp['产权所属'].unique(),
                   "抵押分类": house_data_temp['抵押分类'].unique(),
                   "面积分类": house_data_temp['面积分类'].unique(),
                   "房价分类": house_data_temp['房价分类'].unique()
                   }
    if select_list is None:
        select_list = [0, 0, 0, 0, 0, 0]
    else:
        select_columns = ['装修情况', '楼层分类', '产权所属', '抵押分类', '面积分类', '房价分类']
        select_list = np.array([int(i) for i in select_list])
        select_count = np.sum(select_list > 0)
        if select_count > 0:
            condition = ''
            init_value = 1
            for i in range(len(select_list)):
                if select_list[i] > 0:
                    if init_value < select_count:
                        condition += "(house_data_temp[select_columns[%d]]==select_data[select_columns[%d]][select_list[%d]-1]) & " % (
                            i, i, i)
                        init_value += 1
                    else:
                        condition += "(house_data_temp[select_columns[%d]]==select_data[select_columns[%d]][select_list[%d]-1])" % (
                            i, i, i)
            house_data_temp = house_data_temp[eval(condition)]
    show_counts = 15 if len(house_data_temp) >= 15 else len(house_data_temp)
    house_list_dict = {'mingcheng': list(house_data_temp['小区名称'].values),
                       'suozaiquyu': list(house_data_temp['所在区域'].values),
                       'jiegou': list(house_data_temp['户型结构'].values),
                       'zhuangxiu': list(house_data_temp['装修情况'].values),
                       'huxing': list(house_data_temp['房屋户型'].values),
                       'chaoxiang': list(house_data_temp['房屋朝向'].values),
                       'louceng': list(house_data_temp['所在楼层'].values),
                       'chanquan': list(house_data_temp['产权所属'].values),
                       'diya': list(house_data_temp['抵押信息'].values),
                       'mianji': list(house_data_temp['建筑面积'].values),
                       'danjia': list(house_data_temp['房价'].values),
                       'zongjia': list(house_data_temp['总价'].values),
                       'shijian': list(house_data_temp['挂牌时间'].values),
                       'lianjie': list(house_data_temp['链接'].values),
                       }

    data = {'city_pinyin': city_pinyin,
            'city_name': city_name,
            'region_name': region_name,
            'region_select': region_select,
            'select_data': select_data,
            'house_list_dict': house_list_dict,
            'show_counts': show_counts,
            'select_list': select_list
            }
    return data
