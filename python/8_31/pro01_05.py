# CSV文件操作

# 引入模块
import csv
import random

title = ["name", "age", "语文成绩", "数学成绩", "英语成绩"]
names = ["pete", "peter", "Bob"]


with open("./scores.csv", "w", encoding="utf8") as file:
    # 创建CSV对象
    scores = csv.writer(file)
    scores.writerow(title)
    for name in names:
        score = [random.randint(90, 100) for _ in range(3)]
        score.insert(0, name)
        score.insert(1, random.randint(19, 22))
        # 遍历写入文件
        scores.writerow(score)
    file.close()
    pass

with open("./scores.csv", "r", encoding="utf8") as f:
    # 创建CSV对象
    read_scores = csv.reader(f)
    print(type(read_scores))
    for data in read_scores:
        print(data)
    pass


