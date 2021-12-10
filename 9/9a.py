import sys
import numpy as np

def lowpoint(y, x, matrix):
	ymax, xmax = matrix.shape
	val = matrix[(y, x)]

	top = (y - 1, x)
	bottom = (y + 1, x)
	left = (y, x - 1)
	right = (y, x + 1)

	if y == 0:
		top = None
	if y == (ymax - 1):
		bottom = None
	if x == 0:
		left = None
	if x == (xmax - 1):
		right = None

	points = [top, bottom, left, right]
	points = [x for x in points if x is not None]

	bool_vector = []
	for p in points:
		if matrix[p] > val:
			bool_vector.append(True)
		else:
			bool_vector.append(False)

	if False in bool_vector:
		return False
	else:
		return True


with open('9.input.txt', 'r') as fh:
	m = fh.read().split('\n')
	m = [list(i) for i in m]
	m = np.array(m)
	m = m.astype(int)
	ydim, xdim = m.shape

	low = []
	low_vals = []

	for y in range(0, ydim):
		for x in range(0, xdim):
			if lowpoint(y, x, m):
				low.append((y, x))
				low_vals.append(1 + m[(y, x)])

	print(low)
	print(low_vals)
	print(sum(low_vals))