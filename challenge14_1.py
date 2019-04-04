class  Square:
    square_list = []

    def __init__(self, l):
        self.l = l
        self.square_list.append(self)

    def __repr__(self):
        return "{} by {} by {} by {}".format(self.l, self.l, self.l, self.l)

s = Square(29)
print(s)
print("")
a = Square(5)
print(Square.square_list)