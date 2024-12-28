from helper import *
import os
import sys
# import heapq
from collections import deque

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')

    p1 = 0
    scores = []
    for l in L:
        v, s = solve(l)
        p1 += v
        if not v:
            scores.append(complete(s))
    Pr(p1)
    p2 = sorted(scores)[len(scores)//2]
    Pr(p2)

def solve(l):
    stack = deque()
    for idx, v in enumerate(l):
        if v in ('(','[','{','<'):
            stack.append(v)
            continue
        a = stack.pop()
        if v == ')' and a != '(':
            return 3, None
        elif v == ']' and a != '[':
            return 57, None
        elif v == '}' and a != '{':
            return 1197, None
        elif v == '>' and a != '<':
            return 25137, None
    return 0, stack

def complete(stack):
    s = 0
    while len(stack) > 0:
        v = stack.pop()
        s *= 5
        if v == '(':
            s += 1
        elif v == '[':
            s += 2
        elif v == '{':
            s += 3
        elif v == '<':
            s += 4
    return s

if __name__ == '__main__':
    main()
