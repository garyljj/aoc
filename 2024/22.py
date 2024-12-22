from helper import *
import os
import sys
# import heapq
from collections import deque, defaultdict

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip().split('\n')
    l = [int(i) for i in L]

    pt1 = 0
    final = defaultdict(int)
    for ll in l:
        q = deque()
        d = {}
        for i in range(2000):
            nll = nextn(ll)
            q.append(nll%10-ll%10)
            if len(q) > 4:
                q.popleft()
                key = tuple(q)
                if key not in d:
                    d[key] = nll%10
            ll = nll

        for k,v in d.items():
            final[k] += v
        pt1 += ll
    
    Pr(pt1) # 37990510
    pt2 = max(final.values())
    Pr(pt2) # 23

def nextn(ll):
    ll = mixprune(ll*64, ll)
    ll = mixprune(ll//32, ll)
    ll = mixprune(ll*2048, ll)
    return ll

def mixprune(res,sec):
    return prune(mix(res,sec))

def mix(v,s):
    return v ^ s

def prune(s):
    return s % 16777216

if __name__ == '__main__':
    main()