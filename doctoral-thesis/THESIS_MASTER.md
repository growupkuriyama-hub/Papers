# Doctoral Thesis Master Plan

## Title

**Observation Is Not Enough — Finite Observation and Resource Tradeoffs in Identification in the Limit**

Status: **fixed working dissertation title**  
Planning baseline: **2026-09-30**

---

## 1. Dissertation-level thesis

The dissertation studies positive-data grammatical inference under finite algebraic observation.

Its central progression is:

[
	ext{fixed observation}
longrightarrow
	ext{positive reconstruction}
longrightarrow
	ext{compression of observation}
longrightarrow
	ext{resource geometry of reconstruction}.
]

The final synthesis is:

> A finite observer determines which fragments may be safely identified, but minimizing the observer and minimizing the positive evidence required for reconstruction are distinct optimization problems.

The phrase **Observation Is Not Enough** is therefore not only rhetorical. The intended final synthesis is supported by two different kinds of separation:

- **optimizer separation:** minimum observation and minimum reconstruction may be attained by different observers;
- **scalar insufficiency:** even when an observation size is optimal, that size alone need not control reconstruction cost.

These dissertation-level claims remain subject to final proof audit and literature-priority audit before they are frozen into thesis TeX.

---

## 2. Five core research components

### Core A — #1 fixed-h CFG

Directory: `../01_fixed-h-cfg/`

Title: *Distributional Learning of Context-Free Languages under Fixed Finite-Monoid Typing*

Role in dissertation:
- establishes the fixed-observation CFG reconstruction framework;
- connects finite-monoid typing with positive-data identification in the limit;
- supplies the first reconstruction layer on which later resource questions are asked.

Current research status: **TCS major revision; still evolving**.

Thesis role: foundational reconstruction chapter.

---

### Core B — #2 fixed-h MCFG

Directory: `../02_fixed-h-mcfg/`

Title: *Positive-Data Learning of Multiple Context-Free Languages under Fixed Finite-Monoid Typing*

Role in dissertation:
- extends fixed-observation reconstruction from CFGs to bounded-fan-out linear MCFGs;
- introduces multidimensional / tuple-sensitive reconstruction;
- provides the higher-rank reconstruction architecture later analyzed by OFET.

Current research status: **pre-submission working manuscript; still evolving**.

Thesis role: multidimensional reconstruction chapter.

---

### Core C — #3 SCL-Compression

Directory: `../03_scl-compression/`

Title: *Finite-Monoid Compression in Syntactic Concept Lattices: Arity Hierarchies and a Pseudovariety Trichotomy*

Role in dissertation:
- turns finite observation from a fixed bias into an optimization object;
- defines and studies finite-monoid compression through tuple-substitution safety;
- gives congruence and relational-morphism formulations of compression;
- provides the semantic-compression side of the final Observation-Is-Not-Enough synthesis.

Current research status: **arXiv v1 public; still evolving for dissertation integration**.

Important integration note:
- the Clark--Wurm tuple interface and the current #2/OFET admissible occurrence interface are not identical;
- dissertation notation must keep these interfaces distinct rather than silently identify their minima.

Thesis role: finite-observation compression chapter.

---

### Core D — OFET

Directory: `../06_ofet/`

Title: *Observer--Fragmentation--Exposure Tradeoffs: From Rectangular CFG Exposure to Ordered MCFG Scheduling*

Role in dissertation:
- decomposes reconstruction into finite resources beyond observer size;
- studies fragmentation, exposure, arithmetic span, ordered scheduling, and hierarchical reuse;
- gives exact resource frontiers on explicit CFG/MCFG test families;
- supplies the reconstruction-resource side of the final synthesis.

Current research status: **arXiv v1 public; internal post-arXiv revision active; journal not yet submitted**.

Thesis role: reconstruction-resource geometry chapter.

---

### Core E — Observation Is Not Enough

Directory: `../07_observation-is-not-enough/`

Working paper role:
- bridge #3 and OFET;
- distinguish Clark--Wurm compression from the current admissible reconstruction interface;
- formulate general observer-refinement / resource monotonicity principles;
- formalize optimizer separation on the (R_{m,q}) family;
- formalize fixed-compression / unbounded-reconstruction on the (X_{2,r}) family;
- connect minimum relational-morphism compression witnesses to reconstruction suboptimality;
- package the observer-resource Pareto viewpoint.

