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


with open('17.test.txt', 'r') as fh:
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
    y_max = max(y1, y2) + 1
    target = defaultdict(list)
    ymax = dict()

    max_y_stride = (y2 - y1)

    for z in range(x_max):
        for w in range(500):    # Arbitrary brute force y vel
            position = (0, 0)
            xvel = z
            yvel = w

            current_ymax = 0
            within_target = False

            # print(position)

            while position[1] <= x_max and position[0] >= y_max:
                new_position, newxvel, newyvel = step(position, xvel, yvel)

                if new_position[0] > current_ymax:
                    current_ymax = new_position[0]

                # print(new_position, newxvel, newyvel, within(new_position, target_area))

                if within(new_position, target_area):
                    within_target = True
                    break
                position = new_position
                xvel = newxvel
                yvel = newyvel

            if within_target:
                target[current_ymax].append((w, z))

    print(target.keys())
    print(max(target.keys()))
    sys.exit()
    for t in sorted(target.keys()):
        print(t, target[t])