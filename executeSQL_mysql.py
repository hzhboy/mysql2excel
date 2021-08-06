# -*- coding:utf-8 -*-
import mysql.connector
# 打开数据库连接（请根据自己的用户名、密码及数据库名称进行修改）
db = mysql.connector.connect(host='localhost',user='root',passwd='12345',database='stulist')
# 使用cursor()方法获取操作游标 
cursor = db.cursor()
# 使用execute方法执行SQL语句
sql = "SELECT*,CASE WHEN sex='m' THEN '男' WHEN sex='f' THEN '女' ELSE 'ccc' END AS aaa FROM ban3;"
try:
    cursor.execute(sql)
    # 使用 fetchone() 方法获取一条数据,再次调用会返回第二条数据
    # data = cursor.fetchone()
    # fetchmany(num)获取num条数据
    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchall()
    print(cursor.rowcount, "条记录")
    for data1 in data:
        print(data1)
    # # 向数据库提交
    # db.commit()

except mysql.connector.Error as e:
    print('connect fails!{}'.format(e))
    # # 发生错误时回滚
    # db.rollback()
    print(cursor.rowcount, "条记录")
# 执行sql语句
db.close()