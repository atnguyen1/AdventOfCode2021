instructions = list()
with open("2.input.txt", 'r') as fh:
	for line in fh:
		line = line.rstrip().split(' ')
		instructions.append((line[0], int(line[1])))

# Depth, X
position = [0, 0]

for i in instructions:
	if i[0] == 'forward':
		position[1] += i[1]
	elif i[0] == 'down':
		position[0] += i[1]
	elif i[0] == 'up':
		position[0] -= i[1]

print(position)
print(position[0] * position[1])