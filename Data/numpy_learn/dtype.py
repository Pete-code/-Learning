import numpy

"""
numpy 的数据类型以及修改数据类型
默认的数据类型 查看笔记

"""

# 实际的意义 : 在Excel中导入数据是可以指定数据的类型，加快海量数据的处理速度以及时间
array_int8 = numpy.array([1, 2, 3], dtype="int8")
print("array_int8 is {} ".format(array_int8))
print("the type of array_int8 is {}".format(array_int8.dtype))

array_string = numpy.array(['1', '2', '3'], dtype="string_")
print("array_string is {} ".format(array_string))
print("the type of array_string is {}".format(array_string.dtype))

array_string_unicode = numpy.array(['1', '2', '3'], dtype="U")
print("array_string_unicode is {} ".format(array_string_unicode))
print("the type of array_string_unicode is {}".format(array_string_unicode.dtype))


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        pass

    pass


array_object = numpy.array(Person("Jane", 20), dtype="object_")
print("array_object is {} ".format(array_object))
print("the type of array_object is {}".format(array_object.dtype))


#  改变数据的类型 ndarray.astype

array_string_u = array_string.astype("U")
print(array_string_u.dtype)
print(array_string.dtype)

