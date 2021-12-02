instructions = list()
with open("2.input.txt", 'r') as fh:
	for line in fh:
		line = line.rstrip().split(' ')
		instructions.append((line[0], int(line[1])))

# Depth, X, Aim
position = [0, 0, 0]

for i in instructions:
	if i[0] == 'forward':
		position[1] += i[1]
		position[0] += (position[2] * i[1])
	elif i[0] == 'down':
		position[2] += i[1]  # Increase Aim
	elif i[0] == 'up':
		position[2] -= i[1]  # Decrease Aim

print(position)
print(position[0] * position[1])