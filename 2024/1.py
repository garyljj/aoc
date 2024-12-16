from helper import *
import os
import sys
# import heapq
from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')

    lst1,lst2 = [],[]
    d = defaultdict(int)
    for i in L:
        a,b = i.split()
        lst1.append(int(a))
        lst2.append(int(b))
        d[int(b)] += 1

    lst1,lst2 = sorted(lst1),sorted(lst2)

    p1 = 0
    p2 = 0
    for i in range(len(lst1)):
        p1 += abs(lst1[i]-lst2[i])
        p2 += lst1[i] * d[lst1[i]]
    Pr(p1)
    Pr(p2)


if __name__ == '__main__':
    main()

