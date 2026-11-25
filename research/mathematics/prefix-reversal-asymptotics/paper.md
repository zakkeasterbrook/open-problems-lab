# Asymptotic enumeration of generating triples of prefix reversals

**Research project directed by Zakk Easterbrook; mathematical derivation, exposition and computations generated with assistance from ChatGPT (GPT-6.2).**  
**November 24, 2026 (US Eastern time). Preliminary research note, v0.1.0.**

## Abstract

Let $r_i$ denote reversal of the first $i$ positions in $S_n$, and let $f(n)$ count pairs $2\leq k<m<n$ with $\langle r_n,r_m,r_k\rangle=S_n$. We prove, subject to the classical theorem of Jones on primitive permutation groups containing a cycle, that

$$f(n)=c_{n\bmod 4}n^2+O(n\log n),\qquad (c_0,c_1,c_2,c_3)=\frac1{\pi^2}(3/4,9/8,1,3/2).$$

The proof supplies a necessary and sufficient generation criterion away from a boundary containing only $O(n)$ pairs, and then evaluates the resulting coprime lattice count. The group-theoretic method builds directly on the commutator and primitivity arguments in Lei, Zhao, Zhu and Wu (October 2026); the key observation is that the transitivity needed for those arguments follows directly from the gap arithmetic in the interior. All four constants in Blanco et al.'s Conjecture 1 differ from these constants. An existing trureturing result already refutes the residue-zero assertion; this note does not claim priority for that refutation. Its stated open questions include the exact leading coefficients and matching lower bounds. A targeted literature search found no earlier statement of these exact coefficients, but worldwide priority is unverified. The note is AI-assisted and has not been independently refereed or formally verified in a proof assistant.

## 1. Definitions and statement

For $1\leq x\leq n$, define $r_i(x)=i+1-x$ if $x\leq i$ and $r_i(x)=x$ otherwise. Let $a=n-m$, $b=n-k$, so $1\leq a<b\leq n-2$, and put $G=\langle r_n,r_{n-a},r_{n-b}\rangle$. Composition acts right to left. We call a pair interior if

$$2\leq a<b,\qquad a+b\leq n-3.$$

**Theorem A (interior classification).** For interior pairs, $G=S_n$ if and only if:

1. $\gcd(a,b)=1$;
2. when $n$ is even, $a$ and $b$ have opposite parity;
3. at least one of $n,n-a,n-b$ is congruent to 2 or 3 modulo 4.

**Theorem B (asymptotic enumeration).** The formula in the abstract holds along each of the four residue classes, with an absolute implied constant. No assertion of an $O(n)$ remainder or exact classification on the boundary is made.

## 2. Necessary conditions and boundary bound

The sign of $r_i$ is $(-1)^{\lfloor i/2\rfloor}$, so condition 3 is necessary.

If a common divisor $d\geq3$ divides $a$ and $b$, all three reversal lengths are congruent to $n$ modulo $d$. A reversal either fixes $x$ or sends it to $n+1-x$ modulo $d$. Consequently the union of residue classes $1$ and $n$ modulo $d$ is a nonempty proper invariant subset of $\{1,\ldots,n\}$: it is nonempty since it contains 1, and proper since $d\leq a<n$ and it contains at most two of the $d$ residue classes. This precludes transitivity.

If 2 divides both gaps, then all three lengths have the same parity as $n$. For odd $n$, odd-length reversals preserve position parity; for even $n$, all even-length reversals preserve the partition into consecutive pairs $\{1,2\},\{3,4\},\ldots,\{n-1,n\}$. In either case $G\ne S_n$ for $n\geq4$. Thus condition 1 is necessary. If $n$ is even and both gaps are odd, the shorter reversals preserve parity and the full reversal exchanges the parity classes. These classes give a nontrivial invariant partition, proving condition 2.

Finally, draw an edge for each transposition in the disjoint transposition decompositions of the three reversals. The connected components of this graph are exactly the orbits of the generated group: each edge is a possible generator move, and each generator moves a point along an edge or fixes it. If $G=S_n$, connectivity requires at least $n-1$ distinct edges. The total number of edges, even allowing multiplicity, is at most

$$\lfloor n/2\rfloor+\lfloor(n-a)/2\rfloor+\lfloor(n-b)/2\rfloor\leq(3n-a-b)/2.$$

Hence $a+b\leq n+2$. This deliberately weak bound is sufficient for the asymptotic argument. See also Lei et al., Theorem 3.1, for stronger parity-dependent boundary bounds.

## 3. The commutator and transitivity

