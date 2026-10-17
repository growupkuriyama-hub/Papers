# v71 archival repository of results excluded from the I&C submission core

This is **not compiled into the v71 article**. These original v70 text fragments
are preserved verbatim for possible use in a separate note, further paper,
or doctoral thesis. Some original cross-references and macros require
context from the v70 manuscript. Do not claim the proofs are independently
certified by merely archiving them.

Original source: GitHub `02_fixed-h-mcfg/main.tex`, **v70**,
blob SHA `cbd6c1f0bad1b9141a61561d866b6357531a9684` and `appendix_bracketed_substitutability.tex`,
blob SHA `1d2bded06a88fa042877f08d53e6e23187a11c57`. Previous complete v70 source is available
in Git history at merge commit `8de71485799120c963b58b701921e25eb62aede4`.

## Contents

The retained core keeps `thm:boundary-polydata`,
`thm:intrinsic-ranktwo-witness`,
`thm:arbitrary-filter-separation`,
`prop:strong-fanout-separation`, and
`thm:window-abelian-polydata`.
The omitted fan-out-one lower bound is attributed in prose to
the revised companion CFG #1 manuscript, rather than treated as
a new #2 MCFG result.

## 1. Standalone operator-independent fan-out-one lower-bound proposition

```latex
\begin{proposition}[No original-thickness bound at fan-out one]
\label{prop:fanout-one-lower-bound}
There exist a fixed two-element semilattice typing $h_{\mathrm U}$
and reduced good fan-out-one, rule-rank-two grammars $G_n$
with $\|G_n\|=O(n)$ and $\theta_{G_n}\le4n$
whose languages $L_n$ belong to $\Cmcf{1}{h_{\mathrm U}}$,
with the following property: for every set-driven operator
$\mathcal O$ having characteristic samples for all targets in
$\Cmcf{1}{h_{\mathrm U}}\cap\mathsf{MCFL}(1,2)$,
each characteristic sample for $L_n$ contains a word of
length $3\cdot2^n-2$. In particular, its total encoded
positive length is at least $3\cdot2^n-1$.
This applies to $\mathcal B_{1,h_{\mathrm U}}$ and to
$\mathcal B^{\le r}_{1,h_{\mathrm U}}$ for fixed $r\ge2$.
\end{proposition}

\begin{proof}
Use the bracketed-doubling family of the companion CFG manuscript
\cite[Proposition~6.3 and Appendix~C]{kuriyamaCFG}.
Let
$\Gamma=\{\mathtt a,\lfloor,\rfloor,\lceil,\rceil\}$ and
$U_1=\{1,\zeta\}$ with $\zeta^2=\zeta$.
Define $h_{\mathrm U}:\Gamma^*\to U_1$ by
sending $\lceil,\rceil$ to $\zeta$ and the other letters to $1$.
For $n\ge1$ take
\[
 \begin{aligned}
 S&\to E_n,& E_0&\to\mathtt a,\\
 E_i&\to\lfloor{}E_{i-1}E_{i-1}\rfloor
       \mid\lceil{}E_{i-1}\rceil
       &&(1\le i\le n).
 \end{aligned}
\]
This is a reduced good fan-out-one grammar of rank two and
size $O(n)$. Put $u_j=\lceil^j\mathtt a\rceil^j$.
Every unary rule occurs in a successful derivation of
$u_n$, of length $2n+1$; the binary rule at $E_i$ occurs
in the word
$\lceil^{n-i}\lfloor{}u_{i-1}u_{i-1}\rfloor\rceil^{n-i}$,
of length $2n+2i\le4n$. Hence $\theta_{G_n}\le4n$.

By Proposition~\ref{prop:app-bracketed-substitutable},
$L_n:=L(G_n)$ is Clark--Eyraud substitutable,
hence is in $\Cmcf{1}{h_{\mathrm U}}$.
The only word of $L_n$ with $h_{\mathrm U}$-value $1$
is the completely binary expansion $w_n^\ast$,
and $|w_n^\ast|=3\cdot2^n-2$.
Put $L_n^-:=L_n\setminus\{w_n^\ast\}
=L_n\cap h_{\mathrm U}^{-1}(\{\zeta\})$.
The regular fiber $h_{\mathrm U}^{-1}(\{\zeta\})$
is $(1,h_{\mathrm U})$-substitutable; the
intersection closure in
Proposition~\ref{prop:abelian-coset-filter}(i)
therefore gives $L_n^-\in\Cmcf{1}{h_{\mathrm U}}$.
Moreover $L_n^-$ is finite, so it has a
rank-at-most-two CFG presentation and lies in
$\mathsf{MCFL}(1,2)$.

Let $K^\ast$ be a characteristic sample of $L_n$
for $\mathcal O$ and $K^-$ one of $L_n^-$.
If $w_n^\ast\notin K^\ast$, then
\[
 K^\ast\subseteq K^\ast\cup K^-\subseteq
 L_n^-\subsetneq L_n .
\]
Since $\mathcal O$ is set-driven, the characteristic
property applied to the same finite sample
$K^\ast\cup K^-$ forces its hypothesis language
to equal both $L_n$ and $L_n^-$, a contradiction.
Thus $w_n^\ast\in K^\ast$ and
$\|K^\ast\|_+\ge|w_n^\ast|+1$.
\end{proof}

For $n\ge2$, $L_n^-$ is not substitutable under trivial
typing; the semilattice typing is what admits the second
language of the distinguishing pair. Consequently,
this lower bound does not contradict Yoshinaka's
polynomial data bound for untyped
substitutability~\cite[Lemma~7]{Yoshinaka2011}.

This fan-out-one obstruction is the
distinguishing-pair result of the companion CFG paper,
expressed using the current MCFG learning model.
It is not a claim of a new intrinsic lower bound for
higher fan-out. Proposition~\ref{prop:typed-thickness-exponential}
instead concerns the cost of \emph{full refinement}
for an easy language and must not be confused with
this operator-independent phenomenon.
```

