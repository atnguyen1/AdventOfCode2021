import sys
from collections import deque

with open('10.input.txt', 'r') as fh:
    data = fh.read().split('\n')
    matches = {'(': ')', '[': ']', '{': '}', '<': '>'}
    opens = ['(', '[', '{', '<']
    close = [')', ']', '}', '>']
    score_lookup = {')': 3, ']': 57, '}': 1197, '>': 25137}
    score = 0

    corrupted = list()

    for z, d in enumerate(data):
        vals = list(d)

        stack = deque()
        for v in vals:
            if v in opens:
                stack.append(v)
            elif v in close:
                pos = close.index(v)

                if (len(stack) > 0):
                    if opens[pos] == stack[-1]:   
                        stack.pop()
                    else:
                        # Corrupted
                        corrupted.append(z)
                        score += score_lookup[v]
                        break
    print(score)