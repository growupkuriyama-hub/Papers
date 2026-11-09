# 探索依頼：ファンアウト2で $U_1$ の上への型付けに超多項式の下界はあるか（`op:fanout-two`）

（論文 #2「MCFL の正データ学習：局所群とファンアウトの境界」用。2026-11-09 作成。この依頼文だけで作業できるように書いてある。リポジトリ `growupkuriyama-hub/Papers` の `02-v2-lg-fanout-boundary/` が読めるなら、末尾の「参照ファイル」も使ってよい。読めなくても作業できる。）

## 0. あなたの役割と成果物

あなたは形式言語理論・文法推論・有限半群の研究者として、下の**問題 U**を探索する。結論はどちらの向きでもよい。

- **否定の向き（本命）**：ファンアウト2のクラスに属し、型 $1$ の最短の語が文法の大きさと厚さについて超多項式に長い族を作る。成功すれば、論文の未解決問題 `op:fanout-two` が肯定的に解決する。つまり「ファンアウト2でも境界は $\mathbf{LG}$」が示される。
- **肯定の向き**：ある $U_1$ 型付けについて、ファンアウト2で多項式の上界を証明する。これは「境界がファンアウトで動く」方向の強い証拠になる。
- **部分結果**：新しい障害の補題、閉じた道の一般化、条件付きの定理など。

**成果物**は2つ。

1. 報告 `claude_fanout2_U1_lower_2026-11-09.md` を1本。
   - 各主張に **[証明済み] / [条件付き] / [観察（計算のみ）] / [予想]** のどれかを付ける。
   - 証明は省略せずに書く。
2. 検証スクリプト `check_claude_fanout2_U1_lower_2026-11-09.py` を1本。
   - 標準ライブラリのみで書き、実行時間は数分以内に収める。
   - 小さい $n$ について、クラスの所属（有界長での二穴代入可能性）、$\|G\|$、$\bar\theta_G$、$\mu_1$ を実際に計算する。

**禁止事項**

- 計算で確かめただけのことを [証明済み] と書かない。
- 有界長の検査はクラス所属の証明にならない。所属の証明は必ず手で書く。

## 1. 定義（原稿どおり）

### 文法

- $f$-MCFG $G=(V,\Sigma,P,S)$ を考える。各非終端記号 $A$ にファンアウト $\mathrm{fan}(A)\le f$ があり、規則は $A\to\rho(B_1,\dots,B_r)$ の形をとる。テンプレート $\rho=(\alpha_1,\dots,\alpha_{\mathrm{fan}(A)})$ は、終端記号と変数 $\xi_j^\kappa$ からなる。
- **大きさ**：$\|G\|:=|V|+\sum_{\text{規則}}(1+r+\sum_i|\alpha_i|)$。$|\alpha_i|$ は終端記号と変数の出現の数を数える。
- **良い (good)**：次の4条件をすべてみたす文法をいう。
  - $\varepsilon$-free：どの $\alpha_i$ も空でない。
  - nondeleting：各変数がちょうど一回現れる。
  - nonpermuting：$\xi_j^1,\dots,\xi_j^{d_j}$ がこの順に現れる。
  - nonmerging：$\xi_j^\kappa\xi_j^{\kappa+1}$ という因子がない。
- **既約 (reduced)**：すべての非終端記号が到達可能かつ生産的。
- **厚さ**：規則 $R$ について $\theta_G(R):=\min\{|w|: w\in L(G)\text{ の成功する導出で }R\text{ を使うもの}\}$ とおく。これは導出の長さではなく、文の長さである。$\theta_G:=\max_R\theta_G(R)$、$\bar\theta_G:=\max\{1,\theta_G\}$。

### 文脈と代入可能性

- **$d$-文脈**：$E=v_0\square_1v_1\cdots\square_dv_d$。ただし $v_0,v_d\in\Sigma^*$、$v_1,\dots,v_{d-1}\in\Sigma^+$（隣り合う穴の間は空でない）。$\mathcal E_d$ でその全体を表す。
- **分布**：$\mathcal D^{(d)}_L(\mathbf x):=\{E\in\mathcal E_d:E[\mathbf x]\in L\}$。
- **型付け**：$s:\Sigma^+\twoheadrightarrow\mathsf S$（有限半群への全射準同型）。
- **$(f,s)$-タプル代入可能**：すべての $1\le d\le f$ と $\mathbf x,\mathbf y\in(\Sigma^+)^d$ について、成分ごとの型が等しく、$\mathcal D^{(d)}_L(\mathbf x)\cap\mathcal D^{(d)}_L(\mathbf y)\ne\emptyset$ ならば、$\mathcal D^{(d)}_L(\mathbf x)=\mathcal D^{(d)}_L(\mathbf y)$。
- **$\mathcal C_{f,s}$**：$(f,s)$-タプル代入可能な $f$-MCFL の全体。

