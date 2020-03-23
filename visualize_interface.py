from abc import ABC, abstractmethod

class Visualizer(ABC):
	@abstractmethod
	def __init__(self, width, height, num_elts):
		pass

	@abstractmethod
	def meow(self):
		pass

	@abstractmethod
	def exit(self):
		pass