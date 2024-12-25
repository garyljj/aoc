from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')

    c = [0]*len(L[0])
    f = [(set(),set()) for _ in range(len(L[0]))]
    for l in L:
        for i,v in enumerate(l):
            c[i] += 1 if v == '1' else -1
            if v == '1':
                f[i][1].add(l)
            elif v == '0':
                f[i][0].add(l)
            else:
                assert False

    gamma,eps = '',''
    for cc in c:
        assert cc != 0
        gamma += '1' if cc > 0 else '0'
        eps += '1' if cc < 0 else '0'
    p1 = int(gamma,2) * int(eps,2)
    Pr(p1)

    o2,co2 = set(L),set(L)
    for i, ff in enumerate(f):
        if len(o2) > 1:
            check = 0
            for o in o2:
                check += 1 if o[i] == '1' else -1
            if check < 0:
                o2 = o2.intersection(ff[0])
            else: # if more common or same also use 1
                o2 = o2.intersection(ff[1])
        if len(co2) > 1:
            check = 0
            for o in co2:
                check += 1 if o[i] == '1' else -1
            if check < 0:
                co2 = co2.intersection(ff[1])
            else: # if more common or same also use 0
                co2 = co2.intersection(ff[0])
    p2 = int(o2.pop(),2) * int(co2.pop(),2)
    Pr(p2)

if __name__ == '__main__':
    main()
