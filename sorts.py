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


class Bubble(Sorter):
	def sort(self, arr):
		for i in range(len(arr)-1):
			for j in range(len(arr)-1):
				if arr.compare(j, j+1) > 0:
					arr.swap(j, j+1)

class Comb(Sorter):
	#taken from https://en.wikipedia.org/wiki/Comb_sort
	def sort(self, arr):
		length = len(arr)
		shrink = 1.3
		_gap = length
		sorted = False
		while not sorted:
			# Python has no builtin 'floor' function, so we/I just have one variable (_gap) to be shrunk,
			# and an integer variable (gap) to store the truncation (of the other variable) in and 
			# to use for stuff pertaining to indexing
			_gap /= shrink
			#gap = np.floor(_gap)
			gap = int(_gap)
			if gap <= 1:
				sorted=True
				gap=1
			# equivalent to `i = 0; while (i + gap) < length: ...{loop body}... i += 1`
			for i in range(length - gap):
				sm = gap+i
				if arr.compare(i,sm) > 0:
					arr.swap(i,sm)
					sorted = False

class Insertion(Sorter):
	def sort(self, arr):
		for i in range(1, len(arr)):
			x = arr[i]
			j = i - 1
			while j >= 0 and arr[j] > x:
				arr[j+1] = arr[j]
				j -= 1
			arr[j+1] = x

class Selection(Sorter):
	def sort(self, arr):
		for i in range(0,len(arr)-1):
			m = i
			for j in range(i+1,len(arr)):
				if arr.compare(j, m) < 0:
					m = j
			if m != i:
				arr.swap(m,i)

