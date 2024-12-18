from helper import *
import os
import sys
# import heapq
from collections import deque

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    L = open(FN).read().strip()
    l = [int(i) for i in L]

    p1 = execute(l, isPart1=True)
    Pr(p1)

    p2 = execute(l, isPart1=False)
    Pr(p2)

def execute(l, isPart1):
    files = []
    space = []

    for i, val in enumerate(l):
        if i % 2 == 0:
            id = i//2
            file = deque([(id,1)]*val) if isPart1 else deque([(id,val)])
            files.append(file)
        else:
            space.append(val)

    for i in range(1, len(files))[::-1]:
        havSpace = True
        si = 0
        while len(files[i]) > 0 and files[i][0][0] == i and havSpace: #compact current id
            id,size = files[i][0]
            for si in range(si, len(space)):
                if si < i and space[si] >= size:
                    files[i].popleft()
                    files[si].append((id,size))
                    space[si] -= size
                    space[i-1] += size
                    break
            else:
                havSpace = False

    ans = 0
    idx = 0
    for f,s in zip(files,space):
        for id,size in f:
            for _ in range(size):
                ans += id * idx
                idx += 1
        idx += s
    return ans



    










if __name__ == '__main__':
    main()


# def main():
#     main2()

# def main2():
#     l = []
#     ll = {}
#     space = []
#     i = 0
#     for idx, v in enumerate(parse('9.txt')):
#         if idx%2==0:
#             l.append([i])
#             ll[i] = int(v)
#             i += 1
#         else:
#             space.append(int(v))
#     space.append(0)

#     for i in range(len(l)-1,-1,-1):
#         for j, sp in enumerate(space):
#             if j >= i:
#                 break
#             if ll[i] <= sp:
#                 l[j].append(i)
#                 if i not in l[i]:
#                     print("huhuhhhhh")
#                 l[i].remove(i)
#                 space[j] -= ll[i]
#                 space[i-1] += ll[i]
#                 break

#     c = 0
#     cc = []
#     idx = 0
#     for a,b in zip(l,space):
#         for i in a:
#             for _ in range(ll[i]):
#                 c += i * idx
#                 cc.append(i)
#                 idx += 1
#         idx += b
#         cc.extend(['.']*b)
#     # print(''.join(map(str,cc)))
#     print(c)

# def main1():
#     l = []
#     i = 0
#     for idx, v in enumerate(parse('9.txt')):
#         if idx%2==0:
#             l.extend([i]*int(v))
#             i += 1
#         else:
#             l.extend(['.']*int(v))
#     curr = 0
#     last = len(l) - 1
#     while True:
#         if last <= curr:
#             break

#         if l[curr] == '.':
#             if l[last] == '.':
#                 last -= 1
#                 continue
#             l[curr], l[last] = l[last], l[curr]
#         curr += 1

#     c = 0
#     for i,v in enumerate(l):
#         if v == '.':
#             break
#         c += i * int(v)
#     print(c)

# def parse(fn):
#     with open(fn) as f:
#         l = f.read().strip()
#     return l

# if __name__ == "__main__":
#     main()
