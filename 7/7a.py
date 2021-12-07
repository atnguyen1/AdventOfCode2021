import sys
import numpy as np

with open('7.input.txt', 'r') as fh:
	data = [int(x) for x in fh.read().split(',')]
	median = int(np.median(data))
	fuel_costs = [abs(x - median) for x in data]
	print(fuel_costs)
	print(sum(fuel_costs))