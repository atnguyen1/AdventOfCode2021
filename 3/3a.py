import sys
from collections import Counter

data = list()
position_map = list()

with open('3.input.txt', 'r') as fh:
	data = fh.read().split('\n')
	data = [list(x) for x in data]
	for pos in data[0]:
		position_map.append(Counter())

for d in data:
	for index, char in enumerate(d):
		position_map[index][char] += 1

gamma = list()
epsilon = list()

for i, c in enumerate(position_map):
	sums = c.most_common(2)
	gamma.append(sums[0][0])
	epsilon.append(sums[1][0])

gamma = ''.join(gamma)
epsilon = ''.join(epsilon)
gamma_dec = int(gamma, 2)
epsilon_dec = int(epsilon, 2)
power_consumption = gamma_dec * epsilon_dec


print(gamma, gamma_dec)
print(epsilon, epsilon_dec)
print(power_consumption)