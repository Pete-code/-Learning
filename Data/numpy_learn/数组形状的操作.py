"""
1. reshape 和 resize
    reshape 不会修改原来数组本身，而resize会修改数组本身
2. flatten和ravel
    相同点：都是将数组修改为一维数组
    不同点: flatten是返回一个拷贝而ravel是返回一个引用，也就是说，再改变数组元素的值，flatten不会影响原来的数组，而ravel会影响原来数组的值
"""

import numpy
array1 = numpy.random.randint(1, 10, size=(3, 4))
# reshape and resize
print("array1 is \r\n{}".format(array1))
array2 = array1.reshape((2, 6))
print("the effect of reshape ")
print("array1 is \r\n{}".format(array1))
print("array2 is \r\n{}".format(array2))

array3 = array1.resize((2, 6))
print("the effect of resize ")
print("array1 is \r\n{}".format(array1))
print("array3 is \r\n{}".format(array3))


#  flatten and ravel
array4 = numpy.random.randint(2, 10, size=(3, 4))
print("the effect of flatten ")
array5 = array4.flatten()
print("array4 is \r\n{}".format(array4))
print("array5 is \r\n{}".format(array5))

element1 = array5[0]
array5[0] = 1
print("before change ,the element is {}".format(array4[0, 0]))
print("after change ,the element is {}".format(array4[0, 0]))

print("the effect of  ravel ")
array6 = array4.ravel()
print("array4 is \r\n{}".format(array4))
print("array6 is \r\n{}".format(array6))
print("before change ,the element is {}".format(array4[0, 0]))

element2 = array6[0]
array6[0] = 1
print("after change ,the element is {}".format(array4[0, 0]))




