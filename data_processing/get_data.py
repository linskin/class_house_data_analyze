import pandas as pd
from sqlalchemy import create_engine, text
import data_processing.data_category as dc


# 获取MySQL数据
def get_sql_data():
    engine = create_engine('mysql+pymysql://root:123456@localhost:3306/house')
    sql = text('SELECT * FROM house_info')
    connect = engine.connect()
    house_data = pd.read_sql(sql, connect)
    house_data.columns = ['城市', '地区', '链接', '小区名称', '所在区域', '房屋户型', '所在楼层',
                          '建筑面积', '户型结构', '房屋朝向', '建筑结构', '装修情况', '梯户比例', '挂牌时间',
                          '交易权属', '产权所属',
                          '抵押信息', '房价', '经度', '纬度', '核心卖点', '小区介绍', '户型介绍', '交通出行']
    house_data['城市拼音'] = house_data['链接'].apply(
        lambda x: x.replace('http://node4:8000/details?line=/', '').split('/')[0])
    house_data['地区拼音'] = house_data['链接'].apply(
        lambda x: x.replace('http://node4:8000/details?line=/', '').split('/')[1])
    house_data['房价'] = house_data['房价'].astype('int')
    house_data['经度'] = house_data['经度'].astype('float')
    house_data['纬度'] = house_data['纬度'].astype('float')
    house_data['总价'] = round(
        house_data['建筑面积'].apply(lambda x: float(x.replace('㎡', ''))) * house_data['房价'] / 10000, 2)
    house_data['总价'] = house_data['总价'].apply(lambda x: str(x) + '万')
    house_data['面积分类'] = house_data['建筑面积'].apply(dc.area_category)
    house_data['抵押分类'] = house_data['抵押信息'].apply(dc.diya_category)
    house_data['楼层分类'] = house_data['所在楼层'].apply(dc.floor_category)
    house_data['房价分类'] = house_data['总价'].apply(dc.price_category)
    house_data['城市'] = house_data['城市'].apply(lambda x: x + '市')
    return house_data
