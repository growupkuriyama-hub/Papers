# 07 — Minimum Observer Size Is Not Enough

## Current title

**Minimum Observer Size Is Not Enough: Exact Tradeoffs in Positive-Data Grammar Reconstruction**

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

> How do observer image size, congruence refinement, and characteristic positive evidence trade off under the fixed #1/#2 reconstruction systems?

## Main theorem package

1. **Observer refinement and kernel invariance**
   - the fixed #1/#2 constructors depend on an observer only through its kernel;
   - moving to a finer observer deletes substitution links and cannot lower characteristic-data cost.

2. **Exact maximally-coarse-observer separation on (R_{m,q})**
   - (mathrm{obs}_1(R_{m,q})=qm);
   - (H^-) and (H^+) are both maximally coarse safe and are incomparable;
   - the minimum-image observer and the reconstruction-optimal observer are disjoint;
   - exact encoded-cost gap (4(m-1)(q-1));
   - with (q=m^2), relative image overhead tends to 1 while the reconstruction-cost ratio tends to 2.

3. **Universal-observer penalty**
   - bounded unknown observation remains learnable by universal product compilation (background from #2);
   - on (R_{m,q}), a sufficiently rich universal observer separates all length-two main suffixes;
   - the minimum characteristic sample then equals the whole finite target language.

4. **Exact affine reconstruction on (X_{k,r})**
   - the one-state observer is safe and reconstruction-optimal;
   - minimum characteristic-sample cardinality is exactly (1+r(k-1));
   - the lower bound is an affine-span invariant tied directly to #2's Start/Const/Comp/Link rules;
   - for (X_{2,r}), the exact cardinality is (r+1) and encoded cost is ((2r+1)(r+1)).

## Relation to public OFET preprint

The broader `06_ofet` manuscript is already public as **arXiv:2609.34560v1** and contains predecessor versions of the exact `R_{m,q}` observer/characteristic-data formulas and the `X_{k,r}` affine result under a nontrivial slot observer.

Paper 07 is therefore a **focused sharpening / superseding journal candidate**, not an unrelated second publication of the same theorem package. Its sharpenings include the kernel/refinement formulation, incomparable maximally coarse safe observers, the universal-product penalty, and the trivial-observer `X_{k,r}` theorem. Do not submit both OFET and paper 07 independently with overlapping results without restructuring the overlap.
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
- MOINE: beyond one fixed observer, with exact separation between observer image size, safe-congruence coarseness, and reconstruction evidence.

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
