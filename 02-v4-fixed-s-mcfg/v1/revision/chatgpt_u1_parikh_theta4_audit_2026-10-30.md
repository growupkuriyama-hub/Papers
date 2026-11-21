<!-- PART 1/1 START -->
| Item | Status | Location in this answer |
|---|---|---|
| Audit of existing proof (P1)–(P6) | **PROVED** after one repaired omitted inequality (P4) | §1, especially §1.4; no fatal counterexample found |
| Universal improvement from \(\theta^5\) to \(\theta^4\) in `lem:app-u1-parikh` | **UNRESOLVED** | §2 describes the exact P5/P6 obstruction |
| Other proved partial result: conditional \(\theta^4\) bound \(\alpha\le\theta\), plus small-\(q\) corollary | **PROVED** | §3; insertable lemma in §3.1 |

## 1. Referee audit of (P1)–(P6)

I use the notation and hypotheses frozen in the question. In particular \(h=d\in\{1,2\}\), \(K=\min\{k\ge h:(p+k,q)\in P\}\), \(p+q\le \theta\), and we only discuss the hard case \(K>\theta+2\). All replacements below are substitutions of a complete derivation of the same typed nonterminal in a successful derivation, hence produce a successful derivation of some string. Because \(L\) is Parikh-saturated, once the new Parikh vector lies in \(P\), the string belongs to \(L\).