## 2. Nonboundary DFA-ranked rank-one separator

```latex
\subsection{Strictness and Typings beyond Prefix--Suffix Windows}
\label{subsec:comparison-separations}

The prefix--suffix typings do not exhaust the finite-typing framework.
Let $\Sigma_Q:=\{\mathtt 0,\mathtt 1,\mathtt\#,\mathtt a,\mathtt b\}$ and
\[
  Q:=\{w\mathtt\#\mathtt a^i\mathtt b^j:w\in\{\mathtt 0,\mathtt 1\}^*,\ i,j\ge0,\ \text{$w$ contains $\mathtt{11}$}\}.
\]
Fix a complete DFA for $Q$, let $h_Q:\Sigma_Q^*\to M_Q$ be its transition
morphism, and let $\mathsf{Acc}_Q\subseteq M_Q$ satisfy $Q=h_Q^{-1}(\mathsf{Acc}_Q)$.

\begin{proposition}[A non-boundary typing beyond every prefix--suffix window]
\label{prop:nonboundary-rankone-separator}
For every $s\ge1$, let
\[
 J_s:=\{w\mathtt\#\mathtt a^{sn}\mathtt b^n:
       w\in\{\mathtt 0,\mathtt 1\}^n,
       \text{$w$ contains $\mathtt{11}$}\}.
\]
Then $J_s$ is a non-context-free fan-out-two rank-one language satisfying
\[
  J_s\in\Cmcf{2}{h_Q},
  \qquad
  J_s\notin\Cmcf{2}{h_{\Sigma_Q}^{k,\ell}}
  \quad\text{for every }k,\ell\ge0.
\]
\end{proposition}

\begin{proof}
A fan-out-two rank-one grammar is
\[
\begin{aligned}
 A&\to(\mathtt{11},\mathtt a^{2s}\mathtt b^2),\\
 A&\to(\mathtt 0\xi_1^1,\mathtt a^s\xi_1^2\mathtt b)(A)
   \mid(\mathtt 1\xi_1^1,\mathtt a^s\xi_1^2\mathtt b)(A),\\
 A&\to(\xi_1^1\mathtt 0,\mathtt a^s\xi_1^2\mathtt b)(A)
   \mid(\xi_1^1\mathtt 1,\mathtt a^s\xi_1^2\mathtt b)(A),\\
 S&\to(\xi_1^1\mathtt\#\xi_1^2)(A).
\end{aligned}
\]
It generates $J_s$.  Intersecting with
$\mathtt 1^*\mathtt\#\mathtt a^*\mathtt b^*$ gives
$\{\mathtt 1^n\mathtt\#\mathtt a^{sn}\mathtt b^n:n\ge2\}$, which is
not context-free: otherwise the indicated block homomorphism, inverse image,
and regular intersection would yield
$\{\mathtt x^n\mathtt\#\mathtt y^n\mathtt z^n:n\ge2\}$.

Moreover $J_s=Q\cap\varphi_s^{-1}(0,0)$ for the abelian map
$\varphi_s(\mathtt 0)=\varphi_s(\mathtt 1)=(-s,-1)$,
$\varphi_s(\mathtt a)=(1,0)$, $\varphi_s(\mathtt b)=(0,1)$, and
$\varphi_s(\mathtt\#)=(0,0)$, so
Proposition~\ref{prop:abelian-coset-filter} gives
$J_s\in\Cmcf{2}{h_Q}$.

Fix $k,\ell\ge0$, put $n_0:=k+\ell+4$, and take
$x=\mathtt 0^k\mathtt{0110}\mathtt 0^\ell$ and
$y=\mathtt 0^k\mathtt{0100}\mathtt 0^\ell$.  With
\[
 E=\mathtt{11}\blank_1\mathtt\#\mathtt a^{s(n_0+2)}\mathtt b^{n_0+2},
 \qquad F=\blank_1\mathtt\#\mathtt a^{sn_0}\mathtt b^{n_0},
\]
the factors $x,y$ have the same $h_{\Sigma_Q}^{k,\ell}$-type and
$E[x],E[y],F[x]\in J_s$, whereas $F[y]\notin J_s$.  Thus the
$(2,h_{\Sigma_Q}^{k,\ell})$ condition already fails at arity one.
\end{proof}

Thus the arbitrary-$h$ rank-one theorem reaches beyond every fixed
prefix--suffix typing.  Since
$J_s=\varphi_s^{-1}(0,0)\cap h_Q^{-1}(\mathsf{Acc}_Q)$, this witness concerns
non-boundary typing, not regular-filter separation.  We next obtain strictness
at every fan-out with a separator-free witness; Yoshinaka's Example~3 uses
separator-marked equal-block languages instead~\cite[Example~3]{Yoshinaka2011}.
```

