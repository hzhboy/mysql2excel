# 执行sql，返回数据
def runSQL(sql):
    import mysql.connector
    # 打开数据库连接（请根据自己的用户名、密码及数据库名称进行修改）
    db = mysql.connector.connect(host='localhost',user='root',passwd='12345',database='stulist')
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # 使用execute方法执行SQL语句
    #sql = "SELECT*,CASE WHEN sex='m' THEN '男' WHEN sex='f' THEN '女' ELSE 'ccc' END AS aaa FROM ban3;"
    try:
        cursor.execute(sql)
        # 使用 fetchone() 方法获取一条数据,再次调用会返回第二条数据
        # data = cursor.fetchone()
        # fetchmany(num)获取num条数据
        # 使用 fetchone() 方法获取一条数据
        data = cursor.fetchall()
        print(cursor.rowcount, "条记录")
        # # 向数据库提交
        # db.commit()

    except mysql.connector.Error as e:
        print('connect fails!{}'.format(e))
        # # 发生错误时回滚
        # db.rollback()
        print(cursor.rowcount, "条记录")
    # 执行sql语句
    cursor.close()
    db.close()
    return data

#写excel
def toexcel(data, filename="数据.xlsx"):
    import xlsxwriter as xw
    #新建excel
    workbook  = xw.Workbook(filename, {'constant_memory': True})
    #新建工作薄
    worksheet = workbook.add_worksheet()
    # 写入数据
    for x in range(0, len(data)): #行
        for y in range(0, len(data[0])): #列
            worksheet.write(x, y, data[x][y])
    print("写excel成功，共%d行！" %(len(data)))
    #关闭保存
    workbook.close()

#main
def main():
    data = runSQL("SELECT * FROM `stulist`.`list`;")
    print(data)
    toexcel(data, "数据.xlsx")

if __name__ == '__main__':
    main()