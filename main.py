import sorts
import visualize
from random import shuffle

def main(filename, sort_f, size):
	visualize.setup(size)
	arr = [i for i in range(1,size+1)]
	shuffle(arr)
	for i in sort_f(arr):
		visualize.add_step(arr, highlight=i)
	visualize.render(filename,delay=30)
	

if __name__ == '__main__':
	main(filename="selection", sort_f=sorts.selection, size=50)
	print("Finished")