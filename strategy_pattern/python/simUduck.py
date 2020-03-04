from duck_zoo import *

def print_heading(message):
	print("="*30)
	print(message)
	print("="*30)

def main():
	print_heading("Mallard Duck Test")
	duck1 = MallardDuck()
	duck1.display()

	print_heading("Rubber Duck Test")
	duck2 = RubberDuck()
	duck2.display()

	print_heading("Wooden Duck Test - Dynamic Fly Method")
	duck3 = DecoyDuck()
	duck3.display()
	duck3.set_fly_behaviour(FlyWithRockets())
	duck3.display()

	print_heading("Rubber Duck Test - Dynamic Quack Method")
	duck4 = RubberDuck()
	duck4.display()
	duck4.set_quack_behaviour(Quack())
	duck4.display()


if __name__ == '__main__': main()
