"""Exact finite checks for the Cazenave Conjecture 1 deduction.

For all connected graphs in NetworkX's graph atlas (orders 2 through 7),
check Foster's identity and the clique upper bounds in rational arithmetic.
Certify the three target inequalities using rational eigenvalue and square-root
intervals, not floating-point eigensolvers. These checks are not a proof for
arbitrary order, and do not independently replay Shaik's formalized theorem.
"""
import json
from collections import Counter
from math import isqrt
from pathlib import Path
import networkx as nx
import sympy as sp

S = 10**9
EPS = sp.Rational(1, S)

def lower_inverse_sqrt(k):
    return sp.Rational(isqrt(S*S//k), S)


def check(G):
    n = len(G)
    G = nx.convert_node_labels_to_integers(G, ordering='sorted')
    edges = list(G.edges())
    m = len(edges)
    deg = dict(G.degree())
    A = sp.zeros(n)
    B = sp.zeros(n-1,m)  # delete the last row of oriented incidence matrix
    for j,(u,v) in enumerate(edges):
        A[u,v] = A[v,u] = 1
        if u < n-1: B[u,j] = 1
        if v < n-1: B[v,j] = -1
    # The diagonal of the orthogonal projection onto row(B) equals
    # effective resistance on each edge; avoid explicitly forming m x m P.
    H = (B*B.T).inv()
    cliques = list(nx.find_cliques(G))
    q = {tuple(sorted((u,v))):max(len(C) for C in cliques if u in C and v in C)
         for u,v in edges}
    resistances = [(B[:,j].T*H*B[:,j])[0] for j in range(m)]
    assert sum(resistances) == n-1
    assert all(0 < p <= sp.Rational(2,q[tuple(sorted(e))]) for p,e in zip(resistances,edges))
    assert sum(sp.Rational(2,k) for k in q.values()) >= n-1
    # Every adjacency eigenvalue is real. Rational isolating intervals
    # are disjoint, ordered and include multiplicities.
    roots = []
    for ab, mult in A.charpoly().as_poly().intervals(eps=EPS):
        roots.extend([ab]*mult)
    assert len(roots) == n
    (l0,l1),(t0,t1) = roots[-1],roots[-2]
    assert l0 > 0 and t0 >= -1
    assert 2*(t1+1) <= n
    # Square bound is exact because 0 <= t+1 and L > 0.
    assert l1*l1+(t1+1)**2 <= 2*m
    assert l1*(t1+1) <= m
    Rlo = sum(lower_inverse_sqrt(deg[u]*deg[v]) for u,v in edges)
    assert Rlo >= t1+1
    return m


def main():
    counts=Counter(); edges=0
    for G in nx.graph_atlas_g():
        if len(G) < 2 or not nx.is_connected(G):
            continue
        edges+=check(G); counts[len(G)]+=1
    result={'graphs_by_order':dict(sorted(counts.items())),
            'graphs':sum(counts.values()),'edge_resistance_checks':edges,
            'target_inequalities_per_graph':3,'failures':0,
            'arithmetic':'exact rational with certified characteristic-polynomial root intervals',
            'networkx':nx.__version__,'sympy':sp.__version__}
    print(json.dumps(result,indent=2))
    Path(__file__).with_name('results.json').write_text(json.dumps(result,indent=2)+'\n')

if __name__=='__main__': main()
