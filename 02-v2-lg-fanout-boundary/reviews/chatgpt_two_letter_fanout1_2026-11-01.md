# 二文字内容型付けのファンアウト1：超多項式下界の探索とスペクトル障害

**調査日**：2026-11-01  
**対象**：Takayuki Kuriyama, `Papers/02-v2-lg-fanout-boundary/main.tex`（Git blob `20259d0959400d42cd07e04c40cb3cc38252ce22`、取得時点の `main`）、`parked/parked_u1_typing_level.tex`（blob `38145cf3761f387adf88cc5c8801a6be402f8b13`）。  
**結論**：T1 の超多項式下界族も、T3 の無条件多項式上界も得られていない。ただし、内容型付けでの「混合型は必ず短い」という一般補題と、文字数スペクトル・正の加法重みスペクトルに基づく、両再構成作用素に共通する多項式特徴データ上界を証明する。三文字族の素朴な二文字符号化は深さ3で不成立と有限全数検査で判定した。

## 0. 主張別の判定表

| 主張 | 判定 | 根拠 |
|---|---|---|
| 二文字内容型付け `c` のファンアウト1で超多項式下界がある | **未解決** | §1、§7 |
| 同じ対象で一様多項式特徴データがある | **未解決** | §1、§5–7 |
| `C_{1,s_{U,2}} ⊆ C_{1,c}`；`s` の超多項式下界は `c` に移るが逆は自動ではない | **証明済み（原稿確認）** | §1 |
| **混合内容型の最短語は** `μ_{\{a,b\}}(L) ≤ 3(r+1)|V|θ̄`（任意の reduced good CFG、代入可能性不要） | **証明済み** | §2、補題1 |
| 有限 `(1,c)`-代入可能言語における純語は `a^p`、`b^q` が各高々一つ | **証明済み（既知）** | §2、補題2 |
| `h_a,h_b` を正の a/b 出現数の異なる値の個数とすると `t_typ(G,c) ≤ (r+1)|V|θ̄ max(3,h_a,h_b)` | **証明済み（本報告で c に拡張）** | §3、定理3 |
| 両方のスペクトルが有限なら両 B 作用素に `O_r(max(3,h_a,h_b) ‖G‖²θ̄)` の特徴データ | **証明済み** | §3、系4 |
| 正の加法重み `ψ_λ` が高々 k 種類なら `t_typ(G,c) ≤ (r+1)|V|θ̄ max(3,kM_λ)`、`M_λ=max(1,λ,1/λ)` | **証明済み（条件付き、λ 依存）** | §4、定理5 |
| `k` だけを使い `λ` に依存しない上界がこの方法で得られる | **未解決** | §4 |
| 全語長の種類数 `h_len` が有限なら最長語は `≤h_len θ̄` | **証明済み（既報、再利用）** | §4 |
| `L_{1,2}` は `(1,c)` と `(1,s_{U,2})` の双方に所属 | **全数検査で確認、一般族の証明は既存原稿** | §6 |
| `A_i→A_{i-1}A_{i-1} \mid b` の素朴な倍増族は `n=2` で不成立 | **反証（具体的証人あり）** | §6 |
| 三文字 `K_n` を `A→a,B→aa,C→b` と二文字符号化する方法は `n=3` で不成立 | **反証（具体的証人あり）** | §6 |
| `L={b,ab}` は `(1,c)` に属するが `(1,s_{U,2})` には属さない | **証明済み・全数検査確認** | §1、§6 |
| 新しい補題の文献上の独立した新規性 | **未確認** | §8 |

ここで `θ̄=\bar\theta_G≥1`、`r` は文法の最大規則ランク、`v=|V|`。定理中の `t_typ` は**文法の全実現型付き非終端の最短収率長の最大値**であって、言語全体の最短型語 `μ` と同一ではない。下記で `O_r` と記した定数は固定した `r_max` のみに依存し、アルファベットと内容半束は `{a,b}` に固定する。

## 1. 量化、型付けの方向、下界の作用素

