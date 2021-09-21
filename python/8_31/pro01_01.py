# 面向对象联系
# 电子时钟模拟，创建一个时钟对象，模拟电子时钟
import time


class Clock(object):
    def __init__(self, sec, minute, hour):
        self.sec = sec
        self.minute = minute
        self.hour = hour
        pass

    def run(self):
        self.sec += 1
        if self.sec >= 60:
            self.sec = 0
            self.minute += 1
            pass
        if self.minute >= 60:
            self.minute = 0
            self.hour += 1
            pass
        pass

    def show(self):
        # 学习f的方法
        return f'{self.hour:0>2d}:{self.minute:0>2d}:{self.sec:0>2d}'


timer = Clock(0, 0, 0)
while True:
    print(timer.show())
    time.sleep(1)
    timer.run()
    pass
