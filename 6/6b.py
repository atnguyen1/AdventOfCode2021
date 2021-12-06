import sys
from collections import deque

with open('6.input.txt', 'r') as fh:
	data = [int(x) for x in fh.read().split(',')]

	fish_counter = deque([0] * 9)

	for d in data:
		fish_counter[d] += 1

	#print(fish_counter)

	days = 256

	for d in range(days):
		fish_hatch = fish_counter.popleft()

		#print(fish_hatch)
		#print(fish_counter)

		fish_counter[6] += fish_hatch
		fish_counter.append(fish_hatch)

		#print(fish_counter)
	print(sum(fish_counter))