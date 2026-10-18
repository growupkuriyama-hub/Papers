# MCFG #2: 研究メモ — 型付けの代数的二分法と指数の下界

Date: 2026-10-18 (JST)
Status: **研究メモ（未証明の予想を含む）。本文には入れていない。**
Inputs: Costa (2001) "Some pseudovariety joins involving locally trivial semigroups (and groups)";
Simon (1990) "Factorization forests of finite height"; #1 CFG companion の semilattice 下界。

## 1. 現在の定理を代数的に言い換える

v75/v76 の多項式定理の仮定は「$h\preceq(h^{k,\ell}_\Sigma,g)$（固定窓と有限群の積を通って分解する）」という表示依存の条件である。

**主張（証明スケッチ、要検証）.** $h:\Sigma^*\to M$ について次は同値。

1. ある $k,\ell$ と有限群への準同型 $g$ があって $h\preceq(h^{k,\ell}_\Sigma,g)$。
2. 半群 $h(\Sigma^+)$ が pseudovariety $\mathbf{LI}\vee\mathbf G$ に属する。

スケッチ：
- (1⇒2)：$h^{k,\ell}_\Sigma(\Sigma^+)\in\mathbf{LI}$、$g(\Sigma^+)\in\mathbf G$。$h(\Sigma^+)$ はその積の部分半群の準同型像であり、$\mathbf{LI}\vee\mathbf G$ に属する。
- (2⇒1)：Eilenberg 対応により、join $\mathbf V\vee\mathbf W$ の +-言語多様体は $\mathbf V$ と $\mathbf W$ の言語の Boolean 閉包である。各 $h$-類は有限個の窓言語と群言語の Boolean 結合なので、$k,\ell$ の最大値と群の直積を取れば一つの $(h^{k,\ell},g)$ を通って分解する。
- 注意：空語の扱いと、$\mathbf{LI}$ が +-pseudovariety であることの扱いを詰める必要がある。

これが成り立てば、主定理を「$h(\Sigma^+)\in\mathbf{LI}\vee\mathbf G$ なら多項式」と不変な形で書ける。

## 2. 下界側の境界：$\mathbf{Sl}$ と $\mathbf{LG}$

**事実（初等的に証明可能）.** 半群の pseudovariety $\mathbf V$ について
$\mathbf{Sl}\not\subseteq\mathbf V \iff \mathbf V\subseteq\mathbf{LG}$
（$\mathbf{LG}$：すべての局所モノイド $eSe$ が群である半群）。

証明：$S\notin\mathbf{LG}$ なら、ある $eSe$ は群でない有限モノイドである。有限モノイドで唯一の冪等元が単位元なら群なので、冪等元 $f\ne e$ が存在する。このとき $f\in eSe$ から $ef=fe=f$ となり、$\{e,f\}$ は2元半束である。逆は $\mathbf{Sl}\not\subseteq\mathbf{LG}$ から従う。

#1 の指数下界は semilattice 型付けによる。以上から、型付けの世界は次の三つに分かれる。

| 領域 | 状態 |
|---|---|
| $h(\Sigma^+)\in\mathbf{LI}\vee\mathbf G$ | 多項式（本論文、全 fan-out） |
| $h(\Sigma^+)\in\mathbf{LG}\setminus(\mathbf{LI}\vee\mathbf G)$ | **未知（中間帯）** |
| $h(\Sigma^+)\notin\mathbf{LG}$（2元半束を含む） | fan-out 1 で超多項式の例あり（#1）。ただし任意の $h$ への移植は未検証 |

**予想 D（二分法）.** 元文法の size と thickness について特性データ総長が多項式になるための必要十分条件は、$h(\Sigma^+)\in\mathbf{LG}$ である。あるいは境界は $\mathbf{LI}\vee\mathbf G$ そのものかもしれない。どちらかを判定するのが中間帯の問題である。

- $\mathbf{LI}\vee\mathbf G\subsetneq\mathbf{LG}$ が一般に成り立つかは、Costa の join 計算（$\mathbf{LI}\vee\mathbf H\vee\mathbf V$、上界 $\mathbf U_\omega\mathbf V$）で確認すること。本メモ作成時点では未確認。
- 上界側の道具は Simon の factorization forest（任意の有限半群で高さ $\le 9|S|$）。群の場合の「積が 1 の区間」の議論を、半群では「冪等元で挟まれた区間」に置き換えることになる。$\mathbf{LG}$ では $eSe$ が群なので、局所的には群の議論が使える見込みがある。
- 下界側の課題：$h(\Sigma^+)\notin\mathbf{LG}$ なら $h$ は2元半束を「含む」。しかし #1 の文法族を $h$ の中に実現できるかは別問題であり、$\Sigma$ 上の語で $e,f$ を実現して文法族を書き換える必要がある。

## 3. 未解決問題 `op:fanout-two`（fan-out 2 以上の超多項式下界）

- 単純な埋め込みは使えない（本文の注記どおり、$\Cmcf{1}{h}\not\subseteq\Cmcf{f}{h}$）。
- 方針案：#1 の semilattice 族の各規則を「2成分を同時に運ぶ」規則に置き換える。両成分に同じ半束情報を持たせると、fan-out 2 の部分タプルの入れ替えでも substitutability が保たれやすい。対角的な複製で $(f,h)$-substitutability を保てるかが鍵になる。

## 4. 指数 2・3 の最適性（下界）

- 型なし（$h$ 自明）の場合、Yoshinaka (2011) の上界は $O(|P|\tau_G)$ で線形である。窓型付けでの二乗は、canonical tuple の長さ $O(n_{\mathrm{typ}}\bar\theta_G)$（骨格上の各節点が $\bar\theta$ ずつ寄与）と、証拠語の数 $O(\|G\|)$ の積から生じる。
- 下界の候補族：接頭辞の型を実現するために長い鎖 $A_1\to\cdots\to A_n$（各段 $\bar\theta$ 文字）を必要とする非終端記号を $\Theta(n)$ 個の規則が共有する文法。
- 難所：下界は「任意の特性サンプル」に対して示す必要がある。本論文の構成した標本が長いことだけでは不十分である。#1 の下界証明（distinguishing pair 論法）がどこまで流用できるかを先に確認すべき。

## 5. 次の具体的な一手

1. §1 の同値性を、空語の扱いを含めて厳密に書く（1〜2ページで済む見込み）。本文に remark として入れる価値がある。
2. Costa の2論文から $\mathbf{LI}\vee\mathbf G$ と $\mathbf{LG}$ の差を示す具体例を拾う。
3. 中間帯の最小の具体例（$\mathbf{LG}$ に属し $\mathbf{LI}\vee\mathbf G$ に属さない小さな半群）で、上界・下界のどちらが成り立つかを小さい計算実験で調べる。
