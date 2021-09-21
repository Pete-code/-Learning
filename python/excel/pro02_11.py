# Openpyxl 公式
# openpyxl 不进行计算，只是将公式写入单元格中
import random

import openpyxl

# 创建并写入工作簿
book = openpyxl.Workbook()
sheet = book.active

rows = ((random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3)),
        (random.randint(46, 986) for _ in range(3))
        )
for row in rows:
    sheet.append(row)
    pass
# print(len(rows))
# 确定将公式植入那个单元格
cell = sheet.cell(row=14, column=4)
cell.value = "=SUM(A1:C14)"
cell.font = cell.font.copy(bold=True)
book.save("pro02_11.xlsx")