`c(w)=\operatorname{alph}(w)` を非空語の内容とする。正の型は `{a}`, `{b}`, `{a,b}`。`s=s_{U,2}` は `s(a)=1, s(b)=ζ` であり、`s(w)=1` は `b` を含まない場合、`ζ` は `b` を含む場合である。`s` は `c` の合成写像だから `s\preceq c`、従って

\[
\mathcal C_{1,s}\subseteq\mathcal C_{1,c},\qquad
\ker(c)\subseteq\ker(s).
\]

前者は `c` で比較する因子の組が少ないことから直接従う。原稿 `lem:typing-monotone` のより精密な結論は、`L∈C_{1,s}` と有限正例集合 `F⊆L` に対し

\[
L(\mathcal B^{\le r}_{1,c}(F))\subseteq L(\mathcal B^{\le r}_{1,s}(F))\subseteq L,
\]

かつ無制限ランク版でも同じ、というものである。従って `c` で特徴標本が作れれば同じ `F` は `s` でも特徴標本である。**ここから導けるのは `s` で超多項式なら `c` も超多項式、という反対向きの対偶である**。ただし、`c` にしか属さない反例族については `s` に対する下界は一切主張できない。

包含は真である。`L={b,ab}` の内容 `b` と `ab` は異なるので同じ内容の二つの異なる観測因子が比較されず、`L∈C_{1,c}`。しかし `s(b)=s(ab)=ζ` で両方とも空文脈で受理され、`(a,ε)` は `b` の文脈だが `ab` の文脈ではない。従って `L∉C_{1,s}`。有限集合なので両者とも CFG で生成可能という側の問題はない。

原稿 `prop:rare-type` を正確に適用すれば、任意の実現内容型 `t` に対して、その内容型の語が特徴標本に必ず現れる。これは **`\mathcal B^{\le r}_{1,c}` と `\mathcal B_{1,c}` の両方**に成立する。さらに `L` と `L\setminus c^{-1}(t)` の双方に特徴標本を持つ**任意の集合駆動作用素**にも成立し、とりわけクラス `C_{1,c}` 全体に特徴標本を持つ作用素に成立する。少なくとも

\[
\|F\|_+\ge \sum_{t\in c(L\cap\Sigma^+)}\bigl(\mu_t(L)+1\bigr)
+\mathbf1_{\{\varepsilon\in L\}}
\]

である。逆に、特定の対象 `L` のみに対応して設計した任意の作用素や Gold 学習器の収束時間については、この論法は下界を与えない。`§3–§4` の上界は**両方の B 作用素**についてだけ述べ、任意の集合駆動作用素に対する上界は主張しない。

**重要な注意**：`c` では `b` だけの長い語が稀なら `{b}` 型下界になるが、`s` では同じ `b` が混合語とともに `ζ` 型に入るので、その下界は `s` に移らない。一方、長い `a^N` はどちらの型付けでも純型なので、`L∈C_{1,s}` が別途示せたときは双方に下界が働く。

## 2. どの稀な型を狙うべきか

**補題1（混合型の普遍的短語補題）。** `G` を `{a,b}` 上の reduced good なファンアウト1・規則ランク `≤r` の文法とし、`v=|V|`、`θ=\bar\theta_G` とする。非終端 `A` が `a,b` の両方を含む語を生成できるなら、そのような語を長さ高々

\[
\boxed{3(r+1)v\theta}
\tag{1}
\]

で生成できる。特に `L(G)` に混合語があれば `\mu_{\{a,b\}}(L(G))≤3(r+1)vθ`。**代入可能性も、言語の有限性も仮定しない。**

*証明*。`A` の導出木の中で、`a` と `b` をそれぞれ一箇所、端末出現として標識する。二つの標識が保存される導出木のうち、収率長、次に節点数を最小にするものを取る。標識を含む節点から根への二経路の和集合を骨格 `Q` と呼ぶ。`Q` 外の部分木は、同じ非終端の長さ `≤θ` の非標識収率に差し替えても二つの標識が残る。したがって最小性から、`Q` 外の各部分木の収率長は `≤θ`。

