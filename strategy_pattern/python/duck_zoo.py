from duck import Duck
from quak_behaviour import *
from fly_behaviour import *


class MallardDuck(Duck):

	def __init__(self):
		self._quak_behaviour = Quack()
		self._fly_behaviour = FlyWithWings()

	def display(self):
		print("This is a Mallard Duck")
		self.preform_fly()
		self.preform_quack()

class RubberDuck(Duck):

	def __init__(self):
		self._quak_behaviour  = Squeak()
		self._fly_behaviour = FlyNoWay()

	def display(self):
		print("This is a Rubber Duck")
		self.preform_fly()
		self.preform_quack()


class DecoyDuck(Duck):

	def __init__(self):
		self._quak_behaviour  = MuteQuack()
		self._fly_behaviour = FlyNoWay()

	def display(self):
		print("This is a Wooden Decoy Duck")
		self.preform_fly()
		self.preform_quack()