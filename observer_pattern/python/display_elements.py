import abc
import observer

class DisplayElement(abc.ABC):
	@abc.abstractmethod
	def display(self):
		''' Displays relevent information '''


class CurrentConditionsDisplay(observer, display):
	def display(self):

	def update(self):


class ForecastDisplay(observer, display):
	def display(self):

	def update(self):


class StatisticsDisplay(observer, display):
	def display(self):

	def update(self):