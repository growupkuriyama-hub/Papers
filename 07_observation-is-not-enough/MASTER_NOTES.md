# Observation Is Not Enough — Research Master

Status: working manuscript v3 exists in main.tex; mathematical proof audit and internal literature-priority audit are closed. External expert priority check and independent human proof read remain recommended.

## 1. Purpose

This component connects #3 SCL-Compression with OFET at theorem level.

The target distinction is

semantic compression of observation
versus
positive reconstruction resources.

The intended conclusion is stronger than a conceptual analogy:

> minimum finite observation and minimum positive reconstruction are distinct optimization problems.

The manuscript formalizes two complementary phenomena.

## 2. Interface distinction

Use separate notation for the two tuple interfaces.

- cmp_f^{CW}(L): Clark--Wurm fixed-order tuple-context compression used by #3; empty tuple components and empty separators are allowed.
- cmp_f^{+}(L): current #2/OFET admissible occurrence interface; tuple components are nonempty and internal separators are nonempty.

General theorem:

cmp_f^{+}(L) <= cmp_f^{CW}(L).

Strict inequality occurs on X_{k,r}.

Rule: never write the two minima as universally identical unless an explicit bridge lemma has been proved for the family under discussion.

## 3. Formalized theorem package

### A. Observation--Reconstruction Separation on R_{m,q}

Using the exact OFET resource formulas,

cmp_1^{CW}(R_{m,q}) = qm,

while compression-optimal observers and reconstruction-optimal observers have disjoint optimizer sets.

Exact encoded-data gap:

4(m-1)(q-1).

With q=m^2:

- reconstruction-optimal observer size / minimum observer size tends to 1;
- compression-optimal encoded reconstruction cost / reconstruction-optimal cost tends to 2.

Interpretation: asymptotically negligible observation overhead can yield a factor-two reconstruction improvement.

### B. Exact Clark--Wurm Compression of X_{k,r}

The v2 manuscript proves

cmp_1^{CW}(X_{k,r}) = 1,

and

cmp_f^{CW}(X_{k,r}) = 2 for every f >= 2.

The two-state upper bound is the emptiness observer e with e(epsilon)=1 and e(w)=z for nonempty w, where z^2=z.

The proof uses the unique skeleton

A_1 ... A_r B_1 ... B_r.

Audit result: the all-arity argument passed an internal adversarial proof audit. The revised proof makes the unique skeleton intervals, empty-separated blocks, invariant tuple-support set U, and slotwise index transfer explicit.

The ancillary script xkr_cw_small_audit.py supplies finite exhaustive sanity checks. It is evidence only, not part of the proof.

### C. Admissible-interface collapse on X_{k,r}

For the current nonempty #2/OFET interface,

cmp_f^{+}(X_{k,r}) = 1

for every finite f. Hence, for f >= 2,

cmp_f^{+}(X_{k,r}) < cmp_f^{CW}(X_{k,r}).

### D. Compression--Reconstruction Coincidence on X_{k,r}

The #3-optimal two-state emptiness observer acts trivially on the nonempty tuple components seen by the OFET occurrence learner and generates the same observer-sensitive rules as the slot observer.

Under the OFET encoded-data convention,

mcd^*(X_{k,r}) = 2r[1+r(k-1)],

with minimum characteristic-sample cardinality

1+r(k-1).

Important bookkeeping note: current #2 defines positive sample size as sum(|w|+1), whereas OFET defines its mcd scale as sum max(1,|w|). The bridge paper now states explicitly that its displayed mcd values use the OFET scale. Cardinality results are unaffected.

### E. Fixed Compression, Unbounded Reconstruction

Fix k=2 and put L_r=X_{2,r}. Then

cmp_2^{CW}(L_r)=2

for every r, while the global minimum characteristic-sample cardinality is r+1 and the OFET encoded minimum is

2r(r+1)=Theta(r^2).

Hence no function of cmp_2^{CW}(L) alone can universally upper-bound this learner-relative positive reconstruction cost on any reconstruction class containing all X_{2,r}.

Scope caution: alphabet size, target-word length, and witnessed rule rank grow with r. The theorem does not rule out bounds that use those parameters in addition to compression.

### F. Observer Refinement and Coincidence Principles

Use

h <= g iff h = pi o g,

so g is finer than h.

Formalized results:

- image size is nondecreasing under refinement;
- safety is preserved by refinement;
- residual and transition fragmentation are nondecreasing;
- for the fixed CFG and occurrence-MCFG architectures, finer observation removes semantic substitution rules;
- characteristic-sample families therefore become no larger under refinement;
- any strict tradeoff of larger observer size but smaller reconstruction cost must occur between refinement-incomparable observers;
- if the safe-observer preorder for the fixed reconstruction interface has a least element, that observer minimizes every refinement-monotone reconstruction resource.

