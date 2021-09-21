# 线程执行的顺序
import threading
import time

"""
线程的执行顺序是无序的 ,是由CPU调度决定的
"""


def task():
    time.sleep(1)
    # 获取当前线程的线程对象
    print(threading.current_thread())
    pass


if __name__ == "__main__":
    for i in range(5):
        sub_thread = threading.Thread(target=task)
        sub_thread.start()
        pass

    pass