骨格の各節点に、その節点以下にある標識の集合（`{a,b}`、`{a}` または `{b}`）を付ける。祖先と真の子孫で**非終端名と標識集合が同じ**なら、祖先部分木を子孫部分木で置き換えられ、両標識を保ったまま収率長が減るか、同長で節点数が減る。矛盾する。骨格の二経路の共有幹には集合 `{a,b}` しか現れず、分岐後の各枝には `{a}` または `{b}` しか現れない。それぞれの区間では同じ非終端は二度出ないため、共有幹と二枝は各々高々 `v` 節点、従って `|Q|≤3v`。各骨格節点が直接書く端末は `≤θ`、骨格外の子は高々 `r` 個で各 `≤θ`（原稿 `lem:thickness-equivalence`）。ゆえに収率長は `|Q|(r+1)θ` 以下。□

これは**文法の内部非終端に対する短語**にも使える点が重要である。内容型 `{a,b}` の短さだけでは全ての型付き非終端の `t_typ` は抑えられないが、超多項式の稀な**根の内容型**を作るなら、残りは `{a}` 又は `{b}` しかない。

**補題2（有限言語の純語の一意性、既知）。** 有限 `L∈C_{1,c}` は `a^p` の形の語を高々一つ、`b^q` の形の語を高々一つしか含まない。

*証明*。`a^p,a^q∈L`、`p<q` とすると、二因子は `{a}` 型で空文脈を共有する。代入可能性により文脈集合が等しい。`(a^{q-p},ε)` は `a^p` の文脈なので `a^q` の文脈でもあり、`a^{2q-p}∈L`。同じ置換を繰り返せば無限集合となり矛盾。`b` も対称。□

従って T1 の `prop:rare-type` 戦略で必要なのは、**同じ有限言語に多数の純語を入れることではなく、唯一の非常に長い純語と、それを文法の小さい `θ` と両立させる多数の混合語を入れること**である。

## 3. 内容型付けに特有の文字数スペクトル上界

`x∈{a,b}` について

\[
H_x(L)=\{|w|_x:w\in L,\ |w|_x>0\},\qquad h_x=|H_x(L)|\in\mathbb N\cup\{0,\infty\}.
\]

ここで `h_x` は語数でも run 数でもなく、その文字の**正の出現回数の異なる値の個数**である。

**定理3（内容型の対称スペクトル上界）。** `G` を上記の reduced good CFG とする。`h_a,h_b<∞` なら

\[
\boxed{t_{\mathrm{typ}}(G,c)\le (r+1)v\theta\max\{3,h_a,h_b\}.}
\tag{2}
\]

さらに、`A` が純 `a` 収率 `a^N` を持ち、その最短純 `a` 収率が `N>θ` なら `h_b≥\lceil N/((r+1)vθ)\rceil`。`a,b` を交換した主張も成り立つ。**この定理の短語長部分は、代入可能性を使わない。**

*証明*。原稿の `lem:thickness-equivalence` により全ての非終端に長さ `≤θ` の非型付き収率 `ω_B` があり、各非終端 `A` に成功文脈 `E_A` がある。純 `a` の型付き非終端を一つ固定し、その最短収率 `a^N`、その中で節点数最小の導出木 `T` を取る。全節点の収率は純 `a` である。同じ非終端が祖先・子孫に二度現れれば、祖先を子孫で置き換えて純型を保ちつつ短縮（又は節点数減少）できるため、道長は高々 `v`。

収率長 `>θ` の節点を重節点と呼ぶ。これらは祖先に関して閉じる。重節点 `u` の部分木を `ω_{B_u}` に差し替えると、部分木長は厳密に減る。もし `ω_{B_u}` に `b` がなければ、純 `a` の型が保たれ、`a^N` の最短性に反する。従って**すべての重節点の短い差替え語は `b` を含む**。

