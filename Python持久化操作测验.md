# Python持久化操作测验

标签： Python

---
xlwt,openpyxl,xlrd
## 第一题
现有如下图1所示的data.csv文件数据，请使用python读取该csv文件数据，并添加一条记录后输出如图2所示的output.csv文件（10分）
原数据：

|name|stuNo|
|--|--|
|ZhangSan|101|
|LiSi|102|
|WangWu|103|

目标结果：

|name|stuNo|
|--|--|
|ZhangSan|101|
|LiSi|102|
|WangWu|103|
|Jack|104|

读取csv，加一条数据，然后再输出
思路：需要导入csv模块，然封装两个函数，功能分别为读取和插入。

- 定义读取函数：
```python
import csv  # 导入csv模块
#读取数据
def readData(csvName):   #参数为带路径及文件名后缀的文件名
    with open(csvName,'r') as newData:   #'r' 表示读
        read = csv.reader(newData)
        for i in read:
            print(i)
readData('./data.csv')
```

- 定义插入函数：

一次失败的尝试：
```python
#写入数据
def writeData(csvName,*data):
    with open(csvName,'w') as newData2:
        writer = csv.writer(newData2)
        writer.writerow(data)
```
写完之后数据都覆盖了 尴尬

这回把原来的数据读出来，再加上新数据，然后重新写入。
```python
import csv

#读取数据
def readData(csvName):
    with open(csvName, 'r') as newData:
        read = csv.reader(newData)
        data = []
        for i in read:
            data.append(i)
    return data
print(readData('./data.csv'))

#写入数据
def writeData(csvName, *data):
    insertInto = readData(csvName)  #读取原数据放在insertInto中
    insertInto.append(list(data))   #将要插入的数据加在原数据后面 不定长参数传入的是个元组，转换一下
    with open(csvName, 'w', newline='') as writeCSV:  #写入没有空行 
        writeSheet = csv.writer(writeCSV)
        writeSheet.writerows(insertInto)
writeData('./data.csv', 'Jack', '104')
print(readData('./data.csv'))

```
## 第二题
如下所示的Excel表格数据，请编写python代码筛选出Points大于5的数据，并按Points进行排序后输出如图2所示的Excel文件结果（20分）
**原图：**

|Rank| Team | Points|
|--|--|--|
|1|Russia|12|
|2|Japan|6|
|3|South Korea| 9|
|4|Cameroon|1|
|5|Argentina|2|
|6|Brazil|15|

**结果：**

|Rank| Team | Points|
|--|--|--|
|6|Brazil|15|
|1|Russia|12|
|3|South Korea| 9|
|2|Japan|6|

```python
import xlrd
from xlutils.copy import copy

def reoutData(howManyRows):  #函数参数为需要前多少行的数据
    #读取文件
    readWorkbook = xlrd.open_workbook('./rank.xlsx')
    readSheets = readWorkbook.sheets()
    readSheet = readSheets[0]
    nrows = readSheet.nrows
    ncols = readSheet.ncols
    fileds = readSheet.row_values(0)   #获取表头

    data = []
    for i in range(1, nrows):
        myRowValues = readSheet.row_values(i)
        data.append(myRowValues)     #获取数据存在Data列表里

    if howManyRows > len(data):   #如果参数大于数据量
        print("没有那么多！")
    else:
        #对数据进行排序  冒泡了
        for i in range(len(data) - 1):
            for j in range(len(data) - 1 - i):
                if data[j][2] < data[j + 1][2]:
                    data[j], data[j + 1] = data[j + 1], data[j]

        writeWorkbook = copy(readWorkbook)  #用xlutils来复制一份工作簿
        ws = writeWorkbook.get_sheet(1)
        for i in range(len(fileds)):  #写表头
            ws.write(0, i, fileds[i])

        for i in range(howManyRows):   #写内容
            for j in range(ncols):
                ws.write(i+1, j, data[i][j])
        writeWorkbook.save('./rank.xls')python

reoutData(4)
```
输出结果即为上表。

## 第三题
请用sql语句完成以下需求（30分）
（1）使用sql创建出如下图所示的数据表，数据库名为movies，表名为movieRank，表中包含MovieName、boxOffice、percent、days、totalBoxOffice五个字段，字段的信息如下图所示：

|名|类型|长度|小数点|不是null|主键|
|--|--|--|---|----|---|
|MovieName|varchar|255|0|not null|primaryKey|
|boxOffie|float|0|0|not null||
|percent|float|0|0|not null||
|days|int|0|0|not null||
|totalBoxOffice|float|0|0|not null||


（2）使用sql语句向movieRank表中添加若干条数据（材料中已提供movieData.txt）
（3）使用sql语句查询movieRank表中的数据并按照totalBoxOffice字段进行排序
（4）使用sql语句计算出字段totalBoxOffice字段的总和

```sql
--创建新表
create table movieRank(
moviename varchar(255),
boxOffice float,
percent float,
days int(11),
totalBoxOffice float);

--添加数据
insert into movieRank values
('21克拉','1031.92','15.18', '2', '2827.06'),
('狂暴巨兽','2928.28','43.07','9','57089.20'),
('起跑线','161.03','2.37','18','19873.43'),
('头号玩家','1054.87','15.52','23','127306.41'),
('红海行动','45.49','0.67','65','364107.74');

--按票房排序
select * from movieRank ORDER BY totalBoxOffice;

--票房总和
select sum(totalBoxOffice) from movieRank 
```
结果：
（2）：

|moviename|boxOffice|percent|days|totalBoxOffice
|--|--|--|
|21克拉|1031.92|15.18|2|2827.06|
|狂暴巨兽|2928.28|43.07%|9|57089.20
|起跑线|161.03|2.37%|18|19873.43
|头号玩家|1054.87|15.52%|23|127306.41
|红海行动|45.49|0.67%|65|364107.74

 (3):
 
