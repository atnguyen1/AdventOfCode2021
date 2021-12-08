import sys

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

 0 1 2 3 4 5 6
[0 0 0 0 0 0 0]

[1 1 1 0 1 1 1]   0
[0 0 1 0 0 1 0]   1    
[1 0 1 1 1 0 1]   2
[1 0 1 1 0 1 1]   3
[0 1 1 1 0 1 0]   4
[1 1 0 1 0 1 1]   5
[1 1 0 1 1 1 1]   6
[1 0 1 0 0 1 0]   7
[1 1 1 1 1 1 1]   8
[1 1 1 1 0 1 1]   9


1. Find the 1 digit,
2. Find the 2 / 5 digit compare to 1 digit only 1 char difference,  this fixes position 2 and 5
3a The 3 digit contains 1 signals

3. Find 7 digit, this fixes position 0
4. Find 4 digit
5. Find 3 digit 

  0:      1:      2:      3:      4:
 aaaa    ....    aaaa    aaaa    ....
b    c  .    c  .    c  .    c  b    c
b    c  .    c  .    c  .    c  b    c
 ....    ....    dddd    dddd    dddd
e    f  .    f  e    .  .    f  .    f
e    f  .    f  e    .  .    f  .    f
 gggg    ....    gggg    gggg    ....

  5:      6:      7:      8:      9:
 aaaa    aaaa    aaaa    aaaa    aaaa
b    .  b    .  .    c  b    c  b    c
b    .  b    .  .    c  b    c  b    c
 dddd    dddd    ....    dddd    dddd
.    f  e    f  .    f  e    f  .    f
.    f  e    f  .    f  e    f  .    f
 gggg    gggg    ....    gggg    gggg

'''

seven_seg = {'1110111': 0,
			 '0010010': 1,
			 '1011101': 2,
			 '1011011':3,
			 '0111010':4,
			 '1101011':5,
			 '1101111':6,
			 '1010010':7,
			 '1111111':8,
			 '1111011':9}

def get_index(l, val):
	return [i for i, x in enumerate(l) if x == val]

with open('8.input.txt', 'r') as fh:
	data = fh.read().split('\n')

	output_sums = 0

	for d in data:
		input_signals, output_signals = d.split(' | ')
		input_signals = input_signals.split(' ')
		output_signals = output_signals.split(' ')

		lookup = dict()
		signal_vector = [0] * 7

		sigs = input_signals
		sigs_len = [len(s) for s in sigs]

		lookup[1] = set(sigs[get_index(sigs_len, 2)[0]])
		lookup[4] = set(sigs[get_index(sigs_len, 4)[0]])
		lookup[7] = set(sigs[get_index(sigs_len, 3)[0]])
		lookup[8] = set(sigs[get_index(sigs_len, 7)[0]])

		five_sigs = [set(sigs[x]) for x in get_index(sigs_len, 5)]  # 2,3,5
		six_sig = [set(sigs[x]) for x in get_index(sigs_len, 6)]   # 0,6,9

		# Find 3
		for i in five_sigs:
			if len(lookup[1].difference(i)) == 0:
				lookup[3] = i

		# Determine 'A' locaation
		signal_vector[0] = lookup[7].difference(lookup[1])

		# Determine 'C', 'F' location
		for i in six_sig:
			a = lookup[1].difference(i)
			if len(a) == 1:
				signal_vector[2] = a
				signal_vector[5] = lookup[1].difference(a)
				lookup[6] = i

		# Determine 'G' location and 'D' location
		c = lookup[3].difference(lookup[7])   # Subtract 7 locations and 4 locations
		signal_vector[6] = c.difference(lookup[4])
		signal_vector[3] = c.intersection(lookup[4])
		signal_vector[1] = lookup[4].difference(lookup[3])

		alphas = set(['a', 'b', 'c', 'd', 'e', 'f', 'g'])
		found = set().union(*(signal_vector[0:4] + signal_vector[5:]))

		signal_vector[4] = alphas.difference(found)
		signal_vector = [list(x)[0] for x in signal_vector]
		signal_vector_index = dict(zip(signal_vector, range(0,7)))

		# print(signal_vector)
		# print(signal_vector_index)

		output_number = list()
		for o in output_signals:
			o = list(o)
			# print(o)

			output = [signal_vector_index[i] for i in o]
			output_digit = [0] * 7

			# print(output)

			for i in output:
				output_digit[i] = 1

			# print(output_digit)

			output_digit = ''.join([str(i) for i in output_digit])
			output_number.append(output_digit)


		# print(output_number)
		output_number = [seven_seg[i] for i in output_number]
		full_number = int(''.join([str(x) for x in output_number]))
		print(full_number)
		output_sums += full_number

	print('Total', output_sums)