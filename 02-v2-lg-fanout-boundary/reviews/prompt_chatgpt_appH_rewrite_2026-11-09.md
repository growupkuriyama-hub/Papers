# 査読依頼（ChatGPT 向け）：付録H の書き直し —— 孤立した文字による U₁ 型付けの分類と、指数 (76,21) → (22,8)

（2026-11-09。報告書名：`chatgpt_appH_rewrite_review_2026-11-09.md`（＋必要なら `check_chatgpt_appH_rewrite_2026-11-09.py`）。冒頭に判定表を置くこと。）

## あなたの役割

あなたは理論計算機科学（形式言語、文法推論、有限半群）の査読者です。
下に貼った LaTeX は、論文 #2 の §7 の二段落と付録H の**書き直し**で、Claude の別のセッションが書きました。**新しい数学を含み、まだ独立に検証されていません。**
好意的に読まず、反例を探すつもりで一行ずつ検査してください。分からないことは分からないと書いてください。

あなたは以前、旧版の付録H（二文字の内容型付け c、指数 (76, 21)）を査読し、「軽微な修正で正しい」と判定しました（`reviews/chatgpt_S1_proofnote_review_2026-11-09.md`）。また五観点の査読（`reviews/chatgpt_compress_review_2026-11-09.md`）の G4 で、U₁ 型付けへの一般化を「研究課題」としました。**今回の書き直しはその一般化を主張しています。** 以前の判断に引きずられず、今回の論証そのものを検査してください。

## 背景と文脈

- 原稿の正本：GitHub `growupkuriyama-hub/Papers`、`02-v2-lg-fanout-boundary/main.tex`。
  - 書き直し前は main（commit `76d4a1d`）。
  - 書き直しを適用した版はブランチ `appH-rewrite`。
  - 読めれば、§2（`def:grammar-properties`）、§3（`def:output-refinement`、`lem:typed-homogeneity`）、§4（`cor:distribution-representatives`、`prop:rare-type`）、§7（`prop:three-letter-family`、`cor:typing-level-obstruction`、`prop:binary-u1-quadratic`）、付録I（`lem:app-u1-code`）と突き合わせてください。
- 記号：
  - ≡_{L,s}：同じ型かつ同じ分布。
  - τ：代表元の長さ。型付き非終端の生成語と ≡_{L,s} で同値な語の最短の長さ。特徴標本の長さは系 `cor:distribution-representatives` で N_typ(1 + 2θ̄ + r_max τ) + 1 以下。
  - θ̄：厚さ。各規則を使う最短の成功語の長さの最大。
  - ‖G‖：文法の大きさ。
- 旧版からの主な変更：
  - **仮定**：Σ = {a,b} の内容型付け c → 「孤立した文字」（Def. `def:isolated-letter`。s⁻¹(s(a)) = a⁺ で、a を含み a⁺ にない語が全て同じ型）。c の二文字と、型1の文字が一つの U₁ 型付け（任意の Σ）を含む。
  - **定理の対象**：全ての型 → 型 s(a) だけ。他の型は補題 `lem:app-h-other`。
  - **数え上げの最後**：C(M+1,j) ≥ 3^{M/3−1} → (27/4)^{⌊M/3⌋} ≤ (M+1)²·（記録の数）（二項分布の最大項）。
  - **選択**：「現在の値の2倍を初めて超える」→「これまでの和を初めて超える」（補題 `lem:app-h-select`）。
  - **埋め草**：商 ≤ 2+4K² → ≤ 3（補題 `lem:app-h-filler`。v_i > d を使う）。
  - **新しい系**：`cor:u1-classification`（ファンアウト1で、U₁ への型付けが多項式データを持つ ⟺ 型1の文字がちょうど一つ）。
  - **記号**：K → k_V、λ → ℓ_z。

## 依頼

**課題1（最優先）.** 下の LaTeX の全ての定義・補題・定理・系とその証明を検査し、判定表に「正しい／修正が要る（どこを、どう直すか）／誤り（反例）」で答えてください。書き手自身が挙げた**危ない箇所**（上から順に）：

1. 補題 `lem:app-h-filler` の q_i ≤ 3。全ての i₀ ≤ i ≤ i\* で v_i > d が必要。根拠は「X_i は X_{i\*} の祖先で、X_{i\*} の産出は二つの種を含むので n_{X_i} ≥ d + n_Y」。k_V の次数が 15 → 11 に下がったのはこの一点による。
2. 孤立の仮定 (I1)(I2) の使用箇所が全て正当か。
   - 補題 `lem:app-h-base`：W₁, W₂, W₃ と、消去の後に比べる全ての語が a 混合であること。とくに ωa^{g₀}ω、悪い場合の ωωa と aωω。
   - 補題 `lem:app-h-borrow`：aω_{X_i} と aΩ_i。
   - 補題 `lem:app-h-period`(i)(ii)：a^f z₀。(iii)：a と a^{1+p₀}。
   - 系の (ii)：型1の型付き非終端が「a⁺ の生成語を持つ A」だけであること。
   - **ChatGPT G4 の懸念**（三文字目の文字の文脈が新しい情報を持つ）が、この証明のどこかで実際に問題になるか。
3. 補題 `lem:app-h-select`：「j_t より下（添字が小さい）で v_i > S_t となる最大の i」について v_{i+1} ≤ S_t（i+1 = j_t の場合を含む）。(★) の適用範囲 i < i\*。形式的な値 v_i := n（i < i₀）との整合。
4. 補題 `lem:app-h-count` の最後：j ∈ [⌊M/3⌋, ⌊2M/3⌋] の導出、単峰性による C(M+1,j) ≥ C(M+1,k) ≥ C(3k,k)、比 t_{i+1}/t_i = (3k−i)/(2i+2)、t_k ≥ 1/(3k+1)。
5. 二分化の数え方：k_V ≤ ‖G‖ + σ_G ≤ 2‖G‖、|P′| ≤ ‖G‖ + σ_G。原稿の ‖G‖ の定義と照合すること。系の N_typ（c で ≤ 12(‖G‖+2)、U₁ で ≤ 2k_V + 4|P′| ≤ 12‖G‖）。
6. 指数の計算：
   - μ^{M−2} ≤ (27/4)^{⌊M/3⌋}。
   - 3k_V + M + 4 ≤ 5k_V(M+1)。
   - 15625 = 625·25 の出どころ。
   - C_η < e³⁴、80γ/79 < 1.7479、C₀ < 10³⁶、C < 10⁴³、C′ < 10⁴⁵。
7. 補題 `lem:app-h-other`(i)：道の上のラベルの縮約が印の葉を保つこと。ぶら下がる部分木が ≤ k_V − 1 個であること。
8. 命題 `prop:binary-u1-quadratic` の後の注意（型1の文字が一つの任意の U₁ 型付けへの拡張）：{a,b} 以外の文字を含む語の分布が空なので、C₁ と下界がそのまま成り立つか。
9. 三文字以上の c_Σ についての注意：L_n ∈ C_{1,c_Σ} の根拠（命題 `prop:three-letter-family`(ii)）、W_n が内容 {a,b} の唯一の語であること、破れる箇所の説明。
10. 系 `cor:u1-classification` の「⟸ でない向き」：型1の文字が二つ以上なら、系 `cor:typing-level-obstruction` の仮定（e = 1, z = ζ が相異なる冪等元で ez = ze = z、u, v, w が文字が互いに素）が満たされること。

**課題2.** 小さな例での検査（補助）。例えば次のもの。
- 正則な C_{1,s} 言語（s は孤立した文字をもつ型付け）で補題 `lem:app-h-base`・`lem:app-h-period` を検査する。
- ランダムな値の列で `lem:app-h-select`・`lem:app-h-filler` を検査する。
- 指数の数値を確かめる。
- スクリプトは標準ライブラリだけで書き、実行方法と所要時間を記してください。計算は証明の代わりにしないでください。

