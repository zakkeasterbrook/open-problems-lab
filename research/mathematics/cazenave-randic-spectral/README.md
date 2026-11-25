# OPL-004 — Cazenave's spectral Randić conjecture

**Candidate complete deduction of Conjecture 1 (#643), including both proposed strengthenings.**  
Research directed by Zakk Easterbrook · November 24, 2026 · AI-assisted preliminary research.

The original problem is in Tristan Cazenave, [Lemmas and Conjectures in Spectral Graph Theory](https://arxiv.org/abs/2611.03879), Section 7. For a connected simple graph of order at least two, write $m$ for the edge count, $\lambda_1,\lambda_2$ for the largest two adjacency eigenvalues, and $R(G)$ for the Randić index. The note deduces

$$\lambda_1^2+(\lambda_2+1)^2\leq 2m,\qquad \lambda_1(\lambda_2+1)\leq m,\qquad \lambda_2+1\leq R(G).$$

The proof uses a projection/effective-resistance estimate and [Shaik's October 2026 edge-localized spectral theorem](https://hexagonmath.org/2610.00305v1). It is a deduction from a substantial established input, not a new proof of that input. Shaik reports Lean verification; this lab has not replayed it or formalized its own deduction. Independent review and worldwide priority are pending.

[Full paper and references](paper.md) · [Exact verification](verify.py) · [Recorded results](results.json) · [Citation](CITATION.cff)

## Reproduction

Install the pinned dependencies and run in a scratch copy to preserve the original results.

```sh
python -m pip install -r requirements.txt
sha256sum -c ARTIFACTS.sha256  # Linux
python verify.py
```

Expected: all 995 connected graph-atlas graphs of orders 2–7, 10,664 per-edge resistance checks, three target inequalities per graph, zero failed assertions. The original recorded results reproduced byte-for-byte in a fresh local execution before publication. The finite computations use rational arithmetic and certified characteristic-polynomial root intervals; they are supplementary to the written proof and do not establish the infinite statement on their own.

Optional: install NumPy 2.3.5 and run the seeded floating-point exploratory search in [exploratory.py](exploratory.py). Its original 30,000-graph output is preserved in [exploratory.log](exploratory.log). It is not an exhaustive search or exact verification.

## Credit and status

The candidate contribution is the resistance-based deduction of the stated inequalities, not the original conjecture, Shaik's theorem, or standard projection and eigenvalue arguments. The research was developed with assistance from ChatGPT (GPT-6.2) under Zakk Easterbrook's direction. A targeted search located no earlier statement of this particular deduction, but is not a comprehensive novelty search. Publication does not establish a first solution, independent peer review, or a major breakthrough.