### $U_1$ 型付けと基本の例

- $U_1=\{1,\zeta\}$（$\zeta^2=\zeta$）、型 $1$ の語は「型 $1$ の文字だけからなる語」である。
- 基本の例は $\Sigma=\{\mathtt a,\mathtt b,\mathtt c\}$ 上の $s_U$：$\mathtt a,\mathtt b\mapsto1$、$\mathtt c\mapsto\zeta$。型 $1$ の語は $\{\mathtt a,\mathtt b\}^+$ の語（$\mathtt a^+$、$\mathtt b^+$ も含む）である。
- 文字数4以上や、型 $1$ の文字が一つだけの型付けを使ってもよい。

### データ長

- 一様多項式データ（定義 `def:uniform-polydata`）：型付け $s$ ごとに多項式 $p$ があり、すべての $L\in\mathcal C_{f,s}$ と、$L\cap\Sigma^+$ のすべての既約で良い fan-out $\le f$、rank $\le r_{\max}$ の表示 $G$ について、標準の作用素 $\mathcal B^{\le r_{\max}}_{f,s}$ の特徴標本 $F$ で $\|F\|_+\le p(\|G\|,\bar\theta_G)$ をみたすものがある。

## 2. 問題 U

> $f=2$、$r_{\max}\ge2$ とする。ある $U_1$ 型付け $s$（例えば $s_U$）について、族 $L_n\in\mathcal C_{2,s}$ と、$L_n\cap\Sigma^+$ の既約で良い fan-out $\le2$、rank $\le r_{\max}$ の表示 $G_n$ であって、次をみたすものはあるか。
> - $\|G_n\|$ と $\bar\theta_{G_n}$ は $n$ について多項式。
> - $\mu_1(L_n):=\min\{|w|:w\in L_n,\ s(w)=1\}$ は $n$ について超多項式。

**下界への変換**：命題 `prop:rare-type` により、標準の作用素とクラス全体で特徴標本をもつ集合駆動型作用素のどの特徴標本も、型 $1$ の語を含む。よって $\|F\|_+\ge\mu_1(L_n)+1$ となり、問題 U に答えれば `op:fanout-two` が解ける。$\mathbf{LG}$ に含まれない擬多様体はすべて $U_1$ を含む（`thm:lg-characterization`）ので、$U_1$ 型付けが1つあれば十分である。

**注意1（$\mathbf{SL}$ との関係）**：`prop:sl-reduction` により、`op:fanout-two` は「内容型付け $c_\Sigma$（語をその文字の集合に送る型付け）がファンアウト2で一様な多項式データをもつか」と同値である。$U_1$ 型付けは $c_\Sigma$ の商である。したがって：

- $\mathcal C_{2,s_U}\subseteq\mathcal C_{2,c_\Sigma}$ が成り立つ。$s_U$ のほうが粗いので、代入可能性の制約は強い。
- $s_U$ の否定例は、$c_\Sigma$ の否定例にもなる。$\{\mathtt a,\mathtt b\}$-語がすべて長いなら、内容 $\{\mathtt a\},\{\mathtt b\},\{\mathtt a,\mathtt b\}$ の語もすべて長いからである。
- 逆に、$c_\Sigma$ で作る方が自由度は大きい。$c_\Sigma$ での否定例でもよいが、その場合も一番効くのは $\mu_{\mathtt{ab}}$（内容がちょうど $\{\mathtt a,\mathtt b\}$ の最短語）を超多項式にすることである。

**注意2（ファンアウト1の上界は移らない）**：表示 $G_n$ はファンアウト2の文法でよい。ファンアウト2では文法が小さくなりうるので、ファンアウト1の上界（下の 3(e)）は移らない。

## 3. 原稿で既に分かっていること

### (a) ファンアウト1での指数下界（`cor:typing-level-obstruction`、`prop:three-letter-family`）