## 3. All-fan-out hierarchy witness H_m

```latex
\begin{theorem}[Strictness at every fan-out]
\label{thm:every-fanout-strictness}
For $m\ge2$ let
$\Sigma_m:=\{\mathtt a_1,\ldots,\mathtt a_{2m}\}$ and
\[
  H_m:=\{\mathtt a_1^n\mathtt a_2^n\cdots\mathtt a_{2m}^n:n\ge1\}.
\]
Then $H_m\in\mathsf{MCFL}(m,1)$ but $H_m$ is not an $(m-1)$-MCFL.  Moreover,
for every $f\ge m$,
\[
  H_m\in\Cmcf{f}{h_{\Sigma_m}^{1,1}}
  \setminus\bigl(\YSub{f}\cup\Ffrag{f}{h_{\Sigma_m}^{1,1}}\bigr).
\]
\end{theorem}

The alphabet $\Sigma_m$ varies with $m$; the hierarchy content of the theorem
is that the witness has minimum fan-out exactly $m$.  For strictness at any
single fixed fan-out $f\ge2$, the case $H_2$ already supplies a witness for
every tested fan-out at least two.

\begin{proof}
A good rank-one grammar is
\[
\begin{aligned}
  A&\to(\mathtt a_1,\mathtt a_3,\ldots,\mathtt a_{2m-1}),\\
  A&\to(\mathtt a_1\xi_1^1\mathtt a_2,
        \mathtt a_3\xi_1^2\mathtt a_4,\ldots,
        \mathtt a_{2m-1}\xi_1^m\mathtt a_{2m})(A),\\
  S&\to(\xi_1^1\mathtt a_2\,\xi_1^2\mathtt a_4\cdots
         \xi_1^m\mathtt a_{2m})(A).
\end{aligned}
\]
It derives from $A$ the tuples
$(\mathtt a_1^n\mathtt a_2^{n-1},\ldots,
  \mathtt a_{2m-1}^n\mathtt a_{2m}^{n-1})$ and hence generates $H_m$.
Seki et al.'s Lemma~3.3, applied with their parameter $m-1$,
shows that
$\{\mathtt a_1^n\cdots\mathtt a_{2m-1}^n:n\ge1\}$ is not an
$(m-1)$-MCFL~\cite[Lemma~3.3, p.~202]{SekiEtAl1991}.  Since MCFLs are closed under homomorphism as a consequence of their
substitution closure~\cite[Theorem~3.9, p.~203]{SekiEtAl1991}, erasing
$\mathtt a_{2m}$ proves that $H_m$ is not an $(m-1)$-MCFL.

For membership, put
$Q_m:=\mathtt a_1^*\cdots\mathtt a_{2m}^*\cap\Sigma_m^+$.
This language is strictly $2$-local, and
\[
  H_m=Q_m\cap\varphi_m^{-1}(0),\qquad
  \varphi_m(w):=(|w|_{\mathtt a_i}-|w|_{\mathtt a_{i+1}})_{1\le i<2m}.
\]
Lemma~\ref{lem:sl2-boundary-control} and
Proposition~\ref{prop:abelian-coset-filter}(ii) therefore give
$H_m\in\Cmcf{f}{h_{\Sigma_m}^{1,1}}$ for every $f\ge m$.

It remains to exclude Yoshinaka's substitution implication.  Put
$d:=\lceil m/2\rceil$.  Since $d\le2m-2d\le2d$, choose
$\ell_i\in\{1,2\}$ with $\sum_i\ell_i=2m-2d$, and set
\[
\begin{aligned}
 q_i&:=2+2(i-1)+\sum_{j<i}\ell_j,&
 x_i&:=\mathtt a_{q_i}\cdots\mathtt a_{q_i+\ell_i-1},\\
 v_0&:=\mathtt a_1,&v_d&:=\mathtt a_{2m},&
 v_i&:=\mathtt a_{q_i+\ell_i}\mathtt a_{q_i+\ell_i+1}\quad(1\le i<d).
\end{aligned}
\]
Then $w_1:=\mathtt a_1\cdots\mathtt a_{2m}=v_0x_1v_1\cdots x_dv_d$.
With $E:=v_0\blank_1v_1\cdots\blank_dv_d$, we have $E[\tuple x]=w_1$.

In $w_2:=\mathtt a_1^2\cdots\mathtt a_{2m}^2$, place $v_0,v_d$ at the two
ends and each interior $v_i=\mathtt a_j\mathtt a_{j+1}$ across its block
boundary.  The intervening nonempty segments form $\tuple y$ with
$E[\tuple y]=w_2$ and $y_1$ beginning in $\mathtt a_1$.  Place each $x_i$ in
$w_2$ starting at the last occurrence of its first letter (straddling the
block boundary when $|x_i|=2$); the remaining material defines
$F\in\mathcal E_d$ with $F[\tuple x]=w_2$.  Its fixed prefix ends in the first
$\mathtt a_2$, so $F[\tuple y]$ contains $\mathtt a_2\mathtt a_1$ and is not
in $H_m$.  Hence
\[
 E[\tuple x],E[\tuple y],F[\tuple x]\in H_m,\qquad
 F[\tuple y]\notin H_m,
\]
with $d\le m\le f$, proving $H_m\notin\YSub{f}$.

The same rectangle excludes $\Ffrag{f}{h_{\Sigma_m}^{1,1}}$: all four complete
words have the same first and last symbols and length at least two, hence the
same whole-word boundary type.  The first three would force the fourth into
both $L_0$ and the same filter, a contradiction.
\end{proof}

Consequently, for every $m\ge2$, every $f\ge m$, and every $r\ge1$,
\[
  \YSL{f}{r}\subsetneq
  \Cmcf{f}{h_{\Sigma_m}^{1,1}}\cap\mathsf{MCFL}(f,r).
\]
The witness $H_m$ has minimum fan-out $m$ and rule rank one.
```

