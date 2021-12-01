from collections import Counter

depths = Counter()
data = list()
windows = list()

with open('1A.input.txt', 'r') as fh:
	data = [int(x.rstrip()) for x in fh.read().split('\n')]

for x in range(0, len(data) - 2):
	windows.append(data[x] + data[x + 1] + data[x + 2])

print(data)
print(windows)

prev = None
for w in windows:
	if prev is None:
		prev = w
		print(w, 'N/A')
	else:
		if w > prev:
			depths['Increased'] += 1
			print(w, 'Increased')
		elif w == prev:
			depths['No Change'] += 1
			print(w, 'No Change')
		elif w < prev:
			depths['Decreased'] += 1
			print(w, 'Decreased')
		prev = w

print(depths)