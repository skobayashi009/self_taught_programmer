class Horse:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner

class Rider:
    def __init__(self, name):
        self.name = name

r = Rider("Tom")
h= Horse("John", r)
print(h.owner.name)