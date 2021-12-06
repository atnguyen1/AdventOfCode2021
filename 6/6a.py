import sys
import numpy

def cycle(state):
	# Won't work too slow
	new_state = list()
	new_fish_count = 0
	for s in state:
		if s == 0:
			new_state.append(6)
			new_fish_count += 1
		else:
			new_state.append(s - 1)

	for x in range(new_fish_count):
		new_state.append(8)

	return new_state

with open('6.input.txt', 'r') as fh:
	data = [int(x) for x in fh.read().split(',')]

	print(data)
	d2 = data
	for x in range(0, 80):
		d2 = cycle(d2)

	print(len(d2))

