import sys
import numpy as np

class Octopi:
	def __init__(self, field):
		self.field = field
		self.flashers = set()
		self.total_flash = 0

	def step(self):
		y_max,x_max = self.field.shape

		# Debugs
		print('Flashed', self.flashers)
		self.total_flash += len(self.flashers)
		self.flashers = set()

		# Increase Energy
		for y in range(0, y_max):
			for x in range(0, x_max):
				self.field[y, x] += 1

		flashers = np.argwhere(self.field > 9)

		while len(flashers) != 0:
			for f in flashers:
				y, x = f
				flash = (y, x)
				if flash not in self.flashers:
					self.flashers.add(flash)
					self.field[y, x] = 0
					self.iterate_neighbors(y, x)

			flashers = np.argwhere(self.field > 9)


	def iterate_neighbors(self, y, x):
		y_max,x_max = self.field.shape

		# 8 grid
		# a b c
		# d o e
		# f g h

		a = (y - 1, x - 1)
		b = (y - 1, x)
		c = (y - 1, x + 1)
		d = (y, x - 1)
		e = (y, x + 1)
		f = (y + 1, x - 1)
		g = (y + 1, x)
		h = (y + 1, x + 1)

		if y == 0:
			a = None
			b = None
			c = None
		if y == y_max - 1:
			f = None
			g = None
			h = None
		if x == 0:
			a = None
			d = None
			f = None
		if x == x_max - 1:
			c = None
			e = None
			h = None

		adjacent = [x for x in [a, b, c, d, e, f, g, h] if x is not None]

		for a in adjacent:
			y, x = a
			flashed = (y, x)
			if flashed not in self.flashers:
				self.field[a] += 1

	def print(self):
		print(self.field)

	def get_total(self):
		print(self.total_flash)

with open('11.input.txt', 'r') as fh:
	data = [list(x) for x in fh.read().split('\n')]

	field = np.array(data).astype(int)

	o = Octopi(field)
	
	for z in range(0, 101):
		print('Step', z)
		#o.print()
		o.step()
		o.get_total()