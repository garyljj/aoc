from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    l = [int(i) for i in L]

    p1 = 0
    p2 = 0
    for i in range(1,len(l)):
        if l[i] > l[i-1]:
            p1 += 1
        if sum(l[i:i+3]) > sum(l[i-1:i+3-1]):
            p2 += 1
    Pr(p1)
    Pr(p2)

if __name__ == '__main__':
    main()