Current research status: **research master only; no TeX source yet**.

Thesis role: synthesis / bridge chapter and dissertation-level theorem package.

---

## 3. Provisional dissertation architecture

### Part I — Foundations

**Chapter 1. General Introduction**
- identification in the limit from positive data;
- substitutability and finite observation;
- why observation becomes an optimization variable;
- dissertation-level question: what does observation determine, and what does it fail to determine?

**Chapter 2. Common Foundations**
- distributions and contexts;
- finite monoid morphisms;
- CFG and MCFG notation;
- positive-data learners and characteristic samples;
- observer refinement;
- explicit distinction between Clark--Wurm tuple contexts and admissible reconstruction contexts.

### Part II — Reconstruction under Fixed Observation

**Chapter 3. Context-Free Reconstruction under Fixed Finite-Monoid Typing**
- adapted from #1.

**Chapter 4. Multiple Context-Free Reconstruction under Fixed Finite-Monoid Typing**
- adapted from #2.

### Part III — Compressing Observation

**Chapter 5. Syntactic Concept Lattices and Finite-Monoid Compression**
- adapted from #3;
- ends with the question of whether a smallest safe observer is also reconstruction-optimal.

### Part IV — Reconstruction as a Multi-Resource Problem

**Chapter 6. Observer--Fragmentation--Exposure Tradeoffs**
- adapted from OFET;
- CFG rectangular exposure;
- higher-rank fragmentation;
- arithmetic span;
- ordered scheduling;
- hierarchical reuse.

### Part V — Observation Is Not Enough

**Chapter 7. Finite Observation and Resource Tradeoffs**
- interface comparison;
- observer refinement and reconstruction monotonicity;
- optimizer separation on (R_{m,q});
- fixed compression with unbounded reconstruction on (X_{2,r});
- coincidence conditions;
- relational-morphism reconstruction separation;
- observer-resource Pareto principle.

**Chapter 8. Conclusions and Open Problems**
- what finite observation controls;
- what reconstruction resources remain independent;
- open route toward more general resource geometry.

---

## 4. Integration invariants

The following rules should be preserved while the five components continue to evolve.

1. **Paper directories remain authoritative.**  
   The dissertation master must never silently override theorem statements in the current paper source.

2. **Do not conflate the two tuple interfaces.**  
   Clark--Wurm compression and the current #2/OFET admissible occurrence interface must be named separately whenever their distinction matters.

3. **Characteristic-data complexity is learner-relative.**  
   Dissertation statements must not present OFET characteristic-data costs as intrinsic sample complexity of the language independent of the reconstruction architecture.

4. **Existing results versus dissertation synthesis must be separated.**  
   Results already proved in #1/#2/#3/OFET should be distinguished from new bridge theorems proved only in the Observation-Is-Not-Enough layer.

5. **No premature TeX synchronization.**  
   Until a component reaches a stable theorem/proof baseline, only its role, dependency, terminology, and status should be synchronized into this master.

---

## 5. Maturity gates before thesis TeX

A paper-derived chapter enters the thesis TeX tree only after all of the following are true:

- theorem statements are stable enough that renumbering/rephrasing will not routinely change;
- proof architecture has passed at least one dedicated audit;
- terminology is reconciled with the dissertation crosswalk;
- the paper has a stable public or submission baseline, or an explicitly frozen internal thesis baseline;
- all known interface mismatches with the other core components are documented.

For Chapter 7 / Observation Is Not Enough, additional gates apply:

- complete formal proof of the (X_{k,r}) Clark--Wurm compression theorem;
- independent adversarial audit of the all-arity upper bound;
- formal proof write-up of the (R_{m,q}) optimizer-separation theorem;
- proof audit of refinement / coincidence / Pareto principles;
- literature-priority search for observer-size versus reconstruction-evidence optimization.

---

## 6. Current non-core papers

The following remain important research assets but are not part of the current dissertation core:

- `../04_relative-factorization/`
- `../05_jalc-occurrence-descriptors/`
- `../misc/`

They may be cited or used for perspective, but they are not currently planned as principal dissertation chapters.

---

## 7. Working completion criterion

The dissertation becomes ready for full TeX assembly when the five core components have stable internal baselines and Chapter 7 has a proof-audited theorem package.

Until then, this file is the dissertation-level source of truth for architecture and integration decisions.