### G. Relational-Morphism Reconstruction Separation

For R_{m,q}, every selector of every minimum-codomain separating relational morphism yields a compression-optimal observer, yet is reconstruction-suboptimal.

Exact lower gap:

4(m-1)(q-1).

Interpretation:

- relational morphism determines compression feasibility;
- the selected functional observer determines reconstruction geometry.

### H. Observer--Resource Pareto Principle

Fix one safety interface I. For a finite natural-valued resource vector

R_L^I(h) = (|im h|, F_1(h), ..., F_s(h)),

Dickson's lemma gives a finite nonempty Pareto-minimal profile set whenever I-safe observers exist and all coordinates are finite.

The corresponding compression number is recovered as the minimum first coordinate. If every coordinate is refinement-monotone, distinct Pareto points can only be represented by refinement-incomparable observers.

For R_{m,q}, the exact two-point frontier also yields a sharp weighted phase transition.

## 4. Proof-audit outcome

The theorem-by-theorem audit is in PROOF_AUDIT_v2.md.

No fatal mathematical gap is currently identified.

Repairs made in v2:

- all generic safety/compression claims are interface-qualified;
- the X_{k,r} Clark--Wurm proof is expanded at its two delicate positional steps;
- unary and vacuous cases are explicit in the positive-interface proof;
- the OFET versus current-#2 encoded-cost convention mismatch is documented;
- fixed-compression minima are fully quantified;
- the Pareto theorem is parametrized by a fixed interface;
- the old MASTER_NOTES escape corruption is removed.

## 5. What this component must not claim

- Do not claim learner-independent sample complexity.
- Do not claim cmp_f^{CW} and cmp_f^{+} are universally equal.
- Do not present R_{m,q} or X_{k,r} as broader language-class separations than proved.
- Do not claim a compression-only lower or upper bound under fixed alphabet/rank/word-length restrictions; that has not been proved.
- Do not claim broad priority for separating representation/model complexity from sample complexity; de la Higuera and teaching-dimension work already establish that broader distinction.
- Do not claim that typing/abstraction granularity affecting inference is new; Coste et al. and active abstraction-refinement work are prior art.
- Scoped wording such as "to the best of our knowledge, no prior work we found optimizes observer image and positive locking-data cost over the same safe finite-monoid observer space" is acceptable after the v3 audit.
- Do not mark the manuscript submission-ready until an external expert priority check and an independent human proof read are complete.

## 6. Current repository state

- main.tex: working manuscript v2, canonical editable source.
- README.md: manuscript overview and build instructions.
- PAPER.yaml: source-of-truth and audit metadata.
- MASTER_NOTES.md: this theorem/provenance master.
- PROOF_AUDIT_v2.md: theorem-by-theorem adversarial audit.
- xkr_cw_small_audit.py: finite exhaustive sanity checker.
- LITERATURE_PRIORITY_AUDIT_v3.md: dedicated literature/precedence audit and novelty boundary.

## 6. Literature-priority audit outcome

The v3 audit searched the project literature first and then external sources across characteristic samples/teaching dimension, typing bias, active abstraction refinement, symbolic automata, incompletely specified FSM minimization, and finite-algebra/distributional learning.

The strongest classical novelty boundary is de la Higuera (1997): characteristic-data efficiency is already known to depend on representation choice, so the broad statement "small representation does not imply small data" is not new.

The closest current conceptual neighbor found is Kim and Choi (FSE 2026), whose dynamic symbolic mapper is explicitly granularity-aware and uses coarse versus fine abstractions differently during active learning. This does not use passive positive-only grammar reconstruction, finite-monoid factor observers, or SCL compression.

No direct predecessor was found, in the searched scope, for the exact common-feasible-space optimization used here: safe finite-monoid observer image versus learner-relative positive locking-data cost, with the R_{m,q} optimizer separation, the X_{2,r} fixed-compression/unbounded-reconstruction result, or the minimum-relational-morphism selector corollary.

The Pareto-finiteness theorem itself is a routine Dickson-lemma application and should not be sold as a standalone priority claim. The new content is the exact instantiated observer-resource geometry.

See LITERATURE_PRIORITY_AUDIT_v3.md for the collision matrix and recommended wording.

The v2 TeX was compile-checked locally and produced a 14-page PDF with no undefined references/citations or overfull boxes. The remaining LaTeX diagnostics are harmless hyperref PDF-string warnings caused by mathematical section titles.
