from helper import *
import os
import sys
# import heapq
from collections import deque

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    L = [tuple(map(int, i.split(','))) for i in L]
    
    size = 7 #example uses 7, actual is 71
    # size = 71

    m = [['.']*size for _ in range(size)]
    HelperTab(m)

    n = 12 #example is 12 bytes, actual is 1024
    # n = 1024
    for x,y in L[:n]:
        m[x][y] = '#'

    path = bfs(m, (size-1,size-1))
    p1 = len(path)
    Pr(p1)

    for x,y in L[n:]:
        m[x][y] = '#'
        if (x,y) not in path:
            continue
        path = bfs(m, (size-1,size-1))
        if not path:
            break
    p2 = f'{x},{y}'
    Pr(p2)
    # 1st attempt: simply do bfs for each obstacle until failure
    # 2nd slight optimization: only do bfs if new obstacle fall on the shortest path


def bfs(m, end):
    q = deque([])
    q.append((0,0,set()))
    visited = set()
    dir = Dir4()
    while True:
        if len(q) == 0:
            return set()
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
                cc = c.copy()
                cc.add((nx,ny))
                q.append((nx,ny,cc))

if __name__ == '__main__':
    main()