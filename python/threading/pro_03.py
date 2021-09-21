# 主线程与子线程的执行顺序
# 多线程
import threading
import time


def sing():
    for i in range(10):
        print("I can sing")
        time.sleep(0.2)
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
    # 若主线程结束后不想等待子线程结束
    # 1. 方法一，创建线程是传递daemon 参数为 True
    # sing_threading = threading.Thread(target=sing, daemon=True)
    # dance_threading = threading.Thread(target=dance, daemon=True)

    # 2. 方法二，设置线程属性
    sing_threading.setDaemon(True)
    dance_threading.setDaemon(True)
    # 启动线程
    sing_threading.start()
    dance_threading.start()
    time.sleep(1)
    print("主线程结束啦...")
    pass
