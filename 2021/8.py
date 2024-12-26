from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')

    mapping = {}
    p1 = 0
    p2 = 0
    for l in L:
        a,b = l.split(' | ')
        a = [''.join(sorted(i)) for i in sorted(a.split(), key=len)]

        mapping[a[0]] = 1
        mapping[a[1]] = 7
        mapping[a[2]] = 4
        mapping[a[-1]] = 8

        for aa in a:
            if len(aa) == 5:
                if len(set(aa).union(set(a[0]))) == 5:
                    mapping[aa] = 3
                elif len(set(aa).difference(set(a[2]))) == 2:
                    mapping[aa] = 5
                else:
                    mapping[aa] = 2
            if len(aa) == 6:
                if len(set(aa).union(set(a[2]))) == 6:
                    mapping[aa] = 9
                elif len(set(aa).union(set(a[0]))) == 6:
                    mapping[aa] = 0
                else:
                    mapping[aa] = 6

        v = 0
        for bb in b.split():
            if len(bb) in (2,3,4,7):
                p1 += 1
            v *= 10
            v += mapping[''.join(sorted(bb))]
        p2 += v

    Pr(p1)
    Pr(p2)

if __name__ == '__main__':
    main()
