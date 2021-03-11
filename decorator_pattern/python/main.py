from beverages import *
from condiments import *

def main():
    print("**************************************")
    print("Hello and Welcome to StarButts Coffee!")
    print("**************************************")
    print("What do the customers want?")
    
    print("Espresso")
    beverage = Espresso()
    print(f"{beverage.get_description()}: ${beverage.cost()}")

    print("Double Mocha House Blend")
    beverage = HouseBlend()
    beverage = Mocha(beverage)
    beverage = Mocha(beverage)
    print(f"{beverage.get_description()}: ${beverage.cost()}")

    print("Soy Mocha Dark Roast with Whipped Cream")
    beverage = DarkRoast()
    beverage = Soy(beverage)
    beverage = Mocha(beverage)
    beverage = Whip(beverage)
    print(f"{beverage.get_description()}: ${beverage.cost()}")

if __name__ == '__main__':
    main()