from visualize_interface import Visualizer
from graphics import *

class NoVis(Visualizer):
	def __init__(self, initial_data=[]):
		pass

	def set(self, key, val):
		pass

	def focus(self, *elts):
		pass

	def clear_focus(self):
		pass

	def exit(self):
		pass

class BarVis(Visualizer):
	def __init__(self, initial_data=[]):
		self.BAR_SIZE = 10
		self.BAR_GAP = 2
		self.PADDING = 5
		self.BASE_COLOR = 'blue'
		self.FOCUS_COLOR = 'lightgreen'
		self.BACKGROUND_COLOR = 'gray'

		s = len(initial_data)
		size_x = 2 * self.PADDING + self.BAR_SIZE * s + self.BAR_GAP * (s-1)
		size_y = 2 * self.PADDING + self.BAR_SIZE * s

		self.win = GraphWin("Sorting visualizer", size_x, size_y)
		self.win.setBackground(self.BACKGROUND_COLOR)
		self.win.yUp() #right side up coordinates
		self.focused = set()

		self.data = [None] * len(initial_data)
		for (key, val) in enumerate(initial_data):
			x1 = self.PADDING + key * (self.BAR_SIZE + self.BAR_GAP)
			x2 = x1 + self.BAR_SIZE 
			y1 = self.PADDING
			y2 = val * self.BAR_SIZE + self.PADDING
			self.data[val-1] = Rectangle(Point(x1,y1), Point(x2,y2))
			self.data[val-1].setFill(self.BASE_COLOR)
			self.data[val-1].draw(self.win)

	def set(self, key, val):
		x = self.PADDING + key * (self.BAR_SIZE + self.BAR_GAP)
		dx = x - self.data[val-1].getP1().getX()
		self.data[val-1].move(dx, 0)
		
	def focus(self, *elts):
		for x in self.focused:
			if x not in elts:
				self.data[x-1].setFill(self.BASE_COLOR)
		self.focused = set()
		for x in elts:
			rect = self.data[x-1]
			rect.setFill(self.FOCUS_COLOR)
			self.focused.add(x)

	def exit(self):
		self.win.promptClose(self.win.getWidth()/2, self.win.getHeight() - 20)

