from helper import *
import os
import sys
# import heapq
from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    l = [list(i) for i in L]
    HelperTab(l)

    d = defaultdict(list)
    for i in range(MAX_X()):
        for j in range(MAX_Y()):
            if get(l,i,j) == '.':
                continue
            d[get(l,i,j)].append((i,j))

    pt1 = set()
    pt2 = set()
    for vals in d.values():
        for i in range(len(vals)-1):
            for j in range(i+1,len(vals)):
                ax,ay = vals[i]
                bx,by = vals[j] 
                vecx, vecy = (bx-ax, by-ay)
                if not IsOutOfBounds(bx+vecx, by+vecy):
                    pt1.add((bx+vecx, by+vecy))
                if not IsOutOfBounds(ax-vecx, ay-vecy):
                    pt1.add((ax-vecx, ay-vecy))
                
                pt2.add((ax,ay))
                pt2.add((bx,by))
                while True:
                    if IsOutOfBounds(bx+vecx, by+vecy):
                        break
                    pt2.add((bx+vecx, by+vecy))
                    bx, by = bx+vecx, by+vecy
                while True:
                    if IsOutOfBounds(ax-vecx, ay-vecy):
                        break
                    pt2.add((ax-vecx, ay-vecy))
                    ax, ay = ax-vecx, ay-vecy
    Pr(len(pt1))
    Pr(len(pt2))

if __name__ == '__main__':
    main()