重節点の反鎖を `m` 個取る。その部分木は互いに素で、先頭から `j=1,\ldots,m` 個を順に `ω` に替えると、固定成功文脈 `E_A` に入れて得る受理語の `b` 出現数は厳密に増加する。全 `m` 個は `H_b(L)` の互いに異なる元なので `m≤h_b`。各深さの重節点は反鎖、深さは高々 `v`、従って重節点総数は `≤vh_b`。根が重くないとき `N≤θ`。重いとき、導出の全ての端末は重節点が直接書くか、重節点に隣接する非重い子部分木が書く（子は高々 `r`、各長さ `≤θ`）。よって `N≤(r+1)vθ h_b`。重い根のとき `h_b≥1`。`b` の純型は同様に `h_a` で抑える。混合型の型付き非終端は補題1で `≤3(r+1)vθ`。全てをまとめれば (2)。根 `A=S` についての反鎖幅の議論は最後の必要条件も与える。□

**系4（両 B 作用素に共通する特徴データ）。** `L∈C_{1,c}`、`G` をその reduced good、ランク `≤r_max` 表示とし、`h_a,h_b<∞` とする。`H=max(3,h_a,h_b)` とすると、原稿 `thm:data-from-typed-thickness` により、`\mathcal B^{\le r_{\max}}_{1,c}` と `\mathcal B_{1,c}` に共通する特徴標本 `K` が存在し、

\[
\boxed{\|K\|_+\le4^{r_{\max}}\|G\|
\bigl[1+2\theta+r_{\max}(r_{\max}+1)v\theta H\bigr]
+\mathbf1_{\{\varepsilon\in L\}}.}
\tag{3}
\]

実際、内容の正の型は3、空収率専用の fresh identity を含む `|S^\sharp|=4` だから、原稿の `N_typ≤|S^\sharp|^{fr_max}‖G‖` に `f=1` を代入すればよい。`H` が `‖G‖,θ` の多項式で抑えられる部分クラスで **`O_{r_max}(H ‖G‖² θ)`** となる。**この上界は `r_max` 固定を仮定し、任意の集合駆動作用素には主張しない**。

10月30日付 `astra_binary_u1_fanout1_2026-10-30.md` §3.4 に、`s_{U,2}` における `b`-出現数のスペクトル上界と同種の反鎖証明が既にある。本定理の新たな点は、内容型 `{b}` も別に扱うための**対称的な `h_a,h_b` の併用**と、内容 `{a,b}` の二標識短語補題を合わせて `c` の**全**実現型を抑える点である。先行研究に対する外部的新規性は未確認。

## 4. 重みの値が k 種類の場合と、既存の定重量障害

`λ>0` を固定し、`ψ_λ(w)=|w|_a+λ|w|_b`、`k=|ψ_λ(L)|` とする。以下は **`k<∞`** の場合の結果である。`λ` は実数でもよい。

**定理5（有限重みスペクトルの条件付き上界）。** `G` を上記 reduced good CFG、`L=L(G)`、`k=|ψ_λ(L)|<∞`、`M_λ=max(1,λ,λ^{-1})` とすると

\[
\boxed{t_{\mathrm{typ}}(G,c)\le (r+1)v\theta\max\{3,kM_\lambda\}.}
\tag{4}
\]

従って `L∈C_{1,c}` なら両 B 作用素について

\[
\|K\|_+\le4^{r_{\max}}\|G\|
\left[1+2\theta+r_{\max}(r_{\max}+1)v\theta\max(3,kM_\lambda)\right]
+\mathbf1_{\{\varepsilon\in L\}}.
\tag{5}
\]

