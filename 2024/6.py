from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    m = [list(i) for i in L]
    HelperTab(m)

    starti = 0
    startj = 0
    for i in range(MAX_X()):
        for j in range(MAX_Y()):
            if m[i][j] == '^':
                starti = i
                startj = j
                m[i][j] = 'x'

    p1 = path(m,starti,startj)
    Pr(p1)

    c = set()
    for i in range(MAX_X()):
        for j in range(MAX_Y()):
            if m[i][j] == 'x' and not (starti == i and startj == j):
                if blockpath(m,i,j,starti,startj):
                    c.add((i,j))
    p2 = len(c)
    Pr(p2)

def blockpath(m, bi, bj, i, j):
    direction = Dir4()
    cd = 0
    toBlock = bi,bj
    visited = set()
    while True:
        nxti,nxtj = i + direction[cd][0], j + direction[cd][1]
        if IsOutOfBounds(nxti,nxtj):
            return False
        if m[nxti][nxtj] == '#' or (nxti == toBlock[0] and nxtj == toBlock[1]):
            cd = (cd + 1) % len(direction)
            continue
        if (i,j,cd) in visited:
            return True
        visited.add((i,j,cd))
        i,j = nxti,nxtj

def path(m,i,j):
    c = 1
    direction = Dir4()
    cd = 0
    while True:
        nxti,nxtj = i + direction[cd][0], j + direction[cd][1]
        if IsOutOfBounds(nxti,nxtj):
            return c
        if not m[nxti][nxtj] == '.' and not m[nxti][nxtj] == 'x':
            cd = (cd + 1) % len(direction)
            continue
        i,j = nxti,nxtj
        if m[i][j] != 'x':
            c += 1
            m[i][j] = 'x'

if __name__ == '__main__':
    main()