- 族 $G_n$：$S\to E_n$、$E_0\to\mathtt a$、$E_i\to\mathtt bE_{i-1}E_{i-1}\mathtt b\mid\mathtt cE_{i-1}\mathtt c$。
- $L_n=L(G_n)$ は Clark–Eyraud 代入可能、$\|G_n\|=13n+7$、$\bar\theta_{G_n}=4n$。
- $W_n$（$W_0=\mathtt a$、$W_i=\mathtt bW_{i-1}W_{i-1}\mathtt b$）は $\mathtt c$ を含まない唯一の語で、$|W_n|=3\cdot2^n-2$。
- よってファンアウト1で $3\cdot2^n-1$ の下界が出る。型 $1$ の文字が2つあればこれが使え、ファンアウト1の $U_1$ 型付けは完全に分類されている（`cor:u1-classification`：多項式 ⟺ 型 $1$ の文字がちょうど1つ）。

### (b) 冪の移送と非持ち上げ（`lem:power-transfer`、`thm:doubling-no-lift`）

冪の移送：$f\ge2$、$L\in\mathcal C_{f,s}$、$u\in\Sigma^+$ とし、$i_0,p$ を $s(u)$ の最終指数と周期とする。$i,j\ge i_0$、$\delta\in p\mathbb Z_{>0}$ で、$L$ のある語が因子 $u^{i+\delta+j+1}$ を含むなら、
$$w_{\mathrm L}u^iw_{\mathrm M}u^{\delta+j}w_{\mathrm R}\in L\iff w_{\mathrm L}u^{i+\delta}w_{\mathrm M}u^jw_{\mathrm R}\in L.$$

非持ち上げ：$\varphi$ を文字ごとに素な語への準同型とし、$n\ge2|\mathsf S|+2$、$f\ge2$ とする。$\varphi(W_n)$ を含む $L\in\mathcal C_{f,s}$ は、同じ型・同じ Parikh ベクトルで $\varphi(\mathtt c)$ の文字を含まない別の語も含む。したがって倍増族はそのままではファンアウト2のクラスに入らない。

### (c) 二文字の場合（`thm:two-letter-content`、`cor:two-letter-semilattice`）

$|\Sigma|=2$ では、すべての $f\ge2$ で内容型付けのデータは多項式で、評価は $O(\|G\|^3\bar\theta_G^{\,4}\log\bar\theta_G)$。したがって**少なくとも三文字が必要**である。

### (d) 稀な型の下界は表示に依存しない（`prop:rare-type`）

下界 $\sum_{m}(\mu_m(L)+1)$ は表示に依存しない。

### (e) ファンアウト1で孤立文字があれば多項式（`thm:two-letter-fanout-one`）

文字 $\mathtt a$ が**孤立**しているとは、$s^{-1}(s(\mathtt a))=\mathtt a^+$ であり、かつ $\mathtt a$ を含み $\mathtt a^+$ にない語がすべて同じ型をもつことをいう。このときファンアウト1では $\tau\le C(\|G\|+2)^{22}\bar\theta_G^{\,8}$。証明は、最短の純な導出の中の同じラベルの二つの出現を可換関係に変え、分布の類の周期性と超増加符号の数え上げを使う。

ファンアウト2での類似は未解決である。型 $1$ の文字が1つの $U_1$ 型付けもファンアウト2では未解決なので、そちらで否定例を作ってもよい。

## 4. 閉じた道（2026-11-01〜11-07 の探索記録。各報告は Claude か ChatGPT が検証済み）

否定例を設計するとき、次の障害をすべてくぐる必要がある。

1. **二穴のはさみ**（ChatGPT N9）：2-文脈 $E=\square_1\omega\square_2$ を使う。成分ごとの型が等しい $(x_1,x_2)$ と $(y_1,y_2)$ について、$x_1\omega x_2,\ y_1\omega y_2\in L$ なら分布が一致する。よって $x_1zx_2\in L\Rightarrow y_1zy_2\in L$ となる。
   - $\mathtt c$ を含む中央 $\omega$ をはさんで「外側の部品」が共有されると、長い $\{\mathtt a,\mathtt b\}$-語が短いものに切り替わる。
   - 「全ての枠を生成するファンアウト2の非終端」を使う候補（$\|G\|=O(n^2)$、$\mu_{\mathtt{ab}}=2^{n+1}+2$）はこれで崩れた。$D_1\to\mathtt{acb}$、$D_n\to\mathtt a^n\mathtt{cb}$、$S\to D_n\mathtt{ab}$ を保つ拡張はすべて $\mu_{\mathtt{ab}}\le n+5$ になる。
