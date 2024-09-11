## 项目背景

随着城市化进程的加快，房地产市场已成为国民经济的重要组成部分。在众多房产交易类型中，二手房交易因其灵活性和选择多样性而受到广泛关注。二手房市场的变化直接反映了房地产市场的供需关系和价格波动，对政策制定者、投资者、购房者以及房产中介等市场参与者具有重要意义。购房者和投资者在做出购买或投资决策时，需要准确、及时的市场信息作为参考。然而，市场上缺乏一个集中、全面且易于使用的平台来提供这些信息。用户迫切需要一个能够提供实时房价数据、历史交易记录、市场趋势分析，并具备强大搜索功能的可视化平台，以辅助他们做出更加明智的决策。一个有效的二手房房价分析和预测平台能够帮助政府及时了解市场供需状况，评估政策效果，为政策制定提供数据支持。尽管市场上已经存在一些提供二手房信息的平台，但大多数平台功能单一，缺乏深度分析和预测功能，且用户体验有待提升。开发一个集数据采集、分析、预测和可视化于一体的综合性平台，能够在竞争激烈的市场中脱颖而出，满足用户多元化的需求。

## 房价预测

![image](https://github.com/user-attachments/assets/8364ee04-ba77-4b14-8cf5-64558d3e3f7f)


![image](https://github.com/user-attachments/assets/6b0dcd85-8b38-4819-8992-fabc8347699e)


## 运行环境

pmdarima django pymysql pandas pillow

numpy 1.26.4

echarts

mysql 8.0

python 3.10

## 运行说明

### 数据库配置

**打开项目文件夹data_processing**

![批注 (1)](https://github.com/user-attachments/assets/f72ebc89-9cc3-49f8-8602-126bd73235c9)

**运行sql_bulider.py**

创建sql架构

![image](https://github.com/user-attachments/assets/b344249f-ef58-4a20-b6dc-fa66dfed6c27)

运行生成的sql文件即可

**数据库配置**

![批注 (2)](https://github.com/user-attachments/assets/478843c6-ed50-4d2e-95c0-cc06449f50ac)

切换至项目根目录

python ./manage runsever

![image](https://github.com/user-attachments/assets/dc993e9a-6659-4597-9538-bbacaa9e7172)

