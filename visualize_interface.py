from abc import ABC, abstractmethod

class Visualizer(ABC):
	@abstractmethod
	def __init__(self, initial_data):
		pass

	@abstractmethod
	def set(self, key, val):
		pass

	@abstractmethod
	def focus(self, *elts):
		pass

	@abstractmethod
	def exit(self):
		pass