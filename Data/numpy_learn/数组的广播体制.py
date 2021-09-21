"""
数组的广播体制
1. 数组和数的运算
2. shape 相同的数组之间的运算
3. shape 不同的数组之间的运算
"""
import numpy
# 数组和数之间的运算
array1 = numpy.random.randint(1, 10, size=(3, 4))
print("array1 is \r\n{}".format(array1))
array2 = array1*10
print("array2 is \r\n{}".format(array2))


array3 = array1 * array2
print("array3 is \r\n{}".format(array3))

# shape 不一样的原则上不能广播计算， 但是单行或者单列的可以进行广播运算
array4 = numpy.random.randint(1, 10, size=(3, 1))
array5 = array4 + array1
print("array5 is \r\n{}".format(array5))
