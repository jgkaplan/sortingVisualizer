from visualize import GraphicsVis
from sorter import *
from wrapped_array import WrappedArray

def main(visualizer, sorts_f, size):
	visualizer.init()

	visualizer.exit()

if __name__ == '__main__':
	# main(visualizer=GraphicsVis(), sort_f=sorts.selection, size=50)
	s = BubbleSorter()
	baseArray = [4,2,5,3,1]
	arr = WrappedArray(baseArray)
	print("Start:")
	print(arr.arr)
	print()
	s.sort(arr)
	print("End:")
	print(arr.arr)