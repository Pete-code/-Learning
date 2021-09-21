# @property 修饰器

class Student(object):
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
        pass

    @property
    # 属性访问器(getter方法) - 获取__name属性
    def name(self):
        return self.__name
        pass

    # 属性修改器(setter方法) - 修改__name属性

    @name.setter
    def name(self, name):
        self.__name = name or "无名氏"
        pass

    pass


# __slots__
class Students:
    __slots__ = ('name', 'age')

    def __init__(self, name, age):
        self.name = name
        self.age = age


stu = Student('王大锤', 20)
# AttributeError: 'Student' object has no attribute 'sex'
stu.sex = '男'

st = Student("Pete", 20)
print(st.name)
st.name = ""
print(st.name)  # 无名氏


