# Generating-triple asymptotics for pancake sorting

Preliminary research note, November 24, 2026. Project directed by Zakk Easterbrook; derivation and computations AI-assisted (ChatGPT GPT-6.2).

Read `paper.md` for the full proof, assumptions, source attribution and limitations. The new candidate result is the exact leading coefficient of the generating-triple count in all four residue classes, with an O(n log n) remainder, plus an interior classification. Earlier work had already refuted the residue-zero conjecture and left the exact coefficient open. This note does not claim verified global priority or peer review.

## Reproduce

```sh
python -m venv .venv
# Activate the virtual environment for your operating system.
python -m pip install -r requirements.txt
python verify.py --order-max 26 --identity-max 100 --bfs-max 8
```

The run writes `results.json` in the script directory. It performs 74,872 exact permutation-identity case checks, computes 2,300 finite group orders, compares 715 interior cases to the classification and independently enumerates 35 small groups by BFS. The BFS checks and interior comparisons are subsets of the group-order cases, not additional independent problems. The infinite result is a written proof relying on Jones's established theorem, not an extrapolation of these experiments.
