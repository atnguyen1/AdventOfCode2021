import sys
from collections import Counter


with open('14.input.txt', 'r') as fh:
    formula, rules = fh.read().split('\n\n')
    formula = list(formula)
    rules = rules.split('\n')
    rule_dict = dict()
    for r in rules:
        a, b = r.split(' -> ')
        rule_dict[a] = b

    print(''.join(formula))
    for x in range(10):
        pairs = list()
        for n in range(len(formula) - 1):
            pairs.append(''.join(formula[n:n + 2]))

        new_formula = list()

        for z, p in enumerate(pairs):
            if p in rule_dict:
                additions = rule_dict[p]
                plist = list(p)
                if z != (len(pairs) - 1):
                    new_formula.append(plist[0] + additions)
                else:
                    new_formula.append(plist[0] + additions + plist[1])

        new_formula = ''.join(new_formula)
        formula = new_formula
        #print(x, formula, len(formula))

    c = Counter(formula)
    counts = c.most_common()

    print(counts[0], counts[-1])
    print(counts[0][1] - counts[-1][1])