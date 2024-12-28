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
    for t in range(1000):
        for i in range(MAX_X()):
            for j in range(MAX_Y()):
                m[i][j] += 1
        f = 0
        for i in range(MAX_X()):
            for j in range(MAX_Y()):
                if m[i][j] > 9:
                    f += flash(m,i,j)
        if t < 100:
            p1 += f
        if checkAllFlash(m):
            break

    Pr(p1)
    p2 = t+1
    Pr(p2)

def checkAllFlash(m):
    for i in range(MAX_X()):
        for j in range(MAX_Y()):
            if m[i][j] != 0:
                return False
    return True

def flash(m,i,j):
    f = 1
    m[i][j] = 0
    for x,y in Dir8():
        ii = i + x
        jj = j + y
        if IsOutOfBounds(ii,jj) or m[ii][jj] == 0:
            continue
        m[ii][jj] += 1
        if m[ii][jj] > 9:
            f += flash(m,ii,jj)
    return f

if __name__ == '__main__':
    main()
