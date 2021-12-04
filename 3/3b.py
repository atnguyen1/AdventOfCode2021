import sys
import copy
from collections import Counter

data = list()
filtered_data = list()
position_map_initial = list()

# Initialize Data structures
with open('3.input.txt', 'r') as fh:
	data = fh.read().split('\n')
	data = [list(x) for x in data]
	for pos in data[0]:
		position_map_initial.append(Counter())

filtered_data = copy.deepcopy(data)
current_inspection_index = 0

oxygen = None

# Find Oxygen
while len(filtered_data) > 1:
	position_map = copy.deepcopy(position_map_initial)

	# Count
	for d in filtered_data:
		for index, char in enumerate(d):
			position_map[index][char] += 1

	gamma = list()
	epsilon = list()
	# print('Index', current_inspection_index)
	# print(position_map)
	for i, c in enumerate(position_map):
		sums = c.most_common(2)
		if len(sums) == 1:
			gamma.append(sums[0][0])
			epsilon.append(sums[0][0])
			continue

		if sums[0][1] == sums[1][1]:    # Equal counts
			if sums[0][0] == '0':
				gamma.append(sums[1][0])    # Keep the 1
				epsilon.append(sums[0][0])  # Keep the 0
			else:
				gamma.append(sums[0][0])
				epsilon.append(sums[1][0])
		else:
			gamma.append(sums[0][0])
			epsilon.append(sums[1][0])

	# Filter List based on gamma
	# print('Gamma', gamma)
	g_filter = gamma[current_inspection_index]

	updated_list = list()
	for f in filtered_data:
		if f[current_inspection_index] == g_filter:
			updated_list.append(f)

	#for u in updated_list:
	#	print(u)

	filtered_data = updated_list

	current_inspection_index += 1

oxygen = ''.join(filtered_data[0])
print('Oxygen', oxygen, int(oxygen, 2))

# Reset Variables
filtered_data = copy.deepcopy(data)
current_inspection_index = 0

co2 = None

# Find CO2
while len(filtered_data) > 1:
	position_map = copy.deepcopy(position_map_initial)

	# Count
	for d in filtered_data:
		for index, char in enumerate(d):
			position_map[index][char] += 1

	gamma = list()
	epsilon = list()
	# print('Index', current_inspection_index)
	# print(position_map)
	for i, c in enumerate(position_map):
		sums = c.most_common(2)
		if len(sums) == 1:
			gamma.append(sums[0][0])
			epsilon.append(sums[0][0])
			continue

		if sums[0][1] == sums[1][1]:    # Equal counts
			if sums[0][0] == '0':
				gamma.append(sums[1][0])    # Keep the 1
				epsilon.append(sums[0][0])  # Keep the 0
			else:
				gamma.append(sums[0][0])
				epsilon.append(sums[1][0])
		else:
			gamma.append(sums[0][0])
			epsilon.append(sums[1][0])

	# Filter List based on gamma
	#print('Epsilon', epsilon)
	e_filter = epsilon[current_inspection_index]

	updated_list = list()
	for f in filtered_data:
		if f[current_inspection_index] == e_filter:
			updated_list.append(f)

	#for u in updated_list:
	#	print(u)

	filtered_data = updated_list

	current_inspection_index += 1

co2 = ''.join(filtered_data[0])
print('Co2', co2, int(co2, 2))
print('Final Val', int(oxygen, 2) * int(co2, 2))

'''

filtered_data = data.copy()
current_inspection_index = 0

oxygen = None
co2 = None

while len(filtered_data) > 1:
	position_map = list()

	# Count
	for d in filtered_data:
		for index, char in enumerate(d):
			position_map[index][char] += 1

	gamma = list()
	epsilon = list()

	for i, c in enumerate(position_map):
		sums = c.most_common(2)
		if sums[0][1] == sums[1][1]:    # Equal counts
			if sums[0] == '0':
				gamma.append(sums[1][0])    # Keep the 1
				epsilon.append(sums[0][0])  # Keep the 0
			else:
				gamma.append(sums[0][0])
				epsilon.append(sums[1][0])
		else:
			gamma.append(sums[0][0])
			epsilon.append(sums[1][0])

	# Filter List based on gamma and epsilon

'''