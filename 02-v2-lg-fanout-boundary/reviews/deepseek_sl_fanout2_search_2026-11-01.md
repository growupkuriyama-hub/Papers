# 半束型付けのファンアウト2代入可能性：計算探索報告

**実行日：** 2026年11月1日  
**対象：** `02-v2-lg-fanout-boundary/main.tex` の定理B・定理C・Open Problem `op:fanout-two`  
**作業場所：** `C:\Users\Owner\Documents\GitHub\Papers\02-v2-lg-fanout-boundary\reviews`  
**スクリプト：** [`check_sl_fanout2_search.py`](check_sl_fanout2_search.py)（Python 3.12.10、標準ライブラリのみ）  
**原稿の状態：** 変更していない。commit・push もしていない。

> **リポジトリ同期について。** 指示どおり `git pull --ff-only` を実行したが、
> `schannel: AcquireCredentialsHandle failed: SEC_E_NO_CREDENTIALS (0x8009030e)`
> で失敗した。以下の計算はローカル HEAD `c38df0d69c41500e4afd1c3217f0f1203cad903a`
> に対して行った。原稿 `main.tex` の作業前後の差分はない。

---

## 0. 判定一覧

**背景。** 原稿の定理Bは、ファンアウト1では「多項式データを許す擬多様体はちょうど局所群
$\mathbf{LG}$」を証明している。ファンアウト2では上界（$\mathbf{LG}$ 側）だけが既知で、
逆方向は Open Problem `op:fanout-two` である。$\mathbf{LG}$ の外の擬多様体は
$U_1=\{1,\zeta\}$（$\zeta^2=\zeta$）を含み、$U_1$ は2元半束 SL と同型である。
したがって SL の型付けで超多項式のデータ下界を作ることが、境界の逆方向の中心課題になる。
この還元（非 LG の擬多様体が SL を含むこと、および SL のデータ下界が境界の逆方向と同値なこと）は
依頼文と理論側の担当であり、本報告では再証明していない。
本報告は、そのための候補を内容型付け $c_\Sigma$ で探し、見つかった障害を分類したものである。

「証明済み」は計算に依存しない証明、または有限言語についての完全な証拠（証人と所属の再検査）を指す。
「計算による観察」は、明示した有限の範囲での全数検査であり、全 $n$ や一般の言語への主張ではない。

| # | 主張 | 判定 | 根拠 |
|---:|---|---|---|
| 1 | 有限言語の $(d,s)$-代入可能性判定器（$d=1,2$）は完全である | **証明済み** | §1.2、[`check_substitutable`](check_sl_fanout2_search.py#L140) |
| 2 | 任意の半束型付け $s$ に対し $\mathcal C^{\mathrm{mcf}}_{f,s}\subseteq\mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}$。$c_\Sigma$ は最も細かく、クラスは最も大きい | **証明済み** | §1.3 |
| 3 | 括弧付き倍増族 $L_n$ は $n\le 4$ でファンアウト1の全型付けに代入可能（CE 性） | **計算（原稿では証明済み）** | §2.1 |
| 4 | 三文字族 $K_2$ はファンアウト2で失敗し、$P_{N,2}$ は通る | **計算** | §2.2 |
| 5 | 非重複型の Thue–Morse 倍増族（水準別マーカー）は $n\le3$ でファンアウト2に通る | **計算** | §3.2 |
| 6 | 同じ族は $n=4$ でファンアウト2に失敗する | **証明済み（$n=4$ に限る）** | §3.3、$677$ 語の完全な証人 |
| 7 | その $n=4$ の失敗は冪の移行ではない | **計算および有限証拠** | §3.3、§5 |
| 8 | 検査した全候補で $u^5$ は現れない | **計算** | §3.2 |
| 9 | Thue の平方のない形態素による族も $n=3$ で失敗する | **計算** | §3.3 |
| 10 | 浅い倍増型 $6^4=1296$ 個の $n\le3$ 全数探索では、$n=3$ のファンアウト2生存者はすべて1語言語である | **計算による観察** | §4 |
| 11 | 水準別マーカー付き Thue–Morse 族の $\lVert G_n\rVert=16n+2$、$\bar\theta_{G_n}=n+1$、$\mu_{\{a,b\}}=2^n$ | **証明済み（全 $n$）** | §5.1 |
| 12 | 語ごとに私用文字を1個持つ有限言語は、全ファンアウトで内容型付け $c_\Sigma$ に代入可能 | **証明済み** | §5.2 |
| 13 | 固定アルファベット上で SL の多項式データを破る族 | **未解決** | §6 |
| 14 | ファンアウト2で境界が LG である／でない | **未解決** | §6 |
| 15 | 上記 Thue–Morse 族が全 $n\ge4$ で失敗する | **未解決**（$n=4$ のみ証明） | §6 |
| 16 | 失敗証人の分類：冪の移行は観測されず、同一ホストの曖昧分解が主である | **計算による観察** | §5.1 |

**最重要の結論。** 今回の範囲では、$c_\Sigma$ 上で「$\lVert G_n\rVert$ と $\bar\theta$ が多項式、かつ希少な内容型の最短長が超多項式」を満たす族は見つからなかった。
しかしこれは「存在しない」の証明ではない。とくに、検査した候補はアルファベットが $n$ とともに増えるため、原稿の固定アルファベットの定理に対する反例には**なっていない**。SL の境界問題は未解決のままである。

---

## 1. 設定、判定器、$c_\Sigma$ の位置づけ

### 1.1 計算した定義

$\Sigma$ を有限アルファベット、$L\subseteq\Sigma^+$ を有限言語とする。$1\le d\le2$ に対し、
$x=(x_1,\ldots,x_d)\in(\Sigma^+)^d$ の分布を
\[
 \mathcal D_L^{(d)}(x)=\{E\in\mathcal E_d:E[x]\in L\}
\]
とする。ここで $E=v_0\square_1v_1\cdots\square_dv_d$、$v_0,v_d\in\Sigma^*$、$v_1,\ldots,v_{d-1}\in\Sigma^+$ である。
型付け $s$ に対し、$s^{(d)}(x)=(s(x_1),\ldots,s(x_d))$ と書く。

内容型付けは
\[
 c_\Sigma(w)=\{a\in\Sigma:a\text{ は }w\text{ に現れる}\}\qquad(w\in\Sigma^+)
\]
で、台集合の和による半束への全射である。以下「内容型」はこの $c_\Sigma$ を指す。
$U_1=\{1,\zeta\}$（$\zeta^2=\zeta$）への型付けは、指定した文字集合を $\zeta$、それ以外を $1$ とする。

$\theta_G(R)$ は原稿 `def:standard-mcfg` の規則 $R$ に対し、
「$R$ を一度以上使う成功導出が生成する文の最短長」であり、$\bar\theta_G=\max_R\theta_G(R)$ である。
$\lVert G_n\rVert$ は原稿の記号レベルの大きさ（非終端の数＋各規則の $1+$ ランク＋右辺の記号数）で計算した。

### 1.2 判定器の完全性（証明）

**補題1.** $L$ が有限で $d\in\{1,2\}$ なら、[`check_substitutable`](check_sl_fanout2_search.py#L140) は
$L$ の $(d,s)$-代入可能性を厳密に判定する。

**証明。** まず、$x\in(\Sigma^+)^d$ が $\mathcal D_L^{(d)}(x)\ne\emptyset$ を満たすなら、
$x$ はある $w\in L$ の $d$ 組の出現として現れる。したがってアルゴリズムが列挙する出現だけを考えればよい。

アルゴリズムは各出現 $(x,E)$ をキー $(E,s^{(d)}(x))$ でまとめ、同じキーの最初の代表 $x_0$ と
新たな $x$ の分布を比較する。もし $s^{(d)}(x)=s^{(d)}(y)$ かつ
$E\in\mathcal D_L^{(d)}(x)\cap\mathcal D_L^{(d)}(y)$ なら、$(x,E)$ と $(y,E)$ はともに列挙され、
同じキーに入る。よってどこかで代表と比較され、分布が異なれば証人が返る。
逆にアルゴリズムが証人を返せば、[`validate_certificate`](check_sl_fanout2_search.py#L196) が
成分の非空性、内部区切りの非空性、型の一致、$E[x],E[y]\in L$、$F$ での所属の食い違いを
文字列の連結で再検査する。証人がなければ、同じキーの全組は同じ分布を持ち、
共通文脈を持つ同型の組はすべて同じキーに属するので、代入可能性が成り立つ。$\square$

アルゴリズムは $d=1,2$ のみを扱う。ファンアウト $f=2$ の定義は $d=1$ と $d=2$ の両方を要求するので、
今回の目的にはこれで足りる。有限言語の全出現を列挙するため、**無限言語や全 $n$ の証明には使えない**。

### 1.3 $c_\Sigma$ で探すことの論理的な位置（証明）

原稿の命題（$s\preceq s'$ なら $\mathcal C^{\mathrm{mcf}}_{f,s}\subseteq\mathcal C^{\mathrm{mcf}}_{f,s'}$）を思い出す。
$s\preceq s'$ は「$s'$ の核が $s$ の核より細かい」という向きである。
内容型付け $c_\Sigma$ は任意の半束型付け $s$ より細かい：
\[
 s(w)=\bigvee_{a\in c_\Sigma(w)}s(a)
\]
だから、$c_\Sigma(w)=c_\Sigma(w')$ なら $s(w)=s(w')$ であり、$s\preceq c_\Sigma$ である。したがって
\[
 \mathcal C^{\mathrm{mcf}}_{f,s}\subseteq \mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}
 \qquad\text{(すべての半束型付け }s\text{ について).}
\]
すなわち、$c_\Sigma$ は**最も細かい**半束型付けであり、そのクラスは最も**大きい**（制約が最も弱い）。
SL のクラスはこの中に含まれる。

この向きの帰結は二つある。
- $c_\Sigma$ で族が見つかっても、それだけでは SL の族ではない。より粗い SL 型付けで
  $(2,s_{SL})$-代入可能性を別に検査しなければならない。
- 逆に、$c_\Sigma$ の**全言語**について「希少型が超多項式になる族は存在しない」ことが証明できれば、
  SL の族も存在しない。$c_\Sigma$ は SL を含む上位クラスだからである。

今回行ったのは有限の $n$ と有限個の型の探索であり、上のどちらの全称命題も証明していない。
したがって「$c_\Sigma$ の探索で候補が見つからない」ことは、SL の候補がないことの証明にはならない。
ただし探索の向きとしては、まず最大のクラス $c_\Sigma$ を見るのが自然である。

---

## 2. T1：判定器の検算

### 2.1 括弧付き倍増族（ファンアウト1）

原稿の
\[
 S_0\to E_n,\quad E_0\to\mathtt a,\quad
 E_i\to\lfloor E_{i-1}E_{i-1}\rfloor\mid\lceil E_{i-1}\rceil
\]
を、記号を `[`、`]`、`<`、`>` に置き換えて実装した。$n=1,\ldots,4$ で、ファンアウト1の
内容型付け・$U_1$ 型付け・自明型付けを全数検査した。

