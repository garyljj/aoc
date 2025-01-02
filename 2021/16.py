from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    transmissions = open(FN).read().strip().split('\n')

    # list all example as input
    for transmission in transmissions:
        t = ''.join([bin(int(t,16))[2:].zfill(4) for t in transmission])

        _, getter = transmitter(t)
        p1,p2 = getPacket(getter)
        Pr(p1)
        Pr(p2)

def transmitter(t):
    def noMorePacket():
        return len(t) < 11 # must at least have size for literal
    def getter(n):
        nonlocal t
        b, t = t[:n], t[n:]
        return b
    return noMorePacket, getter

def getPacket(getter):
    version, typeid = dec(getter(3)), dec(getter(3))
    match typeid:
        case 0:
            t, lit = getSubPacket(getter, sum)
        case 1:
            def prod(lst):
                i = 1
                for l in lst:
                    i *= l
                return i
            t, lit = getSubPacket(getter, prod)
        case 2:
            t, lit = getSubPacket(getter, min)
        case 3:
            t, lit = getSubPacket(getter, max)
        case 4:
            lit = getLiteral(getter)
            return version, lit
        case 5:
            t, lit = getSubPacket(getter, lambda x: int(x[0] > x[1]))
        case 6:
            t, lit = getSubPacket(getter, lambda x: int(x[0] < x[1]))
        case 7:
            t, lit = getSubPacket(getter, lambda x: int(x[0] == x[1]))
    return version + t, lit

def getLiteral(getter):
    val = ''
    while True:
        more = getter(1)
        val += getter(4)
        if more == '0':
            break
    return dec(val)

def getSubPacket(getter, func):
    lits = []
    total = 0
    if getter(1) == '0':
        numbits = dec(getter(15))
        bits = getter(numbits)
        noMorePacket, getter = transmitter(bits)
        while True:
            if noMorePacket():
                break
            t, lit = getPacket(getter)
            total += t
            lits.append(lit)
    else:
        numpack = dec(getter(11))
        for _ in range(numpack):
            t, lit = getPacket(getter)
            total += t
            lits.append(lit)
    return total, func(lits)

def dec(b):
    return int(b,2)

if __name__ == '__main__':
    main()
