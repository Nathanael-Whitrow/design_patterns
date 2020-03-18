import abc

class Observer(abc.ABC):

	@abc.abstractmethod
	def update(self, temperature, humidity, pressure):
		''' Updates the observer with new information from the subject '''
	