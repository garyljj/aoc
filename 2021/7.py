from helper import *
import os
import sys
# import heapq
from collections import Counter

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split(',')
    lst = list(map(int,L))

    p1 = solve(lst.copy())
    Pr(p1)
    p2 = solve(lst.copy(), isPt1=False)
    Pr(p2)

def solve(lst, isPt1=True):
    num = Counter(lst)
    fuel = Counter(lst)

    f = 0
    mx,mn = max(lst), min(lst)
    while mx != mn:
        if num[mx] < num[mn] and isPt1 or fuel[mx] < fuel[mn]:
            f += num[mx] if isPt1 else fuel[mx]
            num[mx-1] += num[mx]
            fuel[mx-1] += fuel[mx] + num[mx]
            mx -= 1
        else:
            f += num[mn] if isPt1 else fuel[mn]
            num[mn+1] += num[mn]
            fuel[mn+1] += fuel[mn] + num[mn]
            mn += 1
    return f

if __name__ == '__main__':
    main()
