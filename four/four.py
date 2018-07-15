import pymysql
import xlwt
conn = pymysql.connect(host='localhost', user='root', passwd='123456', db='movies')
cur = conn.cursor()

cur.execute("insert into movieRank value('犬之岛','617.35','9.08','2','1309.09')")
cur.execute("insert into movieRank value('湮灭','135.34','1.99','9','5556.77')")
conn.commit()

#(2):
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