|MovieName|boxOffice|percent|days|totalBoxOffice|
|---|---|---|--|--|
|21克拉|1031.92|15.18%|2|2827.06
|起跑线|161.03|2.37%|18|19873.43
|狂暴巨兽|2928.28|43.07%|9|57089.20
|头号玩家|1054.87|15.52%|23|127306.41
|红海行动|45.49|0.67%|65|364107.74

 (4):
 
 |sum(totalBoxOffice)|
 |--|
 |578069.7052001953|


## 第四题

此题接第3题题干，在第三提的基础上完成以下需求：（20分）
（1）编写python代码连接mysql数据库，并向movieRank表中新添加两条数据（已提供second.txt）

```python
import pymysql  #导入pymysql模块，Python操作数据库
import xlwt 
#链接数据库
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='movies')
cur = conn.cursor()

cur.execute("insert into movieRank value('犬之岛','617.35','9.08','2','1309.09')")
cur.execute("insert into movieRank value('湮灭','135.34','1.99','9','5556.77')")
conn.commit()
```

（2）编写python代码，查询出所有的电影数据，并输出到一个Excel表movieRank.xlsx中,如下图所示

|MovieName|boxOffice|percent|days|totalBoxOffice|
|---|---|---|--|--|
|21克拉|1031.92|15.18%|2|2827.06
|狂暴巨兽|2928.28|43.07%|9|57089.20
|起跑线|161.03|2.37%|18|19873.43
|头号玩家|1054.87|15.52%|23|127306.41
|红海行动|45.49|0.67%|65|364107.74
|犬之岛|617.35|9.08%|2|130.09|
|湮灭|135.34|1.99%|9|5556.77|

```python
#(2): (接上题)
tableName = 'movieRank'

def sql2xlsx(t_Name):
    sql = "select * from %s"
    cur.execute(sql % t_Name)
    result = cur.fetchall()
    fields = cur.description

    sql2xlx = xlwt.Workbook()  #创建工作簿
    sheet = sql2xlx.add_sheet(tableName)  #创建工作表
    for i in range(len(fields)):
        sheet.write(0, i, fields[i][0])   #第一行第i列写入表头信息'
    for i in range(len(fields)):          #写入表信息
        for j in range(1,len(result)+1):
            sheet.write(j,i,result[j-1][i])
    sql2xlx.save('./sql2xlx.xls')      # 保存Excel文件
    print("ok")

sql2xlsx(tableName)
```
输出结果即为上表。
## 第五题
请编写python代码，使用相关模块完成以下需求：（20分）
（1）编写python代码连接MongoDB数据库，并新建一个building库，在building库下新建一个rooms表
（2）编写python代码读取rooms.csv文件的中的数据，并将数据插入到rooms表中，添加到rooms表中的数据结构如下图所示。

```python
import csv
from pymongo import MongoClient   #导入模块
conn = MongoClient('localhost')  
db = conn.building
coll = db.room     # 链接数据库，创建新集合

#读取数据
def readData(csvName):
    data, datas = [],[]
    with open(csvName,'r') as newData:
        read = csv.reader(newData)
        for i in read:
            data.append(i)
    fields = data[0]
    for i in range(2,len(data)):  #获取表头
        datas.append(data[i])
    print(datas)
    insertInto = []
    for i in range(len(datas)):  #获取表中数据，放到insertInto列表中。
        collection = dict(zip(fields,datas[i]))  #用zip函数把数据压成键值对形式。
        insertInto.append(collection)
    return (insertInto)       

coll.insert_many(readData('./rooms.csv'))

print(readData('./rooms.csv'))
```
数据库中的结果：
>\> db.room.find()
{ "_id" : ObjectId("5b481ef29ae44b0e3cd9247f"), "RoomID" : "101", "Floor" : "1", "Use" : "Retail", "Square Footage" : "1900", "Capacity" : "25", "Price" : "3000" }

{ "_id" : ObjectId("5b481ef29ae44b0e3cd92480"), "RoomID" : "102", "Floor" : "1", "Use" : "Retail", "Square Footage" : "1850", "Capacity" : "25", "Price" : "3000" }

{ "_id" : ObjectId("5b481ef29ae44b0e3cd92481"), "RoomID" : "103", "Floor" : "1", "Use" : "Restroom", "Square Footage" : "250", "Capacity" : "0", "Price" : "0" }

{ "_id" : ObjectId("5b481ef29ae44b0e3cd92482"), "RoomID" : "104", "Floor" : "1", "Use" : "Maintenance", "Square Footage" : "150", "Capacity" : "0", "Price" : "0" }

{ "_id" : ObjectId("5b481ef29ae44b0e3cd92483"), "RoomID" : "200", "Floor" : "2", "Use" : "Studio", "Square Footage" : "875", "Capacity" : "2", "Price" : "850" }

{ "_id" : ObjectId("5b481ef29ae44b0e3cd92484"), "RoomID" : "201", "Floor" : "2", "Use" : "Studio", "Square Footage" : "734", "Capacity" : "2", "Price" : "850" }

{ "_id" : ObjectId("5b481ef29ae44b0e3cd92485"), "RoomID" : "202", "Floor" : "2", "Use" : "Studio", "Square Footage" : "624", "Capacity" : "2", "Price" : "850" }

{ "_id" : ObjectId("5b481ef29ae44b0e3cd92486"), "RoomID" : "203", "Floor" : "2", "Use" : "Studio", "Square Footage" : "624", "Capacity" : "2", "Price" : "850" }
