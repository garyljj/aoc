from helper import *
import os
import sys
# import heapq
from collections import deque

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    L = [tuple(map(int, i.split(','))) for i in L]
    
    # size = 7
    size = 71

    m = [['.']*size for _ in range(size)]
    HelperTab(m)

    # n = 12
    n = 1024
    for x,y in L[:n]:
        m[x][y] = '#'

    p1 = bfs(m, (size-1,size-1))
    Pr(p1)

    for x,y in L[n:]:
        m[x][y] = '#'
        if bfs(m, (size-1,size-1)) == -1:
            break
    p2 = f'{x},{y}'
    Pr(p2)


def bfs(m, end):
    q = deque([])
    q.append((0,0,0))
    visited = set()
    dir = Dir4()
    while True:
        if len(q) == 0:
            return -1
        x,y,c = q.popleft()
        if (x,y) == end:
            return c
        if (x,y) in visited:
            continue
        visited.add((x,y))
        for xx,yy in dir:
            nx = x + xx
            ny = y + yy
            if not IsOutOfBounds(nx,ny) and m[nx][ny] != '#':
                q.append((nx,ny,c+1))

if __name__ == '__main__':
    main()