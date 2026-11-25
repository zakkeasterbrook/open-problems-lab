# Open Problems Lab

![Open Problems Lab — Bring a problem. Explore solutions. Share the evidence.](assets/lab-banner.svg)

**An open, collaborative initiative to solve meaningful problems using artificial intelligence, human insight, and rigorous investigation.**

No problem is too ordinary to investigate. No idea is beyond questioning. From everyday frustrations to unsolved mathematical conjectures, the aim is to turn questions into useful, testable answers.

[Explore projects](RESEARCH.md) · [Submit a problem](https://github.com/zakkeasterbrook/open-problems-lab/issues/new?template=open_problem.md) · [Contribute](CONTRIBUTING.md) · [Research protocol](governance/RESEARCH_PROTOCOL.md) · [AI agent guide](AGENTS.md)

## Start here

| If you want to... | Where to begin |
|---|---|
| Find a better way to do something | [Propose a problem](https://github.com/zakkeasterbrook/open-problems-lab/issues/new?template=open_problem.md) |
| Investigate an existing challenge | [Browse the research ledger](RESEARCH.md) and [open issues](https://github.com/zakkeasterbrook/open-problems-lab/issues) |
| Test or challenge a finding | [Submit a replication or counterexample](https://github.com/zakkeasterbrook/open-problems-lab/issues/new?template=replication.md) |
| Build a prototype, contribute code, or write a proof | [Contribution guide](CONTRIBUTING.md) |
| Work with an AI assistant or coding agent | [Agent guide](AGENTS.md) and [machine-readable index](llms.txt) |
| Reuse or cite a result | The individual project's research note, license and citation metadata |

Anyone can participate, regardless of academic credentials, profession, location or experience. Curious people, students, researchers, engineers, developers, entrepreneurs, and people bringing real-world problems are all welcome. Bring a question, a method, a dataset, a counterexample, or a new perspective. Participation does not require using a particular AI provider, paid subscription, or advanced computing hardware.

## What problems belong here?

| Area | Example questions |
|---|---|
| Everyday life | Can a common task become simpler, safer, more accessible or less expensive? |
| Engineering and invention | Can a device, process, material or design be improved? |
| Artificial intelligence | Can models reason more reliably or use less time, energy and memory? |
| Computer science | Can an algorithm, system, security method or workflow be improved? |
| Mathematics | Can a conjecture be proved, disproved or narrowed? |
| Science and environment | What hypotheses can be tested, and what evidence would distinguish them? |
| Business and economics | Can a customer problem, operational bottleneck or market assumption be tested? |
| Education and accessibility | Can learning, information or tools become more useful to more people? |
| Other fields | Any clearly framed problem with a responsible investigation and a way to assess progress. |

The examples are starting points, not limits on the lab's scope. A problem need not be globally unsolved or academically novel to be worth investigating.

## How the lab works

1. **Define.** State the question in plain language. Record who benefits, constraints, the baseline, and what would count as success.
2. **Investigate.** Find relevant evidence and previous work. Separate established facts from assumptions and identify what is missing.
3. **Explore.** Use AI and human reasoning to generate alternatives, hypotheses, proofs, designs, or prototypes.
4. **Test.** Choose validation that matches the problem: exact proof, reproducible computation, controlled experiments, real-world measurements, or a clearly documented feasibility study.
5. **Challenge.** Seek counterexamples, hidden assumptions, adverse conditions, and existing solutions that might outperform the proposed approach.
6. **Share.** Record the results, code, source attribution, uncertainty, failures, and review status. Invite others to reproduce or improve the work.
7. **Improve.** Update conclusions when better evidence arrives. Preserve the history of corrections and unsuccessful attempts.

AI is a research tool, not an authority. A convincing explanation is not evidence by itself. The lab values a useful negative result as much as a positive one and will not present an idea as a proven discovery merely because an AI suggested it.

See the [research protocol](governance/RESEARCH_PROTOCOL.md) for the standards used to evaluate claims.

## Research portfolio

| ID | Project | Field | Status |
|---|---|---|---|
| OPL-001 | [Asymptotic enumeration of generating triples of prefix reversals](research/mathematics/prefix-reversal-asymptotics/) | Combinatorics / group theory | Candidate proof; finite computational checks recorded |
| OPL-002 | [Predictive Atom 5](https://github.com/zakkeasterbrook/PA5/tree/001026e999b858fa184ecc342e9e24abbe016db8) | AI inference / information access | Published experimental prototype; numerical caveat documented |
| OPL-003 | [The Adaptive Compute Barrier](https://github.com/zakkeasterbrook/PA5/tree/a916efe114992a5effcd05d7a8e7725867d4e650/research/adaptive-compute-barrier) | AI computation / optimization | Published preliminary mathematical result |

[Full research ledger](RESEARCH.md) · [Structured project registry](research/registry.json)

The initial projects illustrate the method; they do not restrict future contributions to mathematics or AI efficiency. None of these projects is asserted to be independently refereed or to have established worldwide priority. Proof, finite testing, publication, formal verification, independent review and novelty are tracked separately.

### Featured investigation: OPL-001

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

[Proof and references](research/mathematics/prefix-reversal-asymptotics/paper.md) · [Verification code](research/mathematics/prefix-reversal-asymptotics/verify.py) · [Recorded results](research/mathematics/prefix-reversal-asymptotics/results.json)

### Reproduce the founding research

Python 3.13.5 and SymPy 1.14.0 were used in the initial research package.

```sh
git clone https://github.com/zakkeasterbrook/open-problems-lab.git
cd open-problems-lab
python tools/check_lab.py
python -m pip install -r research/mathematics/prefix-reversal-asymptotics/requirements.txt
python tools/check_lab.py --reproduce quick
# Repeat the original larger finite verification:
python tools/check_lab.py --reproduce full
```

The reproduction tool runs in a temporary directory and checks resulting records against the archived results. It does not overwrite the evidence. Finite verification is not a formal proof of the infinite theorem. A passing automated check is not peer review.

## Contribute a problem or a solution

Start with the [problem intake template](templates/PROBLEM.md) or [open a problem issue](https://github.com/zakkeasterbrook/open-problems-lab/issues/new?template=open_problem.md). Problems can start as ordinary questions; they do not need a finished research proposal. Include what you want to change and what would make an answer useful.

Contributors can propose new investigations, collaborate on existing work, submit practical prototypes, reproduce tests, offer domain expertise, or identify mistakes. AI-assisted contributions are welcome with transparent disclosure. Give credit to the people and sources that contributed to each finding. The lab does not claim ownership of other people's discoveries simply because they appear here.

Do not submit private data, confidential business ideas, credentials, or undisclosed potentially patentable material to public issues. See [CONTRIBUTING.md](CONTRIBUTING.md) and the [publication and commercialization policy](governance/COMMERCIALIZATION.md).

## Open research and real-world impact

Research can lead to free tools, practical solutions, new scientific results, community projects, or commercially useful products. Potential funding, sponsorships, and commercial applications can support further investigation, but are not prerequisites for participation. Separate confidential work and proprietary product development from public research; never assume that a contributor has transferred intellectual property beyond applicable license terms.

## Attribution and license

Open Problems Lab was founded by [Zakk Easterbrook](https://github.com/zakkeasterbrook) in November 2026. Individual contributors and source researchers are credited in the corresponding project records. Use each project's citation metadata for specific results; cite the relevant commit or archived version.

[Citation metadata](CITATION.cff) · [NOTICE](NOTICE) · [Apache License 2.0](LICENSE)

Original lab materials are Apache-2.0 licensed to the extent applicable rights are held; third-party works retain their own terms. No institutional affiliation, endorsement, DOI, peer-review acceptance, guaranteed discovery, or universal AI attribution is claimed.
