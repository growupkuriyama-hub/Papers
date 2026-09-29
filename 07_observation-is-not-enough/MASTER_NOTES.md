# Observation Is Not Enough — Research Master

Status: **working manuscript v1 exists in `main.tex`; proof/literature audits still open**

## 1. Purpose

This component connects #3 SCL-Compression with OFET at theorem level.

The target distinction is:

[
	ext{semantic compression of observation}
quad	ext{vs.}quad
	ext{positive reconstruction resources}.
]

The intended conclusion is stronger than a conceptual analogy:

> minimum finite observation and minimum positive reconstruction are distinct optimization problems.

The v1 manuscript formalizes two complementary phenomena.

## 2. Interface distinction

Use separate notation for the two tuple interfaces.

- (operatorname{cmp}^{CW}_f(L)): Clark--Wurm fixed-order tuple-context compression used by #3; empty tuple components and empty separators are allowed.
- (operatorname{cmp}^{+}_f(L)): current #2/OFET admissible occurrence interface; tuple components are nonempty and internal separators are nonempty.

General theorem:

[
operatorname{cmp}^{+}_f(L)
le
operatorname{cmp}^{CW}_f(L).
]

Strict inequality occurs on (X_{k,r}).

**Rule:** never write the two minima as universally identical unless an explicit bridge lemma has been proved for the family under discussion.

## 3. Formalized theorem package

### A. Observation--Reconstruction Separation on (R_{m,q})

The v1 manuscript proves, using the exact OFET resource formulas,

[
operatorname{cmp}^{CW}_1(R_{m,q})=qm,
]

while compression-optimal observers and reconstruction-optimal observers have disjoint optimizer sets.

Exact encoded-data gap:

[
4(m-1)(q-1).
]

With (q=m^2):

- reconstruction-optimal observer size / minimum observer size tends to (1);
- compression-optimal encoded reconstruction cost / reconstruction-optimal cost tends to (2).

Interpretation: asymptotically negligible observation overhead can yield a factor-two reconstruction improvement.

### B. Exact Clark--Wurm Compression of (X_{k,r})

The v1 manuscript proves

[
operatorname{cmp}^{CW}_1(X_{k,r})=1,
qquad
operatorname{cmp}^{CW}_f(X_{k,r})=2
quad(fge2).
]

The two-state upper bound is the emptiness observer

[
e(w)=
egin{cases}
1,&w=arepsilon,\
z,&w
earepsilon,
end{cases}
qquad z^2=z.
]

The proof uses the unique skeleton

[
A_1cdots A_rB_1cdots B_r.
]

**Audit flag:** this all-arity argument should receive an independent adversarial proof audit before submission.

### C. Admissible-interface collapse on (X_{k,r})

For the current nonempty #2/OFET interface,

[
operatorname{cmp}^{+}_f(X_{k,r})=1,
]

hence for (fge2),

[
1=
operatorname{cmp}^{+}_f(X_{k,r})
<
operatorname{cmp}^{CW}_f(X_{k,r})
=2.
]

### D. Compression--Reconstruction Coincidence on (X_{k,r})

The #3-optimal two-state emptiness observer acts trivially on the nonempty tuple components seen by the OFET occurrence learner and attains the same hypothesis as the slot observer.

Thus

[
operatorname{mcd}^{star}(X_{k,r})
=
2r[1+r(k-1)],
]

with minimum characteristic-sample cardinality

[
1+r(k-1).
]

### E. Fixed Compression, Unbounded Reconstruction

Fix (k=2) and put (L_r=X_{2,r}). Then

[
operatorname{cmp}^{CW}_2(L_r)=2
]

for every (r), while

[
CD^#(L_r)=r+1,
qquad
CD^{enc}(L_r)=2r(r+1)=Theta(r^2).
]

Hence no function of (operatorname{cmp}^{CW}_2(L)) alone can universally upper-bound the learner-relative positive reconstruction cost on any reconstruction class containing all (X_{2,r}).

### F. Observer Refinement and Coincidence Principles

Use

[
hpreceq g
iff
h=picirc g,
]

so (g) is finer than (h).

Formalized results:

- image size is nondecreasing under refinement;
- safety is preserved by refinement;
- residual / transition fragmentation is nondecreasing;
- for the fixed CFG and occurrence-MCFG architectures, finer observation removes semantic substitution rules;
- characteristic-sample families therefore become no larger under refinement;
- any strict tradeoff of larger observer size but smaller reconstruction cost must occur between refinement-incomparable observers;
- if the safe-observer preorder has a least element, that observer minimizes every refinement-monotone reconstruction resource.

### G. Relational-Morphism Reconstruction Separation

For (R_{m,q}), every selector of every minimum-codomain separating relational morphism yields a compression-optimal observer, yet is reconstruction-suboptimal.

Exact lower gap:

[
4(m-1)(q-1).
]

Interpretation:

- relational morphism determines compression feasibility;
- the selected functional observer determines reconstruction geometry.

### H. Observer--Resource Pareto Principle

For a finite natural-valued resource vector

[
mathcal R_L(h)
=
igl(
|operatorname{im}h|,
F_1(h),ldots,F_s(h)
igr),
]

Dickson's lemma gives a finite nonempty Pareto-minimal profile set whenever safe observers exist and all coordinates are finite.

The compression number is recovered as the minimum first coordinate. If every coordinate is refinement-monotone, distinct Pareto points can only be represented by refinement-incomparable observers.

For (R_{m,q}), the exact two-point frontier also yields a sharp weighted phase transition.

## 4. What this component must not claim

- Do not claim learner-independent sample complexity.
- Do not claim that (operatorname{cmp}^{CW}_f) and (operatorname{cmp}^{+}_f) are universally equal.
- Do not present (R_{m,q}) or (X_{k,r}) as broader language-class separations than proved.
- Do not claim literature priority until a dedicated search has been completed.
- Do not mark the manuscript submission-ready before the all-arity (X_{k,r}) audit and literature-priority audit.

## 5. Current repository state

- `main.tex`: working manuscript v1.
- `README.md`: manuscript overview and build instructions.
- `PAPER.yaml`: source-of-truth and audit metadata.
- `MASTER_NOTES.md`: this theorem/provenance master.

The v1 TeX was compile-checked locally and produced a 13-page PDF with no undefined references/citations or overfull boxes.