**課題3.** 結論への疑い。
- 型1の文字が一つの U₁ 型付けで τ が超多項式になる候補を思いつけば、証明のどの段で破れるはずかを示してください。
- 逆に、孤立の仮定 (I2) を外したときに何が起きるかの見通しがあれば書いてください（任意）。

## 報告の形式

- 判定表（定義・補題・定理・系ごと）。
- 誤り・修正点は、該当するラベルと、直した主張を添えて。
- 全体の判定：「正しい」「軽微な修正で正しい」「重大な穴がある（どこ）」。
- 原稿に入れる前に直すべき書き方の点（任意）。

---

## 検査対象（1）：§7 の二段落（差し替え後）

```latex
\paragraph{Individual typings onto $U_1$.}"
%%       up to (not including) the line "Table~\ref{tab:scope} collects, ..." by PART (a);
%%   (b) replace main.tex from "\section{Two Letters at Fan-Out One}" up to (not including)
%%       "\section{Typings onto \texorpdfstring{$U_1$}{U1} at Fan-Out One}" by PART (b);
%%   (c) apply the old/new pairs of PART (c); each OLD text occurs exactly once in main.tex.
%%
%% Numbering after the change: Definition 7.9 (isolated letter), Theorem 7.10
%% (thm:two-letter-fanout-one), Corollary 7.11 (cor:two-letter-fanout-one),
%% Corollary 7.12 (cor:u1-classification, new).  Labels thm:two-letter-fanout-one and
%% cor:two-letter-fanout-one are kept, so all existing \ref's still resolve.
%% Appendix H labels: lem:app-tl-* / eq:app-tl-* are renamed lem:app-h-* / eq:app-h-*;
%% they were referenced only inside Appendix H.

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%% PART (a): Section 7, paragraphs "Individual typings onto U_1" and
%%%%           "Isolated letters and two letters" (replaces "Two letters")
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\paragraph{Individual typings onto $U_1$.}
Theorem~\ref{thm:fanout-one-data} concerns pseudovarieties.  For an
individual typing at fan-out one, what matters is which words realize a copy
$\{e,z\}$ of $U_1$: letter-disjoint words of type $e$ force exponential data,
while an isolated letter (Definition~\ref{def:isolated-letter}), whose type is
realized only by its own powers, gives polynomial data
(Theorem~\ref{thm:two-letter-fanout-one} below).  For typings onto $U_1$
these two cases are exhaustive (Corollary~\ref{cor:u1-classification}).

\begin{corollary}[A typing-level obstruction at fan-out one]
\label{cor:typing-level-obstruction}
Let $r_{\max}\ge2$ and let $s:\Sigma^+\twoheadrightarrow\mathsf S$ be a typing.
Suppose that distinct idempotents $e,z\in\mathsf S$ satisfy $ez=ze=z$, and that
words $u,v,w\in\Sigma^+$ satisfy $s(u)=s(v)=e$ and $s(w)=z$ and are
\emph{letter-disjoint}: no letter occurs twice in $uvw$.  Let $H_n$ be the image
of the language $L_n$ of Proposition~\ref{prop:three-letter-family}, over three
fresh letters, under $\mathtt a\mapsto u$, $\mathtt b\mapsto v$, $\mathtt c\mapsto w$,
and let $G''_n$ be the image of $G_n$, with rules $S\to E_n$, $E_0\to u$ and
$E_i\to vE_{i-1}E_{i-1}v\mid wE_{i-1}w$.  Then $H_n\in\Cmcf{1}{s}$, $G''_n$ is a
reduced good rank-two presentation of $H_n$ with
\[
 \|G''_n\|=(2|v|+2|w|+9)n+|u|+6,\qquad
 \bar\theta_{G''_n}\le2|u|+2|v|+4n|w|,
\]
and every characteristic sample of $H_n$ for $\mathcal B^{\le r_{\max}}_{1,s}$,
for $\mathcal B_{1,s}$, or for any set-driven operator having characteristic
samples throughout $\Cmcf{1}{s}$ has total encoded length greater than
$(|u|+2|v|)2^n-2|v|$.  So for this single typing no polynomial bounds the
characteristic-data length at fan-out one and rank $r_{\max}$ as in
Definition~\ref{def:uniform-polydata}.
\end{corollary}

\begin{proof}
$L_n$ is finite and Clark--Eyraud substitutable
(Proposition~\ref{prop:three-letter-family}), so $H_n$ is Clark--Eyraud
substitutable by Lemma~\ref{lem:app-u1-code}; it is finite, hence
$H_n\in\Cmcf{1}{s}$.  The grammar is good, and reduced since
$E_i\Rightarrow^*w^iuw^i$.  The size follows from
Definition~\ref{def:standard-mcfg}: the start rule has size $3$, the base rule
$1+|u|$, and the two rules of each level $2|v|+5$ and $2|w|+3$.  Completing every
other choice by the rules $E_j\to wE_{j-1}w$ shows that each rule has a
successful use of length at most $|u|+2n|w|$ (start and unary rules) or
$2|u|+2|v|+(2n+2i-4)|w|$ (the binary rule of level $i$).  In $\{e,z\}$, $e$ is an
identity and $z$ is absorbing, so a word of $H_n$ has type $e$ iff it is the
image of a word of $L_n$ without $\mathtt c$, that is, of $W_n$.  The image $h(W_n)$ has length
$(|u|+2|v|)2^n-2|v|$ by $|h(W_i)|=2|h(W_{i-1})|+2|v|$, and
Proposition~\ref{prop:rare-type} forces it into every such sample.
\end{proof}

With $u,v,w$ letters this is the case of two letters of type $e$; in
particular it applies to every typing onto $U_1$ with at least two letters of
type $1$, since surjectivity gives a letter of type $\zeta$.  It also applies
when no letter has type $e$: for $\mathsf S=\{1,g,z\}$ with identity $1$,
$g^2=1$ and zero $z$, and the typing $\mathtt a,\mathtt b,\mathtt c,\mathtt d\mapsto g$,
$\mathtt t\mapsto z$, take $u=\mathtt{ab}$, $v=\mathtt{cd}$, $w=\mathtt t$ and
$e=1$.  Whether two non-commuting words of type $e$ always suffice, without
letter-disjointness, is open in general; since two words commute iff they are
powers of one word, their absence means that all words of type $e$ are powers of
one primitive word.  For typings onto $U_1$ the question does not arise: with
two letters of type $1$ the corollary applies, and with one, $\mathtt a$ say, the
words of type $1$ are the powers of $\mathtt a$ and the data are polynomial
(Corollary~\ref{cor:u1-classification}).

Let $\Sigma=\{\mathtt a,\mathtt b\}$ and let $s_{U,2}:\Sigma^+\twoheadrightarrow U_1$ send $\mathtt a$ to
$1$ and $\mathtt b$ to $\zeta$ (the binary typing).  For this typing, with a single letter of type $1$,
Corollary~\ref{cor:typing-level-obstruction} does not apply; still, its data can
be quadratic in $\bar\theta_G$ for presentations of logarithmic size.

\begin{proposition}[Quadratic data for the binary typing at fan-out one]
\label{prop:binary-u1-quadratic}
For $m,n\ge1$ let $L_{m,n}\subseteq\{\mathtt a,\mathtt b\}^+$ be the set of all
concatenations of $2^n$ words from $\{\mathtt a^{2^m},\mathtt b\}$.
\begin{enumerate}[label=\textup{(\roman*)},leftmargin=*]
\item $L_{m,n}\in\Cmcf{1}{s_{U,2}}$.
\item $L_{m,n}$ has a reduced good fan-out-one presentation $G_{m,n}$ of rule rank
two with $\|G_{m,n}\|=6m+6n+9$ and $\bar\theta_{G_{m,n}}=2^m+2^n-1$.
\item For $\mathcal B_{1,s_{U,2}}$, for $\mathcal B^{\le r}_{1,s_{U,2}}$ \textup($r\ge1$\textup),
and for every set-driven operator with characteristic samples throughout
$\Cmcf{1}{s_{U,2}}$, every characteristic sample $F$ of $L_{m,n}$ has
$\|F\|_+>2^{m+n}$.
\end{enumerate}
Consequently, for $m=n$ one has $\|G_{n,n}\|=12n+9$, $\bar\theta_{G_{n,n}}=2^{n+1}-1$
and $\|F\|_+>\bar\theta_{G_{n,n}}^{\,2}/4$; in particular, for this typing at
fan-out one there is no bound of the form $p(\|G\|)\,\bar\theta_G$ with $p$ a
polynomial, in contrast with Theorem~\ref{thm:local-group-polydata}.
\end{proposition}

The proof is in Appendix~\ref{app:u1-typings}.  The pure word
$\mathtt a^{2^{m+n}}$ is the product of the block length and the number of
blocks, while $\bar\theta_G$ is about their sum, since a shortest sentence using
the long block fills every other position with $\mathtt b$.  Words containing a
letter other than $\mathtt a$ and $\mathtt b$ have empty distribution in
$L_{m,n}$, so the proposition holds verbatim for every typing onto $U_1$ in
which $\mathtt a$ is the only letter of type $1$ and $\mathtt b$ has type $\zeta$.
The data for these typings at fan-out one are nevertheless polynomial
(Corollary~\ref{cor:two-letter-fanout-one} below), and for $s_{U,2}$ so they are
at every fan-out $f\ge2$ (Corollary~\ref{cor:two-letter-semilattice}).

\paragraph{Isolated letters and two letters.}
The family of Theorem~\ref{thm:fanout-one-data}(iii) uses three letters, two of
them of type $1$.  A letter whose type is realized only by its own powers
already yields polynomial data, over any alphabet.

\begin{definition}[Isolated letter]
\label{def:isolated-letter}
A letter $\mathtt a\in\Sigma$ is \emph{isolated} for a typing $s$ if
$s^{-1}(s(\mathtt a))=\mathtt a^+$ and all words that contain $\mathtt a$ but do
not lie in $\mathtt a^+$ have one common type.
\end{definition}

For instance, let $\Sigma=\{\mathtt a,\mathtt b\}$ and let $c$ be the
\emph{content typing}, $c(w)$ the set of letters of $w$, onto the
three-element semilattice $\{\{\mathtt a\},\{\mathtt b\},\Sigma\}$ under union;
both letters are isolated for $c$, since a word that contains $\mathtt a$ and
lies outside $\mathtt a^+$ has content $\Sigma$.  If $s:\Sigma^+\twoheadrightarrow
U_1$ and $\mathtt a$ is the only letter of type $1$, then $s^{-1}(1)=\mathtt a^+$
and all other words have type $\zeta$, so $\mathtt a$ is isolated, over any
alphabet.  Over three or more letters no letter is isolated for the content
typing, since $\mathtt{ab}$ and $\mathtt{ac}$ have different contents.

\begin{theorem}[Isolated letters: short pure representatives at fan-out one]
\label{thm:two-letter-fanout-one}
Let $\mathtt a$ be isolated for a typing $s:\Sigma^+\twoheadrightarrow\mathsf S$,
let $L\in\Cmcf{1}{s}$, and let $G$ be a reduced good presentation of
$L\cap\Sigma^+$ of fan-out one and any rank.  For every nonterminal $A$ of $G$,
or of its binarization $G'$ \textup(Appendix~\ref{app:two-letter-fanout-one}\textup),
that has a yield in $\mathtt a^+$, the typed nonterminal $A_{s(\mathtt a)}$
satisfies
\[
 \tau_{A_{s(\mathtt a)}}\le C(\|G\|+2)^{22}\bar\theta_G^{\,8},
\]
where $C<10^{43}$ is an absolute constant, independent of $\Sigma$, $s$ and the
rank.  In particular, if $L$ contains a word of $\mathtt a^+$, its shortest one
has length at most $C(\|G\|+2)^{22}\bar\theta_G^{\,8}$.
\end{theorem}

\begin{corollary}[Polynomial data from isolated letters]
\label{cor:two-letter-fanout-one}
Let $r_{\max}\ge2$ and let $s$ be
\begin{enumerate}[label=\textup{(\roman*)},leftmargin=*]
\item a typing over $\Sigma=\{\mathtt a,\mathtt b\}$ whose positive image is a
semilattice \textup(for instance $c$ or $s_{U,2}$\textup), or
\item a typing $s:\Sigma^+\twoheadrightarrow U_1$, over any finite alphabet,
in which exactly one letter has type $1$.
\end{enumerate}
Every $L\in\Cmcf{1}{s}$ with a reduced good fan-out-one presentation $G$ of
$L\cap\Sigma^+$, of any rank, has a common characteristic sample $K$ for
$\mathcal B^{\le r_{\max}}_{1,s}$ and $\mathcal B_{1,s}$ with
\[
 \|K\|_+\le C'r_{\max}(\|G\|+2)^{23}\bar\theta_G^{\,8}+\mathbf 1_{\{\eps\in L\}},
\]
where $C'<10^{45}$ is an absolute constant.
\end{corollary}

\begin{corollary}[Typings onto $U_1$ at fan-out one]
\label{cor:u1-classification}
Let $r_{\max}\ge2$ and let $s:\Sigma^+\twoheadrightarrow U_1$ be a typing.  Then
the bound required of each typing in Definition~\ref{def:uniform-polydata}
holds for $s$ at fan-out one and rank $r_{\max}$ if and only if exactly one
letter has type $1$.  More precisely:
\begin{enumerate}[label=\textup{(\roman*)},leftmargin=*]
\item if exactly one letter has type $1$, the data are bounded as in
Corollary~\ref{cor:two-letter-fanout-one}, for presentations of every rank, and
by Proposition~\ref{prop:binary-u1-quadratic} not by any $p(\|G\|)\bar\theta_G$
with $p$ a polynomial;
\item if at least two letters have type $1$, the targets of
Corollary~\ref{cor:typing-level-obstruction} need data exponential in the size
and the thickness of their reduced good rank-two presentations.
\end{enumerate}
\end{corollary}

\begin{proof}
Since $s$ is onto and $U_1$ is generated by the types of the letters, some letter
has type $1$ and some letter has type $\zeta$.  (i) is
Corollary~\ref{cor:two-letter-fanout-one}(ii) together with
Proposition~\ref{prop:binary-u1-quadratic} and the remark following it, applied
with $\mathtt b$ a letter of type $\zeta$.  For (ii) let $\mathtt a\ne\mathtt b$ have
type $1$ and $\mathtt c$ type $\zeta$; the idempotents $e:=1$ and $z:=\zeta$ are
distinct with $ez=ze=z$, and $u:=\mathtt a$, $v:=\mathtt b$, $w:=\mathtt c$ are
letter-disjoint with $s(u)=s(v)=e$ and $s(w)=z$, so
Corollary~\ref{cor:typing-level-obstruction} applies.
\end{proof}

The proofs of Theorem~\ref{thm:two-letter-fanout-one} and
Corollary~\ref{cor:two-letter-fanout-one} are in
Appendix~\ref{app:two-letter-fanout-one}.  The idea is as follows.  Take a
node-minimal derivation $T$ of a shortest yield $\mathtt a^n$ of a nonterminal.
Two occurrences of one label at distance $d$ give, by cancellation of pure
blocks, a base $z_0$ outside $\mathtt a^+$ that commutes with $\mathtt a^d$ and
satisfies $z_0z_0\sim\mathtt a^{c_0}z_0$.  Short yields outside $\mathtt a^+$ of the
labels on the heavy path of $T$, padded by at most $d$ letters on each side,
collapse to $\mathtt a^ez_0$; isolation is used exactly here, since it makes all
words that contain $\mathtt a$ and lie outside $\mathtt a^+$ comparable.  The
set of exponents $f$ with $\mathtt a^fz_0$ in a given distribution class is a
residue class modulo some $p_0$; if $p_0$ exists, then $\mathtt a\sim\mathtt
a^{1+p_0}$, so pure words have short equivalent representatives.  Otherwise,
membership is decided by the values of the codes.  Each code is chosen to exceed
the sum of the previous ones, which costs a factor of at most $3$ per code, and
the permutations of these codes are counted against the size of the grammar,
as for the doubling families.

Corollary~\ref{cor:two-letter-fanout-one} does not contradict
Theorem~\ref{thm:fanout-one-data}(i), whose quantification is over all
alphabets: the semilattices form a pseudovariety not contained in
$\mathbf{LG}$, and the failure occurs over three letters.  Since the positive
image of every two-letter typing onto a semilattice is a quotient of the image
of $c$, part~(i) of the corollary covers all of them.  Over three or more
letters the failure of isolation for the content typing $c_\Sigma$ is
necessary: $L_n\in\Cmcf{1}{c_\Sigma}$ for $\Sigma\supseteq\{\mathtt a,\mathtt b,\mathtt
c\}$ by Proposition~\ref{prop:three-letter-family}(ii), and $W_n$ is its only word
of content $\{\mathtt a,\mathtt b\}$, so Proposition~\ref{prop:rare-type} forces data
of length at least $3\cdot2^n-1$.  In the proof the failure occurs when the codes
are collapsed: a short yield of content $\{\mathtt a,\mathtt c\}$ and a yield of
content $\{\mathtt a,\mathtt b\}$ of one nonterminal need not be equivalent.
Thus, at fan-out one, a typing onto $U_1$ has polynomial data if and only if
exactly one letter has type $1$ (Corollary~\ref{cor:u1-classification}); the data
are then polynomial but not of the form $p(\|G\|)\,\bar\theta_G$
(Proposition~\ref{prop:binary-u1-quadratic}).

```

