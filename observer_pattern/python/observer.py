import abc

class Observer(abc.ABC):

	@abc.abstractmethod
	def update(self):
		''' Updates the observer with new information from the subject '''
	