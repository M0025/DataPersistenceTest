import xlrd
from xlutils.copy import copy

def reoutData(howManyRows):
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

    if howManyRows > len(data):
        print("没有那么多！")
    else:
        #对数据进行排序
        for i in range(len(data) - 1):
            for j in range(len(data) - 1 - i):
                if data[j][2] < data[j + 1][2]:
                    data[j], data[j + 1] = data[j + 1], data[j]

        writeWorkbook = copy(readWorkbook)
        ws = writeWorkbook.get_sheet(1)
        for i in range(len(fileds)):  #写表头
            ws.write(0, i, fileds[i])

        for i in range(howManyRows):   #写内容
            for j in range(ncols):
                ws.write(i+1, j, data[i][j])
        writeWorkbook.save('./rank.xls')

reoutData(4)


