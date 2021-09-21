# 插入图表
"""
openpyxl库支持创建各种图表，包括条形图，折线图，面积图，气泡图，散点图和饼图。

根据文档，openpyxl仅支持在工作表中创建图表。 现有工作簿中的图表将丢失。
"""

from openpyxl import Workbook
from openpyxl.chart import (
    Reference,
    Series,
    BarChart
)
# 创键工作表单
book = Workbook()
sheet = book.active

rows = [
    ("USA", 46),
    ("China", 38),
    ("UK", 29),
    ("Russia", 22),
    ("South Korea", 13),
    ("Germany", 11)
]

for row in rows:
    sheet.append(row)
    pass

# 创键数据轴
data = Reference(sheet, min_col=2, min_row=1, max_row=6, max_col=2)
# 创键类别轴
categs = Reference(sheet, min_col=1, min_row=1, max_row=6, max_col=1)
# 绘制条形图
chart = BarChart()
chart.add_data(data=data)
chart.set_categories(categs)
# 使用legend和majorGridlines属性，可以关闭图例和主要网格线。
chart.legend = None
chart.y_axis.majorGridlines = None
# 设置每一个条形图都有不同的颜色
chart.varyColors = True
# 设置标题
chart.title = "Olympic Gold medals in London"
# 将条形图添加到工作簿
sheet.add_chart(chart, "A8")
book.save("pro02_13.xlsx")
