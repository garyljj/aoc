from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n\n')

    games = []
    for l in L:
        a,b,p = l.split('\n')
        a = tuple(map(lambda x: int(x[2:]), a.split(': ')[-1].split(', ')))
        b = tuple(map(lambda x: int(x[2:]), b.split(': ')[-1].split(', ')))
        p = tuple(map(lambda x: int(x[2:]), p.split(': ')[-1].split(', ')))
        games.append((*a,*b,*p))

    p1 = 0
    p2 = 0
    for game in games:
        a,b = solve(*game, isPart2=False)
        p1 += a * 3 + b
        a,b = solve(*game, isPart2=True)
        p2 += a * 3 + b

    Pr(p1)
    Pr(p2)

def solve(ax,ay,bx,by,px,py, isPart2):
    if isPart2:
        px += 10000000000000
        py += 10000000000000

    a = (px*by-py*bx) / (ax*by - ay*bx)
    b = (py - a*ay) / by

    if a == int(a) and b == int(b):
        return int(a), int(b)
    return 0, 0

if __name__ == '__main__':
    main()
