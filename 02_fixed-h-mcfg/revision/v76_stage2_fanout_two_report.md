# MCFG #2 Stage 2: attack on `op:fanout-two` (superpolynomial lower bound at fan-out ≥ 2)

Date: 2026-10-18 (JST)
Status: **research report. The open problem is NOT resolved; the manuscript is unchanged by this stage.**
Tool: `revision/tools/tuple_subst_check.cpp` (C++ tuple-substitutability checker with rolling hashes and partitioned passes, cross-validated against a Python checker on $n\le3$). Usage: `tuple_subst_check words.txt d k passes escape_letters`.

## 1. Rigorous reductions obtained

### 1.1 Type-class lemma (lower bound for the paper's operator)

The (Start) rules of `def:reconstruction` link only to sample words. Proposition `prop:reconstruction-soundness` gives $u\equiv_{L,h}w$ whenever $[(w)]\Rightarrow^*u$. Hence:

> **Lemma A.** If $L\in\Cmcf{f}{h}$ and $K$ is characteristic for $L$ under $\mathcal B^{\le r}_{f,h}$, then for every $t\in h(L)$ the sample $K$ contains a word of type $t$.

So, for the paper's operator, `op:fanout-two` is equivalent to the following language-level question:

> Is there an $f$-MCFL family $L_n\in\Cmcf{f}{h}$ with $\|G_n\|\bar\theta_{G_n}$ polynomial, but with typed language thickness
> $\tau_h(L_n):=\max_{t\in h(L_n)}\min\{|w|:w\in L_n,\ h(w)=t\}$ superpolynomial?

The set-driven, operator-independent version additionally needs $L_n\cap h^{-1}(F)\in\Cmcf{f}{h}$. That is automatic by `lem:type-filter`.

By `thm:local-group-polydata`, any positive answer must use $h(\Sigma^+)\notin\mathbf{LG}$, i.e. $h(\Sigma^+)$ must contain $U_1$.

### 1.2 Slide lemma (the structural obstruction)

> **Lemma B.** Let $W=l\,s\,r$, and let $m$ occur in $s$ at more than $|M|^2$ positions $p$ for which $x_1=s[0:p]$ and $x_2=s[p+|m|:]$ are nonempty. Then there are $\tuple x\ne\tuple y$ with the same $h$-vector and the same context $E=l\,\square\,m\,\square\,r$, and $E[\tuple x]=E[\tuple y]=W$.

Proof: pigeonhole on the pair $(h(x_1),h(x_2))$.

Consequence. For a fixed $h$, every sufficiently long word of a $(2,h)$-tuple-substitutable language yields such "slides", and their distributions must coincide. In other words, the language must be invariant under moving the slid factor across *every* separator $m'$ in every other context. This is a commutation-type closure. Window and group components of $h$ do not prevent it: the pigeonhole is over the finite image of $h$.

### 1.3 Central-extension filters (positive side, mild generalization of `prop:abelian-coset-filter`)

Let $\psi:\Sigma^*\to\Gamma$ be a morphism, $Z\le Z(\Gamma)$, and suppose $h$ determines $\psi$ modulo $Z$. Then $L\cap\psi^{-1}(\gamma Z')$ inherits $(f,h)$-substitutability for $Z'\le Z$.

Proof: equal types give $\psi(y_i)=\psi(x_i)z_i$ with $z_i$ central, and a shared context forces $\prod z_i\in Z'$.

Such "weight" languages are slide-invariant at every arity. However, in a reduced grammar every nonterminal's yields then carry a constant central weight. A doubling chain would therefore need short words of weight $2^i$ for every $i\le n$. Over a fixed alphabet this appears impossible: short words realize only a bounded-rank generalized arithmetic progression of weights. This step is heuristic and not proved here. So weight languages are unlikely to give the lower bound.

## 2. Experimental search (all exhaustive over the stated $n$)

Typings used: $h_{\mathrm U}$ (escape presence, image $U_1$), optionally times the window $h^{k,k}$. All images contain $U_1$.

| Family (grammar size, thickness poly in $n$) | $d=1$ | $d=2$ (and $d=3$) | Diagnosed obstruction |
|---|---|---|---|
| #1 bracket doubling $L_n$ | OK | $k=1$ fails $n=3$; $k=2$ OK $n\le3$, **fails $n=4$** (73,253 violations) | periodic slide (Lemma B) inside escape words |
| mirror $u\varphi(u)$, unlabeled escape | – | fails $n=3$ | length slack (escape size ambiguous) |
| mirror, level-labeled escape $\mathtt z\mathtt t^i$ | – | fails $n=3$ ($k=2$) | dyadic alignment |
| flat $\mathtt a$/$\mathtt z$ doubling | fails from $n=2$ | fails | slack |
| flat, level-labeled | fails $n=3$ ($k=2$) | fails | dyadic alignment |
| Polish (prefix) encoding, labeled escapes | OK for $n\le4$ ($k\ge2$) | $k=2$ OK $n=3$, fails $n=4$ (13,150); $k=3$ still fails $n=4$ (10) | structural trade across the separator (Lemma B) |
| substitutable closure of Polish $n=4$ | – | diverges (violations grow to $10^5$ after 6 rounds) | no short pure word appeared |

Pattern: prefix codes and brackets fix $d=1$, because a single hole is pinned by its context. For $d\ge2$, the separator allows structure to be traded between components. Fixed windows only delay the failure, and the required window length grows with $n$.

## 3. Assessment

- A positive answer needs words whose exponential structure is invisible to slides, yet whose grammar has small thickness. Positional (tree, prefix-code, mirror) encodings violate slide invariance. Weight encodings are slide-invariant but (heuristically) cannot support small-thickness doubling.
- This makes a **negative answer plausible** (Conjecture N): at fan-out $\ge2$, $(f,h)$-substitutability might force polynomial typed language thickness for every fixed $h$. If true, the paper's dichotomy would be "LG boundary at fan-out one; no boundary at fan-out $\ge2$". This is a conjecture with experimental support only.

## 4. Suggested use in the manuscript (author decision)

- **Safe now:** add Lemma A as a remark after `op:fanout-two`, reformulating it as a typed-language-thickness question. It is short and rigorous.
- **Possible:** mention that the #1 doubling family fails $(2,h)$-substitutability for windowed semilattice typings at $n=4$. This is already partly in `rem:dichotomy-scope`.
- **Not yet:** any claim about the answer.

## 5. Next steps

1. Try to *prove* Conjecture N for a restricted class, e.g. $h(\Sigma^+)$ a semilattice and $L$ finite. Start from the slide closure: show that long words of type $t$ can be shortened by slides combined with thickness.
2. Alternatively, search for a non-positional construction: languages defined by central-extension weights intersected with a *bounded-depth* positional layer.
3. Make the GAP step in §1.3 rigorous (number of powers of two in a rank-$s$ generalized arithmetic progression).
