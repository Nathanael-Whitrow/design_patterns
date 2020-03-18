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
		weatherData.registerObserver(self)

	def display(self):
		print("Current Conditions: {} C degrees and {}% humidity"
				.format(self._temperature, self._humidity))
	
	def update(self, temperature, humidity, pressure):
		self._temperature = temperature
		self._humidity = humidity
		self.display()

class ForecastDisplay(Observer, DisplayElement):
	def __init__(self, weatherData):
		self._current_pressure = 0.0
		self._last_pressure = 0.0
		self._weatherData = weatherData
		weatherData.registerObserver(self)

	def display(self):
		forecast = "Forecast: "
		if (self._current_pressure > self._last_pressure):
			forecast += "Improving weather on the way!"
		elif (self._current_pressure == self._last_pressure):
			forecast += "More of the same"
		elif (self._current_pressure < self._last_pressure):
			forecast += "Watch out for cooler, rainy weather"

	def update(self, temperature, humidity, pressure):
		self._last_pressure = self._current_pressure
		self._current_pressure = pressure
		self.display()


class StatisticsDisplay(Observer, DisplayElement):
	def __init__(self, weatherData):
		self._max_temp = 0.0
		self._min_temp = 0.0
		self._tempSum = 0.0
		self._num_readings = 1
		self._weatherData = weatherData
		weatherData.registerObserver(self)

	def display(self):
		print("Average temperature: {} Max: {} Min: {}".format(
										self._tempSum / self._num_readings,
										self._max_temp, self._min_temp ))

	def update(self, temperature, humidity, pressure):
		self._num_readings += 1
		self._tempSum += temperature
		if (temperature > self._max_temp): self._max_temp = temperature
		if (temperature < self._min_temp): self._min_temp = temperature
		self.display()