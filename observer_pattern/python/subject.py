import abc

class Subject(abc.ABC):

	@abc.abstractmethod
	def registerObserver(self):
		''' Add a subscriber to be notified of updates '''
	@abc.abstractmethod
	def removeObserver(self):
		''' Remove a subscriber so they will no longer be notified '''
	@abc.abstractmethod
	def notiyObservers(self):
		''' Notify all the current subscribers '''


class WeatherData(Subject):
	def __init__(self):
		self._observers = {}
		self._temperature = 0.0
		self._humidity = 0.0
		self._pressure = 0.0

	def registerObserver(self, observer):
		self._observers.add(observer)

	def removeObserver(self, observer):
		self._observers.remove(observer)

	def notifyObservers(self):
		for observer in self._observers:
			observer.update(self._temperature, self._humidity, self._pressure)

	def measurementsChanged(self):
		notifyObservers()

	def setMeasurements(self, temperature, humidity, pressure):
		self._temperature = temperature
		self._humidity = humidity
		self._pressure = pressure
		measurementsChanged()