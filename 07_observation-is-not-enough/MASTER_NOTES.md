# Observation Is Not Enough — Research Master

Status: **working theorem master; not yet a manuscript**

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

Two complementary phenomena are currently targeted.

---

## 2. Interface distinction

Use separate notation for the two tuple interfaces.

- (operatorname{cmp}^{CW}_f(L)): Clark--Wurm fixed-order tuple-context compression used by #3; empty tuple components and empty separators are allowed.
- (operatorname{cmp}^{+}_f(L)): current #2/OFET admissible occurrence interface; tuple components are nonempty and internal separators are nonempty.

Working structural fact:

[
operatorname{cmp}^{+}_f(L)
le
operatorname{cmp}^{CW}_f(L).
]

Strict inequality occurs on the (X_{k,r}) family.

**Rule:** never write the two minima as universally identical unless an explicit bridge lemma has been proved for the family under discussion.

---

## 3. Theorem package to formalize

### A. Observation--Reconstruction Separation on (R_{m,q})

Target theorem package:

[
operatorname{cmp}^{CW}_1(R_{m,q})=qm,
]

while compression-optimal observers and reconstruction-optimal observers have disjoint optimizer sets.

Using the OFET exact characteristic-data formula, the working gap is

[
4(m-1)(q-1).
]

A quantitative specialization with (q=m^2) gives:

- reconstruction-optimal observer size / minimum observer size (	o 1);
- compression-optimal encoded reconstruction cost / reconstruction-optimal cost (	o 2).

Interpretation: asymptotically negligible observation overhead can yield a factor-two reconstruction improvement.

Status: **working proof package; formal TeX proof still required**.

---

### B. Exact Clark--Wurm Compression of (X_{k,r})

Working target:

[
operatorname{cmp}^{CW}_1(X_{k,r})=1,
qquad
operatorname{cmp}^{CW}_f(X_{k,r})=2
quad(fge2).
]

Candidate optimal two-state observer:

[
e(w)=
egin{cases}
1,&w=arepsilon,\
z,&w
earepsilon,
end{cases}
qquad z^2=z.
]

The all-arity upper bound uses the unique skeleton
[
A_1cdots A_rB_1cdots B_r
]
and must receive an independent adversarial proof audit before publication.

Status: **proved in research notes; proof audit required**.

---

### C. Admissible-interface collapse on (X_{k,r})

For the current nonempty #2/OFET interface, the working conclusion is

[
operatorname{cmp}^{+}_f(X_{k,r})=1
]
for the relevant finite arities, giving strict interface separation for (fge2):

[
1=
operatorname{cmp}^{+}_f(X_{k,r})
<
operatorname{cmp}^{CW}_f(X_{k,r})
=2.
]

Status: **working proof complete; formalization required**.

---

### D. Compression--Reconstruction Coincidence on (X_{k,r})

Although the two tuple interfaces differ, the #3-optimal two-state observer acts trivially on nonempty tuple components and therefore can attain the OFET reconstruction optimum.

Working exact cost:

[
operatorname{mcd}^{star}(X_{k,r})
=
2r[1+r(k-1)],
]
with minimum characteristic-sample cardinality
[
1+r(k-1).
]

Status: **working proof complete; formalization required**.

---

### E. Fixed Compression, Unbounded Reconstruction

Fix (k=2) and let (L_r=X_{2,r}).

Then the target theorem is

[
operatorname{cmp}^{CW}_2(L_r)=2
]
for every (r), while

[
CD^#(L_r)=r+1,
qquad
CD^{enc}(L_r)=2r(r+1)=Theta(r^2).
]

Hence no function of (operatorname{cmp}^{CW}_2(L)) alone can universally upper-bound the learner-relative positive reconstruction cost.

Status: **working proof package complete conditional on B/D audits**.

---

### F. Observer Refinement and Coincidence Principles

Use
[
hpreceq g
iff
h=picirc g,
]
so (g) is finer than (h).

Target structural results:

- image size is nondecreasing under refinement;
- safety is preserved by refinement;
- residual / transition fragmentation is nondecreasing;
- for the fixed reconstruction architectures under study, finer observation removes semantic substitution rules;
- characteristic-sample families therefore become no larger under refinement;
- any strict tradeoff of larger observer size but smaller reconstruction cost must occur between refinement-incomparable observers;
- if the safe-observer preorder has a least element, that observer minimizes every refinement-monotone reconstruction resource.

Status: **working proofs available; theorem hypotheses must be stated architecture-by-architecture**.

---

### G. Relational-Morphism Reconstruction Separation

#3 characterizes finite compression for regular languages via minimum-codomain separating relational morphisms.

For (R_{m,q}), the target bridge result is:

> every selector of every minimum-codomain separating relational morphism yields a compression-optimal observer, yet is reconstruction-suboptimal.

Working lower gap:

[
4(m-1)(q-1).
]

Interpretation:
- relational morphism determines compression feasibility;
- the selected functional observer determines reconstruction geometry.

Status: **working proof available; formal statement required**.

---

### H. Observer--Resource Pareto Principle

For a safe observer (h), use a finite natural-valued resource vector such as

[
mathcal R_L(h)
=
igl(
|operatorname{im}h|,
operatorname{Frag}_h,
operatorname{TFrag}_h,
CD^#_h,
CD^{enc}_h
igr).
]

Target general result:
- the componentwise Pareto-minimal profile set is finite and nonempty when safe observers exist and all coordinates are finite natural numbers;
- (operatorname{cmp}_f) is recovered as the minimum first coordinate;
- if every coordinate is refinement-monotone, distinct Pareto points can only be realized by refinement-incomparable observers.

Proof route: Dickson's lemma plus refinement monotonicity.

Status: **working proof available; scope statement required**.

---

## 4. What this component must not claim

- Do not claim learner-independent sample complexity.
- Do not claim that (operatorname{cmp}^{CW}_f) and (operatorname{cmp}^{+}_f) are universally equal.
- Do not present the (R_{m,q}) or (X_{k,r}) explicit families as general language-class separations beyond what is actually proved.
- Do not claim literature priority until a dedicated search has been completed.

---

## 5. Manuscript creation gate

Create `main.tex` only after:

1. independent proof audit of the all-arity (X_{k,r}) upper bound;
2. formal theorem/proof write-up of the (R_{m,q}) optimizer separation;
3. scope audit of refinement monotonicity for CFG and occurrence-MCFG learners;
4. proof audit of the relational-morphism selector corollary;
5. literature-priority audit;
6. final decision whether this remains a standalone short paper, a thesis-only synthesis chapter, or both.
