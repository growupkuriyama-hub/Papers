# MOINE — Research Master

Date: 2026-09-30  
Status: focused journal-candidate v1

## 1. Design objective

This manuscript replaces the broader bridge paper *Observation Is Not Enough*.

Optimization target:

- minimum manuscript length;
- independently submit-able after #1 and #2;
- maximum impact as the third paper in the dissertation *Identification in the Limit beyond Fixed Observation*.

The paper is not a compressed table of contents of #3 + OFET + old #7. It is a theorem paper with one narrative.

## 2. Narrative

fixed observation  
→ bounded unknown observation  
→ learnability threshold  
→ minimum observation versus minimum reconstruction

The key conceptual distinction is:

- **class-level sufficiency:** bounded finite observation is enough for TxtEx learning;
- **resource-level insufficiency:** the smallest safe observer neither has to minimize reconstruction cost nor determine it numerically.

## 3. Headline results

### A. Finite-Observation Threshold Theorem

Use the universal product observer over all morphisms whose image has size at most m.

Positive side: bounded unknown observation reduces to one fixed observer, so #1/#2 apply.

Negative side: without an observation-size bound, every regular language is admitted via its syntactic morphism, so Gold's superfinite obstruction applies.

### B. R-family optimizer separation

Keep only the exact chain needed for:

- obs_1(R_{m,q}) = qm
- CD_min-observation = 4(m^2 + 2qm - m)
- CD_global = 4(m^2 + qm + q - 1)
- Delta CD = 4(m-1)(q-1)

For q=m^2: observer-size ratio 1+1/m -> 1, reconstruction-cost ratio -> 2.

### C. X-family scalar insufficiency

Use the #1/#2 positive sentence-context interface, not the full Clark--Wurm interface.

This is the main simplification relative to the predecessor paper.

For X_{2,r}:

- obs_2 = 1
- |C|_min = r+1
- ||C||_{+,min} = (2r+1)(r+1)

Therefore minimum observation size alone cannot bound reconstruction cost.

## 4. What was intentionally cut

Do not restore unless a referee specifically requires it:

- full SCL theory;
- pseudovariety trichotomy;
- Clark--Wurm arity sequence 1,2,2,... as a headline result;
- relational morphisms;
- general Pareto/Dickson theorem;
- weighted objective phase transition;
- OFET higher-rank arithmetic/scheduling/hierarchy;
- rank-four computational census.

These are interesting but dilute the third-paper thesis narrative.

## 5. Proof audit priorities

Before journal submission:

1. re-audit the R-family safety check for H^- and H^+ in the streamlined presentation;
2. re-audit the exact sample-graph criterion against the current #1 constructor;
3. re-audit the X-family affine invariant against the current #2 v66 constructor and its exact positive-interface conventions;
4. compile twice and remove undefined references/citations;
5. refresh literature priority around observer minimization versus characteristic-data minimization;
6. decide whether the two research-preprint citations (#3 / OFET) remain in the final journal version or move to an author note / provenance statement.

## 6. Submission posture

The paper should be presented as a new focused theorem contribution, not as a survey or merger.

The main novelty claim should be scoped to the joint optimization problem over the same finite-observer space:

- minimum safe observation versus
- minimum positive reconstruction evidence.

Do not claim learner-independent sample-complexity lower bounds.

## 7. Dissertation role

The target dissertation can now be extremely compact:

1. #1 — CFG under fixed finite observation
2. #2 — MCFG under fixed finite observation
3. MOINE — beyond one fixed observer and limits of minimal observation

No separate #3 / OFET chapter is required for the minimal high-impact track.
