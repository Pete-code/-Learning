"""
numpy 读写文件---以读写CSV文件为例


"""
import numpy

# help(numpy.savetxt)
# help(numpy.loadtxt)

"""
savetxt() 函数参数参数说明
 * fname:文件名
 * X 写入的数组
 * fmt: 文件字符的格式 --  %d %f .....
 * delimiter: 分隔符，注意用什么分隔符写入，读取的时候就用什么分隔符读取，header footer 用同样的分隔符间隔字符
 * newline:
 * header:设置表头一类的东西
 * footer:
 * comments:
 * encoding:
"""

"""
loadtxt() 函数参数说明
fname:file, str, or pathlib.Path
dtype:data-type 读取数据的数据类型
comments:
delimiter:分隔符，注意与写入的分隔符一样
converters:
skiprows:跳过第几行
usecols:只读取第几列
unpack:默认是False ，如果是True的话，所读取的数组最后会转置
encoding:

"""


"""
numpy 独有的文件操作模块
存储：np.save(fname,array)或np.savez(fname,array)。其中，前者函数的扩展名是.npy，后者的扩展名是.npz，后者是经过压缩的。
加载：np.load(fname)。

与numpy.savetxt()对比
1. numpy.savetxt()能添加header而numpy.save() 只能存储同一种类型的数据
2. numpy.savetxt() 只能存储一维或者二维数组，而numpy.save()能存储多维数组
"""
scores = numpy.random.randint(50, 100, size=(20, 2))
file = numpy.savetxt("scores.csv", X=scores, delimiter=",", header="英语成绩, 数学成绩", comments='', fmt="%d")
# 因为分隔符为英文的逗号，所以header 中也要用英文的逗号分隔

file2 = numpy.loadtxt("scores.csv", dtype=int, delimiter=",", skiprows=1, usecols=(1,))
print(file2)


dates = numpy.random.randint(1, 100, size=(4, 5))
numpy.save("datas", dates)
datas = numpy.load("datas.npy")
print(datas)



