import csv  # csv 是python自带的模块
"""
读取CSV文件有两种方式：
1. 通过列表的方式，用索引读取
2. 通过字典的方式，用key值读取
"""
"""
写入CSV文件中
1. 使用列表的方式写入
2. 使用字典的方式写入
"""


#  使用列表的方式读取数据，这样做可能会出现索引错误
def read_csv_demo1():
    with open("房地产投资金额.csv", "r", encoding="utf-8") as fp:
        # reader 是一个迭代器
        reader = csv.reader(fp)
        # 跳过header
        header = next(reader)
        for x in reader:
            area = x[0]
            invest = x[1]
            print("area:{}  invest:{}".format(area, invest))
            pass
        pass
    pass


# 使用字典的方式读取数据，高效准确


def read_csv_demo2():
    with open("房地产投资金额.csv", "r") as fp:
        # 这是有序的字典，并且跳过了第一行的header
        reader = csv.DictReader(fp)
        for x in reader:
            value = {"地区": x["地区"],
                     "投资额": x["投资额"]}
            print(value)
            pass
        pass
    pass

#  使用列表的方式写入数据


def write_csv_demo1():
    headers = ["姓名", "年龄", "身高"]
    value = [
        ["Pete", 20, 165],
        ["Pete", 20, 165],
        ["Pete", 20, 165],
        ["Pete", 20, 165],
        ["Pete", 20, 165]
    ]
    with open("Person1.csv", "w", encoding="utf-8", newline="") as fp:
        writer = csv.writer(fp)
        writer.writerow(headers)
        writer.writerows(value)
        pass

    pass


# 使用字典的方式写入数据

def write_csv_demo2():
    with open("Person2.csv", "w", encoding="utf-8", newline="") as fp:
        headers = ["姓名", "年龄", "身高"]
        value = [
            {"姓名": "Pete", "年龄": 20, "身高": 165},
            {"姓名": "Pete", "年龄": 20, "身高": 165},
            {"姓名": "Pete", "年龄": 20, "身高": 165},
            {"姓名": "Pete", "年龄": 20, "身高": 165},
            {"姓名": "Pete", "年龄": 20, "身高": 165},
            {"姓名": "Pete", "年龄": 20, "身高": 165},
        ]
        writer = csv.DictWriter(fp, headers)    # 传入两个参数，一个是文件指针，一个是header
        writer.writeheader()    # 必须单独调用writerheader()函数写入header
        writer.writerows(value)
        pass

    pass



if __name__ == "__main__":
    # read_csv_demo1()
    read_csv_demo2()
    write_csv_demo1()
    write_csv_demo2()