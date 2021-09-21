import csv
import random
import numpy
import math

"""
需求 创建一个含有空值的成绩列表，并将列表写入一个CSV文件中，处理这个文件，求各科成绩的平均值，其中空值用非空值的平均值代替
这个年级有六百个学生
"""


# 创建成绩单


def scores():
    # 使用字典的方式写入数据
    headers = ["姓名", "学号", "语文成绩", "数学成绩", "英语成绩", "物理成绩"]
    id = range(1, 601)
    datas = []
    chinese_scores = numpy.random.randint(60, 150, size=(1, 600)).flatten().astype(numpy.unicode_)
    math_scores = numpy.random.randint(60, 150, size=(1, 600)).flatten().astype(numpy.unicode_)
    english_scores = numpy.random.randint(60, 150, size=(1, 600)).flatten().astype(numpy.unicode_)
    physic_scores = numpy.random.randint(60, 150, size=(1, 600)).flatten().astype(numpy.unicode_)
    for i in range(5):
        math_scores[random.randint(1, 600)] = ""
        pass

    for i in range(5):
        english_scores[random.randint(1, 600)] = ""
        pass

    for num in range(0, 600):
        dic = {"姓名": "Pete",
               "学号": id[num],
               "语文成绩": chinese_scores[num],
               "数学成绩": math_scores[num],
               "英语成绩": english_scores[num],
               "物理成绩": physic_scores[num]
               }
        datas.append(dic)
        pass
    # 将datas 写入CSV 文件

    with open("scores_all.csv", "w", encoding="utf-8", newline="") as fp:
        writer = csv.DictWriter(fp, headers)
        writer.writeheader()
        writer.writerows(datas)
    pass


def read_scores():
    scores_data = []
    id = range(1, 601)
    total_score = []

    # 读取成绩单, 以列表的方式处理数据
    with open("scores_all.csv", "r", encoding="utf-8", newline="") as fp:
        reader = csv.reader(fp)
        headers = next(reader)
        # print(headers)
        chinese_scores = []
        math_scores = []
        english_scores = []
        physic_scores = []

        # 处理成绩单中的空字符
        for x in reader:
            chinese_scores.append(x[2])
            math_scores.append(x[3])
            english_scores.append(x[4])
            physic_scores.append(x[5])
            pass

        chinese_scores = numpy.array(chinese_scores)
        math_scores = numpy.array(math_scores)
        english_scores = numpy.array(english_scores)
        physic_scores = numpy.array(physic_scores)
        # 处理空字符
        chinese_scores[chinese_scores == ""] = numpy.nan
        math_scores[math_scores == ""] = numpy.nan
        english_scores[english_scores == ''] = numpy.nan
        physic_scores[physic_scores == ''] = numpy.nan

        # 类型转换
        chinese_scores = chinese_scores.astype(float)
        math_scores = math_scores.astype(float)
        english_scores = english_scores.astype(float)
        physic_scores = physic_scores.astype(float)
        #  使用平均值代替NAN
        chinese_scores_clear = chinese_scores[~numpy.isnan(chinese_scores)]
        math_scores_clear = math_scores[~numpy.isnan(math_scores)]
        english_scores_clear = english_scores[~numpy.isnan(english_scores)]
        physic_scores_clear = physic_scores[~numpy.isnan(physic_scores)]

        chinese_scores[numpy.isnan(chinese_scores)] = numpy.mean(chinese_scores_clear)
        math_scores[numpy.isnan(math_scores)] = numpy.mean(math_scores_clear)
        english_scores[numpy.isnan(english_scores)] = numpy.mean(english_scores_clear)
        physic_scores[numpy.isnan(physic_scores)] = numpy.mean(physic_scores_clear)
        for i in range(600):
            total_score.append(chinese_scores[i] + math_scores[i] + english_scores[i] + physic_scores[i])
            # print(chinese_scores_clear)
            # 计算各科的平均分
            chinese_scores_mean = numpy.mean(chinese_scores)
            physic_scores_mean = numpy.mean(physic_scores)
            math_scores_mean = numpy.mean(math_scores)
            english_scores_mean = numpy.mean(english_scores)
            total_score_mean = (chinese_scores_mean + physic_scores_mean + math_scores_mean + english_scores_mean) / 4
            footer = {"姓名": "平均成绩",
                      "学号": 0,
                      "语文成绩": chinese_scores_mean,
                      "数学成绩": math_scores_mean,
                      "英语成绩": english_scores_mean,
                      "物理成绩": physic_scores_mean,
                      "总成绩": total_score_mean
                      }
        #  更新成绩单
        headers = ["姓名", "学号", "语文成绩", "数学成绩", "英语成绩", "物理成绩", "总成绩"]
        for num in range(0, 600):
            dic = {"姓名": "Pete",
                   "学号": id[num],
                   "语文成绩": chinese_scores[num],
                   "数学成绩": math_scores[num],
                   "英语成绩": english_scores[num],
                   "物理成绩": physic_scores[num],
                   "总成绩": total_score[num]
                   }
            scores_data.append(dic)
            pass

        with open("final_scores.csv", "w", encoding="utf-8", newline="") as f:
            writer = csv.DictWriter(f, headers)
            writer.writeheader()
            writer.writerows(scores_data)
            writer.writerow(footer)
            pass


# 求平均值

# 更新成绩单


if __name__ == '__main__':
    scores()
    read_scores()
    # scores = numpy.array(["1", "2"])
    # scores = scores.astype(float)

    pass
