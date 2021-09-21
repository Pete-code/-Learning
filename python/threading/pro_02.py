# 多线程带有参数的任务
# 元组方式传参， 字典方式传参
import threading
import time


def sing(num):
    for i in range(num):
        print("I can sing")
        time.sleep(0.5)
    pass


def dance(num, name):
    for i in range(3):
        print("I can dance")
        time.sleep(0.5)
    pass


if __name__ == "__main__":
    # 创建线程对象
    sing_threading = threading.Thread(target=sing, args=(6,))
    dance_threading = threading.Thread(target=dance, kwargs={"name": "Pete", "num": 3})
    # 启动线程
    sing_threading.start()
    dance_threading.start()
    pass
