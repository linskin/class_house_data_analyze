import datetime
import random

from pypinyin import pinyin, lazy_pinyin

regions = []


#
#
def add_region(city, region, longitude, latitude):
    region_data = {
        "city": city,
        "region": region,
        "longitude": longitude,
        "latitude": latitude
    }
    regions.append(region_data)


#
#
with open("../static/data/shandong_data.csv", encoding='utf-8') as f:
    region_sub = f.readlines()

for sub in region_sub[1:]:
    sub = sub.replace('\n', '')
    list_sub = sub.split(',')
    add_region(list_sub[0], list_sub[1], list_sub[3], list_sub[4])


# Generate random house data
def pinyin(text):
    return ''.join(lazy_pinyin(text))


def generate_random_house_data(region):
    house_types = ["1室1厅", "2室1厅", "2室2厅", "3室1厅", "3室2厅", "4室2厅"]
    orientations = ["东", "南", "西", "北", "南北", "东西"]
    structures = ["砖混结构", "钢混结构", "框架结构"]
    decorations = ["毛坯", "简装修", "精装修"]
    core_points = ["位置优越，生活便利", "环境好，适合居住", "周边设施齐全，交通便捷", "社区安静宜居，绿化充足",
                   "交通便利", ]
    floors = ["低层", "中层", "高层"]
    elevator_occupancy_ratio = ["1梯2户", "2梯4户"]
    transaction_rights_types = ["商品房", "非商品房", "经济适用房"]
    property_rights_types = ["个人产权", "企业产权", "国家产权"]
    mortgage_info_types = ["无抵押", "有抵押"]
    house_structure_types = ["平层", "错层", "复式", "别墅"]
    community_name_types = ["名优住宅", "小区", "公寓", "华庭"]
    area_name_types = ["街道", "社区", "商业区", "商业街", "新区", "开发区"]

    house = {
        "city": region["city"],
        "region": region["region"],
        "link": f"http://node4:8000/details?line=/{pinyin(region['city'][:-1])}/{pinyin(region['region'][:-1])}",
        "community_name": f"{region['region']}" + f"{random.choice(community_name_types)}",
        "area_name": f"{region['region']}街道" + f"{random.choice(area_name_types)}",
        "house_type": random.choice(house_types),
        "floor": random.choice(floors),
        "building_area": f"{random.randint(60, 150)}㎡",
        "house_structure": random.choice(house_structure_types),
        "house_orientation": random.choice(orientations),
        "building_structure": random.choice(structures),
        "decoration_condition": random.choice(decorations),
        "ladder_ratio": random.choice(elevator_occupancy_ratio),
        # "listing_date": str(datetime.date(2024, random.randint(1, 12), random.randint(1, 28))),
        "listing_date": str(datetime.date(random.randint(2019, 2024), random.randint(1, 12), random.randint(1, 28))),
        "transaction_rights": random.choice(transaction_rights_types),
        "property_rights": random.choice(property_rights_types),
        "mortgage_info": random.choice(mortgage_info_types),
        "price": random.randint(7000, 25000),
        "longitude": region["longitude"],
        "latitude": region["latitude"],
        "core_points": random.choice(core_points),
        "community_info": "小区环境优美，适宜居住",
        "house_intro": "户型方正，南北通透",
        "traffic_info": "交通便捷，出行便利"
    }

    return house


# Generate SQL for each region
for region in regions:
    for _ in range(2):  # Generate at least two entries per region
        house = generate_random_house_data(region)
        sql = f"""INSERT INTO house_info 
        (城市, 地区, 链接, 小区名称, 所在区域, 房屋户型, 所在楼层, 建筑面积, 户型结构, 房屋朝向, 建筑结构, 装修情况, 梯户比例, 挂牌时间, 
        交易权属, 产权所属, 抵押信息, 房价, 经度, 纬度, 核心卖点, 小区介绍, 户型介绍, 交通出行)
        VALUES ('{house["city"][:-1]}', '{house["region"]}', '{house["link"]}', '{house["community_name"]}', 
        '{house["area_name"]}', '{house["house_type"]}', '{house["floor"]}', '{house["building_area"]}', 
        '{house["house_structure"]}', '{house["house_orientation"]}', '{house["building_structure"]}', 
        '{house["decoration_condition"]}', '{house["ladder_ratio"]}', '{house["listing_date"]}', 
        '{house["transaction_rights"]}', '{house["property_rights"]}', '{house["mortgage_info"]}', 
        '{house["price"]}', '{house["longitude"]}', '{house["latitude"]}', '{house["core_points"]}', 
        '{house["community_info"]}', '{house["house_intro"]}', '{house["traffic_info"]}');
        """
        print(sql)
        with open("../static/data/sql_data.sql", "a", encoding='utf-8') as f:
            f.write(sql + "\n")
