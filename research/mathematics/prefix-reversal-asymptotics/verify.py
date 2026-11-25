"""Exact finite checks for the prefix-reversal density theorem (requires SymPy)."""
from math import gcd, factorial, pi
from itertools import combinations
from collections import deque
from sympy.combinatorics import Permutation, PermutationGroup
import argparse, json
from pathlib import Path
ROOT=Path(__file__).resolve().parent

def rev(n,k): return tuple(range(k-1,-1,-1))+tuple(range(k,n))
def mul(p,q): return tuple(p[i] for i in q)
def inv(p): return tuple(sorted(range(len(p)),key=p.__getitem__))
def power(p,k):
    r=tuple(range(len(p)))
    while k:
        if k&1:r=mul(r,p)
        p=mul(p,p); k//=2
    return r

def cycles(p):
    seen=set(); out=[]
    for i in range(len(p)):
        if i in seen: continue
        c=[];j=i
        while j not in seen:seen.add(j);c.append(j);j=p[j]
        if len(c)>1:out.append(c)
    return out

def congruence(n,a,b):
    return gcd(a,b)==1 and not(n%2==0 and a%2==b%2) and any((k//2)%2 for k in (n,n-a,n-b))

def check_identities(n,a,b):
    s=a+b;t=n-s
    A=mul(rev(n,n),rev(n,n-a));B=mul(rev(n,n),rev(n,n-b))
    D=mul(mul(A,B),inv(mul(B,A)))
    assert D==tuple((i+2*a)%s if i<s else i for i in range(n))
    if gcd(a,b)!=1:return
    step=gcd(2,s)
    U=power(D,pow(2*a//step,-1,s//step))
    assert U==tuple((i+step)%s if i<s else i for i in range(n))
    S=set(range(s));h=min(a,t);I=S-{A[i] for i in S}
    assert I==set(range(h))
    if step==1:
        assert I-{U[i] for i in I}=={0}
    elif n%2 and a>=3:
        assert h%2 and h>=3
        assert I-{U[i] for i in I}=={0,1}
        V=mul(mul(A,U),inv(A)) if t>=a else mul(mul(rev(n,n),inv(U)),rev(n,n))
        W=mul(V,inv(U))
        assert sorted(map(len,cycles(W)))==[h,h+2]
        assert list(map(len,cycles(power(W,h))))==[h+2]
        assert n-(h+2)>=3

def bfs_order(n,a,b):
    gens=(rev(n,n),rev(n,n-a),rev(n,n-b));e=tuple(range(n));seen={e};q=deque([e])
    while q:
        p=q.popleft()
        for g in gens:
            h=mul(p,g)
            if h not in seen:seen.add(h);q.append(h)
    return len(seen)

def group_order(n,a,b):
    return PermutationGroup([Permutation(rev(n,k)) for k in (n,n-a,n-b)]).order()

def main():
    p=argparse.ArgumentParser();p.add_argument('--order-max',type=int,default=17);p.add_argument('--identity-max',type=int,default=65);p.add_argument('--bfs-max',type=int,default=8);args=p.parse_args()
    report={'order_max':args.order_max,'identity_max':args.identity_max,'bfs_max':args.bfs_max,'identity_checks':0,'exact_group_order_checks':0,'interior_order_checks':0,'bfs_checks':0,'violations':0,'rows':[]}
    for n in range(4,args.identity_max+1):
        for a,b in combinations(range(1,n-1),2):
            if a+b<=n-3:
                check_identities(n,a,b);report['identity_checks']+=1
    for n in range(4,args.order_max+1):
        count=0;interior=0;pred=0;candidate=0
        for a,b in combinations(range(1,n-1),2):
            o=group_order(n,a,b);report['exact_group_order_checks']+=1
            gen=o==factorial(n);count+=gen
            if n<=args.bfs_max:
                assert o==bfs_order(n,a,b);report['bfs_checks']+=1
            if gen:
                assert congruence(n,a,b)
                assert a+b<=n+1
            if a>=2 and a+b<=n-3:
                assert gen==congruence(n,a,b),(n,a,b,o)
                report['interior_order_checks']+=1;interior+=gen;pred+=congruence(n,a,b)
            if a+b<=n and congruence(n,a,b):candidate+=1
        report['rows'].append({'n':n,'actual_f':count,'interior_count':interior,'interior_predicted':pred,'lattice_count':candidate})
        print(n,count,interior,candidate,flush=True)
    report['coefficients']={str(r):c/pi**2 for r,c in enumerate((3/4,9/8,1,3/2))}
    (ROOT/'results.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps({k:v for k,v in report.items() if k!='rows'},indent=2))
if __name__=='__main__':main()