*証明*。混合型は補題1。純 `a` の最短収率 `a^N` を考え、長さ `>H_a:=θ\max(1,λ)` の節点を重いとする。短い代替収率 `ω_B` の重みは高々 `H_a` なので、重節点を短い収率に差し替えると**文全体の `ψ_λ` が厳密に減る**。独立な重節点 `m` 個を順に差し替えれば、`m+1` 個の互いに異なる重みが `L` に現れる。従って `m≤k-1`。純語最短性から道長は `≤v`、全重節点数は `≤v(k-1)`。端末数の計数により `N≤\max\{H_a,(r+1)v(k-1)H_a\}≤(r+1)vkH_a`。純 `b` は `λN` が重みなので、閾値 `H_b=θ\max(1,λ^{-1})` を用いれば同様である。両方を `M_λ` でまとめ、補題1と合わせて (4)。原稿の witness 定理を用いて (5)。□

この定理は `λ` に依存する。従って**単に `k=O(1)` という条件だけで `‖G‖,θ` の多項式上界が得られたとは言えない**。例えば `λ` が入力系列とともに超多項式に大きくなることを (4) は除外しない。**`k` と `M_λ` がともに `‖G‖,θ` の多項式**という追加仮定の下で、T3 の肯定的部分結果となる。`λ` を固定した部分クラスでは特に `O_{r_max,λ}(k‖G‖²θ)` の特徴データ上界が得られる。

一方、`k=1` の定重量全体には、既存の `parked/parked_u1_typing_level.tex` の `prop:binary-u1-weight-slice` と `prop:u1-weight-all-fanout` がすでに **`μ^\star≤\lfloor(θ+1)^2/4\rfloor`** を与え、`L_{m,n}` で鋭い。本報告の (4) はその鋭い二次評価を置き換えるものではない。文法上の純型の厚さと、単に言語の `μ^\star` も混同しない。

**既報の別のスペクトル補題**。`h_len=|\{|w|:w∈L\}|` が有限なら、10月30日付 Astra 報告 §3.6 が、最短受理語長 `μ` に対し `\max_{w∈L}|w|≤μ+(h_len-1)(θ-μ)≤h_len θ` を証明している。これは本報告の新発見ではない。特に長い純語 `a^N` の候補族では `h_len≥N/θ`、すなわち超多項式の純語があれば、文長の異なる値の個数も超多項式に必要である。定理3からはさらに、純 `a` の場合 `h_b≥N/((r+1)vθ)`、純 `b` の場合 `h_a≥N/((r+1)vθ)` が必要である。

## 5. T1 への障害と T3 の限界：一穴と二穴

### 5.1 下界候補に必要な条件

`L_n∈C_{1,c}`、`v_n,‖G_n‖,θ_n=n^{O(1)}`、`μ^\star(L_n,c)=n^{\omega(1)}` を目指す場合、補題1により長い型は純 `{a}` か純 `{b}` に限る。例えば `a^{N_n}∈L_n` を唯一の純 `a` 語として `N_n=n^{\omega(1)}` とするなら、`h_b(L_n)` と `h_len(L_n)` は超多項式でなければならない。また10月30日付 Astra 報告 §2 の「指数欠陥立方体」は、長い純語を低 `θ` で支える場合に多数の短い混合語が必要となるという、より強い（同報告で証明された）障害を与える。ここではその証明を独立に再監査していないため、本報告独自の定理とは数えない。

**「積の二段重ね」の障害**は、単純な `A_i→A_{i-1}A_{i-1}|b` が既に第2段で純 `b,b²` を共存させ、`(1,c)` の有限性制約を破ることで露呈する。`b` への短絡を混合符号に換えても、それがさらに深い場所で別の同内容因子と同一文脈を共有することが障害になる。単一の語長や Parikh ベクトルだけを調べても、この文脈の衝突は発見できない。

### 5.2 付録 H の二穴ステップを一穴へ持ち込めない箇所

付録 H `lem:app-two-runs` の鍵は `x^4` の存在から二成分 `(x,xx)` と `(xx,x)` が**同じ二穴文脈**を共有すること、さらに `x`-run の間で一文字ずつ再配分できることにある。これは一穴の内容 `{x}` の因子についての代入可能性からは導けない。実例として、`L_{1,2}=\{aa,b\}^{4}` は `(1,c)`-代入可能だが、語 `aabaaaa` は言語に入り、`aaabaaa` は入らない。両者は `a` の二 run 間で `a` 一文字を移動しただけである。従って `lem:app-two-runs(i)` の移動原理は一穴版では偽である。