Assume the three conditions of Theorem A and the interior inequalities. Set $s=a+b$, $t=n-s\geq3$, $R=r_n$, $A=Rr_{n-a}$, $B=Rr_{n-b}$. For $d=a,b$, the map $T_d=Rr_{n-d}$ sends $x$ to $x+d$ when $x\leq n-d$ and to $n+1-x$ otherwise. Thus $A=T_a$, $B=T_b$.

Let $D=AB(BA)^{-1}$. We show that $D$ is addition of $2a$ modulo $s$ on $S=\{1,\ldots,s\}$ and fixes $F=\{s+1,\ldots,n\}$. For $x\leq t$, both $AB(x)$ and $BA(x)$ equal $x+s$. For $x=t+j$, $1\leq j\leq s$, we have

$$AB(x)=\begin{cases}a+1-j&j\leq a,\\s+a+1-j&j>a,\end{cases}$$

and the analogous formula with $b$ in place of $a$ for $BA(x)$. Both range over $S$, and their difference modulo $s$ is $a-b\equiv2a\pmod s$. This proves the claimed identity.

Since $\gcd(a,b)=1$, we have $\gcd(2a,s)=\gcd(2,s)$. Hence some power $U$ of $D$ is the rotation by 1 on $S$ if $s$ is odd, or by 2 on $S$ if $s$ is even; in both cases it fixes $F$.

Write $H=\langle A,B\rangle$. If $s$ is odd, $U$ is transitive on $S$. If $s$ is even, $a,b$ are odd and $U$ has exactly two orbits on $S$, its odd and even positions. Since $A(1)=1+a$ is even and lies in $S$, those two orbits are joined in $H$. Thus in either case all of $S$ lies in a single $H$-orbit. Every $x>s$ can be moved into $S$ by repeatedly applying $A^{-1}$, which sends $x$ to $x-a$ whenever $x>a$. This proves that $H$, and therefore $G$, is transitive. No generating assumption in a smaller degree is needed.

We will use the following elementary set identity. With $h=\min(a,t)$,

$$S\setminus A(S)=\{1,\ldots,h\}.$$

Indeed if $t\geq a$, $A(S)=[a+1,a+s]$. If $t<a$, the non-reflected and reflected parts of $S$ give $A(S)=[a+1,n]\cup[t+1,a]=[t+1,n]$. This proves the identity in both cases.

## 4. Primitivity and a cycle with at least three fixed points

A block is a nonempty set $C$ such that for every group element $g$, either $g(C)=C$ or $g(C)\cap C=\varnothing$. In a transitive group the translates of a block partition the domain into equal-sized blocks. A group is primitive if it has no nontrivial such partition. We use Jones (2014), Corollary 1.3: a finite primitive permutation group containing a single nontrivial cycle with at least three fixed points contains the alternating group. This is an established classification theorem; our use of it is not a claim to reprove it.

### 4.1. Odd $s$

Here $U$ is a single $s$-cycle. Suppose a block $C$ for $G$ meets both $S$ and $F$. Because $U$ fixes a member in $F$, $U(C)=C$, and thus $S\subseteq C$. Since $A(1)=a+1\in S$, the block property implies $A(C)=C$. Every point outside $S$ is connected to $S$ by the powers of $A$ as above; hence $C$ is the entire domain.

In a nontrivial invariant block partition no block can therefore meet both $S$ and $F$. Both $S$ and $A(S)$ are unions of blocks. So is $I=S\setminus A(S)=[1,h]$, and so is $I\setminus U(I)=\{1\}$, because $1\leq h<s$. The common block size is then 1, a contradiction to nontriviality. Thus $G$ is primitive. The $s$-cycle $U$ fixes $t\geq3$ positions, and Jones's theorem yields $A_n\leq G$ (where $A_n$ denotes the alternating group, distinct from the permutation $A$).

### 4.2. Even $s$

Coprimality implies that $a$ and $b$ are odd. By condition 2, $n$ is odd. Thus $t$ is odd, $a\geq3$, $b\geq a+2$, and $h=\min(a,t)$ is odd with $h\geq3$. Let $P$ and $Q$ be the odd and even positions of $S$. The map $U$ is a cycle on each of $P,Q$ and fixes $F$.

Suppose a block $C$ meets $S$ and $F$. Then $U(C)=C$, so $C$ contains $P$ or $Q$. Let $C'=A(C)$. If $P\subseteq C$, then $A(1)=1+a\in Q$ and $A(b+2)=s+2\in F$, with $1,b+2\in P$; therefore $U(C')=C'$ and $Q\subseteq C'$. If $Q\subseteq C$, use $A(2)=2+a\in P$ and $A(b+1)=s+1\in F$ instead to obtain $P\subseteq C'$. All these uses of $A(x)=x+a$ are valid since $t\geq3$ and $a\geq3$.

