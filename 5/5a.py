import sys
import numpy as np
from itertools import chain

entries = list()

with open('5.input.txt', 'r') as fh:
	entries = fh.read().split('\n')

max_x = 0
max_y = 0

processed_entries = list()

# Clean up data

for e in entries:
	elist = list(chain.from_iterable([i.split(',') for i in e.split(' -> ')]))
	elist = [int(x) for x in elist]
	processed_entries.append(elist)
	x1,y1,x2,y2 = elist
	# Find bounds for numpy array
	if x1 > max_x:
		max_x = x1
	if x2 > max_x:
		max_x = x2
	if y1 > max_y:
		max_y = y1
	if y2 > max_y:
		max_y = y2

arr = np.zeros((int(max_x) + 1, int(max_y) + 1))

for p in processed_entries:
	x1,y1,x2,y2 = p

	if x1 == x2:
		# Horizontal
		draw_length = abs(y1 - y2)
		if y1 > y2:
			ystart = y2
		else:
			ystart = y1
		for y in range(draw_length + 1):
			arr[ystart + y, x1] += 1
	elif y1 == y2:
		# Vertical
		draw_length = abs(x1 - x2)
		if x1 > x2:
			xstart = x2
		else:
			xstart = x1
		for x in range(draw_length + 1):
			arr[y1, xstart + x] += 1
	else:
		# Diaganol
		print('Ack Diaganol')

print(arr)
points = np.argwhere(arr > 1)
print(points)
print(len(points))
 