import csv
from pymongo import MongoClient
conn = MongoClient('localhost')
db = conn.building
coll = db.room

#读取数据
def readData(csvName):
    data, datas = [],[]
    with open(csvName,'r') as newData:
        read = csv.reader(newData)
        for i in read:
            data.append(i)
    fields = data[0]
    for i in range(2,len(data)):
        datas.append(data[i])
    print(datas)
    insertInto = []
    for i in range(len(datas)):
        collection = dict(zip(fields,datas[i]))
        insertInto.append(collection)
    return (insertInto)

coll.insert_many(readData('./rooms.csv'))

print(readData('./rooms.csv'))
