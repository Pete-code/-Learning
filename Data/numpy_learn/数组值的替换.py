"""
替换
替换的方法有三个：
1. 使用切片和索引替换
2. 使用条件索引替换
3. 使用where函数替换
"""
import numpy

array1 = numpy.random.randint(1, 10, size=(4, 5))
print("array1 is \r\n{}".format(array1))
# 使用切片和索引替换
array1[1, 3] = 0
array1[3] = 1
print("array1 is \r\n{}".format(array1))

# 使用条件索引替换
array1[array1 < 5] = 13  # 满足条件的全部替换为13
print("array1 is \r\n{}".format(array1))

#  使用where方法
a1 = numpy.where(array1 > 6)
print("a1 is \r\n{}".format(a1))    # 分被返回满足条件的元素的行号组成的元组，以及列号组成的元组
a2 = numpy.where(array1 > 6, 0, 1)  # 满足条件的替换为1，不满足条件的替换为0
print("a2 is \r\n{}".format(a2))    # 返回替替换后的数组



