# 多线程
import threading
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
    # 创建线程对象
    sing_threading = threading.Thread(target=sing)
    dance_threading = threading.Thread(target=dance)
    # 启动线程
    sing_threading.start()
    dance_threading.start()
    pass
