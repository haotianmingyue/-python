# 开发者 haotian
# 开发时间: 2022/5/28 21:05
import math
from array import array


class Vector2d:
    typcode = 'd'

    def __init__(self, x, y):
        # 使用 两个前导下划线，把属性标记为私有
        self.__x = float(x)
        self.__y = float(y)

    @property
    def x(self):  # 读值的方法
        return self.__x

    @property
    def y(self):  # 读值的方法
        return self.__y

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

    def angle(self):
        return math.atan2(self.y, self.x)


v_1 = Vector2d(1, 2)
print(hash(v_1))
