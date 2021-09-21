import random
import csv
import numpy
"""
NAN:
NAN 的一些性质
1. NAN 是Not A Number 的缩写，也就是不是一个数字，但是他是浮点型，所以做数据处理时要注意他的数据类型
2. NAN !- NAN 
3. NAN 与任何数据计算的结果仍为NAN
4. NAN的出现是因为有些列表数据的空值
"""
"""
缺失值的处理方式
1. 删除缺失的值
    * 直接删除数据
    * 删除空值所在的行或者列
    numpy.delete()
    delete(arr, obj, axis=None)
    arr :Input array
    obj : 所要删除的行或着列
    axis：0 删除行 1 删除列
    参数说明:
    
"""
# print(numpy.NAN == numpy.NAN)
# data = numpy.random.randint(1, 20, size=(3, 4)).astype(float)   # 注意必须转化为浮点型才能将NAN写入数组，因为NAN是浮点类型
# data[0, 1] = numpy.NAN
# print(data)
# print(numpy.NAN*20)

# 创建带有空值的数组
data = numpy.random.randint(20, 100, size=(30, 40)).astype(float)
for i in range(40):
    data[random.randint(0, 29), random.randint(0, 39)] = numpy.nan
    pass
with open("data.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerows(data)
    pass

# 方法一：直接删除NAN ，但不能保持数组的形状，一般适用于并不要求保持数组的形状，只要数据的情况下
data1 = data.copy()
data1 = data1[~numpy.isnan(data1)]   # 使用布尔索引，返回非空的值，因为数组的结构破坏，所以返回一个一维的数组
print(numpy.size(data1))

with open("data1.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerow(data1)
    pass


# 方法二：直接删除NAN所在的行 ,这种方法能保持数组的形状，但是会删除缺失值所在行或者列的数据
data2 = data.copy()
# 找到NAN所在的行号
lines = numpy.where(numpy.isnan(data2))[0]
print(lines)
# 删除所在的行
data2 = numpy.delete(data2, lines, axis=0)
# help(numpy.delete)
print(numpy.size(data2))
with open("data2.csv", "w", encoding="utf-8", newline="") as fp:
    writer = csv.writer(fp)
    writer.writerows(data2)
    pass