In either case, $A^2(C)$ intersects $C$, using $A^2(1)=1+2a\in P$ or $A^2(2)=2+2a\in Q$, respectively. Thus $A^2(C)=C$. Also $B(1)=b+1\in Q$ and $B(2)=b+2\in P$, so $B(C)=C'$ and $B(C')=C$. The union $C\cup C'$ is invariant under $A,B$, and transitivity of $H$ implies it equals the whole domain. If $C,C'$ were different they would be two disjoint equally sized blocks, impossible since $n$ is odd. Therefore $C$ equals the whole domain.

As in the odd-$s$ case, any nontrivial invariant block partition must have $S$ and $F$ as unions of blocks. The set $I=[1,h]$ is a union of blocks, as is $I\setminus U(I)=\{1,2\}$. The common block size divides both 2 and odd $n$, hence is 1. This proves primitivity.

We now construct a single cycle to apply Jones's theorem. Let $V=AUA^{-1}$ if $t\geq a$, and $V=RU^{-1}R$ if $t<a$. In the first case $A$ translates the whole of $S$ by $a=h$; in the second case $R$ reverses the interval $S$ onto $[t+1,n]$ with $t=h$, so conjugating the inverse rotation gives a positive rotation. Thus in both cases $V$ is addition of 2 modulo $s$ on $[h+1,h+s]$ and fixes its complement.

For $W=VU^{-1}$, one-line evaluation gives the two disjoint cycles

$$\begin{aligned}
 &(1, s+1,s+3,\ldots,s+h, h+2,h,h-2,\ldots,3),\\
 &(2, s+2,s+4,\ldots,s+h-1,h+1,h-1,\ldots,4).
\end{aligned}$$

All remaining positions are fixed. To verify, $W(1)=s+1$, $W(2)=s+2$; for $3\leq x\leq h+2$ we have $W(x)=x-2$; for $h+3\leq x\leq s$ it fixes $x$; for $s+1\leq x\leq s+h-2$ it sends $x$ to $x+2$; and $s+h-1,s+h$ wrap to $h+1,h+2$ respectively. This gives cycle lengths $h+2$ and $h$. Since $h$ is odd, $\gcd(h,h+2)=1$, so $W^h$ is a single $(h+2)$-cycle. It fixes $n-h-2\geq s-2\geq6$ points. Jones's theorem again implies $A_n\leq G$.

Finally, condition 3 supplies an odd permutation in $G$. A subgroup containing $A_n$ and an odd permutation equals $S_n$. This proves Theorem A.

## 5. Counting coprime lattice points

Let $L(n)$ count positive pairs $a<b$ with $a+b\leq n$ satisfying the three arithmetic conditions in Theorem A. By the interior theorem and necessary conditions, every discrepancy between $L(n)$ and $f(n)$ lies on the line $a=1$ or in the bounded-width strip $n-2\leq a+b\leq n+2$. There are $O(n)$ such points, so

$$f(n)=L(n)+O(n).$$

For $r=n\bmod4$, first select the ordered pairs of residues $(a\bmod4,b\bmod4)$ consistent with conditions 2 and 3, and with not both gaps even. Their numbers $M_r$ are as follows:

| $r$ | Allowed parity patterns | Additional sign restriction | $M_r$ |
|---|---|---|---:|
| 0 | opposite | at least one gap is 1 or 2 mod 4 | 6 |
| 1 | not both even | at least one gap is 2 or 3 mod 4 | 9 |
| 2 | opposite | none (full reversal is odd) | 8 |
| 3 | not both even | none (full reversal is odd) | 12 |

For example, in residue zero, there are eight opposite-parity ordered pairs of residues, and the two pairs $(0,3),(3,0)$ have no odd generator. In residue one, there are twelve pairs with not both gaps even, and the three pairs $(0,1),(1,0),(1,1)$ have no odd generator.

Every pair admitted by these modular restrictions has odd greatest common divisor. Use the Möbius function $\mu$ and the identity $1_{\gcd(a,b)=1}=\sum_{d\mid a,\ d\mid b}\mu(d)$. Only odd $d$ contribute. For a fixed odd $d$, writing $a=du$, $b=dv$ maps the $M_r$ allowed residue pairs bijectively to $M_r$ ordered residue pairs for $(u,v)$ modulo 4. In the triangle $0<u<v$, $u+v\leq n/d$ of area $n^2/(4d^2)$, each fixed residue pair contributes

