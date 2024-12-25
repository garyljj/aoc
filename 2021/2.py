from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')

    d,h,td = 0,0,0
    for i in L:
        op,v = i.split()
        if op == 'forward':
            h += int(v)
            td += int(v)*d
        elif op == 'down':
            d += int(v)
        elif op == 'up':
            d -= int(v)
        else:
            assert False, op
    p1 = d * h
    Pr(p1)
    p2 = td * h
    Pr(p2)

if __name__ == '__main__':
    main()