付録 H の後半 `lem:app-two-insertion` は、独立な非終端の**二つの成分**を交換したときに長い run と複数の内部 run を作り、非 Parikh 飽和性と矛盾させる。ファンアウト1では同じ構造の交換に必要な二成分の独立操作がない。`lem:app-two-saturated` の Parikh 最小化も、二穴を使って先に確立した分類と組み合わせた証明なので、そのまま一穴の一般定理にはならない。本報告の代替道具は「二標識の短い混合収率」と「純収率を短くすると別文字の計数が必ず増える」という、一穴でも成り立つ反鎖法である。ただしその方法は `h_a,h_b` を無条件には抑えず、T3 の全面的解決には至らない。

## 6. 有限全数検査：再現可能な結果と反例証人

判定は有限言語 `L` の全非空因子 `x` と**観察される全一穴文脈** `D_L(x)={(u,v):uxv∈L}` を構成し、同じ型の二因子の文脈集合が交差するなら一致するかを判定する。これは有限 `L` に対して論理的に完全な判定である。もちろん、**有限の n での合格は全 n の帰納的証明ではない**。

以下は後掲 Python 3 スクリプトを実行した結果である。

| 対象 | 語数 | `C_{1,c}` | `C_{1,s}` | 所見 |
|---|---:|---|---|---|
| `{b,ab}` | 2 | PASS | FAIL | `c` と `s` の真の差 |
| `{aa,ab,bbb}` | 3 | PASS | PASS | 正の一定重みではない例 |
| `L_{1,2}={aa,b}^4` | 16 | PASS | PASS | 既存二次族の小さい場合 |
| `A_1→A_0A_0\mid b, A_0→a` | 2 | PASS | PASS | 第1段だけ通る |
| 同 `A_2` | 5 | FAIL | FAIL | 純 `b` と `bb` の共存 |
| 同 `A_3` | 24 | FAIL | FAIL | 別の文脈衝突も発生 |
| 符号化 `K_1`, `A→a,B→aa,C→b` | 2 | PASS | PASS | 第1段は通る |
| 符号化 `K_2` | 6 | PASS | PASS | 第2段は通る |
| 符号化 `K_3` | 42 | FAIL | FAIL | 深さ3で混合因子の衝突 |

**第1の完全反例**：`A_2` では `b,bb` が受理されて同じ内容 `{b}` と空文脈を共有するが、`(ε,b)` は `b` の文脈で `bb` の文脈ではない。実際 `bb∈L` だが `bbb∉L`。従って代入可能性違反。

**第2の完全反例（単純な二文字符号化）**：三文字の `K_0={A}`、`K_i=B K_{i-1}K_{i-1}B\cup C K_{i-1} C` に `A↦a, B↦aa, C↦b` を適用する。深さ3の言語について

- `x=babb` と `y=aaaaaab` はどちらも内容 `{a,b}`（**補足**：`y` は実際には `a` と `b` の双方を含む）。共通文脈 `(bb,b)` に対し `bbbabbb` と `bbaaaaaabb` はともに受理される。
- しかし文脈 `(baababaa,ε)` について `baababaa`+`aaaaaab` は受理、`baababaa`+`babb` は非受理である。

よって `D_L(x)∩D_L(y)≠∅` だが `D_L(x)≠D_L(y)` で、**`K_3` の符号化は `C_{1,c}` に入らない**。この一点で、当該符号化による任意段数の証明は不成立となる。元の三文字族が代入可能であることとの矛盾ではない（符号化により因子の新たな一致・重なりが生じるため）。

### Python 3 標準ライブラリだけによる完全検査コード

`py -3 two_letter_fanout1_verify.py` で実行できる。以下は実行したファイルと同一の全文である。

