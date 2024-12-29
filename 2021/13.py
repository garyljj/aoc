from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    points, folds = open(FN).read().strip().split('\n\n')

    m = set()
    for p in points.split('\n'):
        m.add(tuple(map(int,p.split(','))))

    for i,f in enumerate(folds.split('\n')):
        f = f.split('=')
        axis, n = f[0][-1], int(f[1])
        m = fold(m, axis, n)
        if i == 0:
            p1 = len(m)
        if axis == 'x':
            maxx = n
        if axis == 'y':
            maxy = n

    Pr(p1)

    # P2 only works for actual input
    display = [[' ']*maxx for _ in range(maxy)]
    for x,y in m:
        display[y][x] = 'O'
    
    for d in display:
        print(' '.join(d))

def fold(m, axis, n):
    mm = set()
    if axis == 'x':
        for x,y in m:
            if x == n:
                continue
            if x > n:
                x = n+n-x
            mm.add((x,y))
    elif axis == 'y':
        for x,y in m:
            if y == n:
                continue
            if y > n:
                y = n+n-y
            mm.add((x,y))
    else:
        assert 0, axis
    return mm

if __name__ == '__main__':
    main()
