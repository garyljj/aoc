from helper import *
import os
import sys
# import heapq
from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    l = list(map(lambda x: x.split(' -> '), L))

    d1 = defaultdict(int)
    d2 = defaultdict(int)
    for a,b in l:
        x1,y1 = map(int,a.split(','))
        x2,y2 = map(int,b.split(','))

        if x1 == x2 or y1 == y2:
            if y1 == y2:
                for x in range(min(x1,x2), max(x1,x2)+1):
                    d1[(x,y1)] += 1
                    d2[(x,y1)] += 1
            if x1 == x2:
                for y in range(min(y1,y2), max(y1,y2)+1):
                    d1[(x1,y)] += 1
                    d2[(x1,y)] += 1
        else:
            xs = range(x1, x2+1) if x1 < x2 else range(x1, x2-1, -1)
            ys = range(y1, y2+1) if y1 < y2 else range(y1, y2-1, -1)
            for x,y in zip(xs,ys):
                d2[(x,y)] += 1

    p1 = 0
    for v in d1.values():
        if v > 1:
            p1 += 1
    Pr(p1)
    p2 = 0
    for v in d2.values():
        if v > 1:
            p2 += 1
    Pr(p2)

if __name__ == '__main__':
    main()