2. **冪の移送**（上の 3(b)）：長い冪 $u^N$ を含む設計は、冪を二つの成分の間で移されて崩れる。倍増の型 $E_i\to E_{i-1}E_{i-1}\mid d_i$（$d_i\in\{\mathtt b,\mathtt c\}^+$）は、$d_i$ の選び方によらず $n\ge3$ で arity 2 が壊れる。
3. **加法的な重み**：言語全体が非負の加法的重みの1つのレベルに入るなら、$\mu_{\mathtt a}\le(r+1)^2\bar\theta^3$。文字に指数的な重みを持たせる設計は使えない。$\mathtt{a,b}$ を含む語だけが1つのレベルに入る場合も $\mu_{\mathtt{ab}}\le7(r+1)v^2\theta^2$ となる（代入可能性は不要）。
4. **可換群の原像・剰余類**：経路言語（各文字が1辺）×可換群の剰余類×内容 の形の言語は、すべての表示で $\mu_{\mathtt{ab}}\le\max\{9(r+1)v\theta,226v^3\theta^3\}$（定理H、Astra の定理1.2、代数的閉包の報告）。可換群の篩いを通らない語があれば、$\bar\theta$ 以下の長さのものがある。
5. **群の語問題**（ファンアウト1の問題G）：可換群では位数 $\le(r+2)\bar\theta^2$。$\mathbb Z/(2^n-1)\rtimes\langle\times2\rangle$ では文法の大きさが $2^{(2/3-o(1))n}$ になる。小さい文法で大きな群の語問題を作る道は、知られた候補では塞がっている。
6. **隙間の補題**（代入可能性は不要）：長い唯一の型 $1$ の語 $W$ があると、$|W|\le\bar\theta+(r+1)M$ となる。ここで $M$ は $\mathtt c$ を含む語の長さに関わる量である。$W$ を作る規則はそれぞれ短い $\mathtt c$ 入りの語でも使われなければならず（厚さの定義より）、密度版によれば $\zeta$ 型の文字を多く含む長い語が強制される。
7. **唯一語の剛性**（$f\ge2$）：型 $m$ の唯一の語 $W$ について、$\{W\}$ 自身が $(2,s)$-代入可能でなければならない。二文字・長さ $\ge7$ では $x^n$、$x^{n-1}y$、$yx^{n-2}y$、交互の語に限られる。ただし問題 U は唯一性を要求しない（型 $1$ の語が多数あってもすべて長ければよい）。
8. **Parikh 飽和（1頂点）クラス**：命題7.2は解決し、命題7.3は部分的に解決した。予想7.5は反証されたが、命題7.4は未解決である。報告 `claude_conj75_2026-11-07.md` の補題C は、表示側だけから $\mu_{\mathtt{ab}}\le3v\theta+3rv(\theta+\Delta(\theta))$ を与える。ここで $\Delta(\theta)$ は「$\mathtt c$ を高々 $\theta$ 個含む $\mathtt{abc}$-語の、$P$ に対する $\mathtt{a,b}$ の不足の最大」である。**否定例では、$\mathtt c$ の少ない $\mathtt{abc}$-語が大きな $\mathtt{a,b}$ の不足をもたなければならない。**
9. **三文字・一文字の語**：同じ $\mathtt a$-骨格の符号をもつ重い節点は、非終端記号が違っても同じ数の $\mathtt a$ を失う。そこから $P_{\mathtt a}(C)\le\mathrm{poly}(|V|,\bar\theta,|C|_{\mathrm{fix}})\cdot r^M$ が出る（$M$ は符号の種類数）。反例には超対数個の符号が要る。

## 5. 課題

### 課題0（確認、短く）

上の 3(b) と 4.1 を、$s_U$ の場合について自分の言葉で確かめる。

- 長い $\{\mathtt a,\mathtt b\}$-語を守るには、その「外側の部品の対」が、どの $\mathtt c$ 入りの中央とも同時に現れてはならない。
- ところが厚さを小さく保つには、各規則が短い $\mathtt c$ 入りの語で使われなければならない。

この緊張関係を一つの補題として正確に述べる。一般形で証明できればそれ自体が成果である。

### 課題1（本命：否定の向き）

上の障害をすべて避ける族を設計する。考えられる方向（一部は未試行）：