```python
#!/usr/bin/env python3
"""Finite one-hole typed substitutability: exact context enumeration.
Python 3 standard library only. Run: py -3 two_letter_fanout1_verify.py
"""
from collections import defaultdict


def ctype(word):
    return ''.join(sorted(set(word)))


def utype(word):
    return 'zeta' if 'b' in word else 'one'


def contexts_of(language):
    data = defaultdict(set)
    for word in sorted(language):
        for left in range(len(word)):
            for right in range(left + 1, len(word) + 1):
                data[word[left:right]].add((word[:left], word[right:]))
    return data


def check(language, typing):
    """Return (True,None) or a fully checkable counterexample.

    If x,y share a context yet have different context sets, return the
    common context and one distinguishing context (in x or y).
    """
    data = contexts_of(language)
    words = sorted(data, key=lambda x: (len(x), x))
    groups = defaultdict(list)
    for x in words:
        groups[typing(x)].append(x)
    for group in groups.values():
        for i, x in enumerate(group):
            for y in group[i + 1:]:
                common = data[x] & data[y]
                if common and data[x] != data[y]:
                    key = lambda lr: (len(lr[0]) + len(lr[1]), lr)
                    shared = min(common, key=key)
                    only = min(data[x] ^ data[y], key=key)
                    holder = 'x' if only in data[x] else 'y'
                    return False, (x, y, shared, only, holder)
    return True, None


def compressed_all_b(n):
    """A_0 -> a, A_i -> A_{i-1} A_{i-1} | b."""
    words = {'a'}
    for _ in range(n):
        words = {u + v for u in words for v in words} | {'b'}
    return words


def blocks(m, n):
    """L_{m,n} = ({a^(2^m), b})^(2^n)."""
    words = {''}
    for _ in range(2 ** n):
        words = {w + t for w in words for t in ('a' * (2 ** m), 'b')}
    return words


def ternary(n):
    """K_0={A}; K_i=B K_{i-1} K_{i-1} B union C K_{i-1} C."""
    words = {'A'}
    for _ in range(n):
        words = {'B' + x + y + 'B' for x in words for y in words} | {
            'C' + x + 'C' for x in words}
    return words


def binary_code(words, p=1, q=2, t=1):
    table = {'A': 'a' * p, 'B': 'a' * q, 'C': 'b' * t}
    return {''.join(table[ch] for ch in w) for w in words}


def show(name, words):
    print(name, 'size=', len(words), 'lengths=', len({len(w) for w in words}),
          'max_length=', max(map(len, words)))
    for name2, typing in (('content', ctype), ('U1', utype)):
        ok, witness = check(words, typing)
        print('  ', name2, 'PASS' if ok else 'FAIL')
        if not ok:
            x, y, (left, right), (left2, right2), holder = witness
            print('    x=', repr(x), 'y=', repr(y))
            print('    shared context=', repr((left, right)))
            print('      words=', repr(left+x+right), repr(left+y+right))
            print('    separating context=', repr((left2, right2)),
                  'held by', holder)
            print('      in L=', (left2+x+right2) in words,
                  (left2+y+right2) in words)


def main():
    show('c-but-not-U1', {'b', 'ab'})
    show('unequal-weights', {'aa', 'ab', 'bbb'})
    show('quadratic L_(1,2)', blocks(1, 2))
    for n in (1, 2, 3):
        show('naive doubling n=' + str(n), compressed_all_b(n))
    for n in (1, 2, 3):
        show('coded K_n n=' + str(n), binary_code(ternary(n)))


if __name__ == '__main__':
    main()
```

## 7. 到達点、未解決点、次の探索設計

**T1：未達。** `L_n∈C_{1,c}` と小さい `‖G_n‖,θ_n` を両立させ、`μ_{a}` 又は `μ_{b}` を超多項式にする族は得られなかった。有限検査で通った n=1,2 の符号化を一般化したと主張することはできず、n=3 で実際に破綻する。

