from helper import *
import os
import sys
# import heapq
from collections import deque

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    lst = open(FN).read().strip().split(',')
    lst = list(map(int, lst))

    p1 = solve(lst, 80)
    Pr(p1)
    p2 = solve(lst, 256)
    Pr(p2)

def solve(lst, d):
    q = [0]*9
    for l in lst:
        q[l] += 1
    q = deque(q)
    for _ in range(d):
        z  = q.popleft()
        q[-2] += z
        q.append(z)
    return sum(q)

if __name__ == '__main__':
    main()
