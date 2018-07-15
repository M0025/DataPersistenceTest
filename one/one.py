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
    insertInto.append(list(data))   #将要插入的数据加在原数据后面
    with open(csvName, 'w', newline='') as writeCSV:  #写入没有空行
        writeSheet = csv.writer(writeCSV)
        writeSheet.writerows(insertInto)
writeData('./data.csv', 'Jack', '104')
print(readData('./data.csv'))