## 4. Bounded unknown typing

```latex
\begin{proposition}[Unknown typing with a bounded codomain]
\label{prop:bounded-unknown-typing}
Fix $\Sigma$, $f$, and $m_{\max}\ge1$, and let
$\Cboundedtyping{f}{m_{\max}}$ be the union of $\Cmcf{f}{h}$ over all
homomorphisms $h:\Sigma^*\to M$ with $|M|\le m_{\max}$.  There is one finite
homomorphism $U_{\Sigma,m_{\max}}$ such that
\[
 \Cboundedtyping{f}{m_{\max}}
 \subseteq \Cmcf{f}{U_{\Sigma,m_{\max}}},
\]
so the bounded union is TxtEx-identifiable.  In contrast,
$\Calltyping{f}=\bigcup_h\Cmcf{f}{h}$ is not TxtEx-identifiable from positive
data.
\end{proposition}

\begin{proof}
There are only finitely many monoid structures of size at most $m_{\max}$ and
letter maps from $\Sigma$ into them.  Take the product of all resulting
homomorphisms and restrict it to its image.  Every admissible $h$ factors
through this product, so typing refinement gives the displayed inclusion and
Corollary~\ref{cor:gold-explanatory} gives TxtEx identification.  The product
can be extremely large; no polynomial dependence on $m_{\max}$ is claimed.
Without a codomain bound the union contains every regular language, hence all
finite languages and an infinite language, so Gold's obstruction for a class containing all finite languages together with an
infinite language applies~\cite{Gold1967}.
\end{proof}
```

