import sys
from collections import deque

with open('10.input.txt', 'r') as fh:
    data = fh.read().split('\n')
    matches = {'(': ')', '[': ']', '{': '}', '<': '>'}
    opens = ['(', '[', '{', '<']
    close = [')', ']', '}', '>']
    
    score_lookup = {')': 3, ']': 57, '}': 1197, '>': 25137}
    fix_lookup = {')': 1, ']': 2, '}': 3, '>': 4}
    score = 0
    fix_score_list = list()

    corrupted = list()

    for z, d in enumerate(data):
        vals = list(d)
        corrupted = False
        fix_score = 0

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
                        corrupted = True
                        break

        if (not corrupted) and (len(stack) > 0):
            # Fix incomplete

            fix = list()
            while stack:
                fix.append(matches[stack.pop()])

            for f in fix:
                fix_score = fix_score * 5
                fix_score += fix_lookup[f]

        if fix_score > 0:
            fix_score_list.append(fix_score)

    fix_score_list = sorted(fix_score_list)
    l = len(fix_score_list)
    mid = int((l - 1) / 2)
    print(fix_score_list[mid])