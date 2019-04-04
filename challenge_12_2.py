import math

class Circle:
    def __init__(self, r):
        self.r = r
    
    def area(self):
        return math.pi * self.r**2

class Triangle:
    def __init__(self, l, h):
        self.l = l
        self.h = h

    def area(self):
        return 1/2 * self.l * self.h

class Hexagon:
    def __init__(self, r):
        self.r = r

    def calculate_perimeter(self):
        return 6 * self.r

h = Hexagon(1)
print(h.calculate_perimeter())