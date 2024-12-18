from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split()
    l = list(map(int,L))

    p1 = sum(map(lambda x: blink(x,25), l))
    Pr(p1)
    p2 = sum(map(lambda x: blink(x,75), l))
    Pr(p2)

d = {}
def blink(n, times):
    if times == 0:
        return 1
    if (n,times) in d:
        return d[(n,times)]
    s = 0
    if n == 0:
        s = blink(1, times-1)
    elif len(str(n)) % 2 == 0:
        nn = str(n)
        a,b = int(nn[:len(nn)//2]), int(nn[len(nn)//2:])
        s = blink(a, times-1) + blink(b, times-1)
    else:
        s = blink(n*2024, times-1)
    d[(n,times)] = s
    return s

if __name__ == '__main__':
    main()