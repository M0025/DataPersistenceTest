import xlrd
import xlwt
#读取文件
readWorkbook = xlrd.open_workbook('./rank.xlsx')
readSheets = readWorkbook.sheets()
readSheet = readSheets[0]
nrows = readSheet.nrows
ncols = readSheet.ncols

#写入数据
def writeDataPointsDesc():
    neWorkB = xlwt.Workbook()  #创建工作簿
    writeSheet = neWorkB.add_sheet('newTable')  #创建工作表
    #取表头 写表头
    filds = readSheet.row_values(0)
    for i in range(len(filds)):
        writeSheet.write(0, i, filds[i])
    # 获取数据
    data = []
    for i in range(2, nrows):
        data.append(readSheet.row_values(0))
    print(data)
    cols = len(data[0])
    rows = len(data)
    # 对数据排序
    for i in range(rows - 1):
        for j in range(rows - 1 - i):
            if data[j][2] < data[j + 1][2]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print[data]
    #从第二行开始写入数据
    for i in range(cols):
        for j in range(2, rows+1):
            writeSheet.write(i, j, data[i][j])
    neWorkB.save('/two.xls')

writeDataPointsDesc()