- **(i) 中央が単一でない設計**：はさみは $\square\omega\square$ を使う。外側の部品が $\mathtt c$ 入りの中央と同時に現れないように、$\mathtt c$ を常に**二箇所以上**、かつ異なる「位相」に置く。例えば、$\mathtt c$ の位置が二穴文脈の両側の固定部分に必ずまたがるようにする。
- **(ii) 二成分の非終端で符号を運ぶ**：$\mathtt{a,b}$-部分の長さを、二成分の非終端の対応（$x_1\cdots x_2$ の交差依存）で指数的に強制する。ファンアウト2でしか書けない小さい文法を使い、ファンアウト1の上界（3(e)）の外に出る。
- **(iii) 冪を含まない倍増**：Thue–Morse 型など、$u^3$ を含まない語で倍増させ、冪の移送を避ける。単純な冪は 4.2 で壊れる。
- **(iv) 群でも重みでもない不変量**：非可換な（あるいは群でない）有限の不変量で、型 $1$ の語の長さを制御する。4.4 と 4.5 を避けるには、不変量が可換群の剰余類に還元されず、しかも小さい文法をもつ必要がある。
- **(v) 型 $1$ の文字が1つの $U_1$ 型付け**（例 $\mathtt a\mapsto1$、$\mathtt b,\mathtt c\mapsto\zeta$）で、最短の $\mathtt a^N$ を超多項式にする。`prop:typed-thickness-exponential`（$S\to SS\mid\mathtt a\mid\mathtt c$ 型の文法で $t_{\mathrm{typ}}\ge2^n$）は型付きの厚さだけを指数的にする例で、$\tau$ は小さい。ファンアウト2で $\tau$ まで指数的にできるかを調べる。

各候補について、次を順に行う：

1. 文法と $\|G_n\|$、$\bar\theta_{G_n}$ を計算する。
2. 小さい $n$ で、長さ $\le N$ の語に制限した arity 1, 2 の代入可能性をスクリプトで全探索する（違反の語・文脈を出力する）。
3. 違反がなければ、手で所属を証明する。

失敗した候補は、どの障害（4.1〜4.9 か新しいもの）で崩れたかを一行で記録する。**失敗の記録も成果である。**

### 課題2（否定がうまくいかない場合：肯定の向き）

$s_U$（三文字、$\mathtt a,\mathtt b\mapsto1$、$\mathtt c\mapsto\zeta$）について、$f=2$ で $\mu_1(L)\le\mathrm{poly}(\|G\|,\bar\theta_G)$ を示す。さらにできれば $\tau(G,s_U)\le\mathrm{poly}$ も示す。$\tau$ は代表元の長さ（`cor:distribution-representatives`）である。

- 4.1 のはさみと 4.6 の隙間の補題を組み合わせ、長い型 $1$ の語を短くする手続きを作る。
- まず部分クラスから始める：$\mathtt c$ の個数が有界、$\mathtt c$ の連が有界、線形文法、ランク2 など。
- $\mu_1$ だけでも成果である。$\mu_1$ の多項式上界は「$s_U$ ではファンアウト2で稀な型の下界が効かない」ことを意味する。

### 課題3（いずれにせよ）

「否定例が満たすべき必要条件」を、補題の形でできるだけ多く集める。例：

- $\Delta(\theta)$ が大きいこと。
- 外側の部品の対の数が多いこと。
- 符号の種類数が超対数であること。

これで次の探索の設計空間を狭める。

## 6. 報告の形

1. 冒頭3行の要約：どちらの向きに、何が証明されたか。
2. 主結果：主張、ラベル、証明。
3. 試した候補の表：文法、$\|G_n\|$、$\bar\theta$、$\mu_1$、崩れた理由。
4. 必要条件の補題の一覧。
5. 次の一手（3つ以内）。
6. スクリプトの説明と出力の要点（乱数を使うなら種を固定する）。

**原稿との整合**

- 記号と定義は上の §1 に合わせる。
- 「境界がファンアウトで動く」とは、証明できていない限り書かない。

## 7. 参照ファイル（読めれば）

`growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary/` の下にある。

- `main.tex`：本文。§8（`thm:doubling-no-lift`、`prop:sl-reduction`、`op:fanout-two`）、`prop:rare-type`、`lem:power-transfer`。
- `reviews/STATUS_sl_fanout2_2026-11-01.md`：ファンアウト2探索の全体のまとめ。
- `reviews/chatgpt_negative_design_2026-11-06.md`：二穴のはさみ N9。
- `reviews/chatgpt_shortcut_classification_2026-11-06.md`：近道の分類、二穴の枠の移送。
- `reviews/claude_proposition_H_2026-11-07.md`、`reviews/astra_fanout2_core_2026-11-07.md`、`reviews/claude_algebraic_closure_2026-11-07.md`：可換群の閉じた道。
- `reviews/claude_prop72_2026-11-07.md`、`reviews/claude_prop73_2026-11-07.md`、`reviews/claude_conj75_2026-11-07.md`：Parikh 飽和クラスと補題C。
- `reviews/chatgpt_weighted_codes_2026-11-02.md`、`reviews/chatgpt_power_rare_words_2026-11-02.md`、`reviews/chatgpt_skeleton_diversity_2026-11-02.md`：重み、冪、骨格。