| $n$ | 語数 | 最長長 | $\lVert G_n\rVert$ | $\bar\theta$ | $c_\Sigma$ | $U_1$ | 自明（CE） |
|---:|---:|---:|---:|---:|---|---|---|
| 1 | 2 | 4 | 20 | 4 | PASS | PASS | PASS |
| 2 | 6 | 10 | 33 | 8 | PASS | PASS | PASS |
| 3 | 42 | 22 | 46 | 12 | PASS | PASS | PASS |
| 4 | 1806 | 46 | 59 | 16 | PASS | PASS | PASS |

自明型付けはすべての型付けの中で最も粗い。したがって自明型付けでファンアウト1の代入可能性が成り立てば、
原稿の単調性から任意の型付けで成り立つ。上の PASS は、$n\le4$ における CE 性
（Clark–Eyraud 代入可能性）の完全な有限確認である。原稿は全 $n$ の CE 性を既に証明している。

$\lVert G_n\rVert=13n+7$、$\bar\theta_{G_n}=4n$ が $n\le4$ で成り立つことも確認した。
これは原稿の $O(n)$ 評価と整合する。

### 2.2 三文字族 $K_2$ と $P_{N,2}$

先行報告と同じ定義
\[
 K_0=\{\mathtt a\},\qquad
 K_{i+1}=\{\mathtt b ww'\mathtt b:w,w'\in K_i\}\cup
          \{\mathtt c w\mathtt c:w\in K_i\}
\]
を用い、$U_1$ 型付け $s(\mathtt c)=\zeta$、$s(\mathtt a)=s(\mathtt b)=1$ で検査した。

- $K_2$ はファンアウト1を通り、ファンアウト2で失敗した。
- 証人は
  \[
   x=(\mathtt{cba},\mathtt b),\quad y=(\mathtt{cb},\mathtt{ab}),\quad
   E=(\varepsilon,\mathtt a,\mathtt c),\quad
   F=(\mathtt{bca},\mathtt{ab},\varepsilon).
  \]
  $E[x]=E[y]=\mathtt{cbaabc}\in K_2$、$F[x]=\mathtt{bcacbaabb}\in K_2$、
  $F[y]=\mathtt{bcacbabab}\notin K_2$ である。先行報告の証人と同型で、同じ「同一ホストの曖昧分解」に属する。

さらに
\[
 P_{N,2}=\{(\mathtt{ab})^N\}\cup
 \{(\mathtt{ab})^i\mathtt c(\mathtt{ab})^{2-i}:0\le i\le2\}
\]
を $N=1,\ldots,5$ で検査し、すべてファンアウト1・2を通った。

### 2.3 単独言語についての注意

任意の単独言語 $L=\{w\}$ は、全ファンアウト・全型付けで代入可能である。
実際、$E[x],E[y]\in L$ なら $E[x]=E[y]=w$ であり、固定された文脈 $E$ の穴を埋めた文字列が等しいので
$x=y$ である。したがって、単独言語は代入可能性の障害にはならない。
問題は「単独言語の長い語を、多項式サイズ・多項式 $\bar\theta$ の文法で表示できるか」である。
この区別は §3 と §5.2 で再び使う。

---

## 3. T2：重なりのない倍増族

### 3.1 族の定義

以下、マーカーはすべて1文字で、$a,b$（Thue では $a,b,c$）とは異なるものを使う。

**(A) 括弧付き倍増族。** 原稿の $L_n$。比較の基準。

**(B) Thue–Morse 水準別マーカー族（`tm_level_markers`）。**
\[
 U_0=\mathtt a,\quad V_0=\mathtt b,\qquad
 U_i\to U_{i-1}V_{i-1}\mid d_i\ (1\le i\le n),\quad
 V_i\to V_{i-1}U_{i-1}\mid e_i\ (1\le i<n),
\]
開始記号は $U_n$。$d_i,e_i$ は水準ごとに異なる1文字マーカーである。
$V_n$ は $U_n$ から到達不能なので、reduced にするため定義から除いた（言語は変わらない）。
マーカーを除いた語は Thue–Morse 語 $t_n$ ただ一つで、$|t_n|=2^n$ である。

**(C) 単一マーカー族（`tm_single_marker`）。** (B) で全水準のマーカーを同じ `#` にしたもの。

**(D) 括弧マーカー族（`tm_bracket_marker`）。** (B) のマーカーを `[` と `]` の囲みにしたもの。

