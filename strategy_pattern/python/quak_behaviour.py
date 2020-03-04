import abc

class QuakBehaviour(abc.ABC):
	@abc.abstractmethod
	def quack(self):
		""" Makes your duck quak """

class Quack(QuakBehaviour):
	def quack(self):
		print("Quak!")

class Squeak(QuakBehaviour):
	def quack(self):
		print("Squeak!")

class MuteQuack(QuakBehaviour):
	def quack(self):
		print("...")