## 5. Copy-language example

```latex
\begin{remark}[The copy language]
\label{rem:copy}
The standard two-component copying grammar
makes $\mathrm{COPY}=\{ww:w\in\{\mathtt a,\mathtt b\}^+\}$
a $2$-MCFL, but for every finite typing $h$,
already arity-one substitutability fails.
Choose distinct $u,v\in\{\mathtt a,\mathtt b\}^n$
with $h(u)=h(v)$ and $|u|=|v|$ by pigeonhole.
Then $uu,vv$ share the empty context,
while $u\blank_1u$ accepts $uu$ but not $vv$:
otherwise $uvvu\in\mathrm{COPY}$ would give
$uv=vu$ and hence $u=v$.
Thus $\mathrm{COPY}\notin\Cmcf{f}{h}$
for any $f\ge1$.
\end{remark}
```

## 6. Bracketed-doubling proof formerly Appendix B

```latex
% MCFG #2 v70. Standalone appendix section, included from main.tex.
% Adapted from the companion CFG paper, Appendix C.
\section{Substitutability of the bracketed doubling family}
\label{app:bracketed-substitutability}

This appendix supplies the self-contained proof of substitutability
used by Proposition~\ref{prop:fanout-one-lower-bound};
it follows~\cite[Appendix~C]{kuriyamaCFG}.
Write $L_i=L_{G_n}(E_i)$ for the grammar in that proposition. Then
$L_0=\{\mathtt a\}$ and
\[
 L_i=\lceil L_{i-1}\rceil \ \cup\
     \lfloor L_{i-1}L_{i-1}\rfloor
     \qquad (1\le i\le n).
\]
Every word of $L_i$ starts with precisely $i$ opening
brackets followed by $\mathtt a$.

A \emph{stack} is a word over
$\{E_0,\ldots,E_n,\rceil,\rfloor\}$ with top on the left.
Define partial transitions by
\[
\begin{aligned}
 E_0\psi&\xrightarrow{\mathtt a}\psi,&
 E_i\psi&\xrightarrow{\lceil}E_{i-1}\rceil\psi,\\
 E_i\psi&\xrightarrow{\lfloor}E_{i-1}E_{i-1}\rfloor\psi,&
 \rceil\psi&\xrightarrow{\rceil}\psi,\qquad
 \rfloor\psi\xrightarrow{\rfloor}\psi
 \qquad(1\le i\le n),
\end{aligned}
\]
and extend transitions to words. The system is deterministic;
each letter acts as an injective partial map on stacks.
Assign weights $\mathrm{wt}(E_i)=4^i$ and
$\mathrm{wt}(\rceil)=\mathrm{wt}(\rfloor)=1$.
Every transition strictly decreases the total weight.
A run on a nonempty top part $\alpha$ of $\alpha\psi$
therefore reaches $\psi$ at most once and never touches
the suffix $\psi$ before that point.

\begin{lemma}[Stack recognition of doubling blocks]
\label{lem:app-runs}
For $0\le i\le n$, every stack $\psi$ and $w\in\Gamma^*$,
\[
 E_i\psi\xrightarrow{w}\psi
 \quad\Longleftrightarrow\quad w\in L_i.
\]
If $\sigma\xrightarrow{w}\vartheta$ and $w\in L_i$,
then $\sigma=E_i\psi$ and $\vartheta=\psi$
for some stack $\psi$.
\end{lemma}

\begin{proof}
Induct on $i$. For $i=0$ the only possible return
reads $\mathtt a$. At $i\ge1$, the first letter
is $\lceil$ or $\lfloor$ and the resulting
exposed stack is respectively $E_{i-1}\rceil$
or $E_{i-1}E_{i-1}\rfloor$.
To return to $\psi$ one must exhaust the exposed
symbols in order; induction yields respectively
$\lceil z\rceil$ or $\lfloor z_1z_2\rfloor$
with $z,z_1,z_2\in L_{i-1}$. Conversely
every such word gives a returning run.
For the second assertion, the first $i$ opening
brackets of a word in $L_i$, followed by
$\mathtt a$, force the top symbols
$E_i,E_{i-1},\ldots,E_0$ in order;
the first assertion then identifies the
suffix left on the stack.
\end{proof}

\begin{lemma}[Branch synchronization]
\label{lem:app-sync}
If $\sigma\xrightarrow{x}\vartheta$ and
$\sigma\xrightarrow{y}\vartheta$ for nonempty
$x,y$ with different first letters, then
$\sigma=E_i\psi$ for some $i\ge1$, and
\[
 x=zx',\quad y=z'y',\quad z,z'\in L_i,
 \qquad
 \psi\xrightarrow{x'}\vartheta,\quad
 \psi\xrightarrow{y'}\vartheta.
\]
\end{lemma}

\begin{proof}
Only $E_i\psi$ with $i\ge1$ admits distinct
first letters, $\lceil$ and $\lfloor$.
Until the first visit to $\psi$, the
respective stacks have forms
$\alpha\rceil\psi$ and $\beta\rfloor\psi$;
their weights exceed $\mathrm{wt}(\psi)$,
while after such a visit weights are at most
$\mathrm{wt}(\psi)$.
Thus if just one of the two runs visited
$\psi$, their final weights would differ.
If neither visited $\psi$, their final
stacks would still contain incompatible
last exposed closing brackets.
Both runs must therefore visit $\psi$,
and Lemma~\ref{lem:app-runs} identifies the
prefixes read up to that visit.
\end{proof}

\begin{proposition}[Substitutability of the doubling family]
\label{prop:app-bracketed-substitutable}
For each $n\ge1$, if nonempty
$x,y\in\Gamma^+$ share a sentence context
in $L_n$, then
$\D_{L_n}(x)=\D_{L_n}(y)$.
\end{proposition}

\begin{proof}
First prove by induction on $|x|+|y|$
that if $\sigma\xrightarrow{x}\vartheta$
and $\sigma\xrightarrow{y}\vartheta$,
then $\D_{L_n}(x)=\D_{L_n}(y)$.
If one input is empty, strict weight decrease
forces both to be empty. If the first letters
agree, determinism gives the same next stack
and induction applies to the suffixes;
two-sided distributional equivalence is a
congruence, so the common prefix preserves it.
If they differ, Lemma~\ref{lem:app-sync}
writes $x=zx'$ and $y=z'y'$ with
$z,z'\in L_i$ and paths
$\psi\xrightarrow{x'}\vartheta$,
$\psi\xrightarrow{y'}\vartheta$.
Lemma~\ref{lem:app-runs} implies that
$z,z'$ induce identical partial stack
transformations, so
$\D_{L_n}(z)=\D_{L_n}(z')$.
Induction gives
$\D_{L_n}(x')=\D_{L_n}(y')$,
and congruence finishes the step.

Now if $uxv,uyv\in L_n$, determinism
gives a common stack $\sigma$ after $u$
in both accepting runs from $E_n$.
The stacks reached after $x$ and $y$
both read $v$ to the empty stack, hence
coincide by injectivity of the map induced by
$v$. The preceding claim proves the required
distributional equality.
\end{proof}

```
