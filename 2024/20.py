from helper import *
import os
import sys
# import heapq
from collections import deque

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    m = [list(i) for i in L]
    HelperTab(m)

    for i in range(MAX_X()):
        for j in range(MAX_Y()):
            if get(m,i,j) == 'S':
                start = (i,j)
                m[i][j] = '.'
            if get(m,i,j) == 'E':
                end = (i,j)
                m[i][j] = '.'

    fullcost, costmap = bfs(m, start, end)
    assert fullcost != -1

    # ----- actual -----
    # pt1 = bfs2(m,costmap,fullcost,savecost=100,cheattime=2)
    # Pr(pt1)

    # pt2 = bfs2(m,costmap,fullcost,savecost=100,cheattime=20)
    # Pr(pt2)

    # ----- verify example pt1 -----
    for savecost in (2,4,6,8,10,12,20,36,38,40,64):
        print(savecost, bfs2(m,costmap,fullcost,savecost,cheattime=2,atleast=False))
    # ----- verify example pt2 -----
    for savecost in (50,52,54,56,58,60,62,64,66,68,70,72,74,76):
        print(savecost, bfs2(m,costmap,fullcost,savecost,cheattime=20,atleast=False))

def bfs2(m,costmap,fullcost,savecost,cheattime,atleast=True):
    s = 0
    for i,j in costmap:
        currcost = costmap[(i,j)]
        q = deque([(0,i,j)])
        visited = {(i,j)}
        while True:
            if len(q) == 0:
                break
            c,x,y = q.popleft()
            if c > cheattime:
                break

            if get(m,x,y) == '.':
                lastcost = fullcost - costmap[(x,y)]
                if atleast and currcost + c + lastcost <= fullcost-savecost:
                    s += 1
                elif currcost + c + lastcost == fullcost-savecost:
                    s += 1
                        
            for dx,dy in Dir4():
                xx = x + dx
                yy = y + dy
                if (xx,yy) in visited or IsOutOfBounds(xx,yy):
                    continue
                visited.add((xx,yy))
                q.append((c+1,xx,yy))
    return s

def bfs(m, start, end):
    q = deque([(0,*start)])
    visited = {start}
    costmap = {}
    while True:
        if len(q) == 0:
            return -1, costmap
        c,x,y = q.popleft()
        costmap[(x,y)] = c
        if (x,y) == end:
            return c, costmap
        for dx,dy in Dir4():
            xx = x + dx
            yy = y + dy
            if (xx,yy) in visited or get(m,xx,yy) == '#':
                continue
            visited.add((xx,yy))
            q.append((c+1,xx,yy))

if __name__ == '__main__':
    main()
