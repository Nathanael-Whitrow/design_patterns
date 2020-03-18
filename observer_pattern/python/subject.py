import abc

class Subject(abc.ABC):

	@abc.abstractmethod
	def registerObserver(self):
		''' Add a subscriber to be notified of updates '''
	@abc.abstractmethod
	def removeObserver(self):
		''' Remove a subscriber so they will no longer be notified '''
	@abc.abstractmethod
	def notiyObserver(self):
		''' Notify all the current subscribers '''