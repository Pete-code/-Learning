"""
数组的叠加
1. vstack
2. hstack
3. concatenate
注意：需要叠加的数组用[array1, array2] 表示，并且写在前面的数组在合并的时候顺序也在前面
"""

"""
数组的切割
1. hsplit
2. vsplit
3. split 

总的来说，切割的方式有两种，第一是平均切割，第二是自定义切割
    * 平均切割要注意：能整除
    * 自定义切割表达方式为(a, b ,c) 其中的数组表示在某一行（列）之前切割
"""
import numpy

# 数组在垂直方向的叠加, 垂直方向的叠加，两个数组的列数应该相同
array_vbase1 = numpy.random.randint(1, 10, size=(2, 5))
array_vbase2 = numpy.random.randint(1, 10, size=(1, 5))

array_v = numpy.vstack([array_vbase1, array_vbase2])
print("array_v is \r\n{}".format(array_v))


# 数组在水平方向的叠加, 水平方向的叠加，两个数组的行数应该相同
array_hbase1 = numpy.random.randint(1, 10, size=(2, 5))
array_hbase2 = numpy.random.randint(1, 10, size=(2, 4))

array_h = numpy.hstack([array_hbase1, array_hbase2])
print("array_v is \r\n{}".format(array_h)) 

# concatenate方法实现水平，垂直，以及叠加后转化为一维数组
array_mh = numpy.concatenate([array_hbase1, array_hbase2], axis=1)   # 水平方向叠加，axis的参数值为1
print("array_mh is \r\n{}".format(array_mh))

array_mv = numpy.concatenate([array_vbase1, array_vbase2], axis=0)  # 垂直方向上的叠加，axis的参数值为0
print("array_mv is \r\n{}".format(array_mv))


array_mf = numpy.concatenate([array_vbase1, array_vbase2], axis=None)  #  叠加后展开为一维数组，axis的参数值为None
print("array_mf is \r\n{}".format(array_mf))


# 切割
# vsplit 垂直方向分割，分成几行
array_svbase = numpy.random.randint(1, 10, size=(4, 3))
array_sv1 = numpy.vsplit(array_svbase, 4)    # 平均切割
print("array_svbase is \r\n{}".format(array_svbase))
print("array_sv1 is \r\n{}".format(array_sv1))
for i in range(4):
    print("array is {}".format(array_sv1[i].flatten()))
    pass

array_sv2 = numpy.vsplit(array_svbase, (2, 3))
print("array_svbase is \r\n{}".format(array_svbase))
print("array_sv2 is \r\n{}".format(array_sv2))

for i in range(3):
    print("array is {}".format(array_sv2[i].flatten()))
    pass


# hsplit 水平方向切割，切割成不同的列

array_shbase = numpy.random.randint(1, 10, size=(3, 4))
array_sh1 = numpy.hsplit(array_shbase, 4)    # 平均切割
print("array_shbase is \r\n{}".format(array_shbase))
print("array_sh1 is \r\n{}".format(array_sh1))
for i in range(4):
    print("array is {}".format(array_sh1[i].flatten()))
    pass

array_sh2 = numpy.vsplit(array_shbase, (2, 3))
print("array_shbase is \r\n{}".format(array_shbase))
print("array_sh2 is \r\n{}".format(array_sh2))

for i in range(2):
    print("array is {}".format(array_sh2[i].flatten()))
    pass


# split 方法， axis = 1 按列切割（水平切割），axis = 0 按行切割（垂直切割）

array_mhsbase = numpy.random.randint(1, 10, (5, 6))
array_mhsv = numpy.split(array_mhsbase, (1, 4), axis=1)
print("array_mhsbase is \r\n{}".format(array_mhsbase))
print("array_mhsv is \r\n{}".format(array_mhsv))

array_mvsbase = numpy.random.randint(1, 10, (5, 6))
array_mvsv = numpy.split(array_mvsbase, (1, 4), axis=0)
print("array_mhsbase is \r\n{}".format(array_mvsbase))
print("array_mhsv is \r\n{}".format(array_mvsv))
