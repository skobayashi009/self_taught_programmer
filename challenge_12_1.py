class Apple:
    def __init__(self, weight, color, place, price):
        self.weight = weight
        self.color = color
        self.place = place
        self.price = price

    def highter_price(self):
        self.price += 100

apple = Apple(10, "dark red", "Aomori", 100)
apple.highter_price()
print(apple.price)