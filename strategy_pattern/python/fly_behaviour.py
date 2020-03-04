import abc

class FlyBehaviour(abc.ABC):
	@abc.abstractmethod
	def fly(self):
		""" Makes your duck fly """

class FlyWithWings(FlyBehaviour):
	def fly(self):
		print("I'm flying with my wings Jack")

class FlyWithRockets(FlyBehaviour):
	def fly(self):
		print("I'm flying with rockets Jack")

class FlyNoWay(FlyBehaviour):
	def fly(self):
		print("Jack I can't fly")