**(E) Thue の平方のない形態素族（`thue_squarefree_level_markers`）。**
\[
 h(\mathtt a)=\mathtt{abc},\quad h(\mathtt b)=\mathtt{ac},\quad h(\mathtt c)=\mathtt b
\]
の反復 $h^n(\mathtt a)$ を背骨にし、各水準の非終端に葉マーカーを付けた。
元の規則は $A_i\to A_{i-1}B_{i-1}C_{i-1}$ でランク3なので、CFG の右二分化
（[`binarize_cfg`](check_sl_fanout2_search.py#L382)）でランク2にした。
$n=1,2,3$ で二分化前後の言語が一致することを確認した（出力 `T2_BINARIZATION`）。

**(F) 基塊を変えた Thue–Morse 族（`tm_base_ab_ba`, `tm_base_ba_ab`）。**
(B) の $U_0,V_0$ を $\mathtt{ab},\mathtt{ba}$ または $\mathtt{ba},\mathtt{ab}$ にしたもの。
背骨の語は $2^{n+1}$ 程度になる。

> **固定アルファベットに関する重要な制限。** (B)–(F) は水準ごとに新しいマーカー文字を追加するので、
> アルファベットは $n$ とともに増える。したがってこれらは原稿の「固定アルファベット」の反例ではない。
> ここでの目的は、固定アルファベットに移す前に、非重複性・$\bar\theta$・希少型の間に何が起きるかを
> 切り分けることである。

### 3.2 統計と全数検査

「型の最短」は内容型ごとの最短語長、「希少型」はその最大値である。
`type_min_all` には**すべての内容型**の最短長と語数が入っている（付録の生出力）。
表には紙面の都合で、希少型と、マーカーを使わない語（pure 語）だけを示す。

| 族 | $n$ | 語数 | 最長 | $\lVert G\rVert$ | $\bar\theta$ | 型数 | 希少型（最短, 語数） | pure 語（個, 長さ） | $u^3$ なし | $u^5$ なし | f1 ($c_\Sigma$) | f2 ($c_\Sigma$) |
|---|---:|---:|---:|---:|---:|---:|---|---|---|---|---|---|
| 括弧 | 1 | 2 | 4 | 20 | 4 | 2 | `[]a` (4,1) | 1, 4 | yes | yes | PASS | PASS |
| 括弧 | 2 | 6 | 10 | 33 | 8 | 3 | `[]a` (10,1) | 1, 10 | yes | yes | PASS | PASS |
| 括弧 | 3 | 42 | 22 | 46 | 12 | 3 | `[]a` (22,1) | 1, 22 | **no** (`<`) | yes | PASS | **FAIL** |
| TM 水準別 | 1 | 2 | 2 | 18 | 2 | 2 | `ab` (2,1) | 1, 2 | yes | yes | PASS | PASS |
| TM 水準別 | 2 | 5 | 4 | 34 | 3 | 5 | `ab` (4,1) | 1, 4 | yes | yes | PASS | PASS |
| TM 水準別 | 3 | 26 | 8 | 50 | 4 | 15 | `ab` (8,1) | 1, 8 | yes | yes | PASS | PASS |
| TM 水準別 | 4 | 677 | 16 | 66 | 5 | 51 | `ab` (16,1) | 1, 16 | yes | yes | PASS | **FAIL** |
| TM 単一マーカー | 1 | 2 | 2 | 18 | 2 | 2 | `ab` (2,1) | 1, 2 | yes | yes | PASS | PASS |
| TM 単一マーカー | 2 | 5 | 4 | 34 | 3 | 3 | `ab` (4,1) | 1, 4 | yes | yes | **FAIL** | — |
| TM 単一マーカー | 3 | 24 | 8 | 50 | 4 | 3 | `ab` (8,1) | 1, 8 | **no** (`#`) | yes | **FAIL** | — |
| TM 括弧マーカー | 1 | 2 | 3 | 21 | 3 | 2 | `[]a` (3,1) | 1, 2 | yes | yes | PASS | PASS |
| TM 括弧マーカー | 2 | 6 | 6 | 43 | 5 | 3 | `[]a` (5,1) | 1, 4 | yes | yes | PASS | PASS |
| TM 括弧マーカー | 3 | 42 | 12 | 65 | 8 | 3 | `ab` (8,1) | 1, 8 | **no** (`[`) | yes | **FAIL** | — |
| Thue 平方なし | 1 | 2 | 3 | 31 | 3 | 2 | `abc` (3,1) | 1, 3 | yes | yes | PASS | PASS |
| Thue 平方なし | 2 | 9 | 6 | 63 | 5 | 9 | `0abc` (6,1) | 1, 6 | yes | yes | PASS | PASS |
| Thue 平方なし | 3 | 136 | 12 | 95 | 6 | 59 | `0abc` (12,3) | 1, 12 | yes | yes | PASS | **FAIL** |
| 基塊 `ab/ba` | 2 | 5 | 8 | 36 | 5 | 5 | `ab` (8,1) | 1, 8 | yes | yes | PASS | PASS |
| 基塊 `ab/ba` | 3 | 26 | 16 | 52 | 6 | 15 | `ab` (16,1) | 1, 16 | yes | yes | PASS | **FAIL** |
| 基塊 `ab/ba` | 4 | 677 | 32 | 68 | 7 | 51 | `ab` (32,1) | 1, 32 | yes | yes | PASS | **FAIL** |
| 基塊 `ba/ab` | 2 | 5 | 8 | 36 | 5 | 5 | `ab` (8,1) | 1, 8 | yes | yes | PASS | PASS |
| 基塊 `ba/ab` | 3 | 26 | 16 | 52 | 6 | 15 | `ab` (16,1) | 1, 16 | yes | yes | PASS | **FAIL** |
| 基塊 `ba/ab` | 4 | 677 | 32 | 68 | 7 | 51 | `ab` (32,1) | 1, 32 | yes | yes | PASS | **FAIL** |

（`—` はファンアウト1で既に落ちたため、ファンアウト2を検査していないことを示す。
`u^3` の「no」は、その族の言語に $u^3$ を因子に持つ語が存在するという意味である。
すべての族で $u^5$ は存在しなかった。）

**観察1（非重複性だけでは足りない）。** Thue–Morse 背骨は $u^3$ を含まず、Thue の平方のない語は
$u^3$ も含まない。それでも TM 水準別 $n=4$、Thue $n=3$、基塊族 $n=3,4$ はファンアウト2で落ちる。
したがって「$u^5$ を避ければファンアウト2に通る」という予想は、$c_\Sigma$ では成り立たない。

**観察2（小さい $n$ の一致は証明ではない）。** TM 水準別は $n=1,2,3$ でファンアウト2に通り、
$n=4$ で落ちる。基塊族は $n=2$ で通り、$n=3$ で落ちる。
$n=3$ までの一致から全 $n$ を結論してはいけない、という指示の実例になっている。

**観察3（希少型の分離）。** TM 水準別 $n=4$ は
\[
 \lVert G_4\rVert=66,\quad \bar\theta_{G_4}=5,\quad
 \mu_{\{a,b\}}(L_4)=16
\]
である。§5.1 で全 $n$ の $\mu_{\{a,b\}}=2^n$ を証明するので、希少型の最短長は $n$ について指数的である。
$n=4$ ではまだ $16$ に過ぎないが、文法サイズと $\bar\theta$ は $n=4$ でそれぞれ $66$ と $5$ であり、
$n$ を上げても $O(n)$ のままである。問題はファンアウト2の代入可能性だけである。

### 3.3 $n=4$ の失敗証人（有限だが完全な証明）

TM 水準別 $n=4$ の言語 $L_4$ は677語からなる。その完全な列挙に対する検査で、次の証人が見つかった。
\[
 x=(\mathtt{baab},\mathtt{ba}),\qquad
 y=(\mathtt{ba},\mathtt{abba}),
\]
\[
 E=(\mathtt E,\mathtt C,\varepsilon),\qquad
 F=(\mathtt C,\mathtt{ba},\mathtt{CCba}).
\]
ここで `C` は水準1の $U$-マーカー、`E` は水準3の $U$-マーカーである。実際、
\[
 E[x]=\mathtt{EbaabCba},\qquad E[y]=\mathtt{EbaCabba},
\]
\[
 F[x]=\mathtt{CbaabbabaCCba},\qquad F[y]=\mathtt{CbabaabbaCCba}.
\]
$E[x],E[y],F[x]\in L_4$ で $F[y]\notin L_4$ である。また
\[
 c_\Sigma(x)=(c_\Sigma(\mathtt{baab}),c_\Sigma(\mathtt{ba}))
 =(\{a,b\},\{a,b\})
 =c_\Sigma(y).
\]
スクリプトは $E[x],E[y]\in L_4$ と $F[x]\in L_4$、$F[y]\notin L_4$ を文字列の連結で再検査している。
したがって $L_4\notin\mathcal C^{\mathrm{mcf}}_{2,c_\Sigma}$ は $n=4$ について**証明済み**である。

この証人は冪の移行ではない。$x,y$ の成分はどれも同一の原始語の冪ではなく、
$E[x]$ と $E[y]$ は共通の枠の中で2つのブロックを入れ替えた形をしている。
$L_4$ には $u^3$ を因子に持つ語すらない（出力 `first_u3: null`, `first_u5: null`）。
したがって、原稿の `lem:power-transfer` だけでは説明できない失敗である。
理論側には、**同一ホストの曖昧分解**と**ブロック交換**を扱う二穴の移送補題が必要になる。

**Thue 平方なし $n=3$ の失敗（同一ホスト型）。**
\[
 x=(\mathtt{abcdba},\mathtt{cba}),\qquad
 y=(\mathtt{abcd},\mathtt{abcba}),
\]
\[
 E=(\varepsilon,\mathtt b,\mathtt c),\qquad
 F=(\varepsilon,\mathtt 0,\mathtt c).
\]
このとき
\[
 E[x]=E[y]=\mathtt{abcdbabcbac},
\]
すなわち2つの異なる二組が**同じ語**を埋める。にもかかわらず
\[
 F[x]=\mathtt{abcdba0cbac}\in L_3,\qquad
 F[y]=\mathtt{abcd0abcbac}\notin L_3.
\]
$L_3$ は $u^3$ を含まない。これは冪ではなく、同じ語の2つの異なる因子分解が原因である。

**括弧族 $n=3$ の失敗（長さの変わる交換）。**
\[
 x=(\texttt{[<a>[aa},\texttt{]]}),\qquad
 y=(\texttt{[<a><a>},\texttt{]}).
\]
$E=(\texttt{[<<a>>},\texttt{]},\varepsilon)$、$F=(\texttt{[},\texttt{]<<a>>},\varepsilon)$ で、
$E$ は両方を受け、$F$ は $x$ だけを受ける。ここでは $E[x]$ と $E[y]$ の長さが異なる。
木の再結合で長さが変わるタイプである。

### 3.4 型ごとの最短長について

付録の生出力の各 `T2_ROW` の `type_min_all` に、その族・その $n$ の**全内容型**について
`[型, 最短長, その型の語数]` を列挙した。表には希少型だけを示した。
たとえば TM 水準別 $n=4$ では51型あり、最短長16の型 `ab` は1語、最短長12の型 `Cab` は15語である。
Thue $n=3$ では59型あり、pure 語の型 `abc` は1語で長さ12、マーカーを含む型 `0abc` は3語で長さ12である。
「希少型が一語だけ」という設計は、マーカーを含む型では必ずしも成り立たない。
pure 語の型に限れば一語である。

---

## 4. T3：浅い倍増型の系統探索

### 4.1 探索空間

依頼の形の特別な場合
\[
 X_i\to \alpha X_{i-1}\beta Y_{i-1}\gamma\mid\delta,\qquad
 Y_i\to \alpha Y_{i-1}\beta X_{i-1}\gamma\mid\delta
\]
を、$\alpha,\beta,\gamma,\delta\in\{\varepsilon,\mathtt a,\mathtt b,\mathtt c,\mathtt{ab},\mathtt{ba}\}$ の
$6^4=1296$ 通りで列挙した。$X_0=\mathtt a$、$Y_0=\mathtt b$、開始は $X_n$。
これは $\delta$ を定数語に限った形であり、依頼にあった `δ X_{i-1} ε` 型の1段短絡は含まない。
$\alpha,\ldots,\varepsilon$ を長さ0〜2の語から選ぶ完全な $13^5$ 探索は行っていない。
$Y_n$ は $X_n$ から到達不能なので除いた（reduced のため）。
各型につき $n=1,2,3$ で、言語を最大500語まで列挙し、$d=1,2$ の内容型代入可能性を全数検査した。
500語を超える型は打ち切った（出力 `skipped`）。

### 4.2 結果

| $n$ | テンプレート数 | 打切り | f1 生存 | f2 生存 | f2 生存かつ2語以上 | 宣言した条件を満たす候補 |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 1296 | 0 | 1063 | 1063 | 846 | 831 |
| 2 | 1296 | 0 | 406 | 84 | 14 | 10 |
| 3 | 1296 | 0 | 216 | **3** | **0** | **0** |

ここで「宣言した条件を満たす」は、2語以上、$\mu^\star=\max_w|w|$、$\bar\theta\le4n+4$ の3条件を
すべて満たすこととした（スクリプトの `viable_by_declared_criteria`）。
$n=1,2$ の値は語長が小さいための見かけ上のもので、漸近の証拠ではない。

$n=3$ でファンアウト2に生き残った3型は、いずれも**1語言語**である。

| $\alpha,\beta,\gamma,\delta$ | 語数 | 最長 | $\lVert G\rVert$ | $\bar\theta$ | 型数 |
|---|---:|---:|---:|---:|---:|
| $(\varepsilon,\varepsilon,\mathtt c,\varepsilon)$ | 1 | 15 | 45 | 15 | 1 |
| $(\mathtt c,\varepsilon,\varepsilon,\varepsilon)$ | 1 | 15 | 45 | 15 | 1 |
| $(\varepsilon,\varepsilon,\varepsilon,\varepsilon)$ | 1 | 8 | 40 | 8 | 1 |

1語言語は §2.3 のとおり自明に代入可能である。しかし $\bar\theta$ が語長そのもの（15 または 8）であり、
「希少型の最短長が超多項式で $\bar\theta$ が多項式」という分離は起きない。
$n=1,2$ の「候補」は語長が2〜10程度で、漸近の証拠にはならない。
**$n=3$ の時点で、2語以上あり f2 に通り $\bar\theta\le 16$ という型は一つもない。**

この探索は浅い型のごく一部である。長さ2のパラメータを5個並べる完全な $13^5$ 探索は行っていない。
また $n\le3$ なので、「指数的な希少型」を数値で確認すること自体ができない。
したがってこの節の結論は「この1296型の範囲では候補なし」であり、一般の不可能性ではない。

---

## 5. T4：失敗の構造

### 5.1 分類の集計

T2 の22行のうち、失敗した10行の**最初の証人**を分類した。すべての違反を列挙した分類ではない。

| 分類 | 件数 | 例 |
|---|---:|---|
| $d=1$ の長さ変化（マーカーの挿入・削除） | 3 | `##` と `#`、$E=(\varepsilon,\varepsilon)$、$F=(\varepsilon,\#)$ |
| $d=2$ 同一ホストの曖昧分解 | 5 | Thue $n=3$、基塊族 $n=3,4$ |
| $d=2$ 非冪のブロック交換 | 1 | TM 水準別 $n=4$ |
| $d=2$ 非冪の長さ変化交換 | 1 | 括弧族 $n=3$ |
| $d=2$ 冪の移行（power transfer） | **0** | 検査範囲では検出されず |

### 5.2 何が族を潰しているか

1. **マーカーの重複（$d=1$）。** 単一マーカー族では `##` と `#` が同じ内容型 $\{\#\}$ を持ち、
   $E=(\varepsilon,\varepsilon)$ が両方を受け、$F=(\varepsilon,\#)$ で `###` と `##` に分かれる。
   これは冪の移行の最も退化した形である。水準ごとにマーカーを分ければ消えるが、アルファベットが増える。

2. **同一ホストの曖昧分解（$d=2$）。** 2つの異なる二組 $x,y$ が同じ文脈 $E$ で**同じ語**を作る。
   Thue $n=3$ の例では $E[x]=E[y]=\mathtt{abcdbabcbac}$ である。
   この場合、$x$ と $y$ は同じ語の異なる因子分解であり、$u^5$ は不要である。
   K2 の古典的な反例もこの型である（$E[x]=E[y]=\mathtt{cbaabc}$）。
   したがって「同じ因子の繰り返し」を排除するだけでは、$c_\Sigma$ のファンアウト2を守れない。

3. **非冪のブロック交換（$d=2$）。** TM $n=4$ の $x=(\mathtt{baab},\mathtt{ba})$、$y=(\mathtt{ba},\mathtt{abba})$。
   $E[x]=\mathtt{EbaabCba}$ と $E[y]=\mathtt{EbaCabba}$ は異なるが、同じ枠で2つのブロックを入れ替えた形である。
   ここでも冪はない。

4. **長さの変わる木の再結合（$d=2$）。** 括弧族 $n=3$ では、$E[x]$ と $E[y]$ の長さが異なる。
   これは「同じ長さのブロックを移す」形の補題では捕まらない。

**理論側への含意。** 原稿の `lem:power-transfer` は $u^{a+d+b+2}$ を含む語から
$u$ の冪を二穴で移す補題である。今回の $c_\Sigma$ の失敗は、その補題の前提を満たさない形で先に起きている。
より一般的な二穴移送の補題には、少なくとも
(a) 同一ホストの2つの因子分解、
(b) 異なるホスト間のブロック交換、
(c) 長さの変わる再結合
を扱う必要がある。

---

## 6. T5：証明できること

### 6.1 水準別マーカー付き Thue–Morse 族の定量評価（全 $n$）

§3.1 (B) の文法 $G_n$ を再掲する。
\[
 S\to U_n,\quad U_0\to\mathtt a,\quad V_0\to\mathtt b,
\]
$1\le i\le n$ に対し
\[
 U_i\to U_{i-1}V_{i-1}\mid d_i,
\]
$1\le i<n$ に対し
\[
 V_i\to V_{i-1}U_{i-1}\mid e_i.
\]
$d_i,e_i$ は相異なる1文字マーカーで、$\{a,b\}$ にも互いにも含まれない。

**定理2.** すべての $n\ge1$ について次が成り立つ。

1. $G_n$ は reduced で good、ファンアウト1、ランク2。
2. $\lVert G_n\rVert=16n+2$、$\bar\theta_{G_n}=n+1$。
3. マーカーを使わない語はただ一つで、Thue–Morse 語 $t_n$ であり、$|t_n|=2^n$。
4. $c_\Sigma(t_n)=\{a,b\}$ であり、内容型 $\{a,b\}$ を持つ語は $t_n$ のみ。
   したがって $\mu_{\{a,b\}}(L_n)=2^n$。

**証明。**
(1) 各非終端は開始から到達可能で、各規則は非空の右辺を持つ。線形・非削除・非置換・非併合は
右辺の並びから直ちに成り立つ。ランクは2以下である。

(2) 非終端は $S$、$U_0,\ldots,U_n$、$V_0,\ldots,V_{n-1}$ の $2n+2$ 個。
規則数は $1+2+2n+2(n-1)=4n+1$。
大きさは
\[
 (2n+2)+3+4+7n+7(n-1)=16n+2.
\]
ここで $S\to U_n$ は $3$、$U_0\to a,V_0\to b$ は各 $2$、
各 $U_i$ の2規則は $5+2=7$、各 $V_i$（$i<n$）の2規則も $7$ である。

$\bar\theta=n+1$ を示す。上界：各規則を使う成功文で長さ $n+1$ 以下のものを構成する。
- $S\to U_n$：$U_n\to d_n$ で長さ1。
- $U_i\to d_i$：$U_n,\ldots,U_{i+1}$ を二股規則で下り、各段の兄弟 $V_j$ をマーカー $e_j$ にする。
  長さは $1+(n-i)\le n$。
- $V_i\to e_i$（$i<n$）：$U_{i+1}$ まで下り、その先の兄弟をマーカーにして長さ $1+(n-i-1)\le n$。
- $U_0\to a$ と $V_0\to b$：$U_n$ から $U_0$ まで二股で下り、兄弟 $V_1,\ldots,V_{n-1}$ をマーカー、
  $V_0$ を $b$ にすると長さ $n+1$。
- $U_i\to U_{i-1}V_{i-1}$（$i\ge1$）：両子をマーカーにすると長さ $2+(n-i)\le n+1$。
- $V_i\to V_{i-1}U_{i-1}$（$i\ge1$）：同様に高々 $n+1$。

下界：$U_0\to a$ を使う成功文は、$U_n,\ldots,U_1$ のすべてで二股規則を使わなければならない。
各段の兄弟 $V_{j}$ は非空の語を生成するので、文の長さは少なくとも $1+n=n+1$ である。
よって $\theta_{G_n}(U_0\to a)=n+1$、したがって $\bar\theta=n+1$。

(3) マーカーを使わない導出では、各 $U_i,V_i$ にマーカーなしの規則がただ一つずつあるので、
導出は完全に強制される。帰納法で $U_i$ の語 $u_i$、$V_i$ の語 $v_i$ が一意に定まり、
$u_0=a,v_0=b$、$u_i=u_{i-1}v_{i-1}$、$v_i=v_{i-1}u_{i-1}$、$|u_i|=|v_i|=2^i$ である。
開始 $U_n$ の語は $u_n=t_n$ で、長さ $2^n$。

(4) マーカー規則を使えば $d_i$ または $e_i$ が語に残る（非削除性）。
したがって内容型が $\{a,b\}$ になるのはマーカーなしの $t_n$ だけである。
$n\ge1$ で $t_n$ は $a,b$ の両方を含むので、その内容型はちょうど $\{a,b\}$ である。
よって $\mu_{\{a,b\}}=|t_n|=2^n$。$\square$

**系3.** 上の族は、すべての $n$ で
\[
 \lVert G_n\rVert=16n+2=O(n),\qquad \bar\theta_{G_n}=n+1=O(n),\qquad
 \mu_{\{a,b\}}(L_n)=2^n
\]
を満たす。$n\le3$ ではファンアウト2にも属するが、$n=4$ では属さない（§3.3）。
したがって、この族は「望ましい量的性質をすべて持ち、$n=4$ で壊れる」実例である
（$n\le3$ ではファンアウト2に属し、$n=4$ では属さない。$n\ge5$ は未解決）。

**注意。** 系3は全 $n$ のファンアウト2失敗を主張しない。$n\ge5$ の失敗は未解決である。
またマーカーが水準ごとに異なるので、固定アルファベットの族ではない。

### 6.2 私用文字を持つ有限言語（証明）

**補題4（私用文字補題、内容型付け）。** 有限言語 $L$ の各語 $w$ に、$w$ にだけ現れ、他の $L$ の語には現れない
文字 $p_w$ が存在するとする。このとき $L$ はすべての $f\ge1$ について
$(f,c_\Sigma)$-代入可能である。すなわち $L\in\mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}$ がすべての $f$ で成り立つ。
（一般の型付け $s$ では、私用文字が同じ $s$-型に潰れ得るので、この主張は成り立たない。）

**証明。** $d\ge1$、$x,y\in(\Sigma^+)^d$、$c_\Sigma^{(d)}(x)=c_\Sigma^{(d)}(y)$、
$E\in\mathcal E_d$、$E[x],E[y]\in L$ とする。$w=E[x]$、$v=E[y]$ と置く。
$w\ne v$ と仮定する。$p_w$ は $w$ に現れる。
もし $p_w$ が $E$ の固定部分に現れるなら、$p_w$ は $v=E[y]$ にも現れ、$p_w$ の私用性に反する。
よって $p_w$ はある穴 $i$ に入る $x_i$ に現れる。
内容型が成分ごとに等しいので、同じ成分 $y_i$ にも $p_w$ が現れる（台集合が等しい）。
すると $p_w$ は $v=E[y]$ に現れ、やはり私用性に反する。
したがって $w=v$ である。

$E[x]=E[y]$ で $E$ は固定された文脈だから、成分ごとに $x_i=y_i$ である。
実際、$E=v_0\square_1v_1\cdots\square_dv_d$ とし、左から順に比べれば、
$v_0x_1v_1\cdots=v_0y_1v_1\cdots$ から $x_1v_1\cdots=y_1v_1\cdots$、
長さを比べるか右消約性で $x_1=y_1$、以下同様に $x_i=y_i$ が従う。
よって共通文脈を持つ同型の2組は一致する。$\square$

**系5.** $L=\{p_1\mathtt a^{m_1}\mathtt b,\ldots,p_k\mathtt a^{m_k}\mathtt b\}$ のように、
各語に固有の文字 $p_i$ を付けた有限言語は、任意のファンアウトで $c_\Sigma$-代入可能である。
スクリプトの `T5_PRIVATE_LETTERS` は15語のこの形を $d=1,2$ で検査し、通ることを確認した。

**限界。** 固定アルファベット $\Sigma$ では、私用文字は高々 $|\Sigma|$ 個しかない。
したがって私用文字補題だけでは、$n$ とともに語数が増える固定アルファベットの族を作れない。
実際、§3 の族は $n$ 個のマーカーを必要とし、固定アルファベットの反例にはなっていない。
この補題は「なぜ水準別マーカーが効くのか」の説明であり、SL の下界ではない。

### 6.3 括弧族の統計（検算）

原稿の括弧族について、$n\le4$ で
\[
 \lVert G_n\rVert=13n+7,\qquad \bar\theta_{G_n}=4n
\]
を確認した（$20,33,46,59$ と $4,8,12,16$）。
これは原稿の $O(n)$ 評価の範囲内であり、新しい主張ではない。

### 6.4 この報告の限界

- 判定器は有限言語の $d=1,2$ のみを厳密に扱う。$f>2$ や無限言語には、そのままでは使えない。
- 候補の族は $n=4$（一部 $n=3$）までしか全数検査していない。$n=4$ の失敗は証明だが、全 $n$ ではない。
- 水準別マーカー族は固定アルファベットではない。原稿の設定への反例ではない。
- T3 の1296型は、依頼の5パラメータ形の特別な場合（定数 $\delta$）であり、$13^5$ の完全探索ではない。
- T4 の分類は各族の最初の証人による。すべての違反の分類ではない。
- $c_\Sigma$ は半束型付けの中で最も大きいクラスである。$c_\Sigma$ の有限探索の不在は、
  SL の不在の証明ではない。逆に、$c_\Sigma$ の全言語について不在が証明できれば SL も排除できる。

### 6.5 下界の作用素について

今回、超多項式の下界を**証明した族はない**。したがって「どの作用素の下界か」を新たに主張することはない。
仮に §3 の族が全 $n$ でファンアウト2に属さず、$\lVert G_n\rVert\bar\theta_{G_n}=O(n^2)$ であったなら、
原稿の `prop:rare-type` により、$\mathcal B^{\le r}_{2,c_\Sigma}$、$\mathcal B_{2,c_\Sigma}$、
および $\mathcal C^{\mathrm{mcf}}_{2,c_\Sigma}$ 全体で特徴標本を持つ任意の set-driven 作用素に対して
\[
 \|F\|_+\ge \mu_{\{a,b\}}(L_n)+1=2^n+1
\]
が従う。しかしこの含意の前提（全 $n$ のファンアウト2所属の失敗）は、いまは $n=4$ でしか示されていない。

---

## 7. 結論と残る問題

1. **判定器は厳密に動く。** 有限言語については、$d=1,2$ の代入可能性を完全に判定し、
   証人を文字列の連結で再検査できる。既知の $K_2$・$P_{N,2}$・括弧族の挙動と一致した。

2. **非重複性は十分でない。** Thue–Morse 背骨、Thue の平方のない形態素、基塊を変えた族のいずれも、
   $u^5$ を含まないのに $c_\Sigma$ のファンアウト2で落ちる。
   TM 水準別は $n\le3$ で通って $n=4$ で落ちるので、「小さい $n$ の一致」は証明にならない。

3. **失敗の主因は冪の移行だけではない。** 検査した最初の証人10件のうち、冪の移行は0件であった。
   同一ホストの曖昧分解が5件、非冪のブロック交換が1件、長さ変化が1件、$d=1$ のマーカー重複が3件である。
   とくに同一ホスト型は、K2 の古典的反例とも共通する。
   理論側の二穴移送補題は、この形を扱う必要がある。

4. **候補は見つからなかった。** 1296個の浅い倍増型の $n\le3$ 全数探索では、
   $n=3$ のファンアウト2生存者はすべて1語言語で、$\bar\theta$ が語長に等しかった。
   多項式 $\bar\theta$ と超多項式の希少型を両立する候補は、この範囲にはない。

5. **固定アルファベットが最大の障害。** 水準別マーカーは $n$ 個の文字を要する。
   私用文字補題はその仕組みを証明するが、固定アルファベットでは語数が $|\Sigma|$ で抑えられる。
   固定アルファベットでマーカーを共有すると、今回観測された $d=1$ の重複や同一ホストの曖昧分解が戻ってくる。
   この障壁を突破する方法は、今回の計算では見つからなかった。

6. **SL の境界は未解決。** 今回の結果は、$c_\Sigma$ という最も細かい（したがって最も大きい）クラスで
   候補を探したが、$n=4$ の障害に当たった、という報告である。
   SL のクラスは $c_\Sigma$ の部分クラスなので、一般に「$c_\Sigma$ に族が存在しない」ことが証明できれば
   SL にも存在しない。しかし今回示したのは有限範囲の不在だけであり、その全称命題は証明していない。
   固定アルファベット上で、全 $n$ のファンアウト2代入可能性・多項式 $\lVert G_n\rVert$・多項式 $\bar\theta$・
   超多項式の希少型を同時に持つ族の存在は、依然として未解決である。

### 次の計算・証明の候補

- TM 水準別の $n=4$ 証人を $n\ge5$ に持ち上げる。マーカー列 $e_4\cdots e_{n-1}$ を後置したとき、
  $F[y]$ の非所属が保存されるかを、文法の一意解析で証明する。
- 固定アルファベットで、水準を「マーカーの個数」ではなく「マーカーの位置パターン」で符号化する。
  ただし $d=1$ の重複を避けるため、同じマーカーの連続を文法で禁止する必要がある。
- 同一ホストの曖昧分解を排除する十分条件を定式化する。
  たとえば「すべての語が一意に因子分解される」ことと、$c_\Sigma$ の代入可能性の関係を調べる。
- $n=4$ の全数検査を、$n=5$ の 458,330 語でも実行可能なように、
  分布の共有を記号的に判定するアルゴリズムへ置き換える。

---

## 付録A：実行環境とコマンド

- OS：Windows（PowerShell）
- Python：`Python 3.12.10`（`sys.version.split()[0]`、CPython）
- 標準ライブラリのみ。外部パッケージなし。
- 作業ディレクトリ：`C:\Users\Owner\Documents\GitHub\Papers\02-v2-lg-fanout-boundary\reviews`
- 実行コマンド：
  ```text
  py -3 check_sl_fanout2_search.py all
  ```
- 終了コード：0
- 実行時間：149.039 秒（内訳：T1 88.248 秒、T2 4.123 秒、T3 56.351 秒、T4 0.000 秒、T5 0.316 秒）
- 出力：下に標準出力の全文を貼る。

`all` は T1, T2, T3, T4, T5 を順に実行する。引数なしの
`py -3 check_sl_fanout2_search.py` は T1, T2, T4, T5 を実行する（T3 は約56秒かかるため別モード）。
`t1`, `t2`, `t3`, `t4`, `t5` の個別モードもある。

### 出力全文

```text
ENV {"argv": ["check_sl_fanout2_search.py", "all"], "implementation": "cpython", "modes": ["t1", "t2", "t3", "t4", "t5"], "python": "3.12.10", "script_version": "1.0 (2026-11-01)"}
T1_BEGIN {"version": "1.0 (2026-11-01)"}
T1_BRACKETED {"cert1": null, "f1_U1": true, "f1_content": true, "f1_trivial_implies_CE": true, "maxlen": 4, "n": 1, "size": 20, "theta": 4, "words": 2}
T1_BRACKETED {"cert1": null, "f1_U1": true, "f1_content": true, "f1_trivial_implies_CE": true, "maxlen": 10, "n": 2, "size": 33, "theta": 8, "words": 6}
T1_BRACKETED {"cert1": null, "f1_U1": true, "f1_content": true, "f1_trivial_implies_CE": true, "maxlen": 22, "n": 3, "size": 46, "theta": 12, "words": 42}
T1_BRACKETED {"cert1": null, "f1_U1": true, "f1_content": true, "f1_trivial_implies_CE": true, "maxlen": 46, "n": 4, "size": 59, "theta": 16, "words": 1806}
T1_K2 {"cert1": null, "cert2": {"E": ["", "a", "c"], "Ex": "cbaabc", "Ey": "cbaabc", "F": ["bca", "ab", ""], "Fx": "bcacbaabb", "Fy": "bcacbabab", "class": "d2-same-host ambiguous factorization", "d": 2, "x": ["cba", "b"], "y": ["cb", "ab"]}, "f1_U1": true, "f2_U1": false, "language": ["bbaabbaabb", "bbaabcacb", "bcacbaabb", "bcaccacb", "cbaabc", "ccacc"], "words": 6}
T1_P {"N": 1, "cert1": null, "cert2": null, "f1_U1": true, "f2_U1": true, "words": 4}
T1_P {"N": 2, "cert1": null, "cert2": null, "f1_U1": true, "f2_U1": true, "words": 4}
T1_P {"N": 3, "cert1": null, "cert2": null, "f1_U1": true, "f2_U1": true, "words": 4}
T1_P {"N": 4, "cert1": null, "cert2": null, "f1_U1": true, "f2_U1": true, "words": 4}
T1_P {"N": 5, "cert1": null, "cert2": null, "f1_U1": true, "f2_U1": true, "words": 4}
T1_SINGLETON {"cert": null, "f2_content": true, "word": "abba"}
T1_END {}
TIME {"seconds": 88.248, "section": "t1"}
T2_BEGIN {"version": "1.0 (2026-11-01)"}
T2_BINARIZATION {"n": 1, "same_language": true, "words": 2}
T2_BINARIZATION {"n": 2, "same_language": true, "words": 9}
T2_BINARIZATION {"n": 3, "same_language": true, "words": 136}
T2_ROW {"V": 3, "f1_content": true, "f2_content": true, "family": "bracketed", "first_u3": null, "first_u5": null, "good": true, "maxlen": 4, "mu_star": 4, "n": 1, "no_u3": true, "no_u5": true, "num_types": 2, "pure_count": 1, "pure_lengths": [4], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 4, "rarest_type": "[]a", "reduced": true, "rules": 4, "size": 20, "theta": 4, "type_min_all": [["<>a", 3, 1], ["[]a", 4, 1]], "type_min_top": [["[]a", 4, 1], ["<>a", 3, 1]], "words": 2}
T2_ROW {"V": 4, "f1_content": true, "f2_content": true, "family": "bracketed", "first_u3": null, "first_u5": null, "good": true, "maxlen": 10, "mu_star": 10, "n": 2, "no_u3": true, "no_u5": true, "num_types": 3, "pure_count": 1, "pure_lengths": [10], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 10, "rarest_type": "[]a", "reduced": true, "rules": 6, "size": 33, "theta": 8, "type_min_all": [["<>[]a", 6, 4], ["<>a", 5, 1], ["[]a", 10, 1]], "type_min_top": [["[]a", 10, 1], ["<>[]a", 6, 4], ["<>a", 5, 1]], "words": 6}
T2_ROW {"V": 5, "f1_content": true, "f2_content": false, "family": "bracketed", "first_u3": {"u": "<", "word": "<<<a>>>"}, "first_u5": null, "good": true, "maxlen": 22, "mu_star": 22, "n": 3, "no_u3": false, "no_u5": true, "num_types": 3, "pure_count": 1, "pure_lengths": [22], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 22, "rarest_type": "[]a", "reduced": true, "rules": 8, "size": 46, "theta": 12, "type_min_all": [["<>[]a", 8, 40], ["<>a", 7, 1], ["[]a", 22, 1]], "type_min_top": [["[]a", 22, 1], ["<>[]a", 8, 40], ["<>a", 7, 1]], "words": 42}
T2_CERT2 {"cert": {"E": ["[<<a>>", "]", ""], "Ex": "[<<a>>[<a>[aa]]]", "Ey": "[<<a>>[<a><a>]]", "F": ["[", "]<<a>>", ""], "Fx": "[[<a>[aa]<<a>>]]", "Fy": "[[<a><a>]<<a>>]", "class": "d2-nonpower length-changing exchange", "d": 2, "x": ["[<a>[aa", "]]"], "y": ["[<a><a>", "]"]}, "family": "bracketed", "n": 3}
T2_ROW {"V": 4, "f1_content": true, "f2_content": true, "family": "tm_level_markers", "first_u3": null, "first_u5": null, "good": true, "maxlen": 2, "mu_star": 2, "n": 1, "no_u3": true, "no_u5": true, "num_types": 2, "pure_count": 1, "pure_lengths": [2], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 2, "rarest_type": "ab", "reduced": true, "rules": 5, "size": 18, "theta": 2, "type_min_all": [["C", 1, 1], ["ab", 2, 1]], "type_min_top": [["ab", 2, 1], ["C", 1, 1]], "words": 2}
T2_ROW {"V": 6, "f1_content": true, "f2_content": true, "family": "tm_level_markers", "first_u3": null, "first_u5": null, "good": true, "maxlen": 4, "mu_star": 4, "n": 2, "no_u3": true, "no_u5": true, "num_types": 5, "pure_count": 1, "pure_lengths": [4], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 4, "rarest_type": "ab", "reduced": true, "rules": 9, "size": 34, "theta": 3, "type_min_all": [["Cab", 3, 1], ["Cc", 2, 1], ["D", 1, 1], ["ab", 4, 1], ["abc", 3, 1]], "type_min_top": [["ab", 4, 1], ["Cab", 3, 1], ["abc", 3, 1], ["Cc", 2, 1], ["D", 1, 1]], "words": 5}
T2_ROW {"V": 8, "f1_content": true, "f2_content": true, "family": "tm_level_markers", "first_u3": null, "first_u5": null, "good": true, "maxlen": 8, "mu_star": 8, "n": 3, "no_u3": true, "no_u5": true, "num_types": 15, "pure_count": 1, "pure_lengths": [8], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 8, "rarest_type": "ab", "reduced": true, "rules": 13, "size": 50, "theta": 4, "type_min_all": [["CDab", 4, 1], ["CDc", 3, 1], ["Cab", 6, 3], ["Cabc", 5, 8], ["Cabd", 4, 1], ["Cc", 4, 1], ["Ccd", 3, 1], ["Dab", 5, 1], ["Dabc", 4, 1], ["Dd", 2, 1], ["E", 1, 1], ["ab", 8, 1], ["abc", 6, 3], ["abcd", 4, 1], ["abd", 5, 1]], "type_min_top": [["ab", 8, 1], ["Cab", 6, 3], ["abc", 6, 3], ["Cabc", 5, 8], ["Dab", 5, 1], ["abd", 5, 1], ["CDab", 4, 1], ["Cabd", 4, 1], ["Cc", 4, 1], ["Dabc", 4, 1]], "words": 26}
T2_ROW {"V": 10, "f1_content": true, "f2_content": false, "family": "tm_level_markers", "first_u3": null, "first_u5": null, "good": true, "maxlen": 16, "mu_star": 16, "n": 4, "no_u3": true, "no_u5": true, "num_types": 51, "pure_count": 1, "pure_lengths": [16], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 16, "rarest_type": "ab", "reduced": true, "rules": 17, "size": 66, "theta": 5, "type_min_all": [["CDEab", 5, 1], ["CDEc", 4, 1], ["CDab", 8, 17], ["CDabc", 7, 104], ["CDabcd", 7, 32], ["CDabd", 6, 16], ["CDabe", 5, 1], ["CDc", 6, 3], ["CDcd", 5, 8], ["CDce", 4, 1], ["CEab", 7, 3], ["CEabc", 6, 8], ["CEabd", 5, 1], ["CEc", 5, 1], ["CEcd", 4, 1], ["Cab", 12, 15], ["Cabc", 9, 224], ["Cabcd", 7, 104], ["Cabce", 6, 8], ["Cabd", 8, 17], ["Cabde", 5, 1], ["Cabe", 7, 3], ["Cc", 8, 1], ["Ccd", 6, 3], ["Ccde", 4, 1], ["Cce", 5, 1], ["DEab", 6, 1], ["DEabc", 5, 1], ["DEd", 3, 1], ["Dab", 10, 3], ["Dabc", 8, 17], ["Dabcd", 6, 16], ["Dabce", 5, 1], ["Dabd", 7, 8], ["Dabe", 6, 1], ["Dd", 4, 1], ["Dde", 3, 1], ["Eab", 9, 1], ["Eabc", 7, 3], ["Eabcd", 5, 1], ["Eabd", 6, 1], ["Ee", 2, 1], ["F", 1, 1], ["ab", 16, 1], ["abc", 12, 15], ["abcd", 8, 17], ["abcde", 5, 1], ["abce", 7, 3], ["abd", 10, 3], ["abde", 6, 1], ["abe", 9, 1]], "type_min_top": [["ab", 16, 1], ["Cab", 12, 15], ["abc", 12, 15], ["Dab", 10, 3], ["abd", 10, 3], ["Cabc", 9, 224], ["Eab", 9, 1], ["abe", 9, 1], ["CDab", 8, 17], ["Cabd", 8, 17]], "words": 677}
T2_CERT2 {"cert": {"E": ["E", "C", ""], "Ex": "EbaabCba", "Ey": "EbaCabba", "F": ["C", "ba", "CCba"], "Fx": "CbaabbabaCCba", "Fy": "CbabaabbaCCba", "class": "d2-nonpower block exchange", "d": 2, "x": ["baab", "ba"], "y": ["ba", "abba"]}, "family": "tm_level_markers", "n": 4}
T2_ROW {"V": 4, "f1_content": true, "f2_content": true, "family": "tm_single_marker", "first_u3": null, "first_u5": null, "good": true, "maxlen": 2, "mu_star": 2, "n": 1, "no_u3": true, "no_u5": true, "num_types": 2, "pure_count": 1, "pure_lengths": [2], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 2, "rarest_type": "ab", "reduced": true, "rules": 5, "size": 18, "theta": 2, "type_min_all": [["#", 1, 1], ["ab", 2, 1]], "type_min_top": [["ab", 2, 1], ["#", 1, 1]], "words": 2}
T2_ROW {"V": 4, "f1_content": true, "f2_content": true, "family": "tm_bracket_marker", "first_u3": null, "first_u5": null, "good": true, "maxlen": 3, "mu_star": 3, "n": 1, "no_u3": true, "no_u5": true, "num_types": 2, "pure_count": 1, "pure_lengths": [2], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 3, "rarest_type": "[]a", "reduced": true, "rules": 5, "size": 21, "theta": 3, "type_min_all": [["[]a", 3, 1], ["ab", 2, 1]], "type_min_top": [["[]a", 3, 1], ["ab", 2, 1]], "words": 2}
T2_ROW {"V": 7, "f1_content": true, "f2_content": true, "family": "thue_squarefree_level_markers", "first_u3": null, "first_u5": null, "good": true, "maxlen": 3, "mu_star": 3, "n": 1, "no_u3": true, "no_u5": true, "num_types": 2, "pure_count": 1, "pure_lengths": [3], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 3, "rarest_type": "abc", "reduced": true, "rules": 8, "size": 31, "theta": 3, "type_min_all": [["D", 1, 1], ["abc", 3, 1]], "type_min_top": [["abc", 3, 1], ["D", 1, 1]], "words": 2}
T2_ROW {"V": 6, "f1_content": false, "f2_content": null, "family": "tm_single_marker", "first_u3": null, "first_u5": null, "good": true, "maxlen": 4, "mu_star": 4, "n": 2, "no_u3": true, "no_u5": true, "num_types": 3, "pure_count": 1, "pure_lengths": [4], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 4, "rarest_type": "ab", "reduced": true, "rules": 9, "size": 34, "theta": 3, "type_min_all": [["#", 1, 2], ["#ab", 3, 2], ["ab", 4, 1]], "type_min_top": [["ab", 4, 1], ["#ab", 3, 2], ["#", 1, 2]], "words": 5}
T2_CERT1 {"cert": {"E": ["", ""], "Ex": "##", "Ey": "#", "F": ["", "#"], "Fx": "###", "Fy": "##", "class": "d1-length-changing (insertion/deletion)", "d": 1, "x": ["##"], "y": ["#"]}, "family": "tm_single_marker", "n": 2}
T2_ROW {"V": 6, "f1_content": true, "f2_content": true, "family": "tm_bracket_marker", "first_u3": null, "first_u5": null, "good": true, "maxlen": 6, "mu_star": 5, "n": 2, "no_u3": true, "no_u5": true, "num_types": 3, "pure_count": 1, "pure_lengths": [4], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 5, "rarest_type": "[]a", "reduced": true, "rules": 9, "size": 43, "theta": 5, "type_min_all": [["[]a", 5, 1], ["[]ab", 4, 4], ["ab", 4, 1]], "type_min_top": [["[]a", 5, 1], ["[]ab", 4, 4], ["ab", 4, 1]], "words": 6}
T2_ROW {"V": 12, "f1_content": true, "f2_content": true, "family": "thue_squarefree_level_markers", "first_u3": null, "first_u5": null, "good": true, "maxlen": 6, "mu_star": 6, "n": 2, "no_u3": true, "no_u5": true, "num_types": 9, "pure_count": 1, "pure_lengths": [6], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 6, "rarest_type": "0abc", "reduced": true, "rules": 16, "size": 63, "theta": 5, "type_min_all": [["0Dac", 4, 1], ["0Dd", 3, 1], ["0abc", 6, 1], ["0abcd", 5, 1], ["Dabc", 4, 1], ["Dbd", 3, 1], ["E", 1, 1], ["abc", 6, 1], ["abcd", 5, 1]], "type_min_top": [["0abc", 6, 1], ["abc", 6, 1], ["0abcd", 5, 1], ["abcd", 5, 1], ["0Dac", 4, 1], ["Dabc", 4, 1], ["0Dd", 3, 1], ["Dbd", 3, 1], ["E", 1, 1]], "words": 9}
T2_ROW {"V": 8, "f1_content": false, "f2_content": null, "family": "tm_single_marker", "first_u3": {"u": "#", "word": "###"}, "first_u5": null, "good": true, "maxlen": 8, "mu_star": 8, "n": 3, "no_u3": false, "no_u5": true, "num_types": 3, "pure_count": 1, "pure_lengths": [8], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 8, "rarest_type": "ab", "reduced": true, "rules": 13, "size": 50, "theta": 4, "type_min_all": [["#", 1, 4], ["#ab", 4, 19], ["ab", 8, 1]], "type_min_top": [["ab", 8, 1], ["#ab", 4, 19], ["#", 1, 4]], "words": 24}
T2_CERT1 {"cert": {"E": ["", ""], "Ex": "##", "Ey": "#", "F": ["", "###"], "Fx": "#####", "Fy": "####", "class": "d1-length-changing (insertion/deletion)", "d": 1, "x": ["##"], "y": ["#"]}, "family": "tm_single_marker", "n": 3}
T2_ROW {"V": 8, "f1_content": false, "f2_content": null, "family": "tm_bracket_marker", "first_u3": {"u": "[", "word": "[[[a]]]"}, "first_u5": null, "good": true, "maxlen": 12, "mu_star": 8, "n": 3, "no_u3": false, "no_u5": true, "num_types": 3, "pure_count": 1, "pure_lengths": [8], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 8, "rarest_type": "ab", "reduced": true, "rules": 13, "size": 65, "theta": 8, "type_min_all": [["[]a", 7, 1], ["[]ab", 6, 40], ["ab", 8, 1]], "type_min_top": [["ab", 8, 1], ["[]a", 7, 1], ["[]ab", 6, 40]], "words": 42}
T2_CERT1 {"cert": {"E": ["[", "]]"], "Ex": "[ab[b]]", "Ey": "[[ab]]", "F": ["", "[b]]"], "Fx": "ab[b[b]]", "Fy": "[ab[b]]", "class": "d1-length-changing (insertion/deletion)", "d": 1, "x": ["ab[b"], "y": ["[ab"]}, "family": "tm_bracket_marker", "n": 3}
T2_ROW {"V": 17, "f1_content": true, "f2_content": false, "family": "thue_squarefree_level_markers", "first_u3": null, "first_u5": null, "good": true, "maxlen": 12, "mu_star": 12, "n": 3, "no_u3": true, "no_u5": true, "num_types": 59, "pure_count": 1, "pure_lengths": [12], "pure_unique": true, "rank": 2, "rarest_count": 3, "rarest_min": 12, "rarest_type": "0abc", "reduced": true, "rules": 24, "size": 95, "theta": 6, "type_min_all": [["01DE", 4, 1], ["01Dabc", 7, 8], ["01Dabcd", 8, 6], ["01Dac", 7, 1], ["01Dace", 6, 1], ["01Dbd", 6, 2], ["01Dd", 6, 1], ["01Dde", 5, 1], ["01Eabc", 6, 1], ["01abc", 11, 3], ["01abcd", 10, 3], ["01abcde", 7, 1], ["01abce", 8, 1], ["0DEac", 5, 1], ["0DEd", 4, 1], ["0Dabc", 8, 8], ["0Dabcd", 7, 22], ["0Dac", 8, 1], ["0Dacd", 7, 2], ["0Dacde", 6, 2], ["0Dace", 7, 1], ["0Dbd", 6, 2], ["0Dd", 6, 1], ["0Dde", 5, 1], ["0Eabc", 7, 1], ["0Eabcd", 6, 1], ["0abc", 12, 3], ["0abcd", 10, 9], ["0abcde", 7, 3], ["0abce", 9, 1], ["1DEb", 4, 1], ["1Dabc", 7, 3], ["1Dabcd", 8, 2], ["1Dabce", 6, 1], ["1Dbd", 6, 1], ["1Dbde", 5, 1], ["1Eabc", 6, 1], ["1Ee", 3, 1], ["1abc", 11, 1], ["1abcd", 10, 1], ["1abcde", 7, 1], ["1abce", 8, 1], ["DEabc", 5, 1], ["DEbd", 4, 1], ["Dabc", 8, 3], ["Dabcd", 7, 8], ["Dabcde", 6, 2], ["Dabce", 7, 1], ["Dbd", 6, 1], ["Dbde", 5, 1], ["Eabc", 7, 1], ["Eabcd", 6, 1], ["Eace", 4, 1], ["Ede", 3, 1], ["F", 1, 1], ["abc", 12, 1], ["abcd", 10, 3], ["abcde", 7, 3], ["abce", 9, 1]], "type_min_top": [["0abc", 12, 3], ["abc", 12, 1], ["01abc", 11, 3], ["1abc", 11, 1], ["01abcd", 10, 3], ["0abcd", 10, 9], ["1abcd", 10, 1], ["abcd", 10, 3], ["0abce", 9, 1], ["abce", 9, 1]], "words": 136}
T2_CERT2 {"cert": {"E": ["", "b", "c"], "Ex": "abcdbabcbac", "Ey": "abcdbabcbac", "F": ["", "0", "c"], "Fx": "abcdba0cbac", "Fy": "abcd0abcbac", "class": "d2-same-host ambiguous factorization", "d": 2, "x": ["abcdba", "cba"], "y": ["abcd", "abcba"]}, "family": "thue_squarefree_level_markers", "n": 3}
T2_ROW {"V": 6, "f1_content": true, "f2_content": true, "family": "tm_base_ab_ba", "first_u3": null, "first_u5": null, "good": true, "maxlen": 8, "mu_star": 8, "n": 2, "no_u3": true, "no_u5": true, "num_types": 5, "pure_count": 1, "pure_lengths": [8], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 8, "rarest_type": "ab", "reduced": true, "rules": 9, "size": 36, "theta": 5, "type_min_all": [["Cab", 5, 1], ["Cc", 2, 1], ["D", 1, 1], ["ab", 8, 1], ["abc", 5, 1]], "type_min_top": [["ab", 8, 1], ["Cab", 5, 1], ["abc", 5, 1], ["Cc", 2, 1], ["D", 1, 1]], "words": 5}
T2_ROW {"V": 6, "f1_content": true, "f2_content": true, "family": "tm_base_ba_ab", "first_u3": null, "first_u5": null, "good": true, "maxlen": 8, "mu_star": 8, "n": 2, "no_u3": true, "no_u5": true, "num_types": 5, "pure_count": 1, "pure_lengths": [8], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 8, "rarest_type": "ab", "reduced": true, "rules": 9, "size": 36, "theta": 5, "type_min_all": [["Cab", 5, 1], ["Cc", 2, 1], ["D", 1, 1], ["ab", 8, 1], ["abc", 5, 1]], "type_min_top": [["ab", 8, 1], ["Cab", 5, 1], ["abc", 5, 1], ["Cc", 2, 1], ["D", 1, 1]], "words": 5}
T2_ROW {"V": 8, "f1_content": true, "f2_content": false, "family": "tm_base_ab_ba", "first_u3": null, "first_u5": null, "good": true, "maxlen": 16, "mu_star": 16, "n": 3, "no_u3": true, "no_u5": true, "num_types": 15, "pure_count": 1, "pure_lengths": [16], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 16, "rarest_type": "ab", "reduced": true, "rules": 13, "size": 52, "theta": 6, "type_min_all": [["CDab", 6, 1], ["CDc", 3, 1], ["Cab", 10, 3], ["Cabc", 7, 8], ["Cabd", 6, 1], ["Cc", 4, 1], ["Ccd", 3, 1], ["Dab", 9, 1], ["Dabc", 6, 1], ["Dd", 2, 1], ["E", 1, 1], ["ab", 16, 1], ["abc", 10, 3], ["abcd", 6, 1], ["abd", 9, 1]], "type_min_top": [["ab", 16, 1], ["Cab", 10, 3], ["abc", 10, 3], ["Dab", 9, 1], ["abd", 9, 1], ["Cabc", 7, 8], ["CDab", 6, 1], ["Cabd", 6, 1], ["Dabc", 6, 1], ["abcd", 6, 1]], "words": 26}
T2_CERT2 {"cert": {"E": ["D", "a", ""], "Ex": "Dbaababba", "Ey": "Dbaababba", "F": ["C", "abbaa", ""], "Fx": "Cbaababbaabba", "Fy": "Cbaabbaababba", "class": "d2-same-host ambiguous factorization", "d": 2, "x": ["baab", "bba"], "y": ["ba", "babba"]}, "family": "tm_base_ab_ba", "n": 3}
T2_ROW {"V": 8, "f1_content": true, "f2_content": false, "family": "tm_base_ba_ab", "first_u3": null, "first_u5": null, "good": true, "maxlen": 16, "mu_star": 16, "n": 3, "no_u3": true, "no_u5": true, "num_types": 15, "pure_count": 1, "pure_lengths": [16], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 16, "rarest_type": "ab", "reduced": true, "rules": 13, "size": 52, "theta": 6, "type_min_all": [["CDab", 6, 1], ["CDc", 3, 1], ["Cab", 10, 3], ["Cabc", 7, 8], ["Cabd", 6, 1], ["Cc", 4, 1], ["Ccd", 3, 1], ["Dab", 9, 1], ["Dabc", 6, 1], ["Dd", 2, 1], ["E", 1, 1], ["ab", 16, 1], ["abc", 10, 3], ["abcd", 6, 1], ["abd", 9, 1]], "type_min_top": [["ab", 16, 1], ["Cab", 10, 3], ["abc", 10, 3], ["Dab", 9, 1], ["abd", 9, 1], ["Cabc", 7, 8], ["CDab", 6, 1], ["Cabd", 6, 1], ["Dabc", 6, 1], ["abcd", 6, 1]], "words": 26}
T2_CERT2 {"cert": {"E": ["D", "b", ""], "Ex": "Dabbabaab", "Ey": "Dabbabaab", "F": ["C", "abbab", ""], "Fx": "Cabbaabbabaab", "Fy": "Cababbababaab", "class": "d2-same-host ambiguous factorization", "d": 2, "x": ["abba", "aab"], "y": ["ab", "abaab"]}, "family": "tm_base_ba_ab", "n": 3}
T2_ROW {"V": 10, "f1_content": true, "f2_content": false, "family": "tm_base_ab_ba", "first_u3": null, "first_u5": null, "good": true, "maxlen": 32, "mu_star": 32, "n": 4, "no_u3": true, "no_u5": true, "num_types": 51, "pure_count": 1, "pure_lengths": [32], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 32, "rarest_type": "ab", "reduced": true, "rules": 17, "size": 68, "theta": 7, "type_min_all": [["CDEab", 7, 1], ["CDEc", 4, 1], ["CDab", 12, 17], ["CDabc", 9, 104], ["CDabcd", 9, 32], ["CDabd", 8, 16], ["CDabe", 7, 1], ["CDc", 6, 3], ["CDcd", 5, 8], ["CDce", 4, 1], ["CEab", 11, 3], ["CEabc", 8, 8], ["CEabd", 7, 1], ["CEc", 5, 1], ["CEcd", 4, 1], ["Cab", 20, 15], ["Cabc", 11, 224], ["Cabcd", 9, 104], ["Cabce", 8, 8], ["Cabd", 12, 17], ["Cabde", 7, 1], ["Cabe", 11, 3], ["Cc", 8, 1], ["Ccd", 6, 3], ["Ccde", 4, 1], ["Cce", 5, 1], ["DEab", 10, 1], ["DEabc", 7, 1], ["DEd", 3, 1], ["Dab", 18, 3], ["Dabc", 12, 17], ["Dabcd", 8, 16], ["Dabce", 7, 1], ["Dabd", 11, 8], ["Dabe", 10, 1], ["Dd", 4, 1], ["Dde", 3, 1], ["Eab", 17, 1], ["Eabc", 11, 3], ["Eabcd", 7, 1], ["Eabd", 10, 1], ["Ee", 2, 1], ["F", 1, 1], ["ab", 32, 1], ["abc", 20, 15], ["abcd", 12, 17], ["abcde", 7, 1], ["abce", 11, 3], ["abd", 18, 3], ["abde", 10, 1], ["abe", 17, 1]], "type_min_top": [["ab", 32, 1], ["Cab", 20, 15], ["abc", 20, 15], ["Dab", 18, 3], ["abd", 18, 3], ["Eab", 17, 1], ["abe", 17, 1], ["CDab", 12, 17], ["Cabd", 12, 17], ["Dabc", 12, 17]], "words": 677}
T2_CERT2 {"cert": {"E": ["", "a", "e"], "Ex": "Dbaababbae", "Ey": "Dbaababbae", "F": ["", "CbaabCa", "baab"], "Fx": "DbaabCbaabCabbabaab", "Fy": "DbaCbaabCababbabaab", "class": "d2-same-host ambiguous factorization", "d": 2, "x": ["Dbaab", "bba"], "y": ["Dba", "babba"]}, "family": "tm_base_ab_ba", "n": 4}
T2_ROW {"V": 10, "f1_content": true, "f2_content": false, "family": "tm_base_ba_ab", "first_u3": null, "first_u5": null, "good": true, "maxlen": 32, "mu_star": 32, "n": 4, "no_u3": true, "no_u5": true, "num_types": 51, "pure_count": 1, "pure_lengths": [32], "pure_unique": true, "rank": 2, "rarest_count": 1, "rarest_min": 32, "rarest_type": "ab", "reduced": true, "rules": 17, "size": 68, "theta": 7, "type_min_all": [["CDEab", 7, 1], ["CDEc", 4, 1], ["CDab", 12, 17], ["CDabc", 9, 104], ["CDabcd", 9, 32], ["CDabd", 8, 16], ["CDabe", 7, 1], ["CDc", 6, 3], ["CDcd", 5, 8], ["CDce", 4, 1], ["CEab", 11, 3], ["CEabc", 8, 8], ["CEabd", 7, 1], ["CEc", 5, 1], ["CEcd", 4, 1], ["Cab", 20, 15], ["Cabc", 11, 224], ["Cabcd", 9, 104], ["Cabce", 8, 8], ["Cabd", 12, 17], ["Cabde", 7, 1], ["Cabe", 11, 3], ["Cc", 8, 1], ["Ccd", 6, 3], ["Ccde", 4, 1], ["Cce", 5, 1], ["DEab", 10, 1], ["DEabc", 7, 1], ["DEd", 3, 1], ["Dab", 18, 3], ["Dabc", 12, 17], ["Dabcd", 8, 16], ["Dabce", 7, 1], ["Dabd", 11, 8], ["Dabe", 10, 1], ["Dd", 4, 1], ["Dde", 3, 1], ["Eab", 17, 1], ["Eabc", 11, 3], ["Eabcd", 7, 1], ["Eabd", 10, 1], ["Ee", 2, 1], ["F", 1, 1], ["ab", 32, 1], ["abc", 20, 15], ["abcd", 12, 17], ["abcde", 7, 1], ["abce", 11, 3], ["abd", 18, 3], ["abde", 10, 1], ["abe", 17, 1]], "type_min_top": [["ab", 32, 1], ["Cab", 20, 15], ["abc", 20, 15], ["Dab", 18, 3], ["abd", 18, 3], ["Eab", 17, 1], ["abe", 17, 1], ["CDab", 12, 17], ["Cabd", 12, 17], ["Dabc", 12, 17]], "words": 677}
T2_CERT2 {"cert": {"E": ["", "b", "e"], "Ex": "Dabbabaabe", "Ey": "Dabbabaabe", "F": ["", "CabbaCb", "abba"], "Fx": "DabbaCabbaCbaababba", "Fy": "DabCabbaCbabaababba", "class": "d2-same-host ambiguous factorization", "d": 2, "x": ["Dabba", "aab"], "y": ["Dab", "abaab"]}, "family": "tm_base_ba_ab", "n": 4}
T2_END {"rows": 22}
TIME {"seconds": 4.123, "section": "t2"}
T3_BEGIN {"library": ["", "a", "b", "c", "ab", "ba"], "shape": "X_i -> alpha X_{i-1} beta Y_{i-1} gamma | delta; Y_i -> alpha Y_{i-1} beta X_{i-1} gamma | delta", "templates": 1296}
T3_SUMMARY {"n": 1, "skipped": 0, "survive_f1": 1063, "survive_f2": 1063, "survive_f2_multiword": 846, "templates": 1296, "top": [{"maxlen": 8, "mu_star": 8, "num_types": 1, "params": ["ab", "ab", "ab", ""], "size": 22, "theta": 8, "words": 1}, {"maxlen": 8, "mu_star": 8, "num_types": 2, "params": ["ab", "ab", "ab", "a"], "size": 24, "theta": 8, "words": 2}, {"maxlen": 8, "mu_star": 8, "num_types": 2, "params": ["ab", "ab", "ab", "b"], "size": 24, "theta": 8, "words": 2}, {"maxlen": 8, "mu_star": 8, "num_types": 2, "params": ["ab", "ab", "ab", "c"], "size": 24, "theta": 8, "words": 2}, {"maxlen": 8, "mu_star": 8, "num_types": 1, "params": ["ab", "ab", "ba", ""], "size": 22, "theta": 8, "words": 1}, {"maxlen": 8, "mu_star": 8, "num_types": 2, "params": ["ab", "ab", "ba", "a"], "size": 24, "theta": 8, "words": 2}, {"maxlen": 8, "mu_star": 8, "num_types": 2, "params": ["ab", "ab", "ba", "b"], "size": 24, "theta": 8, "words": 2}, {"maxlen": 8, "mu_star": 8, "num_types": 2, "params": ["ab", "ab", "ba", "c"], "size": 24, "theta": 8, "words": 2}, {"maxlen": 8, "mu_star": 8, "num_types": 1, "params": ["ab", "ba", "ab", ""], "size": 22, "theta": 8, "words": 1}, {"maxlen": 8, "mu_star": 8, "num_types": 2, "params": ["ab", "ba", "ab", "a"], "size": 24, "theta": 8, "words": 2}], "viable_by_declared_criteria": 831}
T3_VIABLE {"maxlen": 2, "mu_star": 2, "num_types": 2, "params": ["", "", "", "a"], "size": 18, "theta": 2, "words": 2}
T3_VIABLE {"maxlen": 2, "mu_star": 2, "num_types": 2, "params": ["", "", "", "b"], "size": 18, "theta": 2, "words": 2}
T3_VIABLE {"maxlen": 2, "mu_star": 2, "num_types": 2, "params": ["", "", "", "c"], "size": 18, "theta": 2, "words": 2}
T3_VIABLE {"maxlen": 2, "mu_star": 2, "num_types": 1, "params": ["", "", "", "ba"], "size": 19, "theta": 2, "words": 2}
T3_VIABLE {"maxlen": 3, "mu_star": 3, "num_types": 2, "params": ["", "", "a", "a"], "size": 19, "theta": 3, "words": 2}
T3_VIABLE {"maxlen": 3, "mu_star": 3, "num_types": 2, "params": ["", "", "a", "b"], "size": 19, "theta": 3, "words": 2}
T3_VIABLE {"maxlen": 3, "mu_star": 3, "num_types": 2, "params": ["", "", "a", "c"], "size": 19, "theta": 3, "words": 2}
T3_VIABLE {"maxlen": 3, "mu_star": 3, "num_types": 2, "params": ["", "", "b", "a"], "size": 19, "theta": 3, "words": 2}
T3_VIABLE {"maxlen": 3, "mu_star": 3, "num_types": 2, "params": ["", "", "b", "b"], "size": 19, "theta": 3, "words": 2}
T3_VIABLE {"maxlen": 3, "mu_star": 3, "num_types": 2, "params": ["", "", "b", "c"], "size": 19, "theta": 3, "words": 2}
T3_SUMMARY {"n": 2, "skipped": 0, "survive_f1": 406, "survive_f2": 84, "survive_f2_multiword": 14, "templates": 1296, "top": [{"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["", "a", "b", "c"], "size": 40, "theta": 7, "words": 5}, {"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["", "b", "a", "c"], "size": 40, "theta": 7, "words": 5}, {"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["a", "", "b", "c"], "size": 40, "theta": 7, "words": 5}, {"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["a", "b", "", "c"], "size": 40, "theta": 7, "words": 5}, {"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["b", "", "a", "c"], "size": 40, "theta": 7, "words": 5}, {"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["b", "a", "", "c"], "size": 40, "theta": 7, "words": 5}, {"maxlen": 7, "mu_star": 7, "num_types": 4, "params": ["", "", "b", "c"], "size": 37, "theta": 5, "words": 5}, {"maxlen": 7, "mu_star": 7, "num_types": 4, "params": ["", "a", "", "c"], "size": 37, "theta": 5, "words": 5}, {"maxlen": 7, "mu_star": 7, "num_types": 4, "params": ["", "b", "", "c"], "size": 37, "theta": 5, "words": 5}, {"maxlen": 7, "mu_star": 7, "num_types": 4, "params": ["b", "", "", "c"], "size": 37, "theta": 5, "words": 5}], "viable_by_declared_criteria": 10}
T3_VIABLE {"maxlen": 7, "mu_star": 7, "num_types": 4, "params": ["", "", "b", "c"], "size": 37, "theta": 5, "words": 5}
T3_VIABLE {"maxlen": 7, "mu_star": 7, "num_types": 4, "params": ["", "a", "", "c"], "size": 37, "theta": 5, "words": 5}
T3_VIABLE {"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["", "a", "b", "c"], "size": 40, "theta": 7, "words": 5}
T3_VIABLE {"maxlen": 7, "mu_star": 7, "num_types": 4, "params": ["", "b", "", "c"], "size": 37, "theta": 5, "words": 5}
T3_VIABLE {"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["", "b", "a", "c"], "size": 40, "theta": 7, "words": 5}
T3_VIABLE {"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["a", "", "b", "c"], "size": 40, "theta": 7, "words": 5}
T3_VIABLE {"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["a", "b", "", "c"], "size": 40, "theta": 7, "words": 5}
T3_VIABLE {"maxlen": 7, "mu_star": 7, "num_types": 4, "params": ["b", "", "", "c"], "size": 37, "theta": 5, "words": 5}
T3_VIABLE {"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["b", "", "a", "c"], "size": 40, "theta": 7, "words": 5}
T3_VIABLE {"maxlen": 10, "mu_star": 10, "num_types": 3, "params": ["b", "a", "", "c"], "size": 40, "theta": 7, "words": 5}
T3_SUMMARY {"n": 3, "skipped": 0, "survive_f1": 216, "survive_f2": 3, "survive_f2_multiword": 0, "templates": 1296, "top": [{"maxlen": 15, "mu_star": 15, "num_types": 1, "params": ["", "", "c", ""], "size": 45, "theta": 15, "words": 1}, {"maxlen": 15, "mu_star": 15, "num_types": 1, "params": ["c", "", "", ""], "size": 45, "theta": 15, "words": 1}, {"maxlen": 8, "mu_star": 8, "num_types": 1, "params": ["", "", "", ""], "size": 40, "theta": 8, "words": 1}], "viable_by_declared_criteria": 0}
T3_END {}
TIME {"seconds": 56.351, "section": "t3"}
T4_BEGIN {}
T4_COUNTS {"d1-length-changing (insertion/deletion)": 3, "d2-nonpower block exchange": 1, "d2-nonpower length-changing exchange": 1, "d2-same-host ambiguous factorization": 5}
T4_EXAMPLE {"cert": {"E": ["", ""], "Ex": "##", "Ey": "#", "F": ["", "#"], "Fx": "###", "Fy": "##", "class": "d1-length-changing (insertion/deletion)", "d": 1, "x": ["##"], "y": ["#"]}, "class": "d1-length-changing (insertion/deletion)", "family": "tm_single_marker", "n": 2}
T4_EXAMPLE {"cert": {"E": ["E", "C", ""], "Ex": "EbaabCba", "Ey": "EbaCabba", "F": ["C", "ba", "CCba"], "Fx": "CbaabbabaCCba", "Fy": "CbabaabbaCCba", "class": "d2-nonpower block exchange", "d": 2, "x": ["baab", "ba"], "y": ["ba", "abba"]}, "class": "d2-nonpower block exchange", "family": "tm_level_markers", "n": 4}
T4_EXAMPLE {"cert": {"E": ["[<<a>>", "]", ""], "Ex": "[<<a>>[<a>[aa]]]", "Ey": "[<<a>>[<a><a>]]", "F": ["[", "]<<a>>", ""], "Fx": "[[<a>[aa]<<a>>]]", "Fy": "[[<a><a>]<<a>>]", "class": "d2-nonpower length-changing exchange", "d": 2, "x": ["[<a>[aa", "]]"], "y": ["[<a><a>", "]"]}, "class": "d2-nonpower length-changing exchange", "family": "bracketed", "n": 3}
T4_EXAMPLE {"cert": {"E": ["", "b", "c"], "Ex": "abcdbabcbac", "Ey": "abcdbabcbac", "F": ["", "0", "c"], "Fx": "abcdba0cbac", "Fy": "abcd0abcbac", "class": "d2-same-host ambiguous factorization", "d": 2, "x": ["abcdba", "cba"], "y": ["abcd", "abcba"]}, "class": "d2-same-host ambiguous factorization", "family": "thue_squarefree_level_markers", "n": 3}
T4_NONPOWER {"cert": {"E": ["[<<a>>", "]", ""], "Ex": "[<<a>>[<a>[aa]]]", "Ey": "[<<a>>[<a><a>]]", "F": ["[", "]<<a>>", ""], "Fx": "[[<a>[aa]<<a>>]]", "Fy": "[[<a><a>]<<a>>]", "class": "d2-nonpower length-changing exchange", "d": 2, "x": ["[<a>[aa", "]]"], "y": ["[<a><a>", "]"]}, "family": "bracketed", "n": 3}
T4_NONPOWER {"cert": {"E": ["E", "C", ""], "Ex": "EbaabCba", "Ey": "EbaCabba", "F": ["C", "ba", "CCba"], "Fx": "CbaabbabaCCba", "Fy": "CbabaabbaCCba", "class": "d2-nonpower block exchange", "d": 2, "x": ["baab", "ba"], "y": ["ba", "abba"]}, "family": "tm_level_markers", "n": 4}
T4_END {}
TIME {"seconds": 0.0, "section": "t4"}
T5_BEGIN {}
T5_PRIVATE_LETTERS {"cert1": null, "cert2": null, "f1_content": true, "f2_content": true, "words": 15}
T5_TM_STATS {"V": 4, "n": 1, "pure_count": 1, "pure_lengths": [2], "rules": 5, "size": 18, "size_formula_16n_plus_2": true, "theta": 2}
T5_TM_STATS {"V": 6, "n": 2, "pure_count": 1, "pure_lengths": [4], "rules": 9, "size": 34, "size_formula_16n_plus_2": true, "theta": 3}
T5_TM_STATS {"V": 8, "n": 3, "pure_count": 1, "pure_lengths": [8], "rules": 13, "size": 50, "size_formula_16n_plus_2": true, "theta": 4}
T5_TM_STATS {"V": 10, "n": 4, "pure_count": 1, "pure_lengths": [16], "rules": 17, "size": 66, "size_formula_16n_plus_2": true, "theta": 5}
T5_BRACKETED_STATS {"maxlen": 4, "n": 1, "size": 20, "theta": 4, "words": 2}
T5_BRACKETED_STATS {"maxlen": 10, "n": 2, "size": 33, "theta": 8, "words": 6}
T5_BRACKETED_STATS {"maxlen": 22, "n": 3, "size": 46, "theta": 12, "words": 42}
T5_BRACKETED_STATS {"maxlen": 46, "n": 4, "size": 59, "theta": 16, "words": 1806}
T5_END {}
TIME {"seconds": 0.316, "section": "t5"}
DONE {"seconds": 149.039}
```

