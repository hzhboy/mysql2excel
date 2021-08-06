# (1) 对于2003版本的xls文件，最大行数是65536行
# (2) 对于2007版本的xlsx文件，最大行数是1048576行
#     XlsxWriter支持excel工作表最大1048576行记录，16384条列记录，超出可以选择再建新sheet

# # xlrd读
# import xlrd # 不支持excel2007的xlsx格式
# book = xlrd.open_workbook('读11.xls')
# sheet1 = book.sheets()[0]
# nrows = sheet1.nrows
# print('表格总行数',nrows)
# ncols = sheet1.ncols
# print('表格总列数',ncols)
# row3_values = sheet1.row_values(2)
# print('第3行值',row3_values)
# col3_values = sheet1.col_values(2)
# print('第3列值',col3_values)
# cell_3_3 = sheet1.cell(2,2).value
# print('第3行第3列的单元格的值：',cell_3_3)

# # xlwt写
# import random
# import xlwt # 不支持excel2007的xlsx格式
# workbook = xlwt.Workbook(encoding = 'utf-8')
# worksheet = workbook.add_sheet('guess')
# # 5行（m） x 10列(n)
# for m in range(60000):
#     for n in range(10):
#         str1 = random.choice('abcdef')
#         worksheet.write(m, n, str1)
#     if (m % 10000 == 9999):
#         print('已写入%d行...' % (m + 1))
# workbook.save('写22.xls')
# print("写excel成功，共%d行！" %(m+1))

# # openpyxl读
# import openpyxl
# workbook = openpyxl.load_workbook('读11.xlsx', read_only=True) #只读模式，性能更好
# workbook = openpyxl.load_workbook('读11.xlsx')
# worksheet = workbook['Sheet1']
# row3=[item.value for item in list(worksheet.rows)[2]]
# print('第3行值',row3)
# col3=[item.value for item in list(worksheet.columns)[2]]
# print('第3列值',col3)
# cell_2_3=worksheet.cell(row=2,column=3).value
# print('第2行第3列值',cell_2_3)
# print(worksheet.max_row)# 最大行
# print(worksheet.max_column)#最大列
# mrow = worksheet.max_row
# mcol = worksheet.max_column
# for x in range(1, mrow + 1):
#     print("第%d行：" %x)
#     for y in range(1, mcol + 1):
#         print("    第%d列" %y)
#         cell = worksheet.cell(row=x, column=y).value
#         print('           %s' %cell)

# # openpyxl写
# import openpyxl
# import random
# workbook = openpyxl.Workbook()
# sheet=workbook.active
#
# for n in range(10000):
#     str2 = []
#     for m in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
#         str1 = random.choice('abcdef')
#         xy = '%s%d' %(m, n+1)
#         str2.append(str1)
#         # # 写入方法一：单元格逐个写入[A1]
#         # sheet[xy] = str1
#     # # 写入方法二：单元格逐个写入[1,1]
#     # for m in range(10):
#     #     str1 = random.choice('abcdef')
#     #     sheet.cell(n+1, m+1, str1)
#     # 写入方法三：['zhangsan','lisi','wangwu']列表逐行append写入
#     sheet.append(str2)
#     if (n % 1000 == 999):# 进度判断
#         print('已写入%d行...' % (n + 1))
# workbook.save('写22.xlsx')
# print("写excel成功，共%d行！" %(n+1))

# import xlsxwriter as xw
# import random
# #新建excel
# workbook  = xw.Workbook('写22.xlsx', {'constant_memory': True})
# #新建工作薄
# worksheet = workbook.add_worksheet()
#
# for m in range(10000):
#     for n in range(10):
#         str1 = random.choice('abcdef')
#         # 写入数据
#         # worksheet.write('A1', 1)
#         worksheet.write(m, n, str1)
#     if (m % 10000 == 9999):
#         print('已写入%d行...' % (m + 1))
# print("写excel成功，共%d行！" %(m+1))
# #关闭保存
# workbook.close()

# # 读csv
# import csv
# with open('123.csv','r',encoding='utf-8')as f:
#     # r：只读  用read()
#     # w：只写 用write()         //会清除之前写的内容
#     # a：追加内容 用write()     //会在已经写的内容基础上增加新的内容
#     f_csv = csv.reader(f)
#     for row in f_csv:
#         print(row)
#         print(row[1])

# 写csv
import csv
import random
with open('123.csv','w',encoding='utf-8',newline='')as f:
    csv_writer = csv.writer(f)
    #writerow逐行写入 #writerows字典写入
    #csv_writer.writerow(['1322226666556656465464\t','dsad'])
    for y in range(100000):
        str = []
        for x in range(10):
            str.append(random.choice('abcdef'))
        csv_writer.writerow(str)
        if (y % 10000 == 9999):
            print('已写入%d行...' %(y + 1))
    print("写csv成功，共%d行！" %(y + 1))
f.close()