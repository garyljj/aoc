from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')

    p1 = 0
    p2 = 0
    for l in L:
        a = firstKeyPad(l)
        n = solve(a,2)
        p1 += n*int(l[:-1])

        n = solve(a,25)
        p2 += n*int(l[:-1])
    Pr(p1)
    Pr(p2)

keypad = {
    'A':(3,2),
    '0':(3,1),
    '1':(2,0),
    '2':(2,1),
    '3':(2,2),
    '4':(1,0),
    '5':(1,1),
    '6':(1,2),
    '7':(0,0),
    '8':(0,1),
    '9':(0,2),
}
dirpad = {
    ('^','^'):'A',
    ('^','A'):'>A',
    ('^','<'):'v<A',
    ('^','v'):'vA',
    ('^','>'):'v>A',

    ('A','^'):'<A',
    ('A','A'):'A',
    ('A','<'):'v<<A',
    ('A','v'):'<vA',
    ('A','>'):'vA',

    ('<','^'):'>^A',
    ('<','A'):'>>^A',
    ('<','<'):'A',
    ('<','v'):'>A',
    ('<','>'):'>>A',

    ('v','^'):'^A',
    ('v','A'):'^>A',
    ('v','<'):'<A',
    ('v','v'):'A',
    ('v','>'):'>A',

    ('>','^'):'<^A',
    ('>','A'):'^A',
    ('>','<'):'<<A',
    ('>','v'):'<A',
    ('>','>'):'A',
}


d = {}
def solve(l,n):
    if n == 0:
        return len(l)
    if (l,n) in d:
        return d[(l,n)]
    curr = l[0]
    s = solve(dirpad[('A',curr)], n-1)
    for i in range(1,len(l)):
        prev = curr
        curr = l[i]
        s += solve(dirpad[(prev,curr)], n-1)
    d[(l,n)] = s
    return s

def firstKeyPad(l):
    curr = keypad['A']
    keys = ''
    for ll in l:
        nxt = keypad[ll]
        x = nxt[0] - curr[0]
        y = nxt[1] - curr[1]
        k = ''

        if y < 0:
            k += '<'*-y
        k += 'v'*x if x > 0 else '^'*-x
        if y > 0:
            k += '>'*y

        # reverse order if will go over key gap
        if nxt[0] == 3 and curr[1] == 0 or nxt[1] == 0 and curr[0] == 3:
            k = k[::-1]

        curr = nxt
        keys += k + 'A'
    return keys

if __name__ == '__main__':
    main()