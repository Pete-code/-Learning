# 进程执行带有参数的任务
"""
1. 使用元组传参 args
    * 元组对应的顺序即为参数的顺序
2. 使用字典传参
    * 注意key值对应参数名
"""
import multiprocessing
import time


def sing(num):
    for i in range(num):
        print("I can sing")
        time.sleep(0.5)
    pass


def dance(num, name):
    for i in range(num):
        print(name)
        print("I can dance")
        time.sleep(0.5)
    pass


if __name__ == "__main__":
    # 创建进程对象 targer=函数名（方法名）
    # 使用元素传参
    sing_process = multiprocessing.Process(target=sing, args=(3,))  # 注意传到一个参数时，元组的,不要去掉，不然传递的数据类型不是元组
    # 使用字典传参，注意key值与变量名对应
    dance_process = multiprocessing.Process(target=dance, kwargs={"num": 4, "name": "Pete"})

    # 启动进程，执行任务
    sing_process.start()
    dance_process.start()
    pass
