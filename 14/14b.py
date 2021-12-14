import sys
from collections import Counter, defaultdict


with open('14.input.txt', 'r') as fh:
    formula, rules = fh.read().split('\n\n')
    formula = list(formula)
    rules = rules.split('\n')
    rule_dict = dict()
    for r in rules:
        a, b = r.split(' -> ')
        rule_dict[a] = b

    print('Starting Formula:', ''.join(formula))

    pair_counts = Counter()

    # Parse initial formula
    for n in range(len(formula) - 1):
        pair_counts[''.join(formula[n:n + 2])] += 1

    loop = 0
    total_loop = 40
    # print('Starting Pairs', pair_counts)

    while loop < total_loop:
        new_pair_counts = Counter()
        for key in pair_counts:
            if key in rule_dict:
                new_pair1 = key[0] + rule_dict[key]
                new_pair2 = rule_dict[key] + key[1]
                new_pair_counts[new_pair1] += pair_counts[key]
                new_pair_counts[new_pair2] += pair_counts[key]
 
        loop += 1
        pair_counts = new_pair_counts
        # print(loop, pair_counts)

    total_counter = Counter()
    for key in pair_counts:
        counts = pair_counts[key]
        total_counter[key[0]] += counts
        total_counter[key[1]] += counts

    # Fix for double counting pairs, add 1 for the first and last so your final number is halved
    total_counter[formula[0]] += 1
    total_counter[formula[-1]] += 1

    mc = total_counter.most_common()
    print('Diff', (mc[0][1] - mc[-1][1]) / 2)
