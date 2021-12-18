import sys
import numpy as np
from collections import defaultdict


def within(position, target):
    x1, x2, y1, y2 = target
    ya, xa = position

    if x1 <= xa and xa <= x2:
        if y1 <= ya and ya <= y2:
            return True
        else:
            return False
    else:
        return False


def step(position, xvel, yvel):
    y, x = position

    x += xvel
    y += yvel

    xvel = xvel - 1
    yvel = yvel - 1

    if xvel <= 0:
        xvel = 0

    return (y, x), xvel, yvel


with open('17.input.txt', 'r') as fh:
    # Balistic Calculations
    target = fh.read().rstrip().split(':')[1].split(',')
    x1, x2 = target[0][3:].split('..')
    y1, y2 = target[1][3:].split('..')
 
    x1 = int(x1)
    x2 = int(x2)
    y1 = int(y1)
    y2 = int(y2)

    # Order it so x1 < x2 and y1 < y2
    if y1 > y2:
        y3 = y2
        y2 = y1
        y1 = y3
    if x1 > x2:
        x3 = x2
        x2 = x1
        x1 = x3

    target_area = [x1, x2, y1, y2]
    position = (0, 0)

    # field = np.zeros((100, 100)).astype(int)

    x_max = max(x1, x2) + 1    # Step size can't be larger than the target area bound
    y_max = min(y1, y2) - 1
    target = set()
    ymax = dict()

    max_y_stride = (y2 - y1)

    #test_data = None
    #with open('test.txt', 'r') as fh2:
    #    test_data = fh2.read().split()

    # test_data = sorted(test_data, key=lambda x: (int(x.split(',')[0]), int(x.split(',')[1])))

    #test_data = set(test_data)

    for z in range(x_max):
        for w in range(-500,500):    # Arbitrary brute force y vel
            position = (0, 0)
            xvel = z
            yvel = w

            current_ymax = 0
            within_target = False

            # print(position)
            # {'9,-2', '10,-2', '6,0', '7,-1', '8,-2'}

            while position[1] <= x_max and position[0] >= y_max:
                new_position, newxvel, newyvel = step(position, xvel, yvel)

                #print(new_position, newxvel, newyvel, within(new_position, target_area))

                if within(new_position, target_area):
                    within_target = True
                    break
                position = new_position
                xvel = newxvel
                yvel = newyvel

            if within_target:
                target.add(str(z) + ',' + str(w))


    #print(len(target))
    # print(test_data)
    # print(len(test_data))
    # print(sorted(list(target), key=lambda x: (int(x[0]), int(x[1]))))
    #print(sorted(list(target), key=lambda x: (int(x.split(',')[0]), int(x.split(',')[1]))))
    print(len(target))
    #test_data = set(test_data)
    #print(test_data.difference(target))
