# Research protocol

**Purpose:** maximize the reliability of claims, not the number of claimed discoveries.

## Intake and evidence

The lab accepts any founder-selected problem. Use [the problem template](../templates/PROBLEM.md). Begin with a measurable objective, context, constraints, data permissions, baseline and evidence appropriate to the domain. For private or potentially commercial material, review [disclosure policy](COMMERCIALIZATION.md) before any public commit.

## Additional requirements for original scientific and mathematical claims

- Stable project ID, precise question, original paper and exact location of the statement, source date and link.
- Definitions, quantifiers, assumptions, known special cases, known counterexamples, closest prior art and the most recent search date.
- Evidence that the target was described as open by a source, and a distinction between historical openness and current verified status.
- Intended verification procedure, resource constraints and any ethical, safety or data-license considerations.

## Evidence and review gates

Use domain-appropriate validation. A practical or business proposal is not validated just because its arithmetic is correct: test against realistic baselines, record uncertainties and actual outcomes, and distinguish forecasts from observed results. A prototype is not a production product, a plausible medical or physical hypothesis is not a clinical or experimental finding, and a finite experiment is not a universal mathematical proof.

- **Proof:** include every needed implication; identify established lemmas and hypotheses. For a counterexample, explicitly verify the hypotheses and the violated conclusion.
- **Computation:** preserve versions, deterministic seeds, inputs, raw outputs, known failures and checksums. Describe scope and cost honestly. Do not imply exhaustive infinite verification from finite tests.
- **Independent verification:** prefer different algorithms or exact arithmetic; record disagreements. Distinguish internal replication from review by an external researcher.
- **Formal verification:** state the proof assistant and dependencies. A checked lemma, a placeholder, an axiom assuming the conclusion, or a build with `sorry` is not a formal proof of the target.
- **Novelty:** search original papers, follow-ups, errata and competing results; cite them. State the exact incremental contribution. A public timestamp alone is not priority or peer review.
- **Publication:** include a concise abstract, proof, limits, data provenance, AI assistance disclosure, citation metadata, license and reproduction commands. Use a new version for corrections and keep earlier evidence visible.

## Safety and integrity

No fabricated citations, inflated benchmarks, claimed external endorsements, unauthorized access to data, or release of sensitive personal information. Assess dual-use risk and the consequences of public disclosure for each project. Do not publish credentials or proprietary research traces. The lab is not a substitute for regulated professional judgment. Never present a hypothesis as an established physical or medical finding.

## Corrections

Document the exact affected claim, counterexample, affected version and corrected status. If unresolved, mark the claim withdrawn or disputed. Update the README, machine-readable ledger and relevant research note together. Preserve the prior publication for traceability.
