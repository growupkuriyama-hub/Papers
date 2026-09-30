# 07 — Minimal Observation Is Not Enough

## Current title

**Minimal Observation Is Not Enough: Reconstruction Tradeoffs in Identification in the Limit**

Author: Takayuki Kuriyama  
Internal version: **v1**  
Status: **focused journal-candidate working manuscript**

## Purpose

This directory replaces the former `07_observation-is-not-enough/` bridge manuscript.

The paper is optimized for three goals:

1. **standalone journal submission after #1 and #2;**
2. **minimum length and minimum new machinery;**
3. **maximum dissertation impact when combined with #1 fixed-h CFG and #2 fixed-h MCFG.**

The paper no longer tries to summarize all of #3 SCL-Compression or all of OFET. It keeps only the pieces needed for one sharp question:

> How far can fixed finite observation be relaxed, and does minimum safe observation determine minimum positive reconstruction?

## Main theorem package

1. **Finite-Observation Threshold Theorem**
   - bounded unknown finite observation is reducible to one universal product observer;
   - unrestricted target-dependent finite observation contains all regular languages and is not TxtEx-identifiable.

2. **Reconstruction monotonicity under observer refinement**
   - finer observers admit fewer semantic substitutions;
   - locking-sample cost is nondecreasing along refinement.

3. **Exact optimizer separation on R_{m,q}**
   - obs_1(R_{m,q}) = qm;
   - every observation-optimal observer pays a strictly larger reconstruction cost than a q(m+1)-state observer;
   - exact gap 4(m-1)(q-1);
   - with q=m^2, relative observer overhead tends to 1 while the reconstruction-cost ratio tends to 2.

4. **Fixed minimal observation, unbounded MCFG reconstruction on X_{2,r}**
   - the one-state observer is safe and reconstruction-optimal;
   - minimum characteristic-sample cardinality is r+1;
   - with the current #2 sample encoding, optimal cost is (2r+1)(r+1) = Theta(r^2);
   - therefore no function of the minimum observation number alone bounds reconstruction cost.

## Deliberately removed from the core paper

The following remain valuable research assets but are not needed in this focused paper:

- SCL arity hierarchy and pseudovariety trichotomy;
- Clark--Wurm / positive-interface comparison as a headline topic;
- relational-morphism selector separation;
- full observer-resource Pareto geometry;
- weighted phase transitions;
- OFET rank-four census;
- arithmetic/unimodular/laminar/scheduling hierarchy;
- hierarchical reuse and width--anchor frontiers.

Those results remain in #3, OFET, and repository history. MOINE uses the actual #1/#2 positive reconstruction interface as its primary observation notion.

## Dissertation role

The intended three-paper spine is:

`#1 fixed-h CFG -> #2 fixed-h MCFG -> #7 MOINE`

Interpretation:

- #1: identification under fixed finite observation for CFGs;
- #2: multidimensional extension to MCFGs;
- MOINE: beyond one fixed observer, followed by exact limits of what minimum observation can explain.

This is the preferred high-impact minimal dissertation narrative.

## Source of truth

- `main.tex` — focused journal-candidate manuscript
- `PAPER.yaml` — repository metadata and theorem scope
- `MASTER_NOTES.md` — trimming decisions and proof obligations
- `PROOF_AUDIT_v2.md` — inherited adversarial audit from the predecessor bridge manuscript; re-audit required after the interface simplification
- `LITERATURE_PRIORITY_AUDIT_v3.md` — inherited priority audit; refresh before submission
- `xkr_cw_small_audit.py` — legacy finite sanity checker from the predecessor Clark--Wurm formulation; retained as provenance, not as a proof dependency

## Target size

**Approximately 14–18 journal pages** after final typesetting.

The manuscript should not be allowed to grow back into #3 or OFET.
