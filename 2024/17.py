from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    a,b = open(FN).read().strip().split('\n\n')

    a = a.split('\n')
    A,B,C = map(lambda x: int(x.split(': ')[-1]),a)
    program = list(map(int, b.split(": ")[-1].split(',')))

    res = run(A,B,C,program)
    p1 = ','.join(map(str,res))
    Pr(p1)

    # for part 2 note that
    #   - each output is generate per loop (op3)
    #   - each loop op0 operand is always 3
    #     - means for each num generated, A >> 3
    #   - so we can build A recursively 3 bit at a time for each digit
    possible_vals = [0]
    for p in range(len(program)-1,-1,-1):
        new_possible = []
        for ans in possible_vals:
            for i in range(1 << 3): # 3 bit
                a = (ans << 3) + i
                res = run(a,0,0,program)
                if res[0] == program[p]:
                    new_possible.append(a)
        possible_vals = new_possible

    p2 = min(possible_vals)
    Pr(p2)

def run(A,B,C,program):
    ptr = 0
    res = []
    while True:
        if ptr >= len(program):
            break
        assert ptr != len(program)-1

        op = program[ptr]
        o = program[ptr+1]
        ptr += 2
        if op == 0:
            A = A >> combo(o,A,B,C)
        if op == 1:
            B = o ^ B
        if op == 2:
            B = combo(o,A,B,C) % 8
        if op == 3:
            if A != 0:
                ptr = o
        if op == 4:
            B = B ^ C
        if op == 5:
            res.append(combo(o,A,B,C) % 8)
        if op == 6:
            B = A >> combo(o,A,B,C)
        if op == 7:
            C = A >> combo(o,A,B,C)
    return res

def combo(o,a,b,c):
    if o <= 3:
        return o
    if o == 4:
        return a
    if o == 5:
        return b
    if o == 6:
        return c
    assert o != 7

if __name__ == '__main__':
    main()