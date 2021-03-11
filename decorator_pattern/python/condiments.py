from beverages import Beverage

class CondimentDecorator(Beverage):    
    def get_description(self):
        return self._beverage.get_description() + ", " + self._name
    
    def cost(self):
        return self._cost + self._beverage.cost()

class SteamedMilk(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
        self._name = "Steamed Milk"
        self._cost = 0.1

class Mocha(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
        self._name = "Mocha"
        self._cost = 0.2

class Soy(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
        self._name = "Soy"
        self._cost = 0.15

class Whip(CondimentDecorator):
    def __init__(self, beverage: Beverage):
        self._beverage = beverage
        self._name = "Whip"
        self._cost = 0.1