<!-- PART 1/3 START -->
# v1 / v2 比較査読報告 — Information and Computation 投稿適性

**評価日**：2026-10-30　**対象**：Takayuki Kuriyama の fixed finite-semigroup typing 下の MCFG 特徴データ長に関する２原稿

**版の同定（Git blob SHA）**

- **v1** — `02_fixed-h-mcfg/main.tex`：`17858cdfac03203c2814bc0d01806a340bd4b814`（4,354行）。[GitHub の原稿](https://github.com/growupkuriyama-hub/papers/blob/main/02_fixed-h-mcfg/main.tex)
- **v2** — `02-v2-lg-fanout-boundary/main.tex`：`6955a0db2eec542917f3e331c2441c3b3df51b8a`（4,120行）。[GitHub の原稿](https://github.com/growupkuriyama-hub/papers/blob/main/02-v2-lg-fanout-boundary/main.tex)
- 再構成指示書：`INSTRUCTIONS_FOR_AI.md`、blob `536fbace3826e0a4f22632874089f51a22f006b9`。[GitHub](https://github.com/growupkuriyama-hub/papers/blob/main/02-v2-lg-fanout-boundary/INSTRUCTIONS_FOR_AI.md)
- 退避原稿：`parked/parked_from_v1.tex`、blob `6e0a980ce414318e910634cd0ba5ff4d78bacf8d`。[GitHub](https://github.com/growupkuriyama-hub/papers/blob/main/02-v2-lg-fanout-boundary/parked/parked_from_v1.tex)

## 総合判定

**投稿の母体としては v2 を選ぶ。ただし、現状の v2 をそのまま I&C に投稿することには反対する。**
**v2 は定理 A–C によって、局所群の上界・fan-out 1 の境界・fan-out 2 の現象を一本の論文に整理できた。**
**一方、定理 A(ii) の量化は構成に必要なアルファベット条件を落としており、新設の `cor:trivial-exact` は「最大の特性標本長」と記したため文字どおり偽である。**
**これらを修正し、MCFG 固有の実例を一つ戻せば、v2 は v1 より有望。現状提出時の判定予想は v1＝major revision、v2＝reject 寄りで、修正後の v2＝major revision を出発点と見る。採択確率の数値化はできない。**

### 評価方法・限界

両方の `main.tex` 全ソースを取得し、見出し・ラベル・定理の宣言・全体構成を照合した。v2 は序論から参考文献まで（付録 A–K を含む）を通読・重点検証し、v1 は序論、固有部分、結論を直接読み、移植された本文・付録を v2 と差分照合した。共有ラベル130個のうち109個の「ラベルから次のラベルまで」の区間が文字列一致し、残る差分も節移動・加筆を含めて確認した。**これはソースの一致の検査であって、共有された全補題に対する独立の形式検証ではない。** 新しい数学については下記 §3 に証明の論理と数値計算を示す。両ソースには未解決の `\ref` および重複 `\label` は検出されなかった。

前作については、両稿の §1 `tab:companion-overlap` と、提供された TCS 改訂稿 `TCS-D-26-00494_R1.pdf` の要旨・改訂説明を参照した。外部文献全体についての新規性調査は行っていない。点数は**投稿原稿としての現状評価**であり、証明済みの一般定理でない conjecture を成果として数えない。

## 1. 観点別の採点（最重要）

| # | 観点 | v1 | v2 | 優位 | 根拠（具体的な節・label・短い原文引用） |
|---|---|---:|---:|---|---|
| 1 | **主張の明確さ** | 3 | **5** | v2 | v1 §1 は規則・型付け別の上界表を中心に「The bounds hold...」と整理し、多くの結論を併記。v2 §1 `thm:A`–`thm:C` は「The boundary moves at fan-out two」と主軸を明示。ただし A の修正が前提。 |
| 2 | **科学的な強さ・重要性** | **4** | **4** | 同等 | どちらも `thm:local-group-polydata`、`thm:fanout-one-data`、`thm:binary-u1-polydata`、`prop:block-replacement-interface` を含む。v2 の強い看板は主に整理の効果であり、後者３つが新規追加されたわけではない。 |
| 3 | **MCFG 固有の新規性** | **5** | 4 | **v1** | v1 §6 `prop:feature-cross-typed` は非 CFL の交差依存例、`prop:lg-needed-target`・`prop:nonabelian-needed-target` は型付けの真の分離例を構成。v2 §5 `prop:block-replacement-interface` と §8 `thm:binary-u1-polydata` は残す一方、実例３つを退避した。 |
| 4 | **前作との差分の明確さ** | 4 | **5** | v2 | 両版 §1 `tab:companion-overlap` に「Not new at $f=1$」「not new」を明記。v2 はさらに「Our contribution is the encoded-length analysis and the boundary results above」とまとめ、`prop:binary-u1-weight-slice` も加えた。 |
| 5 | **数学的な正しさ** | **3** | 2 | **v1** | v1 の `prop:linear-factor-all-fanout` は冒頭で「Let $\Sigma$ contain $4f+1$ distinct letters」と必要条件を明記。一方 v2 §1 `thm:A(ii)` は「every typing $s$」と無条件化し、v2 §6 `cor:trivial-exact` は「largest total length of a characteristic sample」と書く。後者は反例で偽（§3.2）。共通証明の完全な正当性を保証する点数ではない。 |
| 6 | **主張と証明の一致** | **3** | 2 | **v1** | v1 §1 の lower-bound 説明・結論にも「under every fixed typing」という過大な要約があるが、命題本文 `prop:linear-factor-all-fanout` は条件付き。v2 `thm:A(ii)` と `cor:trivial-exact` は**定理本文自体**が証明の条件と一致しない。 |
| 7 | **構成の一貫性** | 2 | **4** | v2 | v1 §4 `sec:char-data`、§5 `sec:further`、§6 `sec:comparison` に上界・ランク・比較・下界が分散。v2 は §5 `sec:upper`、§6 `sec:linear`、§7 `sec:fanout-one`、§8 `sec:fanout-two` と A→B→C の順に配置。 |
| 8 | **読みやすさ・導入** | 3 | **4** | v2 | v1 §1 の regime 表は一覧性が高いが、中心となる問いが後方に分散。v2 §1「for which comparison biases is this length polynomial, and does the answer depend on the fan-out?」は問題設定が鮮明。反面、非 CFL の具体例が消えた。 |
| 9 | **長さと密度** | 2 | **3** | v2 | v1 約50頁で §6 比較・本文のランク1定理などに枝葉が多い。v2 47頁／本文約26頁でランク1 `thm:rankone-polydata` を付録 K に移した。ただし §3 `prop:reconstruction-soundness`、`prop:completeness` の再説明はまだ長い。 |
| 10 | **未解決問題の提示** | 3 | **5** | v2 | v1 §7 `op:fanout-two` と `rem:fanout-one-data(b)` に分散。v2 §9 `op:S1` は二文字 U₁・fan-out 1 に焦点を合わせ、`op:fanout-two` と並べ、条件付き含意を明記。 |
| 11 | **題名・要旨の適切さ** | 2 | **4** | v2 | v1 題名は *Polynomial Upper Bounds...* だが `thm:fanout-one-data` と f=2 の境界を含む。v2 題名 *Local Groups and the Fan-Out Dependence...* は内容を表し、要旨の「the exact order for the trivial typing」にはただし書きが必要。 |
| 12 | **博士論文の一章としての適性** | 3 | **4** | v2 | 両稿の前作比較表 `tab:companion-overlap` は役割を分離。v2 の A–C と `op:S1` は「CFG から MCFG への一般化／境界の変化」を一章の問いとして提示できる。ただし v1 §6 の明示的な非 CFL 言語族は博士論文向き。 |

**合計：v1＝37/60、v2＝46/60。差は＋9点。** これは論文の**編集的・概念的な訴求力**の差であって、v2 の定理が自動的により正しいという意味ではない。

**v2 が悪化した観点は #3・#5・#6。** #3 は「MCFG の力が何を可能にするか」を見せる非 CFL の具体例の削除、#5・#6 は新設定理 A の無条件化と最大値の誤記による。数学の新設部分である `prop:binary-u1-weight-slice` には下記の確認範囲で破綻を発見しなかったものの、この改善だけでは誤った定理本文を相殺できない。

### 版間の構造差（主要ラベル）

| 主題 | v1 | v2 | 評価 |
|---|---|---|---|
| 質的学習 | §3 `sec:learner` | §3 `sec:learner` | ほぼ移植。Yoshinaka の質的枠組みと明確に区別すべき。 |
| 特性データ・型付き厚さ | §4 `sec:char-data` | §4 `sec:char-data` | 理論の基礎は共通。 |
| 局所群の多項式上界 | §4.3 `thm:local-group-polydata` | §5 `thm:local-group-polydata` | 同じ主結果を看板に昇格。 |
| 線形因子の下界 | §4 `prop:linear-factor-all-fanout` | §6 同ラベル、`cor:trivial-exact` 新設 | 新系に定式化上の誤り。 |
| fan-out 1 の境界 | §4.3 `thm:fanout-one-data` | §7 同ラベル、新 `prop:binary-u1-weight-slice` | v2 に実質的な数学上の加筆。 |
| fan-out 2 の境界 | §6.3–6.4 | §8 | 新しい定理ではなく、配置・説明が改善。 |
| ランク1 | §5 `thm:rankone-polydata` | 付録 K | 妥当な移動。 |
| 型付けクラスの分離 | §6.1–6.2 | `parked/` | 読者向けの価値も削っている。 |

<!-- PART 1/3 END -->

<!-- PART 2/3 START -->
## 2. v2 で失われたもの・得られたもの

### 2.1 退避した命題の価値

**(a) 多次元代入可能性との比較：一部を戻すべき。** v1 §6.1 `def:yoshinaka-pd-substitutability` は「$\Cmcf{f}{s_{\mathrm{triv}}}=\YSub{f}\cap f\text{-}\mathrm{MCFL}$」と Yoshinaka の基準との一致を示し、`prop:feature-cross-typed` は

\[
L_R=\{\mathtt a^m\mathtt p_i\mathtt b^n\mathtt c^m\mathtt q_j\mathtt d^n : m,n\ge1,(i,j)\in R\}
\]

という、**本当に fan-out 2 が必要な**言語族を固定した window×$\mathbb Z_2^2$ 型付けで扱う。特に $R=\{(0,0),(0,1),(1,0)\}$ は無型・境界型のみでは代入可能でないという明瞭な違いを示す（退避ファイル `prop:feature-cross-typed` の文と証明）。これは応用寄りの I&C 読者にも、前作との差を説明する力がある。**§1 に例１つ、または §5 末尾に短い命題を復帰**し、詳細証明だけ付録または退避文書とするのがよい。

**(b) 型付けクラスの分離：定理は重要だが全部の証明を本文に戻す必要はない。** v1 §6.2 `prop:lg-needed-target` は $\mathbf{LG}\setminus(\mathbf{LI}\vee\mathbf{Grp})$ に必要なスライディング因子情報を非 CFL のターゲットで示し、`prop:nonabelian-needed-target` は $S_3$ と可換群の違いを実際の MCFG ターゲットで示す。v2 §5 `prop:li-g-strict` は代数的な真の包含を示すが、**「その差が学習される言語の上で効く」**例を失っている。分離の**主張だけを２行表に復帰**、証明は博士論文章・別稿に保存という折衷がよい。

**(c) 一文字巡回群 `prop:unary-cyclic-linear`：退避で妥当。** v1 §7 結論の「$\tau(G,s)\le2m\bar\theta_G$」は上界の精密化として美しい。しかし主題は局所群／fan-out の境界であり、単項アルファベットの改良は中心線から外れる。博士論文の補題に残すと価値を失わない。もっともこの一文字例の存在は、**アルファベットを固定して量化する際の注意**を促すので、v2 の定理 A(ii) の修正には役立つ。

### 2.2 v2 の新規の数学と再構成の正味価値

- **`cor:trivial-exact`：考え方は有益、現在の定理文は不可。** trivial typing における最小特性標本の上界 $O(\|G\|\bar\theta_G)$ とマーカー族の下界 $\Omega(\|G\|\bar\theta_G)$ を合わせる観点は、論文の tightness を読者に伝える。ただし §3.2 に示すとおり「最大の特性標本長」という対象は無限に大きくでき、アルファベット／パラメータ条件も不足。**修正された形式でのみ追加価値を認める。**
- **`prop:binary-u1-weight-slice`：価値あり。** §7 における純語長の二次上界と圧縮ブロック族による等号は、`op:S1` の探索空間を自然な subclass について閉じる。構成例と整合し、§3.3 の論証では定理の核心に問題を発見しなかった。単なる表現変更でなく独立の定量的改善である。
- **定理 A–B–C：編集面の価値が大きい。** A が LG 上界と線形因子、B が f=1 の擬多様体・二文字 U₁、C が f=2 の U₁・二穴移行、という正しい「読者の追跡順」を実現する。**ただし A(ii)・A(iii) の文字どおりの内容を修正した後**でなければ構成のメリットは十分に生きない。

## 3. v2 の数学の重点確認

### 3.1 序論の定理 A・B・C と本文の対応

| 導入定理 | 対応先 | 条件・量化子の照合 | 判定 |
|---|---|---|---|
| A(i) `thm:A(i)` | §5 `thm:local-group-polydata` | 固定 $f,r_{\max},s,\Sigma$、正語像 $\mathsf S\in\mathbf{LG}$、reduced good な $G$ という条件が整合。定理本体は rank $\ge2$ も要求しないため導入側の制約は安全。 | **一致** |
| A(ii) `thm:A(ii)` | §6 `prop:linear-factor-all-fanout` | 導入側は「every typing $s$」。命題側は **$|\Sigma|\ge4f+1$** と明記し、その文字を区別して構成。導入の固定アルファベットはこの条件を満たすとは限らない。 | **不一致／反例あり** |
| A(iii) `thm:A(iii)` | §6 `cor:trivial-exact` | 上界と存在的下界を「最も短い特性標本に対する worst-case」と読み替える必要あり。現在の `largest` は誤った最大化。 | **不正確** |
| B(i) `thm:B(i)` | §7 `thm:fanout-one-data` | **$f=1$, $r_{\max}\ge2$**、擬多様体 $\mathbf V$、$\mathbf V\subseteq\mathbf{LG}$ と uniform polynomial の同値。多項式は型付けに依存可能。 | **一致** |
| B(ii) `thm:B(ii)` | §7 `cor:typing-level-obstruction` | 相異なる２文字が冪等元 $e$、１文字が吸収的冪等元 $z$ に写るという仮定と指数長 $3\cdot2^n-1$ が整合。 | **一致** |
| B(iii) `thm:B(iii)` | §7 `prop:binary-u1-quadratic`、`prop:binary-u1-weight-slice` | 二文字 $\mathtt a\mapsto1,\mathtt b\mapsto\zeta$；$m=n$ で $\|G\|=12n+9=O(\log\bar\theta)$、純語長 $4^n$。重み一定の場合のみ二次上界・等号。 | **一致** |
| C(i) `thm:C(i)` | §8 `thm:binary-u1-polydata` | **$f=2$**, fixed $r_{\max}\ge2$、$O(\|G\|^3\bar\theta^5)$；付録 H の係数 $3^{2r}(3+rC_r)$ と整合。 | **一致** |
| C(ii) `thm:C(ii)` | §8 `thm:doubling-no-lift` | **括弧付きの $L_n$ のみ**を対象。本文は **$n\ge2|\mathsf S|+3$** を要求；導入の「family」は十分大きい $n$ の意味なら正しい。三文字 $K_n$ に一般化していない点は適切。 | **実質一致、閾値追記推奨** |

#### A(ii) の反例：一文字アルファベット

序論は §1 冒頭でアルファベット $\Sigma$ を固定し、「For every $f\ge1$ and every typing $s$ there are finite targets ... $\Omega(\|G\|\bar\theta_G)$」と主張する。しかし `prop:linear-factor-all-fanout` 自身は最初に「Let $\Sigma$ contain $4f+1$ distinct letters」と要求する。

さらに量化子欠落にとどまらず、**$\Sigma=\{\mathtt a\}$、trivial typing、$f=1$ でこの一般化は成り立たない**。有限な $(1,s_{\mathrm{triv}})$-substitutable 言語 $L$ に異なる $\mathtt a^p,\mathtt a^q$（$p<q$）があれば、共通文脈 $(\varepsilon,\varepsilon)$ を持つため二語の分布は等しい。文脈 $(\mathtt a^{q-p},\varepsilon)$ で一方から他方へ移し、さらに反復すると $\mathtt a^{q+j(q-p)}\in L$（$j\ge0$）を得て、$L$ が無限になる。したがって**有限 $L$ の正語部分は高々１語**である。

特に $L_k=\{\mathtt a^{2^k}\}$ は rank-two・reduced good の倍増文法 $A_0\to\mathtt a$、$A_i\to A_{i-1}A_{i-1}$（開始 $A_k$）をもち、$\|G_k\|=O(k)$、$\bar\theta_{G_k}=2^k$。その最小特性標本は $\{\mathtt a^{2^k}\}$ で十分（`def:characteristic-sample`、`prop:reconstruction-soundness` と標本整合性）。最小の good 文法サイズも $k$ とともに発散するが、標本長は $2^k+1$ にとどまり、$\Omega(\|G\|\bar\theta)$ に到達しない。**少なくとも「任意の固定アルファベット・任意の型付け」の A(ii) は偽**である。

**修正案**：A(ii) を「For every fixed $f$, every alphabet with at least $4f+1$ letters, and every typing on that alphabet ...」へ変更。A(iii) も同様に制限するか、より小さいアルファベットで成り立つ別の構成を証明してから強化する。v1 の §1 要旨・§7 結論の「under every fixed typing」も同じ範囲修正が必要。

### 3.2 新 `cor:trivial-exact` — **現状は数学的に偽**

v2 §6 `cor:trivial-exact` の原文は「**the largest total length of a characteristic sample** ... is $\Theta(n\theta)$」。しかし §2 `def:characteristic-sample` は、有限な $F\subseteq L$ が $F\subseteq K\subseteq L$ で作用素が常に $L$ を返すことを要求する。したがって $F$ が特性標本なら **任意の有限 $F'$, $F\subseteq F'\subseteq L$ も特性標本**になる。

反例として trivial typing、$f=1$、$L=\{\mathtt a,\mathtt b\}^+$、good 文法 $S\to SS\mid\mathtt a\mid\mathtt b$ を取る。文法サイズと $\bar\theta_G=2$ は定数。`thm:exact-reconstruction` から有限の特性標本 $F$ が存在するが、$F\cup\{\mathtt a^N\}$ も特性標本で、その長さは $N$ とともに無限大へ伸びる。ゆえに**最大長は $\Theta(n\theta)$ どころか無界**。

証明で使う $t_{\mathrm{typ}}\le\bar\theta$ と `thm:data-from-typed-thickness` は、「**短い特性標本が少なくとも一つ存在する**」ことの上界に過ぎず、全特性標本の長さの上界ではない。`prop:linear-factor-all-fanout` は反対に、特定の有限言語で**すべて**の特性標本に多くの語が必要な下界を出す。両者を合わせる正しい対象はたとえば

\[
\operatorname{cs}_{f,s}(L):=\min\{\|F\|_+:F\text{ is a characteristic sample of }L\},
\]

に対する「与えられた grammar budget のクラス上での**最悪の最小長**」である。ただし、元の構成が $|\Sigma|\ge4f+1$、$q\ge k\ge1$、$\bar\theta=2fq+2^k+2f$ を要するので、**任意の独立な $n,\theta$ に関する二変数 $\Theta(n\theta)$ まで証明されていない**。安全な版は次の二つを別々に述べること。

1. **上界**：trivial typing では任意の reduced good rank-$\le r$ 文法 $G$ に $\operatorname{cs}_{f,s_{\mathrm{triv}}}(L)\le C_{f,r}\|G\|\bar\theta_G+\mathbf1_{\{\varepsilon\in L\}}$。
2. **実現される下界**：$|\Sigma|\ge4f+1$ で固定した $f$ に対し、`prop:linear-factor-all-fanout` の $G^{(f)}_{q,k}$ では $\operatorname{cs}(L^{(f)}_{q,k})=(q+1)(W+1)=\Omega_f(\|G^{(f)}_{q,k}\|\bar\theta_{G^{(f)}_{q,k}})$、かつ文法サイズは最小サイズの定数倍。

この形式なら定理と証明が一致する。`thm:A(iii)`、要旨、§9 Tightness の「exact」は**この限定された sharpness の意味**で書き換えるべき。

### 3.3 新 `prop:binary-u1-weight-slice` の証明監査

**判定：本文の仮定の下で核心の証明は整合。現時点で反例や決定的な飛躍は見つからない。** ただし形式証明器による機械検証ではなく、下記の論理点の人手確認である。

**(i) 場合分けと不等式。** §7 で $\psi_\lambda(w)=|w|_{\mathtt a}+\lambda|w|_{\mathtt b}$ は各成功文脈により非終端 $A$ 上で一定の値 $w_A$ を取る。純語は $\mathtt a^{\ell_A}$ の１種類。`lem:thickness-equivalence(ii)` により $A$ の最短生成語長は $\le\theta$。

- $\lambda\le1$：最短語の重み $w_A\le$ その長さ $\le\theta$、ゆえに $\ell_A\le\theta$。
- $\lambda>1$ かつ $\ell_A<\lambda$：$w_A=\ell_A<\lambda$ なので $\mathtt b$ を含む $A$ の生成物は存在しない。最短純語長も $\le\theta$。
- $\lambda>1$ かつ $\ell_A\ge\lambda$：$\mathtt a^{\ell_A}$ の導出木で、長さ $h\ge\lambda$ だが子は全員 $<\lambda$ の節点を選べる。子の重みはそれぞれ $<\lambda$ なので、重みを保存する他の生成に $\mathtt b$ は現れない。その規則 $R$ の部分木の長さは常に $h$。$R$ を使う最短成功文の外側は重み $W-h$、各文字の重みは $\le\lambda$ なので長さは $\ge(W-h)/\lambda$。よって
  \[
  \theta\ge h+\frac{W-h}{\lambda}\ge \frac W\lambda+\lambda-1,
  \quad W\le\lambda(\theta+1-\lambda)\le\frac{(\theta+1)^2}{4}.
  \]
  第２の不等式は $h\ge\lambda$ と $1-1/\lambda>0$、最後は平方完成から従う。$\ell_A\le W$ なので主張の床関数まで成立。

**改善余地**：該当節点の存在、$A$ の重みが成功文脈から固定されること、$R$ を使う *任意の* 導出が純語長 $h$ を与えることをそれぞれ１文ずつ明示すると査読者の再現が容易。

**(ii) 依存グラフによる評価。** 純型は (i) により $B(\theta)$。$\mathtt b$ を含む生成物がある $A$ から、$\mathtt b$ を明示的に書く規則の左辺まで最短依存パスをとれば、重複非終端なしで長さは高々 $v$。付録 I `lem:app-lf-descent` の

\[
\theta_G(R)=o_B+c_R+\sum_j d_{B_j}
\]

を各辺に適用し、最後の規則の寄与 $\le\theta$、先行する各規則ではパス子の最短長 $d_C\ge1$ を差し引いて $\le\theta-1$。合計は **$\theta+(v-1)(\theta-1)=v(\theta-1)+1$**。計算は整合。最短路が成功するように兄弟を最短生成物で補える（good/reduced）点を本文に補うとよい。

**(iii) 定数。** `cor:distribution-representatives` の上界は $N_{\mathrm{typ}}(1+2\theta+r\tau)$。$|\mathsf S^\sharp|=3$ なので $N_{\mathrm{typ}}\le3^r\|G\|$。$\tau\le t_{\mathrm{typ}}\le\max\{B(\theta),v(\theta-1)+1\}$、$B(\theta)\le\theta^2$、$v\le\|G\|$、$1+2\theta\le3\theta^2$（$\theta\ge1$）から **$3^r(r+3)\|G\|^2\theta^2+\mathbf1_{\{\varepsilon\in L\}}$** が出る。主張と一致。`G_{n,n}` は $\theta=2^{n+1}-1$、$\mu^\star=4^n=(\theta+1)^2/4$、等号も成立。

**射程への注意**：証明は *constant weight* の場合のみ。例 $\{\mathtt{aa},\mathtt{ab},\mathtt{bbb}\}$ は §7 で反例として挙げられ、S1 全体の多項式上界を証明したことにはならない。

### 3.4 `prop:binary-u1-quadratic` と付録 J（v1 からの移植）の監査

**判定：主要３点（代入可能性、圧縮文法、厚さ計算）は整合。明確な穴は確認できない。** v2 §7 `prop:binary-u1-quadratic`、付録 J `app:binary-u1-quadratic` は v1 に既にあった結果であり、v2 の独自新定理として二重計上しない。

1. **言語と代入可能性**：$k=2^m,\ M=2^n$、$L_{m,n}=\{\mathtt a^k,\mathtt b\}^M$。付録の条件「all maximal runs of $\mathtt a$ have length divisible by $k$ and $\psi(w)=M$」は、ブロックへの一意分割を与える。共通文脈を持つ同型 $x,y$ について、$\psi(x)=\psi(y)$。純型なら $x=y$、不純型なら境界ランの剰余 $\alpha\equiv\alpha'$, $\beta\equiv\beta'\pmod{k}$ と内部ランの可除性が一致し、任意文脈への差し替えで「各ランが $k$ の倍数」と総ブロック数が同時に保たれる。従って $(1,s_{U,2})$ 代入可能性が成立する。
2. **小さな文法**：$C_0\to\mathtt a$、$C_j\to C_{j-1}C_{j-1}$、$A_0\to C_m\mid\mathtt b$、$A_i\to A_{i-1}A_{i-1}$、開始 $A_n$。帰納的に $C_j$ は $\mathtt a^{2^j}$、$A_i$ は $2^i$ ブロックの連接。good/reduced、rank 2。§2 `def:standard-mcfg` のサイズ（$|V|$ と規則長）を数えると **$6m+6n+9$** で一致。
3. **厚さ・純語**：付録 J の $d_{A_i}=2^i$、$d_{C_j}=2^j$、$o_{A_i}=M-2^i$、$o_{C_j}=M-1+k-2^j$ を上記の厚さ式に代入すると $A_i$ 側の最短使用文長は $M$、長いブロックを強制する $C_j$ 側は $M+k-1$。したがって **$\bar\theta=M+k-1$**。唯一の純語は $\mathtt a^{kM}$ なので `prop:rare-type` により全特性標本は長さ $kM$ の語を含む。$m=n$ で $\|G\|=12n+9$、$\bar\theta=2^{n+1}-1$、下界 $4^n+1>\bar\theta^2/4$ と整合。

留意点は、単一語の必須性を示す `prop:rare-type` の結論が**クラス全体で特性標本を持つ set-driven operator に対する主張**であって、任意の学習方式の時刻・計算量下界ではないこと。本文はこの区別を概ね守っている。

### 3.5 移植された大定理と付録の残余リスク

`thm:local-group-polydata` は §5 `lem:marked-heavy-window-group`、`prop:block-replacement-interface` と付録 B `lem:lg-buffered-owners`・`lem:local-group-shortest` に依存する。所有者ごとの最大 $f$ ブロック、$4kf+1$ を使う独立集合、順序を保つ有限群の置換選択は相互に整合しているように見える。`thm:binary-u1-polydata` も、付録 H の `lem:app-u1-shallow` → `lem:app-u1-deep` → `lem:app-u1-parikh` を経由し、$C_r=42r(r+1)+96(r+1)$ と $3^{2r}(3+rC_r)$ の積を再現できる。しかし特に `lem:app-u1-parikh` の (P1)–(P6) と非可換群の `lem:order-homogenize` の全場合に対する独立の機械的検証まではしていない。**これらを「証明済みの正しさが確定」とは評価しない。**

`thm:doubling-no-lift` には、§8 `lem:power-transfer` が要求する非空の中間文脈と $n\ge2|\mathsf S|+3$ の閾値が明示されており、括弧付き二倍化族の先頭ランを長くする矛盾の論法は成立する。**三文字版 $K_n$ に同一の結論を拡張しない**現在の慎重さは維持すべき。

<!-- PART 2/3 END -->

<!-- PART 3/3 START -->
## 4. I&C 査読者としての major concerns

### v1 の主要懸念

| 順位 | v1 の懸念と根拠 | v2 で解消したか |
|---|---|---|
| 1 | **焦点が分散**。§1 の多条件上界表、§4 `thm:fanout-one-data`、§5 `thm:rankone-polydata`、§6 `sec:comparison` が同列に並び、MCFG の「新しい境界」が目立たない。 | **かなり解消**：v2 `thm:A`–`thm:C`、§5–8 の一本道。ただし A の誤りが新たな問題。 |
| 2 | **非新規の質的学習の比重**。§3 `prop:reconstruction-soundness`、`prop:completeness`、`thm:exact-reconstruction` は §1 で Yoshinaka に帰属しているにもかかわらず本文の分量が大きい。 | **未解消**：v2 §3 もほぼ同じ。 |
| 3 | **全型付け・全 fan-out の下界という言い過ぎ**。§1 と §7 結論は「under every fixed typing」と述べる一方、`prop:linear-factor-all-fanout` は $4f+1$ 文字を要求。 | **悪化**：v2 `thm:A(ii)` の定理本文に昇格。 |
| 4 | **先行 CFG 研究との重複の印象**。§3 の学習作用素、§4 の fan-out 1 境界、§6 の bracketed doubling が長く、真の新規性である interleaved tuple の扱いが霞む。 | **部分解消**：v2 §1 `tab:companion-overlap` と定理 C を強調。ただし中核の証明配置は据え置き。 |
| 5 | **50頁前後・分散した多数の付録**。§6 型付けの分離は魅力的だが、定理の主眼との関係づけが弱い。 | **部分解消**：47頁まで縮小し §6 を退避。ただし MCFG の応用例が同時に失われた。 |

### v2 の主要懸念

| 順位 | v2 の懸念と根拠 | v1 では存在したか |
|---|---|---|
| **1（致命的）** | **`cor:trivial-exact` が偽**。§6「largest total length of a characteristic sample」は `def:characteristic-sample` の単調性から無界。§3.2 に具体反例。 | **存在しない**：v1 にはこの系がなく、結論の「order is exact」は曖昧だが最大標本とは書いていない。 |
| **2（重大）** | **定理 A(ii) の誤った一般化**。`thm:A(ii)` の任意の typing と固定 Σ は `prop:linear-factor-all-fanout` の $4f+1$ 文字条件を失っている。単項 trivial typing の有限ターゲットで反例あり。 | **前兆あり**：v1 要旨・結論の過大な文章。しかし v1 の命題本体には必要条件が残る。 |
| 3 | **A(iii) の二変数 worst-case の量化が未証明**。`cor:trivial-exact` の $n,\theta$ の任意範囲を、$q\ge k$ と $\theta=2fq+2^k+2f$ の族だけで支えられない。 | **新規**：v1 は個々の族の sharpness に近い記述。 |
| 4 | **MCFG 固有性の可視的証拠を削りすぎた**。§1 `tab:companion-overlap` はあるが、非 CFL の明示構成 `prop:feature-cross-typed`、二つの型付け分離命題が `parked/` に消えた。 | **v1 の方が良い**。 |
| 5 | **独立検証と過大な証明負担**。§8 `thm:binary-u1-polydata` は付録 H `lem:app-u1-parikh(P1–P6)` に依存。§5 の非可換 LG は付録 A–B の定数と順序補題に依存。誤りを発見したという意味ではなく、独立査読の重点点。 | **両版共通**。再構成だけでは解消しない。 |

**査読上の区別**：#1・#2 は実際に反例を与えられる**現行文言の誤り**。#5 は難しい証明に対する**検証要請**であり、証明が誤っていると推定して点を下げる材料にはしていない。

## 5. v2 をさらに良くする具体策（優先度順）

| 優先 | 何を | どこで | なぜ／期待する効果 |
|---|---|---|---|
| **P0–1** | `cor:trivial-exact` を削除するか、最小特徴標本長の存在的上界＋構成族での達成という**厳密に証明可能な二文**へ全面改稿。 | §6 `cor:trivial-exact`、§1 `thm:A(iii)`、要旨、§9 Tightness | 最大標本長が無界という反例を除去。**#5・#6・#11**。最優先。 |
| **P0–2** | `thm:A(ii)` に **$|\Sigma|\ge4f+1$** を明記し、$\Sigma$ を固定する §1 の導入と整合させる。別の下界を証明しない限り「every alphabet」としない。 | §1 `thm:A(ii)`、§6 `prop:linear-factor-all-fanout` 前後、要旨、§9、同様に v1 §1・結論 | 一文字 trivial typing 反例を回避。**#5・#6**。 |
| **P0–3** | 修正後の A(i)–(iii)、B(i)–(iii)、C(i)–(ii) の**仮定・量化・目標変数表**を原稿内で再点検。C(ii) には「for sufficiently large $n$」と閾値を追記。 | §1 `thm:A`–`thm:C` と対応本文 | 要旨から証明への連鎖を一意にする。**#1・#5・#6**。 |
| **P1–4** | `prop:feature-cross-typed` の非 CFL 具体族 $L_R$ を簡略な例として復帰。詳細証明は付録または次稿。 | §1「The setting」直後、または §5 導入 | MCFG 固有の正当化を具体化し、v1 の失点を回復。**#3・#8・#12**。 |
| **P1–5** | `prop:lg-needed-target` と `prop:nonabelian-needed-target` を短い「expressive separation」表で要約し、証明は別管理。 | §5 `thm:local-group-polydata` の後 | LG の厳密包含と非可換群の必要性が学習ターゲット上でも実質的であると示す。**#2・#3・#4**。 |
| **P1–6** | §3 の質的再構成はコンパクトな定理・作用素定義・出典への参照とし、証明を既存の付録 C–E に寄せる。 | §3 `prop:reconstruction-soundness`、`prop:completeness`、`thm:exact-reconstruction` | 分量を削り、メインストーリーを §5–8 に集中。**#7・#8・#9**。 |
| **P1–7** | `prop:linear-factor-sharp` の **3文字版を削除せず、本文では短い注意／系に格下げ**。証明は既存の付録 I に維持。 | §6 `prop:linear-factor-sharp` と `app:linear-factor-fanout` | 全 f 版（$4f+1$ 文字）と重複するが、少ない文字での sharpness は重要。とくに A(ii) のアルファベット条件を正す文脈で意味が増す。**#3・#5・#9**。 |
| **P2–8** | `prop:binary-u1-weight-slice` の (i) 臨界節点・成功文脈、(ii) パス長、(iii) 定数代入を各１–２文補い、定理 B(iii) で **constant-weight 限定**を強調。 | §7 `prop:binary-u1-weight-slice`、§1 `thm:B(iii)` | 証明の読みやすさと S1 との切り分けを改善。**#5・#6・#8・#10**。 |
| **P2–9** | `prop:typed-thickness-exponential` の例の詳細や `lem:thickness-equivalence` の証明を付録へ動かし、§4 は witness–representative の橋に集中。 | §4 `sec:char-data` と付録 D/E | 本文約26頁を22–24頁へ圧縮可能。**#7・#9**。 |
| **P2–10** | 未使用 `\port` マクロ・`xcolor` の行を整理し、独立の証明監査を付録 H `lem:app-u1-parikh`、付録 A `lem:order-homogenize`、新系の再定式化に集中させる。 | プリアンブル、付録 A/H、投稿前検査 | 不要な制作痕跡を消し、長大な証明の誤りリスクを低減。**#5・#8・#11**。 |

### 指定された三つの編集判断

**３文字版の線形因子 `prop:linear-factor-sharp` は残す。** ただし現在 §6 で独立の大命題として展開すると、`prop:linear-factor-all-fanout` の読解を妨げる。本文を「f=1 では３文字で実現できる」と１段落に縮め、詳細命題・証明は付録 I に置くのが最善。より強い「すべての２文字アルファベットで同等の下界」という主張は、この原稿からは出ない。

**47頁（本文26頁＋付録・参考文献21頁）は不適格な長さではない。** I&C の理論論文で、非可換群の同時置換と fan-out 2 の Parikh-saturation に完全な証明が必要なら付録21頁は説明可能。ただし内容密度では本文を22–24頁、全体を42–45頁にする利益がある。**42頁という内部目標を守るために新規な証明を削るべきではない**。新規の数学的誤り修正が先、短縮は後。

**S1 を未解決のまま投稿してよい。** §9 `op:S1` は「二文字 U₁、fan-out 1 で最小特性標本長が $\|G\|,\bar\theta_G$ の多項式か」というはっきりした境界問題。`prop:binary-u1-quadratic` の二次下界と `prop:binary-u1-weight-slice` の constant-weight subclass における鋭い上界があるため、未解決であること自体が研究の到達点を明示する。**ただし現在証明済みなのは f=1 における超線形性と f=2 における多項式性であり、同一型付けに対する「f=1 超多項式対 f=2 多項式」の真の分離は未証明**。要旨・題名・§9 でその強い分離を確定したかのように書かないこと。

## 6. I&C での採択見込み・判定予想

**v1 — 予想：major revision。** 数学的主幹である `thm:local-group-polydata`、`thm:fanout-one-data`、`thm:binary-u1-polydata` には I&C 向けの内容があり、§6 `prop:feature-cross-typed` 等が MCFG 固有性を具体化する。しかしタイトルは上界のみに狭すぎ、§1 が結果の羅列、分量約50頁で質的学習・例・境界の優先順位が不明瞭。さらに要旨・結論の「任意の型付け」の無条件下界は `prop:linear-factor-all-fanout` の $4f+1$ 文字条件と矛盾している。数学上の限定修正と大幅な構成修正が要求されるため minor/accept は見込みにくい。編集判断として reject になる可能性もある。

**v2 — 予想：reject（現状のまま提出した場合）。** 定理 A–C により I&C の読者にとっての核心は v1 より伝わるが、**新設の `cor:trivial-exact` に直接的な反例があり、導入の `thm:A(ii)` も固定アルファベット上では偽**である。どちらも論文の冒頭で強調される主結果に直結するため、査読者が実際に発見した場合は mere editorial major revision ではなく証明された主要主張の撤回として扱われ得る。両問題は主な技法の全否定ではなく**定理の対象・量化の修正で治せる**見込みが高いので、P0 修正後の v2 に対しては **major revision** を第一予想とする。追加の独立証明監査まで通れば、v1 より有望と判断するが、採択確率を客観的な百分率で保証する材料はない。

### 最終推薦

**研究成果として主に残すのは v2。投稿時点の原稿としてはまだ差し止める。** 最小限の必須修正は `(1) cor:trivial-exact の全面修正`、`(2) thm:A(ii) のアルファベット条件の明示`、`(3) 要旨・結論・thm:A(iii) との同期` の三つ。その後で v1 の非 CFL 具体例を一つ戻し、§3 を圧縮する。これなら「局所群の普遍上界、fan-out 1 の厳密な擬多様体境界、fan-out 2 の異なる振る舞い」という論文の強みを、証明以上のことを言わずに提示できる。

---

**参照位置の注記**：本文の §・ラベルはすべて該当版の `main.tex` 中の位置を指す。重要箇所：v2 `thm:A` L145、`thm:B` L161、`thm:C` L183、`prop:linear-factor-all-fanout` L1740、`cor:trivial-exact` L1780、`prop:binary-u1-quadratic` L2009、`prop:binary-u1-weight-slice` L2044、`thm:binary-u1-polydata` L2201、付録 J L3780；v1 `prop:linear-factor-all-fanout` L1424、`sec:comparison` L2117、`prop:feature-cross-typed` L2186、`prop:lg-needed-target` L2289、`prop:nonabelian-needed-target` L2306、`sec:conclusion` L2557。GitHub の `main` は将来変わり得るため、評価対象の同一性は冒頭の blob SHA で固定した。

<!-- PART 3/3 END -->
<!-- END OF FILE -->
