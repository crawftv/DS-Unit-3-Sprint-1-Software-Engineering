import random


class Product:
    def __init__(self,  name, price=10, weight=20, flamability=0.5, \
        identifier=random.randint(1000000, 9999999)):
        self.name = name
        self.price = price
        self.weight = weight
        self.flamability = flamability
        self.identifier = identifier

    def stealability(self):
        if (self.price/self.weight) < 0.5:
            return "Not so stealable..."
        elif (self.price/self.weight) < 1.5:
            return "Kinda Stealable"
        else:
            return "very stealable"

    def explode(self):
        if self.weight*self.flamability < 10:
            return "...fizzle"
        elif self.weight*self.flamability < 50:
            return "...booom!"
        else:
            return "...BABOOOM!!"


class BoxingGlove(Product):
    def __init(self, weight=10):
        Product.__init__(self,  name, price=10, weight=10, flamability=0.5,
                         identifier=random.randint(1000000, 9999999))
        self.weight = weight


