import abc

class QuackBehaviour(abc.ABC):
	@abc.abstractmethod
	def quack(self):
		""" Makes your duck quak """

class Quack(QuackBehaviour):
	def quack(self):
		print("Quak!")

class Squeak(QuackBehaviour):
	def quack(self):
		print("Squeak!")

class MuteQuack(QuackBehaviour):
	def quack(self):
		print("...")
