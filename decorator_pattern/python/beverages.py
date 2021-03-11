import abc

class Beverage(abc.ABC):
    def __init__(self):
        self._description = "Unknown Beverage"
    
    def get_description(self):
        return self._description

    @abc.abstractmethod
    def cost(self):
        pass
    
class Espresso(Beverage):
    def __init__(self):
        self._description = "Espresso"
    
    def cost(self):
        return 1.99

class HouseBlend(Beverage):
    def __init__(self):
        self._description = "House Blend Coffee"
    
    def cost(self):
        return 0.89

class Decaf(Beverage):
    def __init__(self):
        self._description = "Decaf"
    
    def cost(self):
        return 1.05
    
class DarkRoast(Beverage):
    def __init__(self):
        self._description = "Dark Roast Coffee"
    
    def cost(self):
        return 0.99