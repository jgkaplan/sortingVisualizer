from visualize_interface import Visualizer
from graphics import *

class GraphicsVis(Visualizer):
	def __init__(self, width, height, num_elts):
		self.win = GraphWin("Sorting visualizer", width, height)
		self.win.yUp() #right side up coordinates
		self.data = [None] * num_elts


	def exit(self):
		self.win.close()