## 検査対象（2）：付録H 全体（差し替え後）

```latex
\section{Isolated Letters at Fan-Out One}
\label{app:two-letter-fanout-one}

This appendix proves Theorem~\ref{thm:two-letter-fanout-one} and
Corollary~\ref{cor:two-letter-fanout-one}.  Throughout,
$s:\Sigma^+\twoheadrightarrow\mathsf S$ is a typing, $\mathtt a\in\Sigma$ is isolated
for $s$ (Definition~\ref{def:isolated-letter}), and $L\in\Cmcf{1}{s}$; we may
assume $\eps\notin L$.  A word of $\Sigma^+$ is \emph{pure} if it lies in
$\mathtt a^+$, \emph{$\mathtt a$-free} if it does not contain $\mathtt a$, and
\emph{$\mathtt a$-mixed} otherwise, that is, if it contains $\mathtt a$ and another
letter.  Isolation is used only through two facts:
\begin{enumerate}[label=\textup{(I\arabic*)},leftmargin=*]
\item all pure words have the type $s(\mathtt a)$, and the words of this type are
the pure words;
\item all $\mathtt a$-mixed words have one type.
\end{enumerate}
For $x\in\Sigma^+$ write $\D(x):=\D^{(1)}_L(x)$ and $x\sim y$ if
$\D(x)=\D(y)$; this is a congruence on $\Sigma^+$, and words with empty
distribution are $\sim$-equivalent.  Thus $x\equiv_{L,s}y$ if and only if
$x\sim y$ and $s(x)=s(y)$.

\subsection{Preliminaries}

\begin{lemma}[Cancellation]
\label{lem:app-h-cancel}
Let $x,y\in\Sigma^+$ have the same type, $z\in\Sigma^+$, $\D(zx)\ne\emptyset$
and $zx\sim zy$.  Then $x\sim y$.  The same holds on the right.
\end{lemma}

\begin{proof}
For $(l,r)\in\D(zx)$ we get $lzyr\in L$, so $x$ and $y$ share the context
$(lz,r)$.
\end{proof}

We apply the lemma only to pure $x,y$ or to $\mathtt a$-mixed $x,y$, which have
the same type by (I1), respectively (I2).  If a nonterminal $X$ has a
derivational context $(l,r)$, two yields of $X$ of the same type share $(l,r)$
and are $\sim$-equivalent (Lemma~\ref{lem:typed-homogeneity}).  For a type $t$
realized by $X$ we write $\tau(X,t)$ for the representative length of the typed
nonterminal $X_t$, the least length of a word of type $t$ that is
$\sim$-equivalent to the yields of $X$ of type $t$.

\paragraph{Binarization.}
Let $G$ be a reduced good presentation of $L$ of fan-out one, and let
$\sigma_G$ be the number of letters occurring in its rules, so
$\sigma_G\le\min\{|\Sigma|,\|G\|\}$.  Replace every rule $X\to Y_1\cdots Y_t$
with $t\ge3$ by a right-linear chain through fresh nonterminals, replace
terminals occurring in right sides of length at least two by preterminals
$T_{\mathtt x}\to\mathtt x$ (only for the letters $\mathtt x$ that are used), and trim.
The resulting grammar $G'$ is reduced and good, has rules of the forms
$X\to YZ$, $X\to Y$ and $X\to\mathtt x$ with $\mathtt x\in\Sigma$, and generates $L$.
A rule $X\to\gamma$ of $G$ gives at most $\max\{0,|\gamma|-2\}$ fresh
nonterminals and at most $\max\{1,|\gamma|-1\}$ rules, both at most the size
$1+r+|\gamma|$ of the rule in $\|G\|$, so
\[
 k_V:=|V'|\le\|G\|+\sigma_G\le2\|G\|,\qquad |P'|\le\|G\|+\sigma_G,
\]
and $k_V\le\|G\|+2$, $|P'|\le\|G\|+2$ if $|\Sigma|=2$.  Moreover
$\theta:=\bar\theta_{G'}\le\bar\theta_G$, since a derivation using a new rule
corresponds to one using the rule of $G$ it comes from.  Every nonterminal of
$G'$ has a yield of length $\le\theta$ and a derivational context $(l,r)$ with
$|l|+|r|\le\theta$: take a shortest sentence through a rule with that
nonterminal on the left, respectively on the right.  The nonterminals of $G$
are nonterminals of $G'$ with the same yields.

\subsection{The Tree and the Base}

Fix a nonterminal $A$ of $G'$ with a pure yield; let $\mathtt a^n$ be the
shortest one, $T$ a derivation tree of $\mathtt a^n$ from $A$ with the least
number of nodes, and $(l,r)$ a derivational context of $A$ with
$|l|+|r|\le\theta$.  Replacing subtrees of $T$ by derivations from the same
labels gives yields $w$ of $A$, hence $lwr\in L$.  A node is \emph{heavy} if
its yield is longer than $\theta$, and a heavy node without heavy children is a
\emph{seed}.

\begin{lemma}
\label{lem:app-h-tree}
\begin{enumerate}[label=\textup{(\alph*)},leftmargin=*]
\item No label repeats on a root-to-leaf path of $T$; such a path has at
most $k_V$ nonterminal nodes.
\item All nodes of $T$ with the same label $Y$ have the same yield
$\mathtt a^{n_Y}$.
\item Every label $Y$ of a heavy node has a yield $\omega_Y\notin\mathtt a^+$ of
length $\le\theta$.
\item Seeds have yields of length $\le2\theta$; seeds are pairwise disjoint;
a subtree containing $k$ seeds has a yield of length $\le k(k_V+2)\theta$; and
the left ends of two consecutive seeds differ by at most $2k_V\theta$.
\end{enumerate}
\end{lemma}

\begin{proof}
(a) If an ancestor and a descendant share a label, replacing the ancestor's
subtree by the descendant's gives a shorter pure yield of $A$ or a smaller
tree.  (b) Otherwise replace the longer subtree by the shorter one.  (c) Let
$\rho$ be the rule at a heavy node labelled $Y$.  A sentence of length
$\le\theta$ using $\rho$ contains a yield $y$ of $Y$ with $|y|\le\theta<n_Y$;
if $y\in\mathtt a^+$, inserting it into $T$ gives a shorter pure yield of $A$.
(d) A seed is not a unit node and has two light children.  If a seed $v$ lay
below a seed $u$, the child of $u$ above $v$ would be heavy.  The heavy nodes of
a subtree with $k$ seeds lie on paths to seeds, so there are at most $kk_V$ of
them, each non-seed one with at most one light child.  Between consecutive
seeds $u,v$ lie the yields of the subtrees hanging off the two paths from
their least common ancestor, at most $2(k_V-1)$ of them; each is light, since a
heavy one would contain a seed between $u$ and $v$.
\end{proof}

Let $X_0$ be the root of $T$ and $X_{i+1}$ the child of $X_i$ with the longer
yield, so that $n_{X_i}\le2n_{X_{i+1}}$.  If the root subtree has at most $k_V$
seeds, then $n\le k_V(k_V+2)\theta$.  Otherwise let $i^*$ be the largest index
whose subtree contains at least $k_V+1$ seeds; then $X_{i^*+1}$ exists,
$i^*\le k_V-2$ by Lemma~\ref{lem:app-h-tree}(a), and
$B_0:=n_{X_{i^*}}\le2k_V(k_V+2)\theta$; we may assume $n_{X_{i^*}}<n$, and
$k_V\ge2$ since $T$ has a binary node.  The seeds below $X_{i^*}$ are
consecutive in $T$; among $k_V+1$ consecutive ones two have the same label $Y$,
at positions $x_1<x_2$ with $d:=x_2-x_1\le2k_V^2\theta$.  Put $g_0:=d-n_Y\ge0$,
$\omega:=\omega_Y$, $x:=x_1$, $y:=n-x_2-n_Y$, and $y_1:=n-x_1-n_Y=d+y$.
Replacing both seeds, the first, or the second by $\omega$ gives the yields
\[
 W_1=\mathtt a^x\omega\mathtt a^{g_0}\omega\mathtt a^y,\qquad
 W_2=\mathtt a^x\omega\mathtt a^{d+y},\qquad
 W_3=\mathtt a^{x+d}\omega\mathtt a^y
\]
of $A$.  Here $x+g_0+y\ge1$: otherwise the two seeds would cover the yield of
the root, which contains at least $k_V+1\ge3$ seeds.  Since $d\ge n_Y\ge1$ and
$\omega\notin\mathtt a^+$, the words $W_1,W_2,W_3$ are $\mathtt a$-mixed.

\begin{lemma}[Base]
\label{lem:app-h-base}
Put $z_0:=\omega\mathtt a^{g_0}$ and $c_0:=d$ if $g_0\ge1$ or $\omega$ is
$\mathtt a$-mixed, and $z_0:=\omega\mathtt a^d$ and $c_0:=2d$ if $g_0=0$ and $\omega$
is $\mathtt a$-free.  Then $z_0$ is $\mathtt a$-mixed, $\D(z_0)\ne\emptyset$,
$d\mid c_0$,
\[
 \mathtt a^dz_0\sim z_0\mathtt a^d\qquad\text{and}\qquad z_0z_0\sim\mathtt a^{c_0}z_0.
\]
\end{lemma}

\begin{proof}
By (I2), $W_1,W_2,W_3$ have one type; they share $(l,r)$, hence are
$\sim$-equivalent.  Cancelling $\mathtt a^x$ on the left and $\mathtt a^y$ on the
right of $W_2\sim W_3$ (Lemma~\ref{lem:app-h-cancel}; the remaining words contain
$\mathtt a^d$ and $\omega$, so they are $\mathtt a$-mixed, and the words cancelled
from are factors of $W_2$, so their distributions are nonempty) gives
$\omega\mathtt a^d\sim\mathtt a^d\omega$.  If $g_0\ge1$
or $\omega$ is $\mathtt a$-mixed, the same cancellation in $W_1\sim W_2$ (now
$\omega\mathtt a^{g_0}\omega$ is $\mathtt a$-mixed) gives $\omega\mathtt
a^{g_0}\omega\sim\omega\mathtt a^d$, whence $z_0z_0\sim\omega\mathtt
a^{d+g_0}=z_0\mathtt a^d$ and $\mathtt a^dz_0\sim z_0\mathtt a^d$.  If $g_0=0$ and
$\omega$ is $\mathtt a$-free, then $n_Y=d$ and $x+y\ge1$.  For $y\ge1$,
cancelling $\mathtt a^x$ and $\mathtt a^{y-1}$ gives $\omega\omega\mathtt
a\sim\omega\mathtt a^{d+1}$, so $z_0z_0\sim\omega\omega\mathtt a^{2d}\sim\omega\mathtt
a^{3d}=z_0\mathtt a^{2d}$; for $y=0$, cancelling $\mathtt a^{x-1}$ gives $\mathtt
a\omega\omega\sim\mathtt a\omega\mathtt a^d$, so $z_0z_0\sim\mathtt
a^{2d}\omega\omega\sim\mathtt a^{2d}z_0$.  The words compared here contain
$\mathtt a$ and $\omega$, so they are $\mathtt a$-mixed, and those cancelled from
are factors of $W_1$.  In both cases $z_0\mathtt
a^{2d}\sim\mathtt a^{2d}z_0$ and $\mathtt a^dz_0\sim z_0\mathtt a^d$.  Finally $z_0$
is a factor of $W_1$ or of $W_2$.
\end{proof}

For a typing onto $U_1$ in which $\mathtt a$ is the only letter of type $1$, the
$\mathtt a$-free words have the type of the $\mathtt a$-mixed ones, and the
second case could be avoided; we do not use this.

An \emph{annotated code} is a pair $(z,e)$ with $e\ge0$, $d\mid e$ and $z\sim
\mathtt a^ez_0$; its \emph{value} is $e+c_0$.  A pure block $\mathtt a^R$ with
$d\mid R$ has value $R$.  For a specified product $u$ of annotated codes and
such blocks, $\operatorname{val}(u)$ is the sum of the values of its factors.
(The exponent $e$ is not determined by $z$ in general, so values are attached
to annotations.)

\begin{lemma}
\label{lem:app-h-collapse}
If $u$ contains at least one code, then $u\sim\mathtt
a^{\operatorname{val}(u)-c_0}z_0$.
\end{lemma}

\begin{proof}
Replace each code by $\mathtt a^ez_0$, move all blocks to the left with
$\mathtt a^dz_0\sim z_0\mathtt a^d$, and use $z_0^t\sim\mathtt a^{(t-1)c_0}z_0$,
which follows by induction from $z_0z_0\sim\mathtt a^{c_0}z_0$ and $d\mid c_0$.
\end{proof}

\subsection{Codes along the Heavy Path}

Let $i_0$ be the least index with $n_{X_i}<n$; then $1\le i_0\le i^*$.  For
$i_0\le i\le i^*$ let $(\mathtt a^{p_i},\mathtt a^{q_i})$ be the context of
$X_i$ inside $T$, so $p_i+q_i\ge1$; the subtree of $X_i$ contains both seeds;
let $L_i,R_i$ be the numbers of letters to the left and right of the first seed
inside it, so $R_i\ge g_0+n_Y\ge1$, and put $\Omega_i:=\mathtt a^{L_i}\omega\mathtt
a^{R_i}$, an $\mathtt a$-mixed yield of $X_i$.

\begin{lemma}
\label{lem:app-h-borrow}
If $\omega_{X_i}$ is $\mathtt a$-mixed, then $\omega_{X_i}\sim\Omega_i$.  If
$\omega_{X_i}$ is $\mathtt a$-free and $p_i\ge1$, then $\mathtt a\omega_{X_i}\sim\mathtt
a\Omega_i$; if $\omega_{X_i}$ is $\mathtt a$-free and $p_i=0$, then
$\omega_{X_i}\mathtt a\sim\Omega_i\mathtt a$.
\end{lemma}

\begin{proof}
Both $l\mathtt a^{p_i}\omega_{X_i}\mathtt a^{q_i}r$ and $l\mathtt a^{p_i}\Omega_i
\mathtt a^{q_i}r$ lie in $L$.  In the first case $\omega_{X_i}$ and $\Omega_i$ are
$\mathtt a$-mixed and share the context $(l\mathtt a^{p_i},\mathtt a^{q_i}r)$.  In the
second case $\mathtt a\omega_{X_i}$ and $\mathtt a\Omega_i$ are $\mathtt a$-mixed and
share the context $(l\mathtt a^{p_i-1},\mathtt a^{q_i}r)$; the third case is
symmetric, with $q_i\ge1$.  Conclude by (I2).
\end{proof}

Choose $s_i',s_i\in[0,d]$ with $d\mid L_i+s'_i$, with $R_i+s_i\equiv g_0\pmod d$
in the first case of Lemma~\ref{lem:app-h-base} and $R_i+s_i\equiv0\pmod d$ in
the second, and with $s'_i\ge1$, respectively $s_i\ge1$, when a letter is
borrowed in Lemma~\ref{lem:app-h-borrow}.  Put $\hat z_i:=\mathtt
a^{s'_i}\omega_{X_i}\mathtt a^{s_i}$.  By Lemma~\ref{lem:app-h-borrow},
$\hat z_i\sim\mathtt a^{s'_i+L_i}\omega\mathtt a^{R_i+s_i}$.  In the first case
$R_i+s_i=g_0+kd$ with $k\ge0$, and in the second $R_i+s_i=d+kd$ with $k\ge0$,
since $R_i\ge g_0+n_Y$; so $\hat z_i\sim\mathtt a^{e_i}z_0$ with
$e_i:=s'_i+L_i+kd$, and $(\hat z_i,e_i)$ is an annotated code, of value
\[
 v_i=n_{X_i}+s_i+s'_i,\qquad|\hat z_i|\le\theta+2d,
\]
in both cases (using $n_{X_i}=L_i+n_Y+R_i$ and $d-g_0=n_Y$, respectively
$n_Y=d$).  For $i<i_0$ put $v_i:=n$ (no code).  Since $X_i$ is an ancestor of
$X_{i^*}$, whose yield contains both seeds, $n_{X_i}\ge d+n_Y$ for $i\le i^*$.
Hence, for all $i\le i^*$,
\begin{equation}
\label{eq:app-h-star}
 v_i\ge n_{X_i}>d,\qquad v_i\le2v_{i+1}+2d\ \ (i<i^*),
\end{equation}
and $v_{i^*}\le B_0+2d$; moreover $n\le2n_{X_{i_0}}\le2v_{i_0}$.

The yield $\mathtt a^{x_1}\omega\mathtt a^{y_1}$ of $A$ equals $\mathtt
a^{x_1}z_0\mathtt a^{h}$ with $h:=y_1-g_0$, respectively $h:=y_1-d$.  Writing
$h=qd+\rho$ and $x_1+qd=e^*+\rho'$ with $0\le\rho,\rho'<d$ and $d\mid e^*$, we
obtain $l_\circ\mathtt a^{e^*}z_0r_\circ\in L$ for $l_\circ:=l\mathtt a^{\rho'}$
and $r_\circ:=\mathtt a^\rho r$, and $V^*:=e^*+c_0=n-\rho-\rho'$.

\subsection{Periodicity and Membership}

\begin{lemma}
\label{lem:app-h-period}
Let $P_0:=\{p\ge0:\mathtt a^pz_0\sim z_0\}$.
\begin{enumerate}[label=\textup{(\roman*)},leftmargin=*]
\item $P_0=\{0\}$ or $P_0=p_0\mathbb N$ for some $p_0\ge1$.
\item If $l'\mathtt a^fz_0r'\in L$ for some $f$, then
$\{f\ge0:l'\mathtt a^fz_0r'\in L\}$ is a single point if $P_0=\{0\}$ and a
full residue class modulo $p_0$ otherwise.
\item If $P_0\ne\{0\}$, then $\mathtt a\sim\mathtt a^{1+p_0}$, so every
$\mathtt a^k$ is $\equiv_{L,s}$-equivalent to some $\mathtt a^{k'}$ with $1\le k'\le p_0$.
\end{enumerate}
\end{lemma}

\begin{proof}
All words $\mathtt a^fz_0$ are $\mathtt a$-mixed, so they have one type by (I2).
(i) $P_0$ is closed under sums, and under differences by
Lemma~\ref{lem:app-h-cancel}, since $\D(\mathtt a^pz_0)=\D(z_0)\ne\emptyset$.
(ii) Two members $f<f'$ give $\mathtt a^fz_0\sim\mathtt a^{f'}z_0$, hence
$f'-f\in P_0$ by Lemma~\ref{lem:app-h-cancel}; conversely the set is closed
under adding and, by $\mathtt a^{p_0}z_0\sim z_0$, under subtracting $p_0$.  (iii)
For $(l',r')\in\D(z_0)$ both $l'\mathtt a^{p_0}z_0r'$ and $l'\mathtt
a^{2p_0}z_0r'$ lie in $L$, so the pure words $\mathtt a$ and $\mathtt a^{1+p_0}$,
which have one type by (I1), share the context $(l'\mathtt a^{p_0-1},z_0r')$.
\end{proof}

Let $D:=\operatorname{lcm}(d,p_0)$, and $D:=\infty$ if $P_0=\{0\}$.  By
Lemma~\ref{lem:app-h-collapse} and Lemma~\ref{lem:app-h-period}(ii), for
every specified product $u$ as above that contains a code,
\begin{equation}
\label{eq:app-h-member}
 l_\circ ur_\circ\in L\iff\operatorname{val}(u)\equiv V^*\pmod D,
\end{equation}
with equality when $D=\infty$; values and $V^*$ are multiples of $d$.  Two
annotations of the same word differ by a multiple of $D$, so membership does
not depend on the annotation.

\subsection{Counting}

\begin{lemma}
\label{lem:app-h-count}
Let $(z_1,e_1),\ldots,(z_M,e_M)$ be annotated codes, $M\ge6$, with
$|z_j|\le\ell_z$, values $w_j$ whose subset sums are pairwise distinct, and
$\Sigma_w:=\sum_jw_j<D$, and let $Q$ be a fixed specified product of codes and
blocks with $\Sigma_w+\operatorname{val}(Q)=V^*$.  Put $m:=|l_\circ|+|r_\circ|
+|Q|+\sum_j|z_j|$.  Then
\[
 (27/4)^{\lfloor M/3\rfloor}\le(M+1)^2k_V(m+1)^2(M\ell_z+1)^2.
\]
\end{lemma}

\begin{proof}
For a permutation $\pi$, the word $w_\pi:=l_\circ z_{\pi(1)}\cdots
z_{\pi(M)}Qr_\circ$ lies in $L$ by \eqref{eq:app-h-member}.  Take a
derivation tree of $w_\pi$ in $G'$, contract unit nodes, and give each node the
weight ``number of the codes $z_{\pi(1)},\ldots,z_{\pi(M)}$ whose first letter
lies in its yield''.  Leaves have weight $\le1$ and the root has weight $M$;
descending to the heavier child we reach a node $u$ of weight
$\kappa\in(M/3,2M/3]$, with label $X$ and yield interval $[p,q)$.  Let $I(\pi)$
be the set of indices $j$ such that $z_j$ lies inside $[p,q)$; then
$\kappa-1\le|I(\pi)|\le\kappa$.  The \emph{record} of $\pi$ consists of $X$,
$p$, $q$, and, for each end of $[p,q)$ lying strictly inside one of the $M$
codes, the index and the offset of that code; there are at most
$k_V(m+1)^2(M\ell_z+1)^2$ records.  The three blocks $l_\circ$, $z_{\pi(1)}\cdots
z_{\pi(M)}$ and $Qr_\circ$ occupy the same positions for all $\pi$.

Let $\pi,\pi'$ have the same record.  Replacing the subtree of $u$ in the tree
of $w_\pi$ by the corresponding subtree of $w_{\pi'}$ gives a derivation of
$w_\pi[0,p)\,w_{\pi'}[p,q)\,w_\pi[q,|w_\pi|)\in L$.  Since an end inside a code
has the same index and offset on both sides, the fragments join into complete
copies of the same code, and the word is $l_\circ u''Qr_\circ$ where $u''$ is a
product of complete codes in which $z_j$ occurs
$1-\mathbf 1[j\in I(\pi)]+\mathbf 1[j\in I(\pi')]$ times; this also covers ends
in $l_\circ$ or $Qr_\circ$, and both ends cannot lie in $Qr_\circ$ because
$\kappa\ge2$.  By \eqref{eq:app-h-member},
$\sum_{I(\pi')}w_j\equiv\sum_{I(\pi)}w_j\pmod D$; both sums lie in
$[0,\Sigma_w)\subseteq[0,D)$, so they are equal, and $I(\pi')=I(\pi)$.

Hence a record and $I=I(\pi)$, $|I|=j$, determine $\pi$ up to the order inside
($\le j!$) and the arrangement of the remaining codes around this block
($\le(M-j+1)!$).  Since $j\in\{\kappa-1,\kappa\}$ and $M/3<\kappa\le2M/3$, $j$
lies in $J:=[\lfloor M/3\rfloor,\lfloor2M/3\rfloor]$, and
$\binom{M+1}{j}\le(M+1)k_V(m+1)^2(M\ell_z+1)^2$ for some $j\in J$.  Put
$k:=\lfloor M/3\rfloor$.  As $\binom{M+1}{\cdot}$ is symmetric and unimodal and
$\lfloor M/3\rfloor+\lfloor2M/3\rfloor\le M$, every $j\in J$ satisfies
$\binom{M+1}{j}\ge\binom{M+1}{k}\ge\binom{3k}{k}$.  Finally, the numbers
$t_i:=\binom{3k}{i}3^{-i}(2/3)^{3k-i}$, $0\le i\le3k$, sum to $1$, and
$t_{i+1}/t_i=(3k-i)/(2i+2)$ is at least $1$ if and only if $i\le k-1$; so $t_k$
is the largest of them and $t_k\ge1/(3k+1)\ge1/(M+1)$.  Since
$t_k=\binom{3k}{k}4^k/27^k$, this gives $\binom{3k}{k}\ge(27/4)^k/(M+1)$, and the
lemma follows.
\end{proof}

\subsection{Selection and Filler}

Put $\Lambda:=\min(V^*,D)$, so $\Lambda\le V^*\le n$.

\begin{lemma}[Selection]
\label{lem:app-h-select}
There are $M\ge0$ indices $i^*=j_1>j_2>\cdots>j_M\ge i_0$ whose values
$w_t:=v_{j_t}$ are superincreasing \textup($w_t>w_1+\cdots+w_{t-1}$\textup), with
$w_1+\cdots+w_M<\Lambda$ and $\Lambda\le3^M(v_{i^*}+d)$.
\end{lemma}

\begin{proof}
If $v_{i^*}\ge\Lambda$, take $M:=0$.  Otherwise take $j_1:=i^*$.  Given
$j_t$ and $S_t:=w_1+\cdots+w_t<\Lambda$, let $i$ be the largest index below $j_t$
with $v_i>S_t$; it exists, since $v_0=n\ge\Lambda$ (recall $i_0\ge1$).  If
$S_t+v_i\ge\Lambda$, stop with $M:=t$; otherwise put $j_{t+1}:=i$.  The values
are superincreasing and their sum is below $\Lambda$ by construction.  A taken
value is less than $\Lambda\le n$, whereas $v_i=n$ for $i<i_0$; so all taken
indices are at least $i_0$.  By the choice of $i$, $v_{i+1}\le S_t$: for
$i+1<j_t$ by maximality, and for $i+1=j_t$ because $v_{j_t}=w_t$.  By
\eqref{eq:app-h-star}, $v_i\le2S_t+2d$.  Hence $S_{t+1}+d\le3(S_t+d)$ whenever $i$
is taken, and $\Lambda\le S_M+v_i<3(S_M+d)$ when the process stops.  With
$S_1=v_{i^*}$ this gives $\Lambda<3^M(v_{i^*}+d)$.
\end{proof}

\begin{lemma}[Filler]
\label{lem:app-h-filler}
Let $0<X<n$ be a multiple of $d$.  There is a specified product $Q$ of at most
$3k_V$ codes among $\hat z_{i_0},\ldots,\hat z_{i^*}$ and at most one pure block
$\mathtt a^{X'}$ with $d\mid X'$ and $X'<v_{i^*}$, such that
$\operatorname{val}(Q)=X$ and $|Q|\le(3k_V+2)\ell_z$, where
$\ell_z:=5k_V^2\theta$.
\end{lemma}

\begin{proof}
For $i=i_0,\ldots,i^*$ in turn, append $q_i:=\lfloor X/v_i\rfloor$ copies of
$\hat z_i$ and replace $X$ by $X-q_iv_i$.  Then $q_{i_0}\le1$, since
$X<n\le2v_{i_0}$.  For $i>i_0$ the current $X$ is less than $v_{i-1}$, and
$v_{i-1}\le2v_i+2d<4v_i$ by \eqref{eq:app-h-star}, so $q_i\le3$.  The final
remainder $X'<v_{i^*}$ is a multiple of $d$, since all values are, and is
appended as a block.  As $i^*-i_0\le k_V-3$, there are at most
$1+3(k_V-3)<3k_V$ codes, each of length $\le\theta+2d\le\ell_z$, and
$X'<v_{i^*}\le B_0+2d\le(6k_V^2+4k_V)\theta\le2\ell_z$.
\end{proof}

\subsection{Proof of Theorem~\ref{thm:two-letter-fanout-one}}

Let $A$ have a pure yield.  By (I1) the yields of $A$ of type $s(\mathtt a)$
are its pure yields, so $\tau(A,s(\mathtt a))\le n$, and it suffices to show
$\tau(A,s(\mathtt a))\le11\cdot3^{M^*}k_V^2\theta$, where
\[
 M^*:=\max\bigl(\{5\}\cup\{M\ge6:(27/4)^{\lfloor M/3\rfloor}
 \le(M+1)^4k_V(3k_V+M+4)^2\ell_z^{\,4}\}\bigr),
\]
a finite number since the left side grows exponentially in $M$.  If the root
subtree has at most $k_V$ seeds, or $n_{X_{i^*}}=n$, then $n\le2k_V(k_V+2)\theta$.
Otherwise take the indices of Lemma~\ref{lem:app-h-select}.

\emph{Counting.}  Suppose $M\ge6$.  Let $X:=V^*-\sum_tw_t$; then $0<X<n$, since
$\sum_tw_t<\Lambda\le V^*\le n$ and $w_1>0$, and $X$ is a multiple of $d$.  Let
$Q$ be given by Lemma~\ref{lem:app-h-filler}.  The codes $\hat z_{j_1},\ldots,\hat
z_{j_M}$ have length $\le\ell_z$ and superincreasing values, so their subset
sums are distinct, and $\sum_tw_t<\Lambda\le D$.  With
$|l_\circ|+|r_\circ|\le\theta+2d\le\ell_z$ we get
$m\le(3k_V+M+3)\ell_z$, and Lemma~\ref{lem:app-h-count}, with
$(m+1)^2(M\ell_z+1)^2\le(3k_V+M+4)^2(M+1)^2\ell_z^{\,4}$, gives $M\le M^*$.  So in
every case $M\le M^*$, and by Lemma~\ref{lem:app-h-select}
\[
 \Lambda\le3^{M^*}(v_{i^*}+d)\le3^{M^*}(B_0+3d)\le10\cdot3^{M^*}k_V^2\theta .
\]

\emph{Conclusion.}  If $\Lambda=V^*$, then $n=V^*+\rho+\rho'<\Lambda+2d$ and
$\tau(A,s(\mathtt a))\le n$.  If $\Lambda=D<V^*$, then $P_0\ne\{0\}$, and by
Lemma~\ref{lem:app-h-period}(iii) $\mathtt a^n\equiv_{L,s}\mathtt a^{n'}$ with
$n'\le p_0\le D$, so $\tau(A,s(\mathtt a))\le n'$.  Together with the small cases,
$\tau(A,s(\mathtt a))\le\max\{2k_V(k_V+2)\theta,\,10\cdot3^{M^*}k_V^2\theta+4k_V^2\theta\}
\le11\cdot3^{M^*}k_V^2\theta$.

\emph{The exponents.}  Put $\mu:=(27/4)^{1/3}$, $\gamma:=\ln3/\ln\mu<1.7260$,
$\eta:=1/80$ and $C_\eta:=\sup_{M\ge0}(M+1)^6\mu^{-\eta M}<e^{34}$ (the maximum of
$6\ln x-(x-1)\eta\ln\mu$ over $x>0$ is attained at $x=6/(\eta\ln\mu)$).  For $M\ge6$
in the set defining $M^*$, $\mu^{M-2}\le(27/4)^{\lfloor M/3\rfloor}$ and
$3k_V+M+4\le5k_V(M+1)$ give
\[
 \mu^M\le15625\,\mu^2(M+1)^6k_V^{11}\theta^4,\qquad\text{hence}\qquad
 \mu^{(1-\eta)M}\le15625\,\mu^2C_\eta k_V^{11}\theta^4,
\]
and $3^M=\mu^{\gamma M}\le(15625\,\mu^2C_\eta k_V^{11}\theta^4)^{\gamma/(1-\eta)}$;
this also holds for $M=5$.  Since $\gamma/(1-\eta)=80\gamma/79<1.7479$, we obtain
\[
 \tau(A,s(\mathtt a))\le11\cdot3^{M^*}k_V^2\theta\le C_0k_V^{2+19.23}\theta^{1+6.992}
 \le C_0k_V^{22}\theta^8,\qquad C_0:=11(15625\,\mu^2C_\eta)^{80\gamma/79}<10^{36}.
\]
As $k_V\le2\|G\|$, $\theta\le\bar\theta_G$, and the nonterminals of $G$ are
nonterminals of $G'$ with the same yields, the theorem follows with
$C:=2^{22}C_0<10^{43}$.  Letting $\eta\to0$ shows that the exponents can be taken
arbitrarily close to $2+11\gamma<20.99$ and $1+4\gamma<7.91$.\qed

\subsection{Other Types and Proof of Corollary~\ref{cor:two-letter-fanout-one}}

\begin{lemma}
\label{lem:app-h-other}
Let $G'$ be as above and let $A$ be a nonterminal of $G'$.
\begin{enumerate}[label=\textup{(\roman*)},leftmargin=*]
\item If $s:\Sigma^+\twoheadrightarrow U_1$ and $\mathtt a$ is the only letter of
type $1$, and $A$ has a yield of type $\zeta$, then
$\tau(A,\zeta)\le(k_V-1)\theta+1$.
\item If $\Sigma=\{\mathtt a,\mathtt b\}$, $s=c$, and $A$ has a yield of content
$\Sigma$, then $\tau(A,\Sigma)\le3k_V\theta+2$.
\end{enumerate}
\end{lemma}

\begin{proof}
(i) Take a derivation of a yield of $A$ of type $\zeta$ with the least number of
nodes and mark a leaf whose letter is not $\mathtt a$.  Replacing the subtree of a
node on the path from the root to the marked leaf by the subtree of a lower node
with the same label keeps the marked leaf, hence the type; so no label repeats on
this path, which has at most $k_V$ nonterminal nodes.  Replacing the at most
$k_V-1$ subtrees hanging off it by yields of length $\le\theta$ gives a yield of
$A$ of type $\zeta$ and length $\le(k_V-1)\theta+1$.  (ii) Take a derivation of a
yield of content $\Sigma$ with the least number of nodes and mark an $\mathtt
a$-leaf and a $\mathtt b$-leaf.  By the same contraction on the three path segments
between the root, the branching node and the two leaves, the skeleton has at most
$3k_V$ nodes; replacing the at most $3k_V$ subtrees hanging off it by yields of
length $\le\theta$ gives a yield of content $\Sigma$ of length $\le3k_V\theta+2$.
In both cases the new word is a yield of $A$ of the same type, hence in the same
class (Lemma~\ref{lem:typed-homogeneity}).
\end{proof}

\begin{proof}[Proof of Corollary~\ref{cor:two-letter-fanout-one}]
In both cases $G'$ is a reduced good presentation of $L\cap\Sigma^+$ of fan-out
one and rank $2\le r_{\max}$, with $\bar\theta_{G'}\le\bar\theta_G$, and
Corollary~\ref{cor:distribution-representatives} applied to $G'$ gives
$\|K\|_+\le N_{\mathrm{typ}}(G',s)(1+2\bar\theta_G+r_{\max}\tau(G',s))
+\mathbf 1_{\{\eps\in L\}}$.  It remains to bound $\tau(G',s)$ and
$N_{\mathrm{typ}}(G',s)$.

(i) The positive image of $s$ is generated by $s(\mathtt a)$ and $s(\mathtt b)$ in a
semilattice, so $s(w)$ depends only on $c(w)$; thus $s\preceq c$,
$\Cmcf{1}{s}\subseteq\Cmcf{1}{c}$, and $\equiv_{L,c}$ refines $\equiv_{L,s}$.
For a typed nonterminal $A_t$ of $G'$ and the $c$-type $t'$ of one of its
yields, $\tau_{A_t}(G',s)\le\tau(A,t')$.  Both letters are isolated for $c$, so
Theorem~\ref{thm:two-letter-fanout-one}, applied to $c$ with $\mathtt a$ and with
$\mathtt b$, and Lemma~\ref{lem:app-h-other}(ii) give
$\tau(G',s)\le C(\|G\|+2)^{22}\bar\theta_G^{\,8}$.  The typed refinement of $G'$
has at most $3k_V$ typed nonterminals and at most nine typed rules per rule, so
$N_{\mathrm{typ}}(G',s)\le3k_V+9|P'|\le12(\|G\|+2)$.

(ii) The typed nonterminals of $G'$ are of the form $A_1$, with $A$ having a
yield in $\mathtt a^+$, and $A_\zeta$.  By
Theorem~\ref{thm:two-letter-fanout-one} and Lemma~\ref{lem:app-h-other}(i),
$\tau(G',s)\le C(\|G\|+2)^{22}\bar\theta_G^{\,8}$.  There are at most $2k_V$ typed
nonterminals and at most four typed rules per rule, so
$N_{\mathrm{typ}}(G',s)\le2k_V+4|P'|\le6(\|G\|+\sigma_G)\le12\|G\|$.

In both cases $1+2\bar\theta_G\le3\bar\theta_G$ gives the bound with
$C':=12(C+2)<10^{45}$.
\end{proof}

```
