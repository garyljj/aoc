
from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    m = [list(map(int,i)) for i in L]
    HelperTab(m)

    p1 = 0
    p2 = 0
    for i in range(MAX_X()):
        for j in range(MAX_Y()):
            if m[i][j] == 0:
                p1 += solve(m, i, j, set())
                p2 += solve(m, i, j, None)
    Pr(p1)
    Pr(p2)

def solve(m, i, j, visited):
    if visited is not None:
        if (i,j) in visited:
            return 0
        visited.add((i,j))
    if m[i][j] == 9:
        return 1
    c = 0
    dir = Dir4()
    for a,b in dir:
        ni, nj = i + a, j + b
        if IsOutOfBounds(ni,nj):
            continue
        if m[ni][nj] == m[i][j] + 1:
            c += solve(m, ni, nj, visited)
    return c

if __name__ == '__main__':
    main()
