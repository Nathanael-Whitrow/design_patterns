import abc
from quack_behaviour import QuackBehaviour
from fly_behaviour import FlyBehaviour

class Duck(abc.ABC):
	""" Abstract Base Class for Ducks """

	@abc.abstractmethod
	def display(self):
		""" Shows the duck, how it flys and what sound it makes """

	def swim(self):
		""" Makes your duck swim """
		print("All ducks float and are therefore witches")

	def preform_quack(self):
		""" Makes your duck quack """
		self._quak_behaviour.quack()
		
	def preform_fly(self):
		""" Makes your duck fly """
		self._fly_behaviour.fly()

	def set_fly_behaviour(self, fly_behaviour):
		if isinstance(fly_behaviour, FlyBehaviour):
			self._fly_behaviour = fly_behaviour

	def set_quack_behaviour(self, quack_behaviour):
		if isinstance(quack_behaviour, QuackBehaviour):
			self._quak_behaviour = quack_behaviour
