import sys
import numpy as np

with open('13.input.txt', 'r') as fh:
    points, instructions = fh.read().split('\n\n')

    points = points.split('\n')

    xmax = 0
    ymax = 0
    data_points = list()
    for p in points:
        x, y = [int(z) for z in p.split(',')]
        if x > xmax:
            xmax = x
        if y > ymax:
            ymax = y
        data_points.append((y, x))

    d = np.zeros((ymax + 1, xmax + 1))

    for p in data_points:
        d[p] = 1

    print(d)

    instructions = instructions.split('\n')



    for i in instructions:
        fold = i.split('=')
        axis = fold[0][-1]
        value = int(fold[1])
        print(fold)

        if axis == 'y':
            d2 = d[value:,:]
            #print(d2)
            d3 = np.flipud(d2)
            #print(d3)
            d4 = d[0:(value + 1),:]
            #print(d4)
            d5 = d3 + d4
            print(d5)
            print(len(np.argwhere(d5 > 0)))
        else:
            print(d)
            d2 = d[:,value:]
            print(d2)
            d3 = np.fliplr(d2)
            print(d3)
            d4 = d[:, 0:(value + 1)]
            print(d4)
            d5 = d3 + d4
            print(d5)
            print(len(np.argwhere(d5 > 0)))

        sys.exit()
