# 工具文件
import random

import openpyxl
book = openpyxl.Workbook()
sheet = book.active
for col in range(10):
    row = (random.randint(10, 100) for _ in range(10))
    sheet.append(row)
    pass

book.save("pro02_05.xlsx")
