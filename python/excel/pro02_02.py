# excel 模块
from openpyxl import Workbook, load_workbook

# 实例化

# 创建文件
wb = Workbook()
sheet = wb.active  # 活跃的sheet
print(sheet.title)
sheet.title = "sheet1"
# 写入数据
# 方式一: 数据直接分配到单元格中
sheet["B9"] = "Pete"
sheet["C9"] = "20"
# 方式二 ,添加列，从第一列开始添加
sheet.append(["Jane", 20])
# 保存表
# wb.save("文件名.xlsx")
wb.save("pro02_02.xlsx")
