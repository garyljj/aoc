from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n\n')

    pattern, lst = L
    pattern = pattern.split(', ')
    lst = lst.split('\n')

    p1 = 0
    p2 = 0
    for l in lst:
        s = solve(pattern, l)
        if s != 0:
            p1 += 1
            p2 += s
    Pr(p1)
    Pr(p2)

d = {}
def solve(pattern, l):
    if len(l) == 0:
        return 1
    if l in d:
        return d[l]

    c = 0
    for p in pattern:
        if str(l).startswith(p):
            c += solve(pattern, l[len(p):])

    d[l] = c
    return c

if __name__ == '__main__':
    main()
