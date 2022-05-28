# 开发者 haotian
# 开发时间: 2022/5/28 16:56


'''
repr() 返回开发者理解的对象的字符串表示形式 --- 带有类型？？
str() 返回用户理解的的对象的字符串表示形式 --- 单纯值？？
有什么不同啊？？
bytes() 返回对象的字节序列表示形式
'''
# a = 'abc'
# b = ['1', '2', '3']
# print(repr(a), str(a), repr(b), str(b))


from array import array
import math


class Vector2d:
    typecode = 'd'

    def __init__(self, x, y):
        # self 代表类实例本身
        self.x = float(x)
        self.y = float(y)
        print(self)

    def __iter__(self):
        return (i for i in (self.x, self.y))

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format((class_name, *self))

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + bytes(array(self.typecode, self)))

    def __eq__(self, other):
        return tuple(self) == tuple(other)

    def __abs__(self):
        return math.hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))


v_1 = Vector2d(1, 2)
print(v_1)