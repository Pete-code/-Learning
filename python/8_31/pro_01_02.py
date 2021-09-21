# 定义一个类描述平面上的点并提供移动点和计算到另一个点距离的方法。
# import cmath
#
#
# class Distance:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#         self.dis = 0
#         pass
#
#     def distance(self, x_purpose, y_purpose):
#         x_distance = (self.x - x_purpose) ** 2
#         y_distance = (self.y - y_purpose) ** 2
#         self.dis = cmath.sqrt(x_distance + y_distance)
#         print(self.dis)
#         pass
#
#     pass
#
#
# distance = Distance(1, 2)
# distance.distance(13, 45)
# print(distance.dis)

# 更好的做法


from math import sqrt


class Point(object):
    #  学习other 的方法
    
    def __init__(self, x=0, y=0):
        """初始化方法

        :param x: 横坐标
        :param y: 纵坐标
        """
        self.x = x
        self.y = y

    def move_to(self, x, y):
        """移动到指定位置

        :param x: 新的横坐标
        "param y: 新的纵坐标
        """
        self.x = x
        self.y = y

    def move_by(self, dx, dy):
        """移动指定的增量

        :param dx: 横坐标的增量
        "param dy: 纵坐标的增量
        """
        self.x += dx
        self.y += dy

    def distance_to(self, other):
        """计算与另一个点的距离

        :param other: 另一个点
        """
        dx = self.x - other.x
        dy = self.y - other.y
        return sqrt(dx ** 2 + dy ** 2)

    def __str__(self):
        return '(%s, %s)' % (str(self.x), str(self.y))


def main():
    p1 = Point(3, 5)
    p2 = Point()
    print(p1)
    print(p2)
    p2.move_by(-1, 2)
    print(p2)
    print(p1.distance_to(p2))


if __name__ == '__main__':
    main()
