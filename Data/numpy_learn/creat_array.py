# 创建数组
"""
创建数组的三种方式
    1. 使用numpy.array()
    2. 使用numpy.arange()
    3. 使用numpy.random()
    4. 使用 numpy.zeros() numpy.ones() numpy.full() numpy.eye()
    注意 数组与列表不同，数组中的数据类型只能有一种构成
"""

import numpy
# method 1
array_basic = numpy.array([1, 2, 3])
print(array_basic)

# methon 2 使用方法与python 中的range 函数相同
array_arange = numpy.arange(1, 3, 1)
print(array_arange)

# method 3 ramdon.xxxxx
array_random1 = numpy.random.random(size=(3, 3))    # size 指定几行几列
array_random2 = numpy.random.randint(1, 20, size=(5, 5))    # 指定随机数的范围，并指定生成几行几列的随机数
print("array_random1 is\n\r {}".format(array_random1))
print("array_random2 is \r\n{}".format(array_random2))


#  method 4 zeros ones full eye
array_zeros = numpy.zeros((2, 2))   # 指定生成几行几列
print("array_zeros is \n\r {}".format(array_zeros))
array_ones = numpy.ones((3, 3))     # 指定生成几行几列
print("array_ones is \n\r{}".format(array_ones))
array_full = numpy.full((8, 8), 8)  # 指定生成几行几列， 并由什么来填充
print("array_full is \r\n {}".format(array_full))
array_eye = numpy.eye(4)    # 指定生成几行几列
print("array_eye is \r\n {}".format(array_eye))
