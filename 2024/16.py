from helper import *
import os
import sys
import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    m = [list(i) for i in L]
    HelperTab(m)

    for i in range(MAX_X()):
        for j in range(MAX_Y()):
            if get(m,i,j) == 'S':
                start = (i,j)
            if get(m,i,j) == 'E':
                end = (i,j)
    
    pt1,pt2 = solve(m,start,end)
    Pr(pt1)
    Pr(pt2)

dir = Dir4()
def solve(m, start, end):
    cost = 0
    d = 1 # facing right
    path = {start}
    l = [(cost,d,*start,path)]
    visited = {}

    while True:
        if len(l) == 0:
            return False
        c,d,x,y,p = heapq.heappop(l)
        if (x,y) == end:
            while True:
                if len(l) == 0:
                    break
                cc,_,xx,yy,pp = heapq.heappop(l)
                if cc > c:
                    break
                if (xx,yy) == end:
                    p = p.union(pp)
            return c, len(p)

        if (x,y,d) in visited and c > visited[(x,y,d)]:
            continue
        visited[(x,y,d)] = c

        heapq.heappush(l, (c+1000, (d+1)%4, x, y, p))
        heapq.heappush(l, (c+1000, (d-1)%4, x, y, p))
        
        nx,ny = x + dir[d][0], y + dir[d][1]
        if not IsOutOfBounds(nx,ny) and not get(m,nx,ny) == '#':
            p = p.copy()
            p.add((nx,ny))
            heapq.heappush(l, (c+1, d, nx, ny, p))

if __name__ == '__main__':
    main()
