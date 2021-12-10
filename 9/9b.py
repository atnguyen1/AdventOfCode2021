import sys
import numpy as np
from collections import deque

def lowpoint(y, x, matrix):
    ymax, xmax = matrix.shape
    val = matrix[(y, x)]

    top = (y - 1, x)
    bottom = (y + 1, x)
    left = (y, x - 1)
    right = (y, x + 1)

    if y == 0:
        top = None
    if y == (ymax - 1):
        bottom = None
    if x == 0:
        left = None
    if x == (xmax - 1):
        right = None

    points = [top, bottom, left, right]
    points = [x for x in points if x is not None]

    bool_vector = []
    for p in points:
        if matrix[p] > val:
            bool_vector.append(True)
        else:
            bool_vector.append(False)

    if False in bool_vector:
        return False
    else:
        return True

def valid_paths(y, x, matrix, basin_set):
    ymax, xmax = matrix.shape

    top = (y - 1, x)
    bottom = (y + 1, x)
    left = (y, x - 1)
    right = (y, x + 1)

    if y == 0:
        top = None
    if y == (ymax - 1):
        bottom = None
    if x == 0:
        left = None
    if x == (xmax - 1):
        right = None

    points = [top, bottom, left, right]
    points = [x for x in points if x is not None]

    not_peaks = list()

    for p in points:
        if matrix[p] != 9:
            if p not in basin_set:
                not_peaks.append(p)

    return not_peaks


with open('9.input.txt', 'r') as fh:
    m = fh.read().split('\n')
    m = [list(i) for i in m]
    m = np.array(m)
    m = m.astype(int)
    ydim, xdim = m.shape

    low = []
    low_vals = []

    for y in range(0, ydim):
        for x in range(0, xdim):
            if lowpoint(y, x, m):
                low.append((y, x))
                low_vals.append(1 + m[(y, x)])

    basins = list()
    for l in low:
        basin_locs = set()
        basin_locs.add(l)

        paths = valid_paths(l[0], l[1], m, basin_locs)
        paths = deque(paths)

        while len(paths) != 0:
            additional_paths = list()

            while len(paths) != 0:
                p = paths.popleft()
                basin_locs.add(p)
                additional_paths += valid_paths(p[0], p[1], m, basin_locs)

            paths += additional_paths

        basins.append(basin_locs)

    basin_size = list()

    for b in basins:
        basin_size.append(len(b))

    basin_size = sorted(basin_size, reverse=True)

    print(basin_size[0] * basin_size[1] * basin_size[2])





    # Greedy approach for low points
    # Take a single low point and recursively add till you get to a position == 9