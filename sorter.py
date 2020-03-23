from abc import ABC, abstractmethod

class Sorter(ABC):
	@abstractmethod
	def sort(arr):
		#In place sort of array
		pass

	@classmethod
	def __subclasshook__(cls, C):
		if cls is Sorter:
			if any("sort" in B.__dict__ for B in C.__mro__):
				return True
		return NotImplemented


class BubbleSorter(Sorter):
	def sort(self, arr):
		for i in range(len(arr)-1):
			for j in range(len(arr)-1):
				if arr[j] > arr[j+1]:
					arr.swap(j, j+1)