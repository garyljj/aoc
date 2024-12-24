from helper import *
import os
import sys
# import heapq
from collections import deque

def main():
    FN = os.path.basename(__file__)[:-2] + 'txt'
    vals,wires = open(FN).read().split('\n\n')

    d = {}
    vals = map(lambda x: x.split(": "), vals.split('\n'))
    for n,v in vals:
        d[n] = int(v)

    q = deque()
    for w in wires.split("\n"):
        a,op,b,_,res = w.split()
        q.append((a,op,b,res))

    while len(q) > 0:
        a,op,b,res = q.popleft()
        if not (a in d and b in d):
            q.append((a,op,b,res))
            continue
        if op == 'AND':
            d[res] = d[a] & d[b]
        elif op == 'XOR':
            d[res] = d[a] ^ d[b]
        elif op == 'OR':
            d[res] = d[a] | d[b]
        else:
            assert False

    final = []
    for k in sorted(filter(lambda x: x[0] == 'z', d.keys()), reverse=True):
        final.append(str(d[k]))
    p1 = int(''.join(final),2)
    Pr(p1)

    """
    for p2, just used plantuml to visualize graph and fix wire manually
    general idea to debug was
    1. all final z bit values is computed with XOR
      - except the final carry over bit with OR
    2. for the carry over parts, OR operation is preceded by AND operation
      - eg. 
        - a AND b -> c
        - d AND e -> f
        - c OR f -> g

    plantuml example:

    @startuml
    digraph a {
        x00 -> z00 [label=XOR]
        y00 -> z00 [label=XOR]
        y00 -> gwq [label=AND]
        x00 -> gwq [label=AND]

        y01 -> pvw [label=AND]
        x01 -> pvw [label=AND]
        y01 -> qgt [label=XOR]
        x01 -> qgt [label=XOR]
        qgt -> z01 [label=XOR]
        gwq -> z01 [label=XOR]

        qgt -> cgt [label=AND]
        gwq -> cgt [label=AND]
        pvw -> kgp [label=OR]
        cgt -> kgp [label=OR]

        y02 -> mqf [label=AND]
        x02 -> mqf [label=AND]
        x02 -> tpf [label=XOR]
        y02 -> tpf [label=XOR]

        kgp -> z02 [label=XOR]
        tpf -> z02 [label=XOR]
        tpf -> jkv [label=AND]
        kgp -> jkv [label=AND]

        jkv -> z03 [label=OR]
        mqf -> z03 [label=OR]
    }
    @enduml
    """

if __name__ == '__main__':
    main()
