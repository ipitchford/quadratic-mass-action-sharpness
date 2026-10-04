"""Exact reactant-support classification; discovery output, not a complete proof."""
from itertools import combinations, permutations
from functools import reduce
import json
import sympy as s

pts=[(0,0,0),(1,0,0),(0,1,0),(0,0,1),(2,0,0),(0,2,0),(0,0,2),(1,1,0),(1,0,1),(0,1,1)]
names=['1','x','y','z','x2','y2','z2','xy','xz','yz']
perms=list(permutations(range(3)))
def canon(support):
    return min(tuple(sorted(tuple(a[i] for i in p) for a in support)) for p in perms)
stats={}
reps={}
for ix in combinations(range(10),5):
    A=s.Matrix([list(pts[i])+[1] for i in ix])
    ns=A.T.nullspace()
    if len(ns)!=1:
        key='affine_deficient'
    else:
        w=ns[0]
        w=w*s.ilcm(*[v.q for v in w])
        w=w/reduce(s.igcd,w)
        deg=sum(max(0,v) for v in w)
        key=str(deg)
        if deg>=4:
            c=canon([pts[i] for i in ix])
            reps.setdefault(c,{'names':[names[i] for i in ix], 'A':[pts[i] for i in ix], 'w':list(map(int,w)), 'degree':int(deg)})
    stats[key]=stats.get(key,0)+1
print(json.dumps({'stats':stats,'quartic_representatives':list(reps.values())},indent=2))
