import collections
from collections.abc import MutableSequence

class WrappedArray(collections.abc.MutableSequence):
	def __init__(self, initial=[], visualizer=None):
		self.arr = initial
		self.vis = visualizer

	def __getitem__(self, key):
		self.vis.focus(self.arr[key])
		return self.arr[key]

	def __setitem__(self, key, val):
		self.arr[key] = val
		self.vis.put(key, val)
		self.vis.focus(self.arr[key])

	def __delitem__(self, key):
		self.arr.pop(key)
		self.vis.remove(key)

	def __len__(self):
		return len(self.arr)

	def insert(self, key, val):
		self.arr.insert(key,val)
		self.vis.put(key,val)


	def swap(self, i, j):
		self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
		self.vis.put(i, self.arr[i])
		self.vis.put(j, self.arr[j])
		self.vis.focus(self.arr[i], self.arr[j])