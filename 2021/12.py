from helper import *
import os
import sys
# import heapq
from collections import defaultdict, deque

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')

    m = defaultdict(list)
    for l in L:
        a,b = l.split('-')
        m[a].append(b)
        m[b].append(a)

    p1 = solve(m)
    Pr(p1)

    p2 = solve(m, isPt2=True)
    Pr(p2)

def solve(m, isPt2=False):
    q = deque([('start',{'start'},None)])
    s = 0
    while len(q) > 0:
        curr, visited, check = q.popleft()
        if curr == 'end':
            s += 1
            continue

        for nxt in m[curr]:
            c = check
            if nxt in visited:
                if isPt2 and c is None and nxt != 'start':
                    c = nxt
                else:
                    continue
            v = visited
            if nxt.islower():
                v = v.copy()
                v.add(nxt)
            q.append((nxt, v, c))
    return s

if __name__ == '__main__':
    main()
