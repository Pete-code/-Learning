# 时间处理模块
# 时间的显示（字符串模式） 时间的转换（转化为时间的格式） 时间的运算
"""
1. 时间戳
2.格式化的时间字符串
3.元祖的形式
"""
import datetime
import time
# 记录开始时间
s_time = time.time()
# 程序跑的时间
print(f"cost{time.time()-s_time}")

# time.localtime([secs]) 将时间戳转化为当前查询时间的时间数据结构

pr = time.localtime()
print(pr)
# time.gmtime() 将时间转化为UTC时间

utc = time.gmtime()
print(utc)
time.sleep(1)
# time.mktime 将时间对象转化为时间戳
print(time.mktime(utc))
# time.strftime(format[,t]) 把元祖的时间对象转化为指定的字符串格式
time_str = time.strftime("%Y-%m-%d-%H-%M-%S", utc)
# time.strptime(time,format)将字符串转化为时间的格式
print(time.strptime(time_str, "%Y-%m-%d-%H-%M-%S"))
# datetime 模块
"""
日期表达 时间运算 时间替换
"""
# datetime.date: 表示日期的类，常见的属性有year mounth day
# datetime.time 表示时间的类，常见属性有hour minute second microsecond
# datetime.datetime 表示时间和日期
#  datetime/timedelta 表示时间的间隔，及两个时间点之间的长度
# datetime.tzinfo 与时区有关的信息

"""
datetime.datetime.now() 返回当前的日期
datetime.date.fromtimestamp()把一个时间戳转换为日期类型
"""
d1 = datetime.datetime.now()
print(d1)
d2 = datetime.date.today()
print(d2)
"""
时间的运算
# datetime.datetime.now() + datetime.timedelta(4)  当前时间加四天
"""
print(datetime.datetime.now() + datetime.timedelta(5))
print(datetime.datetime.now() + datetime.timedelta(hours=2))
"时间替换"
d1.replace(year=2020, month=5, day=2)
print(d1)
