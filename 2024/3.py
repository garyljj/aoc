from helper import *
import os
import sys
# import heapq
# from collections import defaultdict
import re


def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read()

    p1 = 0
    for i in re.findall('mul\((\d+),(\d+)\)', L):
        p1 += int(i[0]) * int(i[1])

    p2 = 0
    do = True
    for i in re.findall("mul\((\d+),(\d+)\)|(do)\(\)|(don't)\(\)", L):
        if i[2]:
            do = True
            continue
        if i[3]:
            do = False
            continue
        if do:
            p2 += int(i[0]) * int(i[1])
    Pr(p1)
    Pr(p2)

if __name__ == '__main__':
    main()