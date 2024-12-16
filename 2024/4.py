from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')

    l = [list(i) for i in L]
    HelperTab(l)

    p1 = 0
    for x in range(MAX_X()):
        for y in range(MAX_Y()):
            p1 += checkHorizontal(l, x, y)
            p1 += checkVertical(l, x, y)
            p1 += checkDia1(l, x, y) # \
            p1 += checkDia2(l, x, y) # /

    p2 = 0
    for x in range(MAX_X()):
        for y in range(MAX_Y()):
            p2 += checkX(l, x, y)

    Pr(p1)
    Pr(p2)

def checkX(l, x, y):
    if l[x][y] != 'A':
        return False
    a,b,c,d = (x-1,y-1),(x+1,y-1),(x-1,y+1),(x+1,y+1)
        
    if Any(
        IsOutOfBounds(*a),
        IsOutOfBounds(*b),
        IsOutOfBounds(*c),
        IsOutOfBounds(*d),
    ):
        return False

    s = get(l,*a) + get(l,*b) + get(l,*c) + get(l,*d)
    return ''.join(sorted(s)) == 'MMSS' and get(l,*a) != get(l,*d)

def check(l):
    global count
    for x in range(len(l)):
        for y in range(len(l[0])):
            count += checkHorizontal(l, x, y)
            count += checkVertical(l, x, y)
            count += checkDia1(l, x, y) # \
            count += checkDia2(l, x, y) # /

WORD = "XMAS"

def checkHorizontal(l, x, y):
    a,b,c,d = (x,y),(x,y+1),(x,y+2),(x,y+3)
    if IsOutOfBounds(*d):
        return False
    return isWord(l,a,b,c,d)
def checkVertical(l, x, y):
    a,b,c,d = (x,y),(x+1,y),(x+2,y),(x+3,y)
    if IsOutOfBounds(*d):
        return False
    return isWord(l,a,b,c,d)
def checkDia1(l, x, y):
    a,b,c,d = (x,y),(x+1,y+1),(x+2,y+2),(x+3,y+3)
    if IsOutOfBounds(*d):
        return False
    return isWord(l,a,b,c,d)
def checkDia2(l, x, y):
    a,b,c,d = (x,y),(x-1,y+1),(x-2,y+2),(x-3,y+3)
    if IsOutOfBounds(*d):
        return False
    return isWord(l,a,b,c,d)

def validIdx(*args):
    for x,y in args:
        if IsOutOfBounds(x,y):
            return False
    return True

def isWord(l,a,b,c,d):
    s = get(l,*a) + get(l,*b) + get(l,*c) + get(l,*d)
    return s == WORD or s[::-1] == WORD

if __name__ == '__main__':
    main()


