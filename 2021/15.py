from helper import *
import os
import sys
import heapq
# from collections import deque
import time

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    m = [list(map(int,i)) for i in L]
    HelperTab(m)

    p1 = solve(m)
    Pr(p1)

    # if mag get too big, should implement to compute the cells
    # instead of literally expanding the map
    mag = 5
    bigm = [[0]*MAX_Y()*mag for _ in range(MAX_X()*mag)]
    for i in range(MAX_X() * mag):
        for j in range(MAX_Y() * mag):
            offset = i//MAX_X() + j//MAX_Y()
            v = m[i%MAX_X()][j%MAX_Y()]
            bigm[i][j] = (v + offset - 1) % 9 + 1
    HelperTab(bigm)
    
    p2 = solve(bigm)
    Pr(p2)

def solve(m):
    start,end=(0,0),(MAX_X()-1,MAX_Y()-1)

    q = [(0, start[0], start[1])]
    visited = set()

    while True:
        if len(q) == 0:
            assert 0, 'no path'

        c,i,j = heapq.heappop(q)
        if (i,j) == end:
            return c

        if (i,j) in visited:
            continue
        visited.add((i,j))

        for x,y in Dir4():
            ii = i + x
            jj = j + y
            if IsOutOfBounds(ii,jj):
                continue
            heapq.heappush(q, (c + m[ii][jj], ii, jj))

if __name__ == '__main__':
    main()
