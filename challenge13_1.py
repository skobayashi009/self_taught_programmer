import math


class Shape:
    def what_am_i(self):
        print("I am a shape")


class Rectangle(Shape):
    def __init__(self, l, w):
        self.l = l
        self.w = w

    def calculate_perimeter(self):
        return 2 * (self.l + self.w)


class Square(Shape):
    def __init__(self, m):
        self.m = m

    def calculate_perimeter(self):
        return 4 * self.m

    def change_size(self, x):
        self.m = m + x


r = Rectangle(1, 2)
s = Square(1)
print(r.calculate_perimeter())
print(s.calculate_perimeter())
r.what_am_i()
s.what_am_i()