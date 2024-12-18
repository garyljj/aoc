from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    lst = []
    for l in L:
        ans, v = l.split(": ")
        vals = list(map(int, v.strip().split()))
        lst.append((ans,vals))

    pt1 = 0
    for ans, vals in lst:
        if solve(int(ans), vals[0], vals[1:], isPt1=True):
            pt1 += int(ans)
    Pr(pt1)

    pt2 = 0
    for ans, vals in lst:
        if solve(int(ans), vals[0], vals[1:], isPt1=False):
            pt2 += int(ans)
    Pr(pt2)

def solve(ans, s, l, isPt1):
    if not l:
        return s == ans
    if s > ans:
        return False
    nl = l[1:]

    pt1 = solve(ans, s*l[0], nl, isPt1) or solve(ans, s+l[0], nl, isPt1)
    if isPt1:
        return pt1
    else:
        return pt1 or solve(ans, int(str(s)+str(l[0])), nl, isPt1)

if __name__ == '__main__':
    main()
