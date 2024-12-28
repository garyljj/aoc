from helper import *
import os
import sys
# import heapq
from collections import deque

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    m = [list(map(int,i)) for i in L]
    HelperTab(m)

    p1 = 0
    basins = []
    for i in range(MAX_X()):
        for j in range(MAX_Y()):
            if isLow(m,i,j):
                p1 += 1 + get(m,i,j)
                basins.append(getSize(m,i,j))

    Pr(p1)
    p2 = 1
    for b in sorted(basins)[-3:]:
        p2 *= b
    Pr(p2)

def isLow(m,i,j):
    for x,y in Dir4():
        if not IsOutOfBounds(i+x,j+y) and get(m,i+x,j+y) <= get(m,i,j):
            return False
    return True

def getSize(m,i,j):
    q = deque([(i,j)])
    visited = {(i,j)}
    s = 0
    while True:
        if len(q) == 0:
            return s
        i,j = q.popleft()
        s += 1
        for x,y in Dir4():
            ii = i + x
            jj = j + y
            if IsOutOfBounds(ii,jj) or (ii,jj) in visited or get(m,ii,jj) == 9:
                continue
            visited.add((ii,jj))
            q.append((ii,jj))

if __name__ == '__main__':
    main()
