# 02-v3 — CFG typing classification (new paper #2)

**Working title:** *Which Fixed Typings Give Polynomial Characteristic Data? A Classification for Substitutable Context-Free Languages*
**Author:** Takayuki Kuriyama
**Status:** started 2026-11-20 — skeleton with draft bridge lemmas (framework of #1), not submitted, no result of this directory has been re-audited in its new form.

## Concept

This is the third-generation paper #2 of the doctoral-thesis track (#1 → #2 → MOINE). It restricts to **fan-out one (context-free grammars)** and collects the results of `02-v2-lg-fanout-boundary` that are closed there:

1. **Pseudovariety level:** a pseudovariety has uniform polynomial characteristic-data length (rank cap ≥ 2) iff it is contained in **LG**.
2. **Typing level:** a typing onto the two-element semilattice U₁ has polynomial data iff exactly one letter has type 1 (isolated-letter theorem; letter-disjoint obstruction).
3. **Shape of the bound:** the factor ‖G‖θ̄ is necessary for every typing; the binary U₁ typing needs θ̄².
4. Optional: rank one is polynomial for every typing.

It answers the question left open by #1 (TCS-D-26-00494), which proves sufficiency for LI∨Grp and an obstruction U₁ but claims no necessity.

## Files

- [`OUTLINE.md`](OUTLINE.md) — design decisions, section plan and **source map** (which label of which archived file each part comes from). Start here.
- [`PAPER.yaml`](PAPER.yaml) — metadata and status.
- [`main.tex`](main.tex) — English manuscript (skeleton: front matter, introduction draft, main-theorem statements, section stubs with source comments).

## Relation to other directories

- `02-v2-lg-fanout-boundary/` is **frozen** as the MCFG asset store (Theorem A at every fan-out, fan-out-two research). Do not edit it from here; copy and record sources in `OUTLINE.md`.
- `01_fixed-h-cfg/` (#1) is under review at TCS; cite it by arXiv:1409.6247v5 numbering.

## Change log

- 2026-11-20: introduction and Section 6 explain why the typing-level classification starts with U₁ (the minimal obstruction outside LG).

- 2026-11-20: directory created; outline, metadata and manuscript skeleton.
- 2026-11-20: switched to the framework of #1 (arbitrary reduced CFGs, BUNF, `Rec_s`, `tau_G`, typed thickness). Added draft bridge lemmas (lambda-elimination with thickness control, typed-thickness transfer, master transfer corollary, rare-type principle for `Rec_s`); restated Theorems A–C in #1's measures. New mathematics is marked DRAFT-NEW and is not yet audited.
- 2026-11-20: Section 4 and Appendix A — self-contained fan-out-one proof of local-group sufficiency. Sections 6–7 and Appendices B–E ported (three-letter family, typing-level obstruction, isolated-letter theorem, U₁ classification, binary quadratic family, linear factor), with operators replaced by `Rec_s`. Added the representative-witness lemma needed because the isolated-letter theorem bounds representatives, not yields. 25 pp.
