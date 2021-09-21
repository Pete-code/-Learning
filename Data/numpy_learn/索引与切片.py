"""
notice: 列与行的切片与索引方法相同，实现各种切片，只需要将方法组合起来使用即可
* 连续索引切片: a:b
* 间断索引切片: [a,b,c]
*array[行,列]
*array[num] 表示行
*array[:,num] 表示列
"""
"""
布尔索引

布尔索引的形式很多，有< > <= >= == != 以及逻辑运算 & |
布尔索引其实有两个步骤
"""
import numpy
array_example = numpy.random.randint(1, 20, size=(4, 5))
print("array_example is \r\n{}".format(array_example))

# 以索引行为例
print("数组单独一行的索引方法{}".format(array_example[1]))
print("数组连续行的索引方法\r\n{}".format(array_example[1:4]))
print("数组间断行的索引方法\r\n{}".format(array_example[[0, 2, 3]]))


# 混合索引举例
print("索引数组单独的元素{}".format(array_example[2, 3]))
print("索引数组连续行和列\r\n{}".format(array_example[1:4, 1:3]))
print("索引数组间断的元素{}".format(array_example[[1, 2, 3], [0, 2, 1]]))

# 单独索引数组列
print("索引数组的列\r\n{}".format(array_example[:, 1:2]))


# 布尔索引
print("布尔索引{}".format(array_example < 10))      # 返回对应位置元素的True 或者False
print("布尔索引返回满足要求的值{}".format(array_example[(array_example < 10)|(array_example > 15)]))


