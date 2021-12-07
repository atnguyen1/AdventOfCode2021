import sys
import numpy as np

with open('7.input.txt', 'r') as fh:
	data = [int(x) for x in fh.read().split(',')]
	firstquant = int(np.quantile(data, 0.25))
	thirdquant = int(np.quantile(data, 0.75))
	#print(firstquant)
	#print(thirdquant)
	
	all_costs = dict()
	for horizontal in range(firstquant, thirdquant):
		fuel_costs = [sum(range(0, abs(x - horizontal) + 1)) for x in data]
		#print(fuel_costs)
		#print(sum(fuel_costs))
		sfc = sum(fuel_costs)
		all_costs[sfc] = horizontal

	print(min(all_costs.keys()))