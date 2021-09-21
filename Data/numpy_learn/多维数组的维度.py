"""
多维数组的维度以及修改维度

ndarray.ndim:  查看数组的维度
ndarray.shape: 查看数组几行几列，返回的元组中有几个元素就为几维数组
ndarray.reshape: 修改数组的形状，返回一个新的数组，注意修改后数组中元素的个数与原来的数组中元素的个数相同
ndarray.size: 查看数组中元素的个数
ndarray.itemsize: 查看数组所占用的内存
"""

import numpy

array_dim1 = numpy.array([1, 2, 3], dtype="int8")
array_dim2 = numpy.array([[1, 2, 3], [4, 5, 6]], dtype="int8")
array_dim3 = numpy.array([
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ],
    [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
])
# 查看数组的维度

print("the dim of array_dim1 is {} ".format(array_dim1.ndim))
print("the dim of array_dim2 is {} ".format(array_dim2.ndim))
print("the dim of array_dim3 is {} ".format(array_dim3.ndim))

# 查看数组几行几列
print("the shape of array_dim1 is {}".format(array_dim1.shape))
print("the shape of array_dim2 is {}".format(array_dim2.shape))
print("the shape of array_dim3 is {}".format(array_dim3.shape))


# 修改数组的类型

array_dim1_change = array_dim1.reshape((3, 1))
array_dim2_change = array_dim2.reshape((3, 2))
# array_dim3_change = array_dim3.reshape((18,))
# 改变为一维数组的另一种方式
array_dim3_change = array_dim3.flatten()
print(" array_dim1_change is \r\n{}".format(array_dim1_change))
print(" array_dim2_change is \r\n{}".format(array_dim2_change))
print(" array_dim3_change is \r\n{}".format(array_dim3_change))


# 查看数组的元素个数

print("the size of array_dim1 is {} ".format(array_dim1.size))
print("the size of array_dim2 is {} ".format(array_dim2.size))
print("the size of array_dim3 is {} ".format(array_dim3.size))

# 查看数组元素所占的内存大小
print("the itemsize of array_dim1 is {} ".format(array_dim1.itemsize))
print("the itemsize of array_dim2 is {} ".format(array_dim2.itemsize))
print("the itemsize of array_dim3 is {} ".format(array_dim3.itemsize))






