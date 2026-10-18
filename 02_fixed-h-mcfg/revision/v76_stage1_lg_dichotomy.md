# MCFG #2 v76 Stage 1: local-group (LG) upper bound and the semilattice boundary

Date: 2026-10-18 (JST)
Status: **merged into the v76 pre-submission working manuscript through PR #41; not independently human-refereed or journal-submitted.** New local-group results remain mathematical-review priorities.
New file: `appendix_local_group.tex` (EN) / `japanese/appendix_local_group_JP.tex` (JP), compiled as the last appendix.

## Result in one line

The polynomial original-thickness bound $O(\|G\|^3\bar\theta_G)$ extends from window–group typings ($\mathbf{LI}\vee\mathbf G$, already characterized in #1 Lemma 7.4) to **all typings with $h(\Sigma^+)\in\mathbf{LG}$**, at every fixed fan-out. $\mathbf{LG}$ is exactly the class of finite semigroups containing no copy of the two-element semilattice $U_1$, which is the obstruction of #1's exponential lower bound. At the pseudovariety level this gives a sharp dichotomy at fan-out one.

## New statements (all proved in the appendix)

| Label | Content |
|---|---|
| `def:local-group-typing` | $\lambda_{k,g}(w)=(h^{k,k}_\Sigma(w),\ \prod g(\text{length-}(k{+}1)\text{ factors}))$ |
| `lem:local-group-morphism` | $\lambda_{k,g}$ is a finite-monoid morphism; explicit product on long elements |
| `lem:local-group-blocks` | Replacing blocks while keeping their windows keeps the root window, and changes $\gamma$ only through an ordered product with fixed constants |
| `thm:lg-characterization` | $h(\Sigma^+)\in\mathbf{LG}$ ⟺ no $U_1$ subsemigroup ⟺ all idempotents in the minimal ideal ⟺ $h\preceq\lambda_{k,g}$ (with $k=\lvert S\rvert$) |
| `prop:li-g-strict` | $\mathbf{LI}\vee\mathbf G\subseteq\mathbf{LG}$, strictly: "parity of $\mathtt{ab}$ occurrences" is LG but not window–group |
| `lem:local-group-shortest` | Shortest tuple with prescribed $\lambda$-type $\le(r+1)b_{\mathrm w}\max\{1,(M_{A,f}-1)n_\lambda\}=O(\|G\|^2\bar\theta)$ |
| `thm:local-group-polydata` | Characteristic data $O(\|G\|^3\bar\theta_G)$ for every LG typing, at every fixed $f$ |
| `lem:type-filter` | $L\cap h^{-1}(F)$ inherits $(f,h)$-substitutability |
| `cor:pseudovariety-dichotomy` | $\mathbf V\subseteq\mathbf{LG}$ ⇒ polynomial at every $f$. $\mathbf V\not\subseteq\mathbf{LG}$ ⇒ $U_1\in\mathbf V$ and an exponential family at $f=1$ (via #1 Prop. 6.3) |
| `rem:dichotomy-scope` | Limits: the lower side is only at $f=1$, and only at the pseudovariety level |

## Proof idea

1. **Algebra (iii⇒iv).** For $S\in\mathbf{LG}$ the minimal ideal $K$ is a Rees matrix semigroup, and words of length $\ge|S|$ land in $K$. Right multiplication acts on the group coordinate through $\rho(\lambda,s)$, which depends only on the $\Lambda$-coordinate. That coordinate is determined by the last $|S|$ letters. Hence the group coordinate is an ordered product over the length-$(|S|{+}1)$ factors.
2. **Shortening.** Heavy subtrees are replaced by shortest derivations with the **same window vector** (existing window lemma, cost $O(\|G\|\bar\theta)$). Then the root $\gamma$ changes like block group values, so the existing order-homogenization and interval lemmas apply. Abelian groups use the Davenport-constant variant.

## Verification

- **Characterization.** 379 random transformation semigroups (81 in LG):
  - (i)⇔(ii)⇔(iii) agree in every case;
  - the window factorization $h(w)=h(\mathrm{pref}_n w)\prod_j e_{\lambda_j}h(w_{j+1})$ holds on random long words.
- **Converse direction.** For $\lambda_{k,g}$ into $S_3$ ($k=1,2$) and $\mathbb Z_3$: the kernel is a congruence (random words), and every $eTe$ of the image is a group.
- **Falsification attempt.** On #1's doubling family $G_n$ ($n\le14$), typed thickness grows as $3\cdot2^n-2$ under $h_{\mathrm U}$. Under four LG typings (three random $S_3$ factor typings and the $\mathtt{[<}$-parity typing) it grows linearly ($\approx4n$), as the theorem predicts.
- **Negative finding.** $L_n$ is **not** $(2,h_{\mathrm U})$-tuple-substitutable: exhaustive check for $n\le3$. Witness: pairs $(\mathtt[,\mathtt{a]})$ and $(\mathtt{[a},\mathtt])$ in context $\mathtt{[[aa]}\,\square\,\mathtt a\,\square\,\mathtt]$. Under content typing it fails at $n=3$. So the lower side does not lift to $f\ge2$ by this family.
- **Build.** EN 45 pp, JP 50 pp. No undefined references, citations or duplicate labels. 98 labels match EN/JP; bibliography keys match.
- **Citations.** #1 citations checked against pinned commit 834e99a1 (Prop. 6.3 = lower bound, Lemma 7.4 = $\mathbf{LI}\vee\mathbf G$ characterization). New references: Straubing 1985, Tilson 1987 (context only), Howie 1995 (Rees theorem and complete simplicity of the minimal ideal).

## What remains (Stage 2 candidates)

1. **Per-typing lower bound.** For every individual $h$ with $h(\Sigma^+)\notin\mathbf{LG}$, is there an exponential family at $f=1$? This needs a substitutability-preserving coding of the doubling family through words $x,y$ with $h(x)=e$, $h(y)=f$ and $ef=fe=f\ne e$.
2. **Fan-out $\ge2$ lower bound for some non-LG typing.** This is `op:fanout-two`. It needs a new family whose tuple splits are rigid.
3. **Abstract and Introduction.** These are unchanged. Suggested abstract sentence if adopted:
   > "More generally, the bound holds whenever the positive image of $h$ is a local group, i.e. contains no two-element semilattice; at fan-out one this is sharp at the level of pseudovarieties."
4. **Independent review.** The (iii)⇒(iv) Rees-coordinate computation and the claim that Lemma `group-interval` applies verbatim to $\gamma$-values need independent checking.
