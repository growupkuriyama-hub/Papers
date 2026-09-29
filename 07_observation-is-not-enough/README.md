# 07 — Observation Is Not Enough

Working bridge paper / doctoral-dissertation synthesis component.

## Current title

**Observation Is Not Enough: Compression and Reconstruction under Finite-Monoid Typing**

Author: Takayuki Kuriyama  
Internal version: **v1**  
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

## Dependencies

The exact `R_{m,q}` fragmentation/characteristic-data formulas and the exact `X_{k,r}` slot-observer characteristic-data formula are imported from `06_ofet/`. The SCL safety interface, congruence characterization, relational-morphism characterization, and selector lemma are imported from `03_scl-compression/`.

The new content of this note is the cross-paper theorem package and the exact Clark--Wurm compression calculation for `X_{k,r}`.

## Build

Run `pdflatex main.tex` twice. The v1 source was compile-checked locally before the repository update and produced a 13-page PDF with no undefined references/citations or overfull boxes.

## Audit status

This is a working manuscript, not yet a priority claim. The all-arity `X_{k,r}` proof and the literature-priority discussion should receive an independent audit before journal or arXiv submission.
