# Minimal Doctoral Thesis Master

## Fixed title

**Identification in the Limit beyond Fixed Observation**

Planning baseline: **2026-09-30**  
Track: **minimal dissertation**

---

## 1. Objective

This plan minimizes thesis-specific work while preserving a clear doctoral-level contribution.

The dissertation uses only:

- #1 fixed-h CFG;
- #2 fixed-h MCFG;
- a short synthesis showing exactly how far the fixed-observer assumption can be relaxed.

The dissertation does **not** depend on completion of:

- #3 SCL-Compression;
- #6 OFET;
- #7 Observation Is Not Enough;
- #4 Relative Factorization;
- #5 JALC.

Those remain independent research assets and may continue after the doctorate.

---

## 2. Core A — CFG reconstruction under fixed finite observation

Directory: `../01_fixed-h-cfg/`

Title: *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*

Current repository status:
- TCS major revision;
- internal version v80;
- manuscript source-of-truth: `../01_fixed-h-cfg/main.tex`.

Dissertation role:
- establish finite-monoid typing as a fixed comparison bias;
- exact reconstruction from finite positive witnesses;
- conservative Gold/TxtEx identification;
- fixed-window recovery and structural boundaries.

No new thesis-specific proof should be added here unless required for integration.

---

## 3. Core B — MCFG reconstruction under fixed finite observation

Directory: `../02_fixed-h-mcfg/`

Title: *Positive-Data Learning of Multiple Context-Free Languages under Fixed Finite-Monoid Typing*

Current repository status:
- pre-submission working manuscript;
- internal version v66;
- arXiv:2605.11644 predates the current internal version;
- manuscript source-of-truth: `../02_fixed-h-mcfg/main.tex`.

Dissertation role:
- lift the fixed-observation reconstruction principle from strings/substrings to tuples and sentence contexts;
- obtain positive-data TxtEx identification for the typed bounded-fan-out MCFG setting;
- isolate the role of fan-out and rule rank;
- provide the existing bounded-unknown-typing proposition that motivates the final synthesis.

No new thesis-specific proof should be added here unless required for integration.

---

## 4. Minimal additional chapter — Beyond Fixed Observation

This is the only dissertation-specific mathematical addition planned.

### 4.1 Question

The #1/#2 learning theorems fix a finite-monoid morphism
[
h:Sigma^*	o M
]
as part of the class definition.

The final question is:

> Must the learner know one particular observer (h) in advance, or is a bounded amount of finite observation sufficient?

### 4.2 Bounded unknown observation

Fix a finite alphabet (Sigma), the relevant grammar-side structural bounds, and an integer (mge1).

Let the bounded-observer union range over all homomorphisms
[
h:Sigma^*	o M
qquad	ext{with}qquad |M|le m.
]

Because there are only finitely many monoid structures of size at most (m) and finitely many letter maps from fixed (Sigma), form the product of all such homomorphisms and restrict to its image:
[
U_{Sigma,m}:Sigma^*	o M_{Sigma,m}.
]

Every admissible (h) factors through (U_{Sigma,m}).  Thus (U_{Sigma,m}) refines every observer in the bounded family.

### 4.3 Target synthesis theorem

The thesis should state one joint theorem/corollary package covering the two reconstruction levels.

**Bounded-observation principle.**

For each fixed finite observer-size bound (m):

- the union of the corresponding #1 CFG classes is contained in one fixed-observer CFG class defined by (U_{Sigma,m}), hence is TxtEx-identifiable from positive data;
- for each fixed fan-out bound (f), the union of the corresponding #2 MCFG classes is contained in one fixed-observer MCFG class defined by (U_{Sigma,m}), hence is TxtEx-identifiable from positive data.

The MCFG half is already present in the current #2 manuscript as Proposition “Unknown typing with a bounded codomain”.  The CFG half should be written as the direct analogue using the #1 refinement and Gold-identification results.

**Unbounded-observation boundary.**

If the codomain-size bound is removed and arbitrary finite observers are allowed, the resulting union contains every regular language.  Therefore it contains all finite languages and an infinite language, so Gold's positive-data obstruction applies and the union is not TxtEx-identifiable.

### 4.4 Interpretation

The fixed-observer assumption is stronger than necessary.

The genuine learnability boundary exposed by #1/#2 is:

[
oxed{
	ext{bounded finite observation}
quad	ext{vs.}quad
	ext{unbounded target-dependent observation}.
}
]

Thus the dissertation moves from learning **under one fixed observation** to identification **beyond fixed observation**, while retaining a finite observation budget.

### 4.5 Scope cautions

- Do not claim a polynomial dependence on the observer-size bound (m); the universal product observer can be extremely large.
- Keep alphabet and grammar-side structural parameters explicit when required by the component theorem.
- The unbounded negative result is a Gold-style class-level nonidentifiability statement, not a lower bound on every restricted subfamily.
- Do not import #3/OFET terminology or machinery into this minimal chapter unless it becomes logically necessary.

### 4.6 Size target

This chapter should remain short: **approximately 5–8 pages** including statement, proof, interpretation, and the CFG/MCFG comparison.

No separate journal paper is required.

---

## 5. Minimal dissertation architecture

### Chapter 1 — Introduction and Common Setup

Target: approximately 8–12 pages.

Only what is needed to connect #1 and #2:
- Gold identification in the limit;
- positive data and characteristic samples;
- substitutability / distributional learning;
- finite-monoid observation;
- why CFG and MCFG are treated in one thesis;
- statement of the final bounded-vs-unbounded observation question.

### Chapter 2 — Context-Free Languages under Fixed Observation

Adapt #1 with minimal rewriting.

### Chapter 3 — Multiple Context-Free Languages under Fixed Observation

Adapt #2 with minimal rewriting.

### Chapter 4 — Beyond Fixed Observation

Approximately 5–8 pages.

Contents:
- universal product observer (U_{Sigma,m});
- bounded unknown-observer identification for CFG and MCFG;
- unbounded-observer nonidentifiability;
- interpretation as the dissertation-level boundary theorem.

### Chapter 5 — Conclusion

Target: approximately 3–5 pages.

No new mathematics.

---

## 6. Minimal-work integration rules

1. **#1 and #2 remain authoritative.**  
   Do not fork their theorem statements inside the dissertation master.

2. **Do not rewrite papers merely for stylistic uniformity.**  
   Only remove duplicated preliminaries and add short transitions when the thesis TeX phase begins.

3. **No #3 / OFET / OINE dependency.**  
   They may be cited in a future-work paragraph, but the minimal thesis must remain complete without them.

4. **One new synthesis theorem package only.**  
   Do not let Chapter 4 grow into a new paper.

5. **No thesis TeX yet.**  
   TeX assembly begins only after #1, #2, and the Chapter-4 proof note are stable.

---

## 7. TeX creation gate

Create `doctoral-thesis-minimal/tex/` only when all are true:

- #1 has a stable post-review manuscript baseline;
- #2 has a stable submission manuscript baseline;
- the CFG analogue of bounded unknown typing has been written and audited;
- the joint bounded/unbounded observation theorem statement is frozen;
- no unresolved terminology mismatch remains between #1 and #2.

Until then, this file is the architecture source-of-truth for the minimal dissertation track.
