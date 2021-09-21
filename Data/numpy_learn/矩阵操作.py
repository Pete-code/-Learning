"""
矩阵的装置和轴对换
1. 矩阵的转置
    * ndarry.T
    * ndarray.transpose() 注意这种方法返回的是一个view ，所以，对改变后的数组进行修改，会影响到原来的数组
2. ndarray.dot() 矩阵的乘法
"""
import numpy
a1 = numpy.arange(0, 24).reshape((4, 6))
a2 = a1.T
print(a2)

a1 = numpy.arange(0, 24).reshape((4, 6))
a2 = a1.transpose()

a1 = numpy.arange(0, 24).reshape((4, 6))
a2 = a1.T
print(a1.dot(a2))
