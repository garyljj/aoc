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





if __name__ == '__main__':
    main()