def area_category(area_data):
    area = float(area_data.replace('㎡', ''))
    if area < 50:
        return "50㎡以下"
    elif area < 70:
        return "50-70㎡"
    elif area < 90:
        return "70-90㎡"
    elif area < 110:
        return "90-110㎡"
    elif area < 130:
        return "110-130㎡"
    elif area < 150:
        return "130-150㎡"
    else:
        return "150㎡以上"


def diya_category(diya_data):
    if '有抵押' in diya_data:
        return "有抵押"
    elif '无抵押' in diya_data:
        return "无抵押"
    else:
        return "暂无数据"


def floor_category(floor_data):
    if '高楼层' in floor_data:
        return "高楼层"
    elif '中楼层' in floor_data:
        return "中楼层"
    elif '低楼层' in floor_data:
        return "低楼层"
    else:
        return "地下室"


def price_category(price_data):
    total_price = float(price_data.replace('万', ''))
    if total_price < 50:
        return "50万以下"
    elif total_price < 80:
        return "50-80万"
    elif total_price < 100:
        return "80-100万"
    elif total_price < 150:
        return "100-150万"
    elif total_price < 2000:
        return "150-200万"
    else:
        return "200万以上"
