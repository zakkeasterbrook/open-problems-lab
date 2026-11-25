# A resistance-based deduction of Cazenave's Randić spectral conjecture

**Open Problems Lab — candidate research note, November 24, 2026 (US Eastern).**
Research directed by Zakk Easterbrook; mathematical exploration, derivation and computational checks generated with assistance from ChatGPT (GPT-6.2). This note has not been independently reviewed, its priority is unverified, and its new deduction has not been formalized in Lean.

## Abstract

Cazenave [1], Conjecture 1 (#643), asks whether every connected finite simple graph with at least two vertices satisfies $R(G)\geq\lambda_2(G)+1$. The same section proposes two stronger inequalities. Using Shaik's October 2026 edge-localized Bollobás–Nikiforov theorem [2, Theorem 1.1], we give a short deduction proving the entire chain

$$\lambda_1^2+(\lambda_2+1)^2\leq 2m,\qquad \lambda_1(\lambda_2+1)\leq m,\qquad \lambda_2+1\leq R(G).$$

The key is a projection (equivalently effective-resistance) inequality: if $c(e)$ is the largest order of a clique containing edge $e$, then $2\sum_{e\in E}1/c(e)\geq n-1$. Combined with [2], this gives $\lambda_1^2+\lambda_2^2\leq 2m-n+1$ for connected noncomplete graphs. A sign-support estimate completes the argument. We give every step of the deduction and handle complete graphs separately. The October theorem is a substantial external dependency, reported formally verified by its author; we have not independently replayed that verification. We do not claim a new proof of the localized Bollobás–Nikiforov theorem itself or a verified first solution.

## 1. Definitions and cited input

Let $G=(V,E)$ be a finite connected simple undirected graph, $n=|V|\geq2$, $m=|E|$. Let $d_v$ be the degree of $v$, $A$ the adjacency matrix, and $L=\lambda_1(A)$, $t=\lambda_2(A)$ in decreasing algebraic order with multiplicities. Define

$$R(G)=\sum_{uv\in E}(d_ud_v)^{-1/2}.$$

For each edge $e$, let $c(e)\geq2$ be the order of a largest clique containing it. The external theorem used is Shaik [2, Theorem 1.1, p. 2]: for every finite simple noncomplete graph of order at least two,

$$L^2+t^2\leq2\sum_{e\in E}\left(1-\frac1{c(e)}\right).\tag{1}$$

The manuscript explicitly uses algebraically ordered eigenvalues, unordered edges, and allows disconnected graphs. Its reported checked declaration is `LocalBN.edgeLocalizedNoncompleteUnordered`, registered as PALOMAR-2026-10-15-000015 v1. The new argument below does not assume a solution of Cazenave's conjecture.

## 2. Local clique reciprocal bound

**Lemma.** Every connected simple graph satisfies $2\sum_e1/c(e)\geq n-1$.

**Proof.** Orient all edges arbitrarily and let $B$ be the $(n-1)\times m$ incidence matrix with one vertex row deleted. Connectedness implies $B$ has full row rank: a linear dependence among its rows, extended by coefficient zero at the deleted vertex, would give a function constant across every edge and therefore constant zero. Thus

$$P=B^\top(BB^\top)^{-1}B$$

is the orthogonal projection in $\mathbb R^m$ onto the row space of $B$; its trace is $n-1$.

Fix an edge $e$ oriented from $u$ to $v$, write $c=c(e)$, and select a clique of order $c$ containing it. Let $\mathbf e_e$ be the coordinate vector of $e$. Define a signed edge flow $f$ supported on this clique: send $2/c$ directly from $u$ to $v$, and for each of the $c-2$ other clique vertices $w$, send $1/c$ along the two-edge path $u,w,v$. Edge signs are taken relative to the chosen orientations. The total net flow from $u$ to $v$ is $2/c+(c-2)/c=1$ and all intermediate net flows vanish. Hence $Bf=B\mathbf e_e$, so $Pf=P\mathbf e_e$. The direct edge and all two-step path edges are distinct. As an orthogonal projection is a contraction,

$$P_{ee}=\|P\mathbf e_e\|_2^2=\|Pf\|_2^2\leq\|f\|_2^2=\frac{4+2(c-2)}{c^2}=\frac2c.$$

Summing over the edges gives the lemma. This is the electrical-network argument using Foster's identity and monotonicity of effective resistance, written solely in elementary linear algebra. QED.

## 3. A two-eigenvalue Hong-type inequality

**Corollary.** If $G$ is connected and noncomplete,

$$L^2+t^2\leq2m-n+1.\tag{2}$$

Indeed, (1) and the lemma give $L^2+t^2\leq2m-2\sum_e1/c(e)\leq2m-n+1$. This strengthening of the classical one-eigenvalue Hong bound is the bridge to the conjecture. The noncomplete qualification is essential: in $K_n$, the left side exceeds $2m-n+1$ by 1. The bound is sharp for every star of order at least three, since $L^2=m=n-1$ and $t=0$.

## 4. Second-eigenvalue size bound

**Lemma.** $t\leq n/2-1$ for every connected graph of order at least two.

**Proof.** Perron–Frobenius gives a strictly positive eigenvector for the simple eigenvalue $L$. Any real eigenvector $y$ for $t$ is orthogonal to it and so has both positive and negative entries. Let $V_+=\{v:y_v>0\}$ and $V_-=\{v:y_v<0\}$. At a maximal coordinate $y_u>0$, the eigenvalue equation gives

$$t y_u=\sum_{v\sim u}y_v\leq (|V_+|-1)y_u.$$

Apply the same reasoning to $-y$ to obtain $t\leq|V_-|-1$. Since the supports are disjoint, $2(t+1)\leq n$. QED.

## 5. Resolution of the entire proposed chain

**Theorem.** Every finite connected simple graph of order $n\geq2$ satisfies all three inequalities in the abstract.

**Proof.** For a noncomplete graph, (2) and Section 4 imply

$$L^2+(t+1)^2\leq(2m-n+1)+2t+1=2m+2(t+1)-n\leq2m.$$

For a complete graph $K_n$, $L=n-1$, $t=-1$, and $2m=n(n-1)$; thus $L^2+(t+1)^2=(n-1)^2\leq2m$ directly, including $K_2$.

The first bound gives the second by $2L(t+1)\leq L^2+(t+1)^2$. Finally, put $x_v=\sqrt{d_v}$. The Rayleigh bound gives

$$\sum_{uv\in E}\sqrt{d_ud_v}=\tfrac12 x^\top A x\leq\tfrac12 L\|x\|^2=Lm.$$

By Cauchy–Schwarz,

$$m^2\leq\left(\sum_{uv\in E}\sqrt{d_ud_v}\right)R(G)\leq LmR(G).$$

Since $m>0$ and $L>0$, this is $R(G)\geq m/L$. Combining with the second bound proves $R(G)\geq t+1$, Cazenave's Conjecture 1. QED.

## 6. Additional consequences already implicit in classical bounds

The following are included to clarify which of the paper's other listed conjectures follow from established mathematics, rather than claiming them as new discoveries.

Conjecture 3: set $S=D^{-1/2}AD^{-1/2}$ where $D$ is the degree diagonal. Both $I+S$ and $I-S$ are positive semidefinite (from the sums of squares for $D+A$ and $D-A$), so $\|S\|_{\rm op}\leq1$. In an orthonormal eigenbasis of $A$, $\operatorname{tr}(AS)=\sum_i\lambda_i u_i^\top Su_i\leq\sum_i|\lambda_i|\leq\operatorname{rk}(A)L$. Directly, $\operatorname{tr}(AS)=2R$. Thus Conjecture 3 follows.

For Conjecture 6(i) and the first inequality in 6(iv), the classical Hong bound $L^2\leq2m-n+1$ and $L\leq n-1$ imply $L^2+L\leq2m$. Together with $R\geq m/L$ this gives

$$R\geq\frac{1+\sqrt{1+8m}}4=:b.$$

Now $b^2-(m+1)/2=(\sqrt{1+8m}-3)/8\geq0$ for $m\geq1$, proving 6(i). Also $3\sqrt{1+8m}\geq8\sqrt m+1$, since the difference of the squares is $8(\sqrt m-1)^2\geq0$. Thus $b\geq(2/3)\sqrt m+1/3$, proving the first half of 6(iv). We make no claim here about 6(ii), 6(iii), the rank-based half of 6(iv), Conjecture 2, or the radius conjecture (Conjecture 7).

## 7. Computational checks and research status

`verify.py` enumerates all 995 connected graphs of orders 2 through 7 in the NetworkX graph atlas. Exact rational arithmetic checks the projection trace, 10,664 per-edge resistance bounds, and the clique reciprocal sum. The three target inequalities and the size bound on $t$ are certified using rational root-isolation intervals for integer adjacency characteristic polynomials and rational lower bounds on the reciprocal square roots defining $R(G)$. All checks passed. The original results are in `results.json`. These checks are supplementary; they do not establish the theorem for infinitely many graphs, nor replay the underlying Lean theorem.

A separate exploratory floating-point search generated 30,000 connected random graph blowups with 3–12 template vertices (independent-set or clique blocks of varying sizes). All three proposed inequalities survived those tests. This exploratory search is provided separately, not characterized as exact or exhaustive.

## References and provenance

1. Tristan Cazenave, *Lemmas and Conjectures in Spectral Graph Theory*, arXiv:2611.03879v1, November 2, 2026, Section 7, Conjecture 1 (#643), p. 10. The two strengthened inequalities are stated immediately following Conjecture 1; Theorem 31 treats bipartite graphs. Theorem 2 gives the classical Favaron–Mahéo–Saclé bound, Theorem 3 the Hong bound. https://arxiv.org/abs/2611.03879
2. Idris Ali Shaik, *Three conjectures on the first two graph eigenvalues*, Hexagon 2610.00305v1, October 17, 2026, Theorem 1.1, p. 2. https://hexagonmath.org/2610.00305v1 ; Palomar record https://palomar-registry.org/entry?id=PALOMAR-2026-10-15-000015&version=1 ; source author's explanation https://shaikidris.github.io/kkp-localized/ . The localized theorem relies on the weighted spectral methods of Coutinho, Liu, Spier, Tang and Zhang. We verified the statement and its reported registration, not the proof assistant build.
3. Chuling Zhang and Xiying Yuan, *A characterization of equality in the edge-localized Bollobás–Nikiforov inequality*, arXiv:2610.36912v1, October 27, 2026. Independent literature reference identifying Shaik's localized result. https://arxiv.org/abs/2610.36912
4. O. Favaron, M. Mahéo and J.-F. Saclé, *Some eigenvalue properties in graphs (conjectures of Graffiti II)*, Discrete Mathematics 111 (1993).
5. Y. Hong, *A bound on the spectral radius of graphs*, Linear Algebra and its Applications 108 (1988).

The claimed contribution is the deduction connecting the localized theorem to all three Cazenave inequalities through the resistance bound, not the prior spectral theorem, the classical projection argument, or the other standard estimates. A targeted search on November 24, 2026 did not locate a prior proof of this particular deduction; this is not a comprehensive priority search. Independent mathematical review, a fresh literature audit, and formal verification of the new deduction are outstanding. No claim of a major world-first breakthrough, endorsement, peer review, or verified exclusive authorship is made.
