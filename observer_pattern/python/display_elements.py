import abc
from observer import Observer

class DisplayElement(abc.ABC):
	@abc.abstractmethod
	def display(self):
		''' Displays relevent information '''


class CurrentConditionsDisplay(Observer, DisplayElement):
	def __init__(self, weatherData):
		self._temperature = 0.0
		self._humidity = 0.0
		self._weatherData = weatherData

	def display(self):
		print("Current Conditions: ", self._temperature, "C degrees and ",
									  self._humidity, "%% humidity")
	
	def update(self, temperature, humidity, pressure):
		self._temperature = temperature
		self._humidity = humidity
		display()

class ForecastDisplay(Observer, DisplayElement):
	def display(self):

	def update(self, temperature, humidity, pressure):


class StatisticsDisplay(Observer, DisplayElement):
	def display(self):

	def update(self, temperature, humidity, pressure):