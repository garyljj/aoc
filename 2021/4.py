from helper import *
import os
import sys
# import heapq
# from collections import defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    nums, *boards = open(FN).read().strip().split('\n\n')

    nums = list(map(int,nums.split(',')))
    boards = list(map(lambda x: [list(i.split()) for i in x.split('\n')], boards))

    blst = []
    for b in boards:
        nboard = []
        for r in b:
            nboard.append(set(map(int,r)))
        for c in range(len(b[0])):
            nboard.append(set(map(lambda x: int(x[c]), b)))
        blst.append(nboard)

    b,n = sim(nums,blst)
    p1 = sum(set().union(*b)) * n
    Pr(p1)

    b,n = sim(nums,blst,isPt1=False) # ok to reuse blst from pt1 as just need find last won
    p2 = sum(set().union(*b)) * n
    Pr(p2)

def sim(nums,blst,isPt1=True):
    won = set()
    for n in nums:
        for bidx, board in enumerate(blst):
            if bidx in won:
                continue
            for rc in board:
                rc.discard(n)
                if not rc:
                    won.add(bidx)
            if bidx in won:
                if isPt1 or len(won) == len(blst):
                    return board, n
    assert False

if __name__ == '__main__':
    main()
