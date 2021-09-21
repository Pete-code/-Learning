# 多进程
"""
编程思路:
1. 导入进程包
2. 通过进程创建进程的对象 指定target
3.启动进程执行任务

"""
import multiprocessing
import time


def sing():
    for i in range(3):
        print("I can sing")
        time.sleep(0.5)
    pass


def dance():
    for i in range(3):
        print("I can dance")
        time.sleep(0.5)
    pass


if __name__ == "__main__":
    # 创建进程对象 targer=函数名（方法名）
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)

    # 启动进程，执行任务
    sing_process.start()
    dance_process.start()
    pass
