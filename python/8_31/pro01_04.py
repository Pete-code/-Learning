# 序列化与反序列化
# json 模块
import json
import pickle

p_dic = {"name": "Pete",
         "age": 20,
         "cars": {"宝马": 2020,
                  "奔驰": 2021,
                  "兰博基尼": 2022},
         "hobbits": "play the violin"}

# dumps and loads
p_str = json.dumps(p_dic, ensure_ascii=False)  # ensure_ascii=False防止中文乱码的问题
# json模块用于字符串和python数据类型间进行转换
print(type(p_str))
print(type(p_dic))
print(p_str)
p_dic_new = json.loads(p_str)
print(p_dic_new)

# dump and load
p2_dic = {"name": "Pete",
          "age": 20,
          "cars": {"宝马": 2020,
                   "奔驰": 2021,
                   "兰博基尼": 2022},
          "hobbits": "play the violin"}

# 打开文件
with open("./mydump.txt", "w") as file:
    # 文件处理
    json.dump(p2_dic, file, ensure_ascii=False)
# 关闭文件
file.close()

with open("./mydump.txt", "r") as file:
    p = json.load(file)
    pass
file.close()
print(type(p))

# pickle 模块

p3_dic = {"name": "Pete",
          "age": 20,
          "cars": {"宝马": 2020,
                   "奔驰": 2021,
                   "兰博基尼": 2022},
          "hobbits": "play the violin"}

# dumps and loads

p3_bytes = pickle.dumps(p3_dic)
print(p3_bytes)
print(type(p3_bytes))

p3_dic_new = pickle.loads(p3_bytes)
print(p3_dic_new)
print(type(p3_dic_new))

# dump and load

with open("./my_pickle_dump.txt", "wb") as file:
    pickle.dump(p3_dic, file)
    file.close()

with open("./my_pickle_dump.txt", "rb") as file:
    p3 = pickle.load(file)
    print(type(p3))
    file.close()

"""
pickle模块与json模块的区别
 （1）pickle模块用于Python语言特有的类型和用户自定义类型与Python基本数据类型之间的转换 
 （2）pickle序列化结果为bites类型，只适合于Python机器之间的交互。
 json序列化结果为str类型，能够被多种语言识别，可用于与其他程序设计语言交互。
 总结
　　（1）序列化与反序列化是为了解决内存中对象的持久化与传输问题；

　　（2）Python中提供了pickle和json两个模块进行序列化与反序列化；

　　（3）dumps()和dump()用于序列化，loads()和load()用于反序列化；

　　（4）pickle模块能序列化任何对象，序列化结果为bites类型，只适合于Python机器之间交互；

　　json模块只能序列化Python基本类型，序列化结果为json格式字符串，适合不同开发语言之间交互。
"""
