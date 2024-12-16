from helper import *
import os
import sys
# import heapq
# from collections import defaultdict
from functools import cmp_to_key

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    a,b = open(FN).read().strip().split('\n\n')

    p,l = [],[]
    for i in a.split("\n"):
        p.append(i.strip().split("|"))
    for i in b.split("\n"):
        l.append(i.strip().split(","))

    p1,p2 = 0,0
    for ll in l:
        d = {}
        for i,v in enumerate(ll):
            d[v] = i

        ok = True
        for pred in p:
            if pred[0] in d and pred[1] in d:
                if d[pred[0]] > d[pred[1]]:
                    ok = False
                    break
        if ok:
            p1 += int(ll[(len(ll)-1)//2])
        else:
            sll = sorted(ll, key=cmp_to_key(cmp(p)))
            p2 += int(sll[(len(sll)-1)//2])

    Pr(p1)
    Pr(p2)

def cmp(p):
    def cmp2(a,b):
        for i in p:
            if a in i and b in i and b == i[0]:
                return 1
        return -1
    return cmp2


if __name__ == '__main__':
    main()
