# 获取进程的编号
"""
获取编号的意义
    当进程过多时，为区分主进程与子进程，方便管理
注意事项
    * 默认的情况下，在主进程结束后，子进程执行完成后才会退出进程
    * 若绕主进程一退出，子进程也结束，可以设置W为守护进程
"""
import multiprocessing
import time
import os

def sing():
    # 使用os模块获取进程的编号
    print("唱歌进程编号{}".format(os.getpid()))
    print("唱歌父进程的编号{}".format(os.getppid()))
    for i in range(10):
        print("I can sing")
        time.sleep(0.5)
    pass


def dance():
    # 使用os模块获取进程的编号
    print("跳舞进程编号{}".format(os.getpid()))
    print("跳舞父进程的编号{}".format(os.getppid()))
    for i in range(10):
        print("I can dance")
        time.sleep(0.5)
    pass


if __name__ == "__main__":
    # 获取父进程的编号
    print("父进程的编号为{}".format(os.getpid()))
    # 创建进程对象 targer=函数名（方法名）
    sing_process = multiprocessing.Process(target=sing)
    dance_process = multiprocessing.Process(target=dance)
    # 设置守护进程
    sing_process.daemon = True
    dance_process.daemon = True

    # 启动进程，执行任务
    sing_process.start()
    dance_process.start()
    time.sleep(1)
    pass