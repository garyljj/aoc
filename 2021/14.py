from helper import *
import os
import sys
# import heapq
from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    poly, rules = open(FN).read().strip().split('\n\n')

    pairmap = defaultdict(int)
    letters = defaultdict(int)
    for i in range(len(poly)):
        letters[poly[i]] += 1
        if i != 0:
            pairmap[poly[i-1]+poly[i]] += 1
    rulemap = {}
    for rule in rules.split('\n'):
        a,b = rule.split(' -> ')
        rulemap[a] = b

    p1 = solve(pairmap,letters,rulemap, 10)
    Pr(p1)
    p2 = solve(pairmap,letters,rulemap, 40)
    Pr(p2)

def solve(pairmap, letters, rulemap, t):
    pairmap, letters, rulemap = pairmap.copy(), letters.copy(), rulemap.copy()

    for _ in range(t):
        nmap = defaultdict(int)
        for k in pairmap:
            if k not in rulemap:
                assert 0
                nmap[k] += pairmap[k]
            else:
                mid = rulemap[k]
                nmap[k[0]+mid] += pairmap[k]
                nmap[mid+k[1]] += pairmap[k]
                letters[mid] += pairmap[k]
        pairmap = nmap

    return max(letters.values()) - min(letters.values())

if __name__ == '__main__':
    main()
