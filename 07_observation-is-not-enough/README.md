# 07 — Observation Is Not Enough

Working bridge paper / doctoral-dissertation synthesis component.

## Current title

**Observation Is Not Enough: Compression and Reconstruction under Finite-Monoid Typing**

Author: Takayuki Kuriyama  
Internal version: **v3**  
Status: **working manuscript**

## Purpose

This paper connects:

- `03_scl-compression/` — finite-monoid compression of principal SCL geometry; and
- `06_ofet/` — observer-sensitive fragmentation, exposure, and characteristic-data cost.

The central result is that minimum safe observation and minimum positive reconstruction are distinct optimization problems.

The manuscript develops two complementary forms of this principle:

1. **Optimizer separation on `R_{m,q}`:** every compression-optimal observer has strictly larger characteristic-data cost than a slightly larger observer.
2. **Fixed compression with unbounded reconstruction on `X_{2,r}`:** `cmp_2^{CW}=2` for every `r`, while the optimal encoded reconstruction cost is `2r(r+1)`.

It also records:

- observer-refinement monotonicity;
- a strict distinction between the Clark--Wurm tuple interface and the current nonempty MCFG sentence-context interface;
- exact Clark--Wurm compression of `X_{k,r}`;
- a relational-morphism selector separation;
- a finite observer-resource Pareto principle; and
- the exact weighted phase transition on the two-point `R_{m,q}` frontier.

## Source of truth

- `main.tex` — canonical editable manuscript source
- `MASTER_NOTES.md` — theorem provenance, proof obligations, and scope cautions
- `PAPER.yaml` — repository metadata
- `PROOF_AUDIT_v2.md` — adversarial theorem-by-theorem proof audit
- `xkr_cw_small_audit.py` — finite exhaustive sanity check for the `X_{k,r}` bridge theorems
- `LITERATURE_PRIORITY_AUDIT_v3.md` — dedicated novelty/precedence audit and claim boundary

## Dependencies

The exact `R_{m,q}` fragmentation/characteristic-data formulas and the exact `X_{k,r}` slot-observer characteristic-data formula are imported from `06_ofet/`. The SCL safety interface, congruence characterization, relational-morphism characterization, and selector lemma are imported from `03_scl-compression/`.

The new content of this note is the cross-paper theorem package and the exact Clark--Wurm compression calculation for `X_{k,r}`.

## Build

Run `pdflatex main.tex` twice. The v2 proof-audited source compiled to 14 pages with no undefined references/citations or overfull boxes. Version v3 adds the literature-priority boundary and related-work references; compile status is recorded separately after the v3 check.

## Audit status

This is a working manuscript. The all-arity `X_{k,r}` proof has passed an internal adversarial audit and finite exhaustive sanity checks; see `PROOF_AUDIT_v2.md`. The dedicated literature-priority audit is now complete; see `LITERATURE_PRIORITY_AUDIT_v3.md`.

The audit found substantial **broad conceptual precedence** (characteristic/teaching data, typing bias, abstraction refinement, compatibility-based state minimization), but **no direct theorem-level predecessor in the searched scope** for optimizing observer image and positive locking-data cost over the same safe finite-monoid observer space. The novelty claim is therefore deliberately scoped. An external expert priority check and an independent human proof read remain recommended before submission.
