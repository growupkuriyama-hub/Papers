# Minimal High-Impact Doctoral Thesis Master

## Fixed title

**Identification in the Limit beyond Fixed Observation**

Planning baseline: **2026-09-30**  
Track: **minimal high-impact dissertation**  
Thesis TeX: **not created yet**

## 1. Objective

Minimize dissertation-specific work while preserving the strongest possible research narrative.

The degree-critical core is exactly:

1. `01_fixed-h-cfg/`
2. `02_fixed-h-mcfg/`
3. `07_Minimal_Observation_Is_Not_Enough/` (MOINE)

No separate #3 SCL-Compression chapter and no separate OFET chapter are required for this track.

The conceptual spine is:

`fixed observation / CFG -> fixed observation / MCFG -> beyond fixed observation -> limits of minimal observation`

## 2. Paper 1 — CFG under fixed finite observation

Directory: `../01_fixed-h-cfg/`

Title: *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*

Current status:
- TCS major revision
- internal version v80

Dissertation role:
- finite-monoid typing as a fixed comparison bias;
- exact positive reconstruction;
- Gold/TxtEx identification;
- quantitative and structural CFG results.

## 3. Paper 2 — MCFG under fixed finite observation

Directory: `../02_fixed-h-mcfg/`

Title: *Positive-Data Learning of Multiple Context-Free Languages under Fixed Finite-Monoid Typing*

Current status:
- pre-submission working manuscript
- internal version v66
- arXiv:2605.11644

Dissertation role:
- multidimensional extension of the fixed-observation principle;
- tuple/sentence-context reconstruction;
- bounded-fan-out MCFG identification;
- rule-rank and characteristic-data analysis.

## 4. Paper 3 — MOINE

Directory: `../07_Minimal_Observation_Is_Not_Enough/`

Title: *Minimal Observation Is Not Enough: Reconstruction Tradeoffs in Identification in the Limit*

Current status:
- focused journal-candidate v1
- target length: approximately 14–18 journal pages
- intended publication order: after #1 and #2

Dissertation role:
- remove the unnecessary requirement that one particular observer be fixed in advance;
- state the **Finite-Observation Threshold Theorem**;
- distinguish minimum safe observation from minimum reconstruction cost;
- provide exact CFG optimizer separation on (R_{m,q});
- provide fixed one-state observation with unbounded optimal MCFG reconstruction on (X_{2,r}).

The three-paper endpoint is:

> Bounded finite observation is sufficient for identification in the limit, but minimum observation does not determine the positive evidence required for exact reconstruction.

## 5. Why MOINE replaces the old short synthesis

The earlier plan reserved a 5–8 page dissertation-only chapter for bounded versus unbounded observation.

That material is now absorbed into MOINE as its opening theorem package.

This costs little additional dissertation work while making the endpoint independently publishable and substantially stronger:

- the threshold result answers how far fixed observation can be relaxed;
- the (R_{m,q}) theorem shows optimizer separation;
- the (X_{2,r}) theorem shows scalar insufficiency.

Thus no separate dissertation-only mathematical chapter is needed.

## 6. Explicit exclusions

The following remain research assets but are outside the degree-critical core:

- `../03_scl-compression/`
- `../04_relative-factorization/`
- `../05_jalc-occurrence-descriptors/`
- `../06_ofet/`

They may be cited as background or future work, but the dissertation must remain complete without dedicated chapters for them.

## 7. Minimal dissertation architecture

### Chapter 1 — Introduction and common setup

Target: approximately 8–12 pages.

- Gold identification in the limit;
- substitutability and positive data;
- finite-monoid observation;
- the CFG-to-MCFG progression;
- statement of the dissertation question.

### Chapter 2 — CFG under fixed observation

Adapt #1 with minimal rewriting.

### Chapter 3 — MCFG under fixed observation

Adapt #2 with minimal rewriting.

### Chapter 4 — Minimal Observation Is Not Enough

Adapt MOINE with minimal rewriting.

This chapter contains the dissertation-level climax:
- Finite-Observation Threshold Theorem;
- reconstruction monotonicity;
- exact optimizer separation;
- fixed minimum observation with unbounded reconstruction.

### Chapter 5 — Conclusion

Target: approximately 3–5 pages.

No new mathematics.

## 8. Integration rules

1. Individual paper directories remain authoritative.
2. Do not rewrite the three papers merely for stylistic uniformity.
3. Dissertation-specific mathematics should be zero or nearly zero once MOINE is stable.
4. Do not re-import #3/OFET machinery unless a proof obligation actually requires it.
5. Keep MOINE focused; do not let it regrow into the old #3 + OFET + OINE aggregate.
6. Do not create thesis TeX until all three core papers have stable theorem/proof baselines.

## 9. TeX creation gate

Create `doctoral-thesis-minimal/tex/` only when:

- #1 has a stable post-review baseline;
- #2 has a stable submission baseline;
- MOINE has passed focused proof re-audit;
- MOINE has passed literature-priority refresh;
- the #1/#2/MOINE notation interface is frozen.

Until then, this master is the architecture source-of-truth.
