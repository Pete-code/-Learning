# 统计
import openpyxl
import statistics as sta

book = openpyxl.load_workbook("pro02_05.xlsx", data_only=True)
sheet = book.active

# 读取表单中的数据
values = []
for col in sheet.columns:  # 读取表单中非空的每一列数据
    for cell in col:    # 读取每一个单元格中的数据，并将数据保存到创建的列表中
        values.append(cell.value)
        pass
    pass
# 数据处理
# 数据的长度
print("Len: {0}".format(len(values)))
# 数据的总和
print("Sum: {0}".format(sum(values)))
# 数据的最小值
print("Min: {0}".format(min(values)))
# 数据的极大值
print("Max:{0}".format(max(values)))
# 数据的平均数
print("Median: {0}".format(sta.median(values)))
print("Mean: {0}".format(sta.mean(values)))
print("Median: {0}".format(sta.median(values)))
print("Standard deviation: {0}".format(sta.stdev(values)))
print("Variance: {0}".format(sta.variance(values)))
