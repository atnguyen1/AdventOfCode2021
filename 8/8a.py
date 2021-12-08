import sys
from collections import Counter

test = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'

'''

1 Uses 2 Signals
4 Uses 4 Signals
7 Uses 3 Signals
8 Uses 7 Signals



0 Uses 6 Signals

2 Uses 5 Signals
3 Uses 5 Signals

5 Uses 5 Signals
6 Uses 6 Signals


9 Uses 6 Signals

'''


with open('8.input.txt', 'r') as fh:
	data = fh.read().split('\n')

	count = 0

	for d in data:
		output = d.split('|')[1].lstrip().rstrip()
		output_l = [len(x) for x in output.split(' ')]

		for o in output_l:
			if o in [2, 4, 3, 7]:
				count += 1

	print(count)