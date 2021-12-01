from collections import Counter

depths = Counter()
prev = None
with open('1A.input.txt', 'r') as fh:
	for line in fh:
		line = line.rstrip()
		line = int(line)
		if prev is None:
			prev = line
			print(line, 'N/A')
		else:
			if line > prev:
				depths['Increased'] += 1
				print(line, 'Increased')
			elif line < prev:
				depths['Decreased'] += 1
				print(line, 'Decreased')
			prev = line

print(depths)
