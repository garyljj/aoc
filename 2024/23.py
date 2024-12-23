from helper import *
import os
import sys
# import heapq
from collections import defaultdict
from itertools import combinations

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')

    d = defaultdict(set)
    for l in L:
        a,b = l.split('-')
        d[a].add(b)
        d[b].add(a)
    
    p1 = 0
    nodes = tuple(d.keys())
    for i in range(len(nodes)):
        for j in range(i+1,len(nodes)):
            if nodes[i] in d[nodes[j]]:
                for k in range(j+1,len(nodes)):
                    if nodes[k] in d[nodes[i]] and nodes[k] in d[nodes[j]]:
                        if nodes[i][0] == 't' or nodes[j][0] == 't' or nodes[k][0] == 't':
                            p1 += 1
    Pr(p1)

    largest = max(map(len,d.values()))
    p2 = solve(nodes, d, largest)
    p2 = ','.join(sorted(p2))
    Pr(p2)

def solve(nodes, d, largest):
    final = set()
    for i in range(largest,-1,-1):
        if i < len(final):
            break
        for n in nodes:
            for c in combinations(d[n], i):
                grp = {n}
                for nn in c:
                    if grp.issubset(d[nn]):
                        grp.add(nn)
                    else:
                        break
                if len(grp) > len(final):
                    final = grp.copy()
    return final

if __name__ == '__main__':
    main()