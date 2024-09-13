## 项目背景

随着城市化进程的加快，房地产市场已成为国民经济的重要组成部分。在众多房产交易类型中，二手房交易因其灵活性和选择多样性而受到广泛关注。二手房市场的变化直接反映了房地产市场的供需关系和价格波动，对政策制定者、投资者、购房者以及房产中介等市场参与者具有重要意义。购房者和投资者在做出购买或投资决策时，需要准确、及时的市场信息作为参考。然而，市场上缺乏一个集中、全面且易于使用的平台来提供这些信息。用户迫切需要一个能够提供实时房价数据、历史交易记录、市场趋势分析，并具备强大搜索功能的可视化平台，以辅助他们做出更加明智的决策。一个有效的二手房房价分析和预测平台能够帮助政府及时了解市场供需状况，评估政策效果，为政策制定提供数据支持。尽管市场上已经存在一些提供二手房信息的平台，但大多数平台功能单一，缺乏深度分析和预测功能，且用户体验有待提升。开发一个集数据采集、分析、预测和可视化于一体的综合性平台，能够在竞争激烈的市场中脱颖而出，满足用户多元化的需求。

## 房价预测

![ARIMA预测分析功能文件上传页面](https://github.com/user-attachments/assets/8364ee04-ba77-4b14-8cf5-64558d3e3f7f)

![ARIMA预测分析功能预测结果展示页面](https://github.com/user-attachments/assets/b4d1db2d-fdee-4536-b1cd-fff393b2d756)

![ARIMA预测分析功能邮件发送页面](https://github.com/user-attachments/assets/ad891f4a-0e9a-4ee2-819c-b23953b3e7b2)

注：图表邮件发送使用的是gmail的smtp，使用时注意网络代理（现已改用foxmail，在国内使用无需配置代理）


## 运行环境

`mysql >= 5.0`

`python >= 3.9`

**依赖库导入**

`pip install -r .\requirements.txt`

## 运行说明

### 数据库配置

#### 数据库架构及表格创建

![数据库架构表格结构](https://github.com/user-attachments/assets/b344249f-ef58-4a20-b6dc-fa66dfed6c27)

```sql
create schema house collate latin1_swedish_ci;
create table house_info
(
    城市     varchar(20)  null,
    地区     varchar(20)  null,
    链接     varchar(100) null,
    小区名称 varchar(20)  null,
    所在区域 varchar(20)  null,
    房屋户型 varchar(20)  null,
    所在楼层 varchar(20)  null,
    建筑面积 varchar(20)  null,
    户型结构 varchar(20)  null,
    房屋朝向 varchar(20)  null,
    建筑结构 varchar(20)  null,
    装修情况 varchar(20)  null,
    梯户比例 varchar(20)  null,
    挂牌时间 varchar(20)  null,
    交易权属 varchar(60)  null,
    产权所属 varchar(60)  null,
    抵押信息 varchar(60)  null,
    房价     varchar(50)  null,
    经度     varchar(20)  null,
    纬度     varchar(20)  null,
    核心卖点 varchar(120) null,
    小区介绍 varchar(120) null,
    户型介绍 varchar(120) null,
    交通出行 varchar(50)  null
)
    collate = utf8mb4_unicode_ci;
```

#### 数据填入

**打开项目文件夹data_processing**

![sqlbuilder位置](https://github.com/user-attachments/assets/f72ebc89-9cc3-49f8-8602-126bd73235c9)

**运行sql_bulider.py**

从项目根目录
```python
cd .\data_processing\
python .\sql_bulider.py
```

运行生成的sql文件即可

![生成的sql文件位置](https://github.com/user-attachments/assets/09b5d988-3e53-44c1-9606-56a18074144b)

#### 数据库连接配置

![数据库连接配置](https://github.com/user-attachments/assets/478843c6-ed50-4d2e-95c0-cc06449f50ac)

#### 启动

切换至项目根目录

```python
python ./manage runsever
```

指定端口（如果需要）

```python
python ./manage runsever 0.0.0.0:8000
```

![运行示意图](https://github.com/user-attachments/assets/dc993e9a-6659-4597-9538-bbacaa9e7172)

