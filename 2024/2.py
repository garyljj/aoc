from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')

    p1 = 0
    p2 = 0
    for lst in L:
        lst = list(map(int, lst.split()))

        a = check(lst, lambda x,y: x < y)
        d = check(lst, lambda x,y: x > y)
        mag = check(lst, lambda x,y: 1 <= abs(x-y) <= 3)
        if mag and (a or d):
            p1 += 1

        for i in range(len(lst)):
            llst = lst[:i] + lst[i+1:]
            a = check(llst, lambda x,y: x < y)
            d = check(llst, lambda x,y: x > y)
            mag = check(llst, lambda x,y: 1 <= abs(x-y) <= 3)
            if mag and (a or d):
                p2 += 1
                break
    Pr(p1)
    Pr(p2)

def check(lst, cond):
    for i in range(1, len(lst)):
        a, b = lst[i-1],lst[i]
        if not cond(a, b):
            return False
    return True

if __name__ == '__main__':
    main()
