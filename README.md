# Open Problems Lab

![Open Problems Lab — AI-assisted problem solving, rigorous investigation, reproducible evidence](assets/lab-banner.svg)

**A founder-led, AI-assisted problem-solving lab. Any meaningful problem is fair game: from everyday obstacles and business ideas to technical challenges, open mathematics and scientific research.**

Founded by [Zakk Easterbrook](https://github.com/zakkeasterbrook). Preliminary AI-assisted research; independent review is essential.

[Research ledger](RESEARCH.md) · [Research protocol](governance/RESEARCH_PROTOCOL.md) · [Contribute](CONTRIBUTING.md) · [Cite](CITATION.cff) · [Agent guide](AGENTS.md)

## Mission

Start with a question Zakk wants to investigate. Use AI as a research and engineering partner: understand the problem, find reliable evidence, propose an approach, test it, and record what actually works. Some projects may lead to mathematical discoveries; others may lead to useful software, business decisions, prototypes or practical solutions. We value a correct negative result over an impressive but unsupported claim. Public projects must pass the appropriate review and disclosure gates.

## Research portfolio

| ID | Project | Field | Status |
|---|---|---|---|
| OPL-001 | [Asymptotic enumeration of generating triples of prefix reversals](research/mathematics/prefix-reversal-asymptotics/) | Combinatorics / group theory | Candidate proof; finite computational checks recorded |
| OPL-002 | [Predictive Atom 5](https://github.com/zakkeasterbrook/PA5/tree/001026e999b858fa184ecc342e9e24abbe016db8) | AI inference / information access | Published experimental prototype; numerical caveat documented |
| OPL-003 | [The Adaptive Compute Barrier](https://github.com/zakkeasterbrook/PA5/tree/a916efe114992a5effcd05d7a8e7725867d4e650/research/adaptive-compute-barrier) | AI computation / optimization | Published preliminary mathematical result |

No listed project is asserted to be independently refereed or to have established worldwide priority. The ledger records proof, computational checks, publication, formal verification, and external review separately.

## Featured research: OPL-001

For the number $f(n)$ of pairs of shorter prefix reversals that generate $S_n$ together with the full reversal, the preliminary note derives

$$f(n)=c_{n\bmod 4}n^2+O(n\log n),\qquad(c_0,c_1,c_2,c_3)=\frac{1}{\pi^2}(3/4,9/8,1,3/2).$$

The note builds on prior permutation-group research and an existing refutation of part of the conjecture. It proposes the exact asymptotic constants; global priority and independent proof review remain unverified.

| Archived test | Count |
|---|---:|
| Exact permutation-identity cases | 74,872 |
| Exact finite group orders | 2,300 |
| Interior classification comparisons (subset) | 715 |
| Independent BFS order checks (subset) | 35 |
| Recorded violations | 0 |

[Read the proof and references](research/mathematics/prefix-reversal-asymptotics/paper.md) · [Verification code](research/mathematics/prefix-reversal-asymptotics/verify.py) · [Recorded results](research/mathematics/prefix-reversal-asymptotics/results.json)

## How problems are investigated

1. **Intake:** state the problem, desired outcome, constraints, and success criteria. For research novelty claims, identify the documented open question and source.
2. **Investigate:** search related work and document existing solutions and limitations.
3. **Develop:** record assumptions and propose a solution, prototype, experiment, theorem or counterexample.
4. **Verify:** use evidence suited to the problem: exact proof for universal math claims, controlled tests for engineering, and measurable outcomes for practical or business questions.
5. **Challenge:** seek counterexamples, hidden assumptions, numerical failure and prior art.
6. **Review:** distinguish internal AI-assisted checks from independent expert review.
7. **Publish:** preserve evidence, authorship and citations; correct or retract errors transparently.

### Reproduce locally

Python 3.13.5 and SymPy 1.14.0 were used in the founding research package. From the repository root:

```sh
python tools/check_lab.py
python -m pip install -r research/mathematics/prefix-reversal-asymptotics/requirements.txt
python tools/check_lab.py --reproduce quick
# Repeat the original larger finite verification:
python tools/check_lab.py --reproduce full
```

The reproduction tool runs in a temporary directory and checks the resulting records against the archived results. It does not overwrite the evidence. Finite verification is not a formal proof of the infinite theorem. A passing automated check is not peer review.

## Research areas

| Area | Example investigations |
|---|---|
| Everyday life and practical problems | Workflows, tools, accessibility, household and service problems |
| Business and entrepreneurship | Validated customer needs, pricing, cost reductions, operating systems and market opportunities |
| Engineering and technology | Software, hardware, automation, reliability and design |
| AI and computing | Inference efficiency, reasoning, algorithms, privacy and optimization |
| Mathematics and science | Published conjectures, proofs, experiments and testable hypotheses |
| Other | Any clearly stated problem with an appropriate investigation and safety plan |

No area is limited to academic conjectures. New projects require a meaningful target and a suitable verification method. There is no claim that all problems are solvable or that the lab has already solved problems in each area.

## Participate

Use the [problem intake template](templates/PROBLEM.md) to record an idea, or open an issue proposing any problem, submitting a replication, or identifying a flaw. Do not submit sensitive or commercially confidential information in a public issue. Read [CONTRIBUTING.md](CONTRIBUTING.md). Human and AI-assisted contributions are welcome. We explicitly acknowledge prior research and do not claim another researcher's result as our own.

## From research to useful products

Open research builds trust and enables independent scrutiny. Viable commercial products, sponsored investigations, consulting, or hosted services can fund further research. A separate pre-disclosure review is required for confidential or potentially patentable ideas; public release is not a default for those projects. See [commercialization policy](governance/COMMERCIALIZATION.md). There is no promised income or funding.

## Citation and licensing

Use each project's own citation file when referencing its results; include the commit or archived version. See [CITATION.cff](CITATION.cff), [NOTICE](NOTICE), and [LICENSE](LICENSE). Original lab materials are Apache-2.0 licensed to the extent applicable rights are held; third-party works retain their own terms. No DOI, institutional affiliation, endorsement, peer-review acceptance, or guaranteed AI attribution is claimed.
