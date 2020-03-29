import collections
import visualizers
from collections.abc import MutableSequence

class WrappedArray(collections.abc.MutableSequence):
	def __init__(self, initial=[], visualizer=visualizers.NoVis):
		self.arr = initial
		self.vis = visualizer(initial)

	def __getitem__(self, key):
		# self.vis.focus(self.arr[key])
		return self.arr[key]

	def __setitem__(self, key, val):
		self.arr[key] = val
		self.vis.set(key, val)
		self.vis.focus(self.arr[key])

	def __delitem__(self, key):
		self.arr.pop(key)

	def __len__(self):
		return len(self.arr)

	def cleanup(self):
		self.vis.exit()

	def insert(self, key, val):
		self.arr.insert(key,val)
		self.vis.set(key,val)

	# <0 if arr[i] < arr[j]
	# =0  if arr[i] == arr[j]
	# >0  if arr[i] > arr[j]
	def compare(self, i, j):
		self.vis.focus(self.arr[i], self.arr[j])
		return self.arr[i] - self.arr[j]

	def swap(self, i, j):
		self.arr[i], self.arr[j] = self.arr[j], self.arr[i]
		self.vis.set(i, self.arr[i])
		self.vis.set(j, self.arr[j])
		self.vis.focus(self.arr[i], self.arr[j])