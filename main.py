import visualizers
import sorts
from wrapped_array import WrappedArray
from random import shuffle
from time import sleep

def main(Visualizer, Sort_class, size):
	baseArray = [i for i in range(1,size+1)]
	shuffle(baseArray)
	vis = Visualizer(baseArray)
	s = Sort_class()
	wrapped = WrappedArray(baseArray, vis)
	s.sort(wrapped)
	vis.exit()

#requirements: array of length n has elements (1, 2, ... n)

if __name__ == '__main__':
	main(Visualizer=visualizers.BarVis, Sort_class=sorts.Bubble, size=10)