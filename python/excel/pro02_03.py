# 操作创建的Excel文件
# 读取单个单元格
import openpyxl
# 打开Excel文件
book = openpyxl.load_workbook("name.xlsx")
sheet = book.active
a1 = sheet["A1"]
a2 = sheet.cell(column=2, row=1)
print(a1.value, a2.value)
# 读取多个单元格
cells = sheet["A1":"B6"]
for c1, c2 in cells:
    # print("{0:8} {1:8}".format(c1.value, c2.value))
    print(c1.value, c2.value)
    pass


