# Fan-out-two research archive: Fable and Claude rounds 12–14

**As of 2026-11-16 JST.** Research-only archive. **The formal `op:fanout-two` problem remains OPEN.** No independent paper is requested or prepared.

## Read this first

The manuscript at [`main.tex`](../main.tex) is the authority for good MCFGs, tuple substitutability, thickess `\bar\theta_G`, Theorem A (LG upper bound), and the unresolved necessity of LG at fan-out ≥2. Research results below must not be promoted to manuscript theorems without separate review.

| Stage | Independently audited state | Complete reproducible source |
|---|---|---|
| **Round 12** (2026-11-15) | Explored 3,093 template families; **no superpolynomial lower bound** satisfying both arities. Produced compensation barriers and independent corrections to a finite pattern classifier; distinguished proved local claims, conditional local-witness lemma LS, and finite tests. | [Round-12 exact sources and audit](ROUND12_COMPLETE_SOURCE_AUDIT_2026-11-16.md) |
| **Fable** (2026-11-15) | Theorems A (doubling-family-collapse with its exact scope), B (abelian sieve), C (commutative unary-length upper bound). C received a full **hand** audit with clarifications, not peer review/formal proof. | [Fable sources, certificates, checkers, audits](FABLE_20261115_COMPLETE_SOURCE_AUDIT_2026-11-16.md) |
| **Round 13** (2026-11-15) | Rotation Rot, skeleton function, bounded skeleton-types **T1** `N < \bar\theta_G[2(r+1)]^{2M+1}` passed independent hand audit. **Original X1 is false**, witnessed by a 40-word tuple-substitutable language. The separate X2 has a repaired range/padding argument. General U remains OPEN. | [Round-13 exact sources and audit](ROUND13_COMPLETE_SOURCE_AUDIT_2026-11-16.md) |
| **Round 14** (2026-11-15–16) | Type-safe X1⁺, substitution/framing tools, **TR transposition theorem** for `de/ed` under proper room hypotheses, independently replayed finite certificates. **Original CA is false**, witnessed by a 67-word language even with three `a` in the connected seed. Corrected CA* needs **additive-seed consistency and room**; TR itself does not use CA. TR-tree needs reconstructed CA*. | [Round-14 exact sources and audit](ROUND14_COMPLETE_SOURCE_AUDIT_2026-11-16.md) |

**Important terminology:** The earlier special **U₂** upper bound (see [special-case status](STATUS_U2_STANDALONE_FORMALIZATION_2026-11-15.md)) is not the central `U_1` semigroup-typing lower-bound question. The research is exploratory: do **not** draft an independent paper without an explicit request.

## Directly readable human reports and checkers

**Round 12:** [original lower-bound search](claude_fanout2_round12_lower_bound_report_2026-11-15.md) · [checkpoint](claude_fanout2_round12_lower_bound_checkpoint1_2026-11-15.md) · [candidate rules](claude_fanout2_round12_candidate_rules_2026-11-15.md) · [independent mathematical audit](audit_claude_fanout2_round12_independent_2026-11-15.md).

**Fable:** [original report](fable_fanout2_open_problem_report.md) · [independent initial audit](audit_fable_fanout2_independent_2026-11-15.md) · [Fable-C full mathematical audit](Fable_C_complete_independent_mathematical_audit_2026-11-15.md).

**Round 13:** [Claude report](claude_round13_noncomm_U_final_report_2026-11-15.md) · [independent audit and X1 refutation](audit_claude_round13_noncomm_U_independent_2026-11-15.md) · [40-word independent checker](round13_independent_X1_counterexample_2026-11-15.py) · [Claude checker](claude_round13_noncomm_U_checker_2026-11-15.py) · [submitted checker log](claude_round13_noncomm_U_checker_output_2026-11-15.txt).

**Round 14:** [Claude report](claude_round14_noncomm_Parikh_report_2026-11-15.md) · [independent audit and CA counterexample](audit_claude_round14_noncomm_Parikh_independent_2026-11-16.md) · [independent checker](independent_round14_audit_2026-11-16.py) · [next obligations](claude_round14_noncomm_Parikh_next_obligations_2026-11-15.md).

**Prompts and continuity:** [Fable initial prompt](PROMPT_FABLE_FANOUT_TWO_OPEN_PROBLEM_FREEDOM_2026-11-15.md) · [Claude R12](PROMPT_CLAUDE_FANOUT2_ROUND12_SUPERPOLYNOMIAL_LOWER_BOUND_2026-11-15.md) · [Claude R13](PROMPT_CLAUDE_ROUND13_FABLE_C_NONCOMMUTATIVE_U_2026-11-15.md) · [Claude R14](PROMPT_CLAUDE_ROUND14_NONCOMMUTATIVE_PARIKH_REDUCTION_2026-11-15.md) · [self-contained ChatGPT handoff snapshot](HANDOFF_PROMPT_FANOUT2_RESEARCH_2026-11-16.md). The historical handoff snapshot says the archive was not on GitHub **at its creation time**; this index supersedes that storage-status remark.

## Mathematical proof-status guardrails

- **PROVED / hand-audited with caveats:** Fable-C (commutative case), R13 T1, R14 TR, plus precisely scoped rotation and substitution lemmas.
- **REFUTED:** R13 original X1 (40-word counterexample); R14 original CA (67-word counterexample); broad bigram-deficit determinacy across content classes (R13 E1).
- **CORRECTED / restricted:** X1⁺ requires **both compared fragments** to have matching componentwise types and positive padding; CA* additionally requires an **additively consistent starting connected seed**, sufficient room, and careful induction.
- **CONDITIONAL:** TR-tree using CA*, `P_tree \Leftarrow CA*+IH+AB`, and further Fable-C transfer statements. A reduction is not proof of the hypotheses.
- **OPEN:** **AB**, equality of deficits for general same-Parikh composite Rot kernels under an actual host; **IH**, producing suitable additive connected host from crossed/nested fan-out-two derivation configurations; **P_tree**, Conjecture **U** for noncommutative language, and full `op:fanout-two`.
- Every 2-hole context must have a **nonempty middle separator** and all compared tuple components must be nonempty; preserve original reduced good grammar size and **original** thickness in asymptotics. A bounded computation is not a universal theorem.

## Reproducibility

All original `.py`, `.cpp`, `.json`, `.txt`, `.md` material in the 4 complete bundles is embedded in UTF-8 with original byte lengths and SHA-256. Each bundle includes a Python extraction example. The original submitted and independent checker logs are preserved; the Round-14 exhaustive long D/E run was not all independently rerun. Check the detailed audits before citing claims.

**No edits were made in this archival change to:** `main.tex`, `japanese/main_JP.tex`, PDFs, `PAPER.yaml`, Theorems A/B/C, or `op:fanout-two`.
