from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')

    robots = []
    for l in L:
        p,v = l.split()
        py,px =tuple(map(int,p[2:].split(',')))
        vy,vx =tuple(map(int,v[2:].split(',')))
        robots.append((px,py,vx,vy))

    maxx,maxy = 7,11 # example use this size
    # maxx,maxy = 103,101

    threshold = 200 # estimated for pt2 (only works on actual input)
    quad = [0]*4

    for s in range(10000):
        th = 0
        m = [['.']*maxy for _ in range(maxx)]
        for px,py,vx,vy in robots:
            px = (px + vx * s) % maxx
            py = (py + vy * s) % maxy
            m[px][py] = 'x'
            if px-1>=0 and m[px-1][py] == 'x':
                th += 1
            if py-1>=0 and m[px][py-1] == 'x':
                th += 1

            if s == 101: # pt1
                q = checkQuad(px,py,maxx,maxy)
                if q:
                    quad[q-1] += 1
        if th > threshold:
            for mm in m:
                print(''.join(mm))
            print(s, '-'*101)
            input() # pause to check picture

    pt1 = quad[0]*quad[1]*quad[2]*quad[3]
    Pr(pt1)

def checkQuad(x,y,maxx,maxy):
    midx,midy = maxx//2, maxy//2
    if x < midx and y < midy:
        return 1
    if x < midx and y > midy:
        return 2
    if x > midx and y < midy:
        return 3
    if x > midx and y > midy:
        return 4
    return 0

if __name__ == '__main__':
    main()