**T2：達成した条件付き障害。** 補題1により稀な内容型 `{a,b}` を使う下界戦略を排除した。定理3・系4により、両文字の出現数スペクトルが高々多項式個の部分クラスでは、両方の B 作用素について一様多項式特徴データが成立する。定理5は**重み種類数 k と λ の大きさに依存**する範囲で同じ結論を与える。語長の種類数の障害は10月30日の既報であり、重複して新規性を主張しない。

**T3：部分的に達成。** 混合内容の短語について、一穴で使える「標識二本の経路を残して他を短縮する」方法を与えた。ただし `a^N` 又は `b^N` という純型を短くするには、別文字を含む差替えを禁止する型の壁があり、短い内容同型の代表元を作れない。付録 H の二穴交換がその壁を壊すのに必要なことを明示した。

**次に狙うべき具体的方向**は、（i）有限 `C_{1,c}` の純 `a^N` と同居し得る混合語について、異なる `b`-出現数の**位置**を一穴文脈がどこまで同定するか、（ii）三文字族の符号化を `A↦a^p,B↦a^q,C↦b^t` の一般の `p,q,t` に拡げたとき、深さ3で必ず違反するか、（iii）長い純語を維持して `h_b` を超多項式に増やす族が、自動的に一致文脈による交換矛盾を作るか、の三つである。いずれも本報告時点で一般命題としては**未証明**である。

## 8. 出典・先行研究の扱い

- 正本：[`main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)。利用箇所：`def:class-cmcf`, `lem:thickness-equivalence`, `thm:data-from-typed-thickness`, `prop:rare-type`, `cor:distribution-representatives`, `lem:typing-monotone`, `prop:sl-reduction`, `thm:two-letter-content`, `cor:two-letter-semilattice`, Appendix H。とくに `thm:two-letter-content` が主張するファンアウト2上界は `τ(G,c)≤[42r(r+1)+117(r+1)]|V|²θ⁵` と、共通特徴標本 `O_r(‖G‖³θ⁵)` であり、本研究のファンアウト1と混同しない。
- 既存の一文字中立型の詳細：[`parked/parked_u1_typing_level.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/parked/parked_u1_typing_level.tex)。`prop:binary-u1-quadratic`, `prop:binary-u1-weight-slice`, `prop:u1-weight-all-fanout`, `prop:three-letter-family`。
- 10月30日の独立探索：[`astra_binary_u1_fanout1_2026-10-30.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/archive-v1/revision/astra_binary_u1_fanout1_2026-10-30.md) と [`astra_binary_u1_fanout1_exponent_2026-10-30.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/archive-v1/revision/astra_binary_u1_fanout1_exponent_2026-10-30.md)。出現数スペクトル、既知の長さスペクトルおよび一定重みの鋭い評価を照合した。
- [`chatgpt_binary_u1_fanout1_2026-10-30.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/archive-v1/revision/chatgpt_binary_u1_fanout1_2026-10-30.md)、[`deepseek_binary_u1_f1_search_2026-10-30.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/archive-v1/revision/deepseek_binary_u1_f1_search_2026-10-30.md)。DeepSeek 予想 C `τ≤‖G‖θ` は既に偽とされているので採用していない。
- A. Clark and R. Eyraud, *Polynomial Identification in the Limit of Substitutable Context-free Languages*, JMLR **8** (2007), 1725–1745, [掲載情報](https://jmlr.csail.mit.edu/beta/papers/v8/clark07a.html)。一穴代入可能性の原典であり、本文の型付きスペクトル評価が同論文で明示的に先取りされているとの確認は**できていない**。
- 追加の外部文献検索を行ったが、今回の `c` 特有の定理3・5と完全一致する既刊定理の有無は**未確認**。「本報告で証明」と「文献上の新規性がある」は異なる評価である。

**最終判断**：本報告はファンアウト1/2の分離そのものを**証明していない**。一方、下界族に必要な「純語しか長くできない」「別文字の計数スペクトルが超多項式に広がる」という具体的かつ検証可能な制約を確立し、有限ケースの符号化反例を再現可能にした。