### 1.1 (P1) Row rigidity
Take \((c_0,y),(c_0+\delta,y)\in P\) with \(c_0\ge1\), \(1\le\delta\le K-h\). Since \(L\) is Parikh-saturated,
\[
b^y a^{c_0}\in L,\qquad b^y a^{c_0+\delta}\in L.
\]
Thus the one-hole context \( b^y a^{c_0-1}\Box\) accepts both \(a\) and \(a^{1+\delta}\). The two words have the same \(s\)-type \(1\). By \(1\)-tuple substitutability, their one-tuple distributions coincide. Let \(c'=p+K-\delta\). Then \(c'\ge p+h\ge1\). The context \(b^q a^{c'-1}\Box\) has
\[
b^q a^{c'} \quad\text{from }a,\qquad
b^q a^{c'+\delta}=b^q a^{p+K}\quad\text{from }a^{1+\delta}.
\]
The latter lies in \(L\), because \((p+K,q)\in P\). Distribution equality therefore gives \(b^q a^{c'}\in L\), so \((p+K-\delta,q)\in P\). Since \(K-\delta\ge h\), this contradicts minimality of \(K\). Hence (P1) is valid.

### 1.2 (P2)
Let \(u'\) be a proper descendant of \(u\) with the same nonterminal and \(b_u=b_{u'}\), and put \(\delta=a_u-a_{u'}\). If \(0<\delta\le K-h\), replacing \(u\) by \(u'\) produces a valid sentence with Parikh vector
\[
(p+K-\delta,q),
\]
contradicting minimality of \(K\). If \(\delta=0\), the replacement has the same whole Parikh vector; by nondeleting/nonpermuting/nonmerging, the terminal-free context between the two identical typed nonterminals is the identity on the tuple, so it gives a derivation of the same word with fewer nodes, contradicting node-minimality of \(T\) (equivalently, choose \(T\) node-minimal among derivations realizing the fixed Parikh vector; Parikh saturation permits this). Thus
\[
a_u-a_{u'}\ge K-h+1. \tag{1}
\]
If three comparable nodes have the same nonterminal and the same \(b\)-value, applying (1) twice gives
\[
p+K\ge a_u-a_{u'''}\ge 2(K-h+1).
\]
For \(h=1\) this gives \(K\le p\); for \(h=2\) it gives \(K\le p+2\), both contradicting \(K>p+2\). Hence along each root-to-leaf path, for each nonterminal and each \(b\)-value there are at most two nodes. Since \(b\)-values lie in \([0,q]\),
\[
\#\{\text{nodes on a path}\}\le 2v(q+1).
\]
Every mixed node lies on a path to one of the \(q\) terminal occurrences of \(b\), so
\[
M\le 2v q(q+1)\le 4v\theta^2. \tag{2}
\]
This proof is valid.

### 1.3 (P3)
Let \(u\) be heavy pure, label \(B\), yield \(a^{\ell_u}\), and let \((x_B,y_B)\) be the Parikh vector of a short yield of \(B\). Since \(\ell_u>\theta+1\) and \(x_B\le\theta\),
\[
g_u:=\ell_u-x_B\ge2.
\]
Replacing the subtree at \(u\) changes the global Parikh vector from \((p+K,q)\) to
\[
(p+K-g_u,\;q+y_B). \tag{3}
\]
For an antichain \(J\) of heavy pure nodes, simultaneous replacement gives
\[
(p+K-\sigma(J),\,q+Y(J)),\qquad
\sigma(J)=\sum_{u\in J}g_u,\quad
Y(J)=\sum_{u\in J}y_{B_u}. \tag{4}
\]
This is a valid derivation, because the replaced nodes are incomparable.

Now suppose \(J,J'\) are antichains, \(Y(J)=Y(J')\), and both \(\sigma(J),\sigma(J')\le K-h\). Then (4) gives two points of \(P\) in the same row \(q+Y(J)\), whose \(a\)-coordinates differ by
\[
|\sigma(J)-\sigma(J')|\le K-h.
\]
Also the smaller \(a\)-coordinate is at least
\[
p+K-\max\{\sigma(J),\sigma(J')\}\ge p+h\ge1.
\]
By (P1), the difference must be \(0\). Hence \(\sigma(J)=\sigma(J')\). Thus (P3) is valid.

### 1.4 (P4): the only place needing a written repair
The first non-implicit assertion in the transcription is the claim in (P4) that, for frequent \(B,C\), the relevant antichains have \(\sigma\le K-h\). This is not immediate from “equal \(Y\)”. It is true, but needs the following short argument.

First assume \(m_B\ge2\). Any two heavy pure \(B\)-nodes are incomparable: if \(u\) were a proper ancestor of \(v\), then (P2) gives \(a_u-a_v\ge K-h+1\); since \(v\) is heavy, \(\ell_v\ge\theta+2\), so
\[
\ell_u\ge K+\theta-h+3,
\]
which exceeds \(p+K\le \theta+K\) for \(h=1,2\), a contradiction.

Choose a heavy pure \(B\)-node \(u\). Since \(m_B\ge2\), there is another heavy \(B\)-node \(v\), disjoint from \(u\). Then
\[
\ell_u\le p+K-\ell_v\le p+K-(\theta+2)\le K-2, \tag{5}
\]
because \(p\le p+q\le\theta\). Hence
\[
g_u=\ell_u-x_B\le K-2
\]
**[revised]** ここから先は保存された原文が存在しないため、指定された原稿と保存された計算過程を照合して再構成した部分である。以下を「前回の原文そのもの」とは扱わない。上の未完の数式は閉じ括弧を補っている。

This also gives \(g_u\le K-h\), because \(h\in\{1,2\}\). The same estimate holds for every heavy pure node labelled \(B\). For two such nodes \(u,u'\), the singleton antichains \(\{u\}\) and \(\{u'\}\) have the same value \(Y=y_B\) and have \(\sigma\le K-h\). Applying (P3), we obtain \(g_u=g_{u'}=:g_B\), and consequently all their yields have the same length \(\ell_B=x_B+g_B\).

If \(y_B=0\), replacing one \(B\)-node gives a point \((p+K-g_B,q)\in P\), with \(h\le K-g_B<K\), contradicting the definition of \(K\). Hence \(y_B\ge1\).

Call \(B\) *frequent* when \(m_B>\theta\). If \(B,C\) are frequent, the short-yield bounds give \(1\le y_B,y_C\le\theta\), so we can choose \(y_C\) distinct heavy pure \(B\)-nodes, and \(y_B\) distinct heavy pure \(C\)-nodes. Each choice is an antichain. Moreover, disjointness of the \(m_B\) heavy \(B\)-subtrees gives
\[
m_B\ell_B\le p+K,
\qquad
y_Cg_B\le(m_B-1)\ell_B\le p+K-\ell_B\le K-2\le K-h,
\]
and symmetrically \(y_Bg_C\le K-h\). The two antichains have the same \(Y=y_By_C\), so (P3) yields
\[
y_Cg_B=y_Bg_C.
\]
Thus, whenever frequent labels exist, they have a common positive ratio
\[
\alpha:=\frac{g_B}{y_B},\qquad
\ell_B=x_B+\alpha y_B\le(1+\alpha)\theta.
\]
The missing bounds on \(\sigma\) have now been supplied. **[revised] The P4 repair is proved.**

### 1.5 (P5): the ratio estimate [revised]

Put
\[
\alpha_*=(r+1)(\theta+1)(2\theta+1)v
\le6(r+1)v\theta^2.
\]
If no frequent label occurs there is no ratio to bound. If frequent labels occur but \(\alpha\le\theta\), then \(\alpha\le\alpha_*\) immediately. Assume \(\alpha>\theta\), choose a heavy pure node \(u\) labelled by a frequent \(B\), and let \(H_u\) be the number of heavy pure nodes in the subtree rooted at \(u\).

Within this pure subtree, heavy nodes are closed under taking ancestors. Each such node writes at most \(\theta\) terminals explicitly, and has at most \(r\) children that fail to be heavy, each of length at most \(\theta+1\). Therefore
\[
\ell_B\le(r+1)(\theta+1)H_u. \tag{6}
\]
Two comparable heavy pure nodes have distinct nonterminal labels by (P3), so there are at most \(v\) heavy-ancestor levels, each an antichain. Every frequent-labelled node on a fixed level has yield length
\(\ell_C=x_C+\alpha y_C\ge\alpha\). Since its yield is inside the \(u\)-yield, the number of these nodes per level is at most
\[
\frac{\ell_B}{\alpha}
\le\frac{(1+\alpha)\theta}{\alpha}
=\theta+\frac{\theta}{\alpha}<\theta+1.
\]
Consequently at most \(v\theta\) nodes on these levels are frequent-labelled. Every nonfrequent nonterminal occurs at most \(\theta\) times among the heavy pure nodes of the *whole* tree, so at most \(v\theta\) additional nodes are nonfrequent-labelled. Hence
\[
H_u\le2v\theta\le v(2\theta+1).
\]
Now \(y_B\ge1\), so
\[
\alpha=\frac{g_B}{y_B}\le g_B\le\ell_B
\le(r+1)(\theta+1)v(2\theta+1)=\alpha_*.
\]
This proves (P5); the argument relies on the *actual disjointness of yields at a fixed heavy-ancestor level*, rather than an implicit independence assumption.

### 1.6 (P6): counting [revised]

Let
\[
T_*=(\alpha_*+1)\theta
\le7(r+1)v\theta^3.
\]
Call a pure node *large* when its yield length is greater than \(T_*\). Since every frequent-labelled heavy pure node has yield length at most \((1+\alpha)\theta\le T_*\), every large pure node has a nonfrequent label. Large nodes are heavy (as \(T_*\ge\theta+1\)), so their total number \(H_{\rm large}\) is at most \(v\theta\).

Within each maximal pure subtree, large nodes are ancestor-closed. Every \(a\)-letter of the successful yield \(W=b^qa^{p+K}\) either is written at a mixed node, is written at a large node, or lies in a maximal nonlarge pure subtree. Such a maximal subtree is rooted at the root of \(T\), or at a child of a mixed node, or at a child of a large node. There are therefore at most \(rM+rH_{\rm large}+1\) such subtrees, each of yield length at most \(T_*\). Since each grammar rule writes at most \(\theta\) terminals, the resulting count is
\[
\begin{aligned}
p+K
&\le \theta M+\theta H_{\rm large}
 +(rM+rH_{\rm large}+1)T_*\\
&\le \theta M+v\theta^2+(rM+rv\theta+1)T_*\\
&\le5v\theta^3+6rv\theta^2\cdot7(r+1)v\theta^3\\
&\le(42r(r+1)+5)v^2\theta^5.
\end{aligned}
\tag{7}
\]
Here \(M\le4v\theta^2\), \(rM+rv\theta+1\le6rv\theta^2\), and \(v,\theta\ge1\), \(r\ge2\).

For the other type cases the manuscript already gives bounds \(8(r+1)v\theta\) (all components of type \(\zeta\)) and \(12(r+1)v\theta^3\) (mixed types). Combining these with (7) yields
\[
\tau(G,s)\le[42r(r+1)+12(r+1)]v^2\theta^5.
\]
This completes the audit of (P1)–(P6), subject to the exact grammatical and Parikh-saturation hypotheses stated at the beginning of §1.

### 1.7 Audit conclusion [revised]

The first omitted justification in the supplied transcription was the small-\(\sigma\) condition for the antichains compared in (P4). It is repaired in §1.4 using the inequality \(m_B\ell_B\le p+K\). The remaining steps (P5)–(P6) are consistent with the manuscript's assumptions, and the audit has not produced a counterexample. This does **not** certify the proof beyond the explicitly audited derivation or establish a new universal exponent improvement.

## 2. Attempt to replace \(\theta^5\) by \(\theta^4\) [revised]

**Status: UNRESOLVED for the full Parikh-saturated lemma.** The bound in (P6) is driven by the product
\[
M\cdot T_*
=O_r(v\theta^2)\,O_r(v\theta^3)
=O_r(v^2\theta^5).
\]
The first factor comes from (P2), which charges mixed nodes to paths ending at \(b\)-occurrences; the second from (P5), whose ratio bound is \(\alpha_*=O_r(v\theta^2)\), giving a threshold \(T_*=O_r(v\theta^3)\).

The present inequalities do not establish any of the following uniform refinements:

1. \(M=O_r(v\theta)\);
2. \(\alpha=O_r(\theta)\) for all hard all-pure cases (hence \(T_*=O(\theta^2)\));
3. a direct count of the actual nonlarge pure subtrees that avoids multiplying the worst-case \(M\) and \(T_*\).

In particular, a local estimate that uses \(T_*=O(\theta^2)\) **cannot** be inserted unconditionally: the currently proved estimate on \(\alpha\) is quadratic in \(\theta\) and also contains \(v\). Conversely, the present bounds are *upper estimates*, not realizability constructions; they do not prove that a \(\theta^4\) bound is false. This is an exact obstruction in the existing *proof method*, not a counterexample to the proposed theorem.

The two conditional refinements below are genuine consequences of the audited inequalities and do not resolve the universal question.

## 3. Proved partial improvement [revised]

### 3.1 Insertable lemma: a conditional \(\theta^4\) bound [revised]

**Proposition.** Fix a reduced good fan-out-\(\le2\), rule-rank-\(\le r\) grammar \(G\) for a Parikh-saturated \((1,s)\)-tuple-substitutable \(L\), where \(r\ge2\), \(v=|V|\), and \(\theta=\bar\theta_G\ge1\). Fix a typed nonterminal \(X=A_{\mathbf t}\) for which all \(h\in\{1,2\}\) components have type \(1\). Let \(K=\tau_X\), and, if \(K>\theta+2\), form the tree \(T\), the frequent heavy pure labels, and their common ratio \(\alpha\) as in (P1)–(P4). If there is no frequent label, set \(\alpha=0\). Under the additional hypothesis
\[
\alpha\le\theta,
\]
we have
\[
K\le20rv\theta^4. \tag{8}
\]
If the same additional hypothesis holds for **every hard all-pure typed class** of \(G\), then
\[
\tau(G,s)\le20rv\theta^4, \tag{9}
\]
and the two canonical reconstruction operators have a common characteristic sample whose encoded length is \(O_r(\|G\|^2\theta^4)\).

**Proof.** If \(K\le\theta+2\), (8) is immediate. Otherwise apply the audited (P1)–(P4). Define
\[
T_0:=\max\{\theta+1,(1+\alpha)\theta\}
\le\theta(\theta+1)\le2\theta^2.
\]
Call a pure node *large* when its yield length exceeds \(T_0\). Such a node is heavy. Every frequent-labelled heavy node has length at most \((1+\alpha)\theta\le T_0\) by (P4). Thus every large node is labelled by a nonfrequent nonterminal, and there are at most \(v\theta\) of them in \(T\).

The argument of (P6), with \(T_0\) in place of \(T_*\), applies verbatim: writing \(H_{\rm large}\le v\theta\) and \(M\le4v\theta^2\),
\[
\begin{aligned}
p+K
&\le \theta M+\theta H_{\rm large}
 +(rM+rH_{\rm large}+1)T_0\\
&\le 4v\theta^3+v\theta^2
 +(4rv\theta^2+rv\theta+1)\,2\theta^2\\
&=8rv\theta^4+(2r+4)v\theta^3+v\theta^2+2\theta^2\\
&\le20rv\theta^4.
\end{aligned}
\]
The last inequality uses \(r\ge2\), \(v,\theta\ge1\). This proves (8).

For the global conclusion, all nonhard all-pure classes satisfy \(\tau_X\le\theta+2\). The original proof bounds the all-\(\zeta\) classes by \(8(r+1)v\theta\) and mixed classes by \(12(r+1)v\theta^3\), each at most \(20rv\theta^4\) for \(r\ge2\). Therefore (9) follows. The characteristic-sample bound follows from `cor:distribution-representatives`, since \(N_{\rm typ}\le3^{2r}\|G\|\), \(v\le\|G\|\), and
\[
\begin{aligned}
\|F\|_+
&\le N_{\rm typ}(1+2\theta+r\tau)+\mathbf1_{\{\varepsilon\in L\}}\\
&\le3^{2r}(3+20r^2)\,\|G\|^2\theta^4
 +\mathbf1_{\{\varepsilon\in L\}}.
\end{aligned}
\]
This completes the proof. \(\square\)

**English LaTeX text proposed for insertion** (a complete statement and proof, not an unconditional amendment to `lem:app-u1-parikh`):

```latex
\begin{lemma}[A conditional fourth-power bound in the all-pure case]
\label{lem:app-u1-parikh-small-ratio}
Assume the hypotheses of Lemma~\ref{lem:app-u1-parikh},
with $r\ge2$, $v=|V|$, and $\theta=\bar\theta_G$.
Fix a realized typed nonterminal $X=A_{\mathbf t}$ all of whose
components have type $1$, and let $K=\tau_X$.
In the hard case $K>\theta+2$, use the node-minimal derivation
and the definitions of heavy pure nodes and frequent nonterminals
from the all-pure part of that lemma.  Let $\alpha$ be the
common ratio $g_B/y_B$ for frequent labels, and set $\alpha=0$
if no frequent label exists.  If $\alpha\le\theta$, then
\[
  K\le20rv\theta^4.
\]
If this condition holds for every hard all-pure typed
nonterminal, then $\tau(G,s)\le20rv\theta^4$.
\end{lemma}
\begin{proof}
The case $K\le\theta+2$ is immediate. Otherwise put
\[
 T_0=\max\{\theta+1,(1+\alpha)\theta\}\le2\theta^2.
\]
By (P4), a frequent label cannot occur on a pure node whose
yield length exceeds $T_0$. Every such large node is heavy
and has a nonfrequent label, so there are at most $v\theta$
large nodes. As in (P6), large nodes are ancestor-closed
within maximal pure subtrees. With $M$ the number of mixed
nodes, (P2) gives $M\le4v\theta^2$, and the same covering
argument as in (P6) yields
\[
\begin{aligned}
p+K
 &\le\theta M+\theta v\theta
       +(rM+rv\theta+1)T_0\\
 &\le4v\theta^3+v\theta^2
       +2\theta^2(4rv\theta^2+rv\theta+1)\\
 &\le20rv\theta^4.
\end{aligned}
\]
Finally, the all-$\zeta$ and mixed-type bounds in the original
proof are $8(r+1)v\theta$ and $12(r+1)v\theta^3$,
respectively, and are also at most $20rv\theta^4$ for
$r\ge2$. This gives the global conclusion under the
stated additional hypothesis.
\end{proof}
```

**Placement.** This lemma may be inserted immediately after `lem:app-u1-parikh`. Under its hypothesis, it replaces the threshold \(T_*=(\alpha_*+1)\theta\) and subsequent count in (P6) by \(T_0\) and the bound (8). It **does not** replace (P1)–(P5), nor justify changing the unconditional main theorem.

### 3.2 A second sufficient condition: few \(b\)'s in the fixed context [revised]

There is also a special-case fourth-power estimate with **no assumption on \(\alpha\)**. In the hard all-pure case, suppose the fixed context \(E_A\) contains \(q\) occurrences of \(b\) and
\[
q(q+1)\le\theta.
\]
Then (P2) gives \(M\le2vq(q+1)\le2v\theta\). In (P6) keep the original \(T_*\le7(r+1)v\theta^3\) and the unchanged bound \(H_{\rm large}\le v\theta\). We obtain
\[
\begin{aligned}
p+K
&\le\theta M+\theta v\theta
 +(rM+rv\theta+1)T_*\\
&\le3v\theta^2+(3rv\theta+1)7(r+1)v\theta^3\\
&\le30r(r+1)v^2\theta^4.
\end{aligned}
\]
Thus \(\tau_X=K\le30r(r+1)v^2\theta^4\). This applies, for example, whenever \(q=0\), and more generally for \(q=O(\sqrt{\theta})\) with \(q(q+1)\le\theta\). It remains a class-by-class bound: the other typed nonterminals need not have the same \(q\).

## 4. Final disposition [revised]

| Claim | Judgment | Basis |
|---|---|---|
| Audit (P1)–(P6), including repaired small-\(\sigma\) step | **PROVED** within the stated hypotheses | §§1.1–1.7 |
| Universal \(\theta^4\) bound, retaining \(v^2\) | **UNRESOLVED** | §2 |
| If every hard all-pure class has \(\alpha\le\theta\), then \(\tau(G,s)\le20rv\theta^4\) | **PROVED (conditional)** | §3.1 |
| If \(q(q+1)\le\theta\) for one hard all-pure class, then \(\tau_X\le30r(r+1)v^2\theta^4\) | **PROVED (conditional)** | §3.2 |

**[revised] Provenance and limitations.** §§1.1–1.3 and the opening of §1.4 above were recovered from the existing truncated `deepseek_answer.md`; everything from the completion of its unfinished display equation onward is a **reconstruction**, not a verbatim recovery. Its calculations were checked against `lem:app-u1-parikh` in the GitHub `main.tex` with blob SHA `4cdaea185e712368b0c0ab5a23b725eb08bbb088`. No universal \(\theta^4\) theorem, counterexample to such a theorem, or public-literature novelty claim is being made. **文献上の新規性：未調査。**

<!-- PART 1/1 END -->
<!-- END OF FILE -->