$$\frac{n^2}{64d^2}+O(n/d+1).$$

This elementary lattice estimate follows by covering with the fundamental $4\times4$ squares: each full square contains one point of each residue pair, and only $O(n/d+1)$ squares intersect the boundary, whose three sides have total length $O(n/d+1)$. The implied constant is uniform over the finitely many residue pairs.

Therefore

$$L(n)=\frac{M_r n^2}{64}\sum_{\substack{d\leq n\\d\text{ odd}}}\frac{\mu(d)}{d^2}+O\left(\sum_{d\leq n}(n/d+1)\right).$$

The error is $O(n\log n)$. Absolute convergence permits extending the main sum to infinity at a further cost $O(n)$. The Euler product and Basel sum give

$$\sum_{d\text{ odd}}\frac{\mu(d)}{d^2}=\prod_{p\ne2}(1-p^{-2})=\frac{6/\pi^2}{1-2^{-2}}=\frac8{\pi^2}.$$

Thus $f(n)=M_r n^2/(8\pi^2)+O(n\log n)$, proving Theorem B. This establishes the existence of the limits and their exact values, including matching lower bounds.

## 6. Comparison and verification

| $n\bmod4$ | Blanco et al.'s proposed coefficient | Theorem B |
|---|---:|---:|
| 0 | $1/13$ | $3/(4\pi^2)$ |
| 1 | $1/9$ | $9/(8\pi^2)$ |
| 2 | $1/10$ | $1/\pi^2$ |
| 3 | $1/7$ | $3/(2\pi^2)$ |

All four values are different from their proposed counterparts (for instance, $\pi^2$ is irrational, or use elementary numerical bounds on $\pi$). Consequently none of the original four leading-coefficient assertions holds with a linear remainder. This is not a statement that the original conjecture was still entirely open: trureturing's prior refutation already establishes failure of the residue-zero clause.

`verify.py` tests the commutator, interval and cycle identities across 74,872 interior triples through degree 100. It computes 2,300 exact finite permutation group orders for degrees 4–26 using SymPy, including 715 interior cases compared with Theorem A. It cross-checks 35 of those orders independently by exhaustive breadth-first group enumeration through degree 8. All checks passed; see `results.json`. These finite checks are supplementary, not the proof of an infinite statement or a formal machine proof of the classification theorem. The claimed main result rests on the written derivation and the cited Jones theorem. No external reviewer has checked the note.

## References and priority disclosure

1. S. A. Blanco, M. P. Golubyatnikov, E. V. Konstantinova, N. V. Maslova and L. A. Nikiforov, *Generating the symmetric group by three prefix reversals*, Discrete Mathematics & Theoretical Computer Science 28:1 (September 24, 2026), DOI 10.46298/dmtcs.16975. Conjecture 1, Section 4.1; Problem 3, Section 1.1. https://arxiv.org/html/2511.16959v3 and https://dmtcs.episciences.org/en/articles/16975
2. Y. Lei, J. Zhao, Z. Zhu and Y. Wu, *On the generation of the symmetric group by index relations of three prefix reversals*, arXiv:2610.30892 (October 22, 2026). Lemmas 3.2–3.3 and the related shift results in Theorems 3.4–3.5 motivate the commutator/primitivity argument above. https://arxiv.org/abs/2610.30892 . The full PDF could not be retrieved; the available detailed source rendering was inspected. Accordingly this note gives its own explicit algebraic derivation rather than relying on missing displayed formulas.
3. G. A. Jones, *Primitive permutation groups containing a cycle*, Bull. Aust. Math. Soc. 89 (2014), 159–165, DOI 10.1017/S000497271300049X. https://doi.org/10.1017/S000497271300049X
4. trureturing, *Prefix-reversal triple count: Conjecture 1 is false*, repository release db6076e3e870, accessed November 24, 2026. The record reports a Lean-checked congruence-sieve refutation of the residue-zero prediction and explicitly lists the true limiting coefficient, existence of a limit, matching lower bound and other three residue-class assertions as open. https://www.trureturing.org/research/prefix-reversal-triple-count/ and https://the-omega-institute.github.io/trureturing-mdbook/Problems/prefix-reversal-triple-count.html

The present contribution is the arithmetic sufficiency argument in the interior and the resulting sharp asymptotic enumeration, not the original problem, the earlier refutation, or the group classification theorem. The proof is substantially inspired by Reference 2; the novelty search is not exhaustive. No claim of verified first discovery, acceptance by the original authors, peer review, or Lean formalization is made. Independent checking and a further literature search are needed before a priority claim. This note does not settle the exact boundary classification or the other conjectures in Reference 1.
