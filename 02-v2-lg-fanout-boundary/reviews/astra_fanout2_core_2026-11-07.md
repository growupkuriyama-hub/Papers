成果の分類：(B) 閉じた部分クラスの多項式上界を証明。同じ定理は「一文字一辺の経路条件＋単一の可換群剰余類」による反例設計に対する (C) の障壁にもなる。(A) は未解決。

# ファンアウト2・三文字・内容型付け：経路と可換群剰余類で定義される言語の三次上界

研究日：2026-11-07（日本時間）。依頼された `q` の一般上界および `op:fanout-two` 全体は解決していない。本報告の新たな結論は、以下の**明示した部分クラス**に限る。一般の Parikh-saturated 言語にも拡張したとは主張しない。

## 1. 結論と対象クラス

### 定義1.1 [証明済み／定義]

`Σ={a,b,c}` とする。次のデータを取る。

1. 有限有向グラフ `D` と開始・終了頂点 `s,t`。**各文字はちょうど一本の辺のラベル**であり、異なる辺が同じ文字を持つことはない。ループと多重辺は許す。
2. 可換群 `A`、準同型 `φ:Σ*→A`、部分群 `H≤A`、`g∈A`。群は有限でなくてもよく、群・係数・指数に一様な上限を置かない。
3. 許される非空内容集合の族 `𝓜⊆2^Σ\{∅}`。

`Path_D(s,t)` を s から t への経路のラベル語集合として、

\[
 L=Path_D(s,t)\cap\varphi^{-1}(g+H)
       \cap\{w\in\Sigma^+:\operatorname{cont}(w)\in\mathcal M\}. \tag{1}
\]

この**等号**を仮定する。「L の全語が右辺を満たす」という包含だけでは不足する。
全ての文字が一頂点のループなら、(1) は可換群剰余類の原像を内容で制限した言語になる。二頂点以上なら、順序に依存する言語も含む。

### 定理1.2 [証明済み／部分クラス (1) における無条件の定理]

`L` が (1) の形で、`G` が L の任意の reduced good MCFG 表示、`θ=\bar θ_G` とする。`L` に内容 `{a,b}` の語があれば、

\[
 \boxed{\mu_{ab}(L)\le 12\theta^3.} \tag{2}
\]

従って、依頼の最短語 W の導出における c-強制の重い節点の任意の反鎖 Q に対して、

\[
 \boxed{q\le\left\lfloor\frac{12\theta^3}{\theta+1}\right\rfloor
              \le12\theta^2.} \tag{3}
\]

定数12は `v,r,D,A,H,g,𝓜` に依存しない。実際、(2) の証明はファンアウト2にも固定ランクにも依存しない。各文字の役割を置換すれば、三文字中の任意の二文字内容にも同じ上界を得る。

### 系1.3 [証明済み／設計障壁 (C)、定理1.2の系]

(1) の形の言語族では、どの good 表示を選んでも

\[
 \bar\theta(G_n)\ge (\mu_{ab}(L_n)/12)^{1/3}.
\]

従って、群の位数・係数やグラフの選択を変えても、`θ=poly(n)` と `μ_ab=n^{ω(1)}` を同時に満たせない。文法サイズを増減してもこの結論は変わらない。

これは「文字の並び順に依存すれば既知の可換設計の障壁を回避できる」とする方針のうち、**一文字一辺の経路制約を一つの可換群剰余類に重ねる設計**を除外する。一般の順序依存不変量、非可換群、多数の受理剰余類、内容ごとに異なる剰余類は除外していない。

### 今回の到達点

切り替え立方体だけの一段・多段 SUB から一般の近道を得たわけではない。(2) は、文法の**全規則**が持つ短い成功証人を、三次元の整数格子にまとめることで証明する。格子内で見つけた短い正ベクトルを実際の語に戻せることが (1) の役割である。一般の言語ではこの最後の操作を正当化できない。

## 2. 出典と既知の結果との区別

次を実際に取得し、使用部分を照合した。

- [定義の正本：59頁凍結原稿](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/parked/2026-11-06_focus/main_before_focus_59pp.tex)：`def:standard-mcfg`、`def:grammar-properties`、`def:class-cmcf`、`lem:thickness-equivalence`、`prop:rare-type`、`prop:full-content-types`、`op:fanout-two`。さらに今回の直接の道具として `prop:abelian-filter-short`、`prop:abelian-coset-filter`、`lem:app-lf-path`。
- [README Change log](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/README.md)：特に (54)、(80)、(138)、(153)、(155)、(157)。取得時の default branch を使用。凍結原稿と現在の焦点化原稿を混同しない。
- [(138) intrusion](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_intrusion_2026-11-04.md)：定理3.1。
- [(153) μ_ab](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_mu_ab_2026-11-05.md)：補題1–3、命題5。
- [(155) virtual_length](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_virtual_length_2026-11-05.md)：定理6.1。
- [(54) Problem G](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_problemG_2026-11-01.md)：定理1。**二文字、有限可換群の単位元原像、CFG**の群位数上界であり、本報告の三文字・任意剰余類・無限群・経路条件を含む主張とは区別する。

11月6日の次の4報は GitHub の指定パスが404だったため、保存済みの完全な本文を読んだ。GitHub に存在する番号を捏造せず、ファイル名と節・定理番号で参照する。

- [shortcut_classification](https://chatgpt.com/library?file_id=libfile_ec6cc4b3da308191ae72048bcd58def7&account_id=personal)：定理3.1、定理6.1–6.2。
- [negative_design](https://chatgpt.com/library?file_id=libfile_2434b5090f788191983561dac0f85403&account_id=personal)：定理D、命題B4／N10。
- [frame_equivalence](https://chatgpt.com/library?file_id=libfile_713bf75cf78c8191a1e825debd1c9d86&account_id=personal)：定理F、定理A4、定理B2／N12。
- [outer_c](https://chatgpt.com/library?file_id=libfile_b02e4697f5f48191990a2700b16df66a&account_id=personal)：A1、S1–S3、§5。

| 本報告の項目 | 既知との関係 |
|---|---|
| §3 の所属証明 | `lem:app-lf-path` と `prop:abelian-coset-filter` の組合せ。既知であり新成果に数えない |
| §4 の短い規則欠損ベクトル | README (80)、`prop:abelian-filter-short` の証明そのもの。新成果に数えない |
| §5 の三次元の座標面上の短代表 | 低次元の整数格子計算。独立に完全証明し、最適性や文献上の初出は主張しない |
| 定理1.2 | 既知の短い欠損ベクトルを**指定された欠損内容型の短代表**に変える帰結。経路への復元を含む。この帰結は上記報告書の主張ではない |
| 系1.3 | N10の一文字出現下界やN12の長さギャップとは別に、剰余類を満たす座標面の代表長を制約する。特定の既知候補を再度失格にするだけの主張ではない |
| §7 の二族 | c の個数・連数・K_c が無限で、非負の等 a,b 重みの一水準でもない。依頼§2の該当する既知上界の仮定を満たさない |

整数線形方程式の小さい解の上界自体は古典的な主題である。関連する原典として [Borosh–Treybig, Bounds on Positive Integral Solutions of Linear Diophantine Equations II (1979)](https://doi.org/10.4153/CMB-1979-045-2) および [Borosh–Flahive–Treybig, Small solutions of linear Diophantine equations (1986)](https://www.sciencedirect.com/science/article/pii/0012365X8690138X) がある。本報告ではそれらの一般定理を適用せず、必要な三次元の評価を以下で全て証明する。文献全体に対する新規性監査は未完了である。

## 3. C₁・C₂ の所属の完全な証明

### 補題3.1 [証明済み／既知の経路補題]

一文字一辺の経路言語 `R=Path_D(s,t)` は、非空成分・非空内部固定部という本件の規約の下で、全 arity の無型付き代入可能性を満たす。

**証明。** `E=e₀□₁e₁…□_d e_d`、`E[x],E[y]∈R` とする。各穴の開始頂点は、直前の固定語の末尾の辺の終点で決まる。第1穴で `e₀=ε` なら s である。終了頂点も直後の固定語の先頭の辺の始点で決まり、最後の穴で `e_d=ε` なら t である。内部の固定語は非空なので、この規定が全穴に適用できる。従って `x_i,y_i` は同じ二頂点間の経路である。

任意の `F[x]∈R` を取る。非空語 `x_i` の最初・最後の文字が各一本の辺を指定するので、Fでの `x_i` の両端頂点もEでの両端頂点と同じである。各 `x_i` を同じ両端の経路 `y_i` で置換すると、隣接する辺の接続、全体の開始頂点s、終了頂点tを保つ。従って `F[y]∈R`。x,yを交換して逆向きも得る。□

### 命題3.2 [証明済み／定義1.1の所属]

(1) の L は全 arity で内容型付き代入可能である。特に fan-out≤2 のMCFG表示があれば `L∈C_{2,c_Σ}` である。

**証明。** `cont(x_i)=cont(y_i)` と `E[x],E[y],F[x]∈L` を仮定する。補題3.1より `F[y]∈Path_D(s,t)`。

可換群を加法記法で書く。固定部の値を消去すると

\[
 \Delta=\sum_i\bigl(\varphi(y_i)-\varphi(x_i)\bigr)
       =\varphi(E[y])-\varphi(E[x])\in H.
\]

可換性により同じΔがFでも差分になり、`φ(F[y])=φ(F[x])+Δ∈g+H`。また各穴の内容が一致するため、`cont(F[y])=cont(F[x])∈𝓜`。穴が非空なので完成語も非空である。従って `F[y]∈L`。対称性で分布の一致を得る。これは `d=1,2` を含む全てのdについての一般証明であり、有限計算を所属の根拠にしていない。□

**クラス記号の注意。** 「arity 1の代入可能性」と「文脈自由言語であることまで含む `C_{1,c}`」は別である。一般の定理1.2では前者を証明している。§7の二族は明示したCFGを持つため、後者にも実際に属する。

## 4. 厚さから得られる短い格子生成元

以下 `π(w)=(|w|_a,|w|_b,|w|_c)` とし、組のπは成分のπの総和とする。

### 補題4.1 [証明済み／README (80) の既知の機構を正確に抽出]

任意の reduced good MCFG G に対し、非負整数ベクトル `p₀` と有限集合 `𝒟⊂ℤ³` が存在して、

\[
 \|p_0\|_1\le\theta,\qquad
 \|\delta\|_\infty\le\theta\quad(\delta\in\mathcal D),\qquad
 \pi(L(G))\subseteq p_0+\Lambda,
 \quad\Lambda=\operatorname{span}_{\mathbb Z}\mathcal D. \tag{4}
\]

さらに `p₀` は実際の成功語のParikhベクトルで、各δは長さ≤θの**二つの成功語の差**である。

**証明。** 各非終端Bに、総長最小の生成組 `u_B` を一つ選び、`q_B=π(u_B)` とする。厚さ補題(ii)から `||q_B||₁≤θ`。`p₀=q_S` とする。

規則 `R:A→ρ(B₁,…,B_k)` の明示終端ベクトルを `t_R` として

\[
 \delta_R=t_R+\sum_{j=1}^k q_{B_j}-q_A. \tag{5}
\]

Rを使う長さ≤θの成功導出を選ぶ。Rの一つの使用位置で、(i)A部分木全体を `u_A` の導出に替えた語p、(ii)Rを残し、各子だけを `u_{B_j}` の導出に替えた語p′を作る。総長最小の生成組への置換なので、どちらも元の語より長くならない。good の非削除性・線形性により各成分の文字はちょうど一度残るから、`π(p′)−π(p)=δ_R`。p,p′は成功語で長さ≤θなので、各座標の差の絶対値も≤θである。

任意の成功導出Tで(5)を全節点について足すと、各非根の `q_B` が親側の正項と自分側の負項で消え、

\[
 \pi(w)=q_S+\sum_{z\in T}\delta_{R(z)}. \tag{6}
\]

従って `𝒟={δ_R:R∈P}` とすれば(4)を得る。□

### 系4.2 [証明済み]

Gが (1) の L を生成するとき、任意の `p∈p₀+Λ` は、整数ベクトルとして群剰余類条件と経路の流量条件を満たす。

**証明。** `φ` を可換群への整数準同型 `Φ:ℤ³→A` に延長する。各δは同じ剰余類g+H内の二成功語の差だから `Φ(δ)∈H`、`Φ(p₀)∈g+H`。

各文字eの辺について、頂点ごとの流出数−流入数を表す整数ベクトルを `∂e` とする。全ての成功語wで `∂π(w)=1_s−1_t`。従って `∂δ=0`、`∂p₀=1_s−1_t`。これらを整数線形結合して結論を得る。□

重要なのは、(4)では逆包含をまだ主張していない点である。一般の文法では `p₀+Λ` の非負ベクトルが生成されるとは限らない。

## 5. 三次元格子の指定座標面における短代表

### 補題5.1：整数直線上の縮小 [証明済み]

整数A,Bが同時には0でなく、正整数x,yが `Ax+By=h` を満たすとする。整数倍の `(B,−A)` を加減するだけで正整数解 `x′,y′` を作れて、

\[
 x'+y'\le |h|+|A|+|B|. \tag{7}
\]

**証明。** A,Bが同符号でともに非零なら、`|h|=|A|x+|B|y≥x+y` だから変更不要。

A=0なら `y=h/B` は正整数で `y≤|h|`。xを `|B|` の整数倍で減らして `1≤x′≤|B|` とできる。B=0の場合も対称。

AB<0なら `(B,−A)` またはその負は両座標が正の `( |B|,|A| )` である。これを、両座標が正のままでいられる最大の非負整数回だけ引く。その結果 `x′≤|B|` または `y′≤|A|`。前者なら

\[
 y'=\left|\frac{h-Ax'}B\right|
       \le\frac{|h|}{|B|}+|A|\le|h|+|A|,
\]

従って(7)。後者も対称。変更は全て指定した整数方向の整数倍である。□

### 補題5.2：三次元の面代表 [証明済み]

`θ≥1` は整数、`p₀∈ℕ³` は `||p₀||₁≤θ`、Λは座標絶対値≤θの整数ベクトル集合𝒟で生成される格子とする。`p₀+Λ` が面

\[
 F_{ab}=\{(x,y,0):x,y\in\mathbb Z_{\ge1}\}
\]

と交わるなら、その交点に `x+y≤12θ³` のベクトルが存在する。

**証明。** 交点の一つpを固定し、`k=dim_ℚ span_ℚ Λ` ごとに分ける。生成集合𝒟から有理線形独立なk本を選ぶ。以下の全変更は、それらの整数線形結合で行う。選んだk本がΛ全体の整数基底であることは仮定しない。

**k=0。** `p=p₀` なので `x+y≤θ`。

**k=1。** 非零生成元uを選ぶ。`p−p₀=αu`、`α∈ℚ`。

- `u_c≠0` なら `α=−p₀,c/u_c`。従って `|α|≤θ` で、
  `x+y≤p₀,a+p₀,b+|α|(|u_a|+|u_b|)≤θ+2θ²≤3θ²`。変更不要。
- `u_c=0` なら `p₀,c=0`。`A=u_b,B=−u_a` とすると少なくとも一方は非零で、
  `Ax+By=h=u_b p₀,a−u_a p₀,b`、`|h|≤θ²`。
  補題5.1の方向 `(B,−A)=−(u_a,u_b)` はΛに属するので、同じ剰余類内で
  `x′+y′≤θ²+2θ≤3θ²` に縮められる。

**k=2。** 独立な生成元u,vを選び、`n=u×v=(A,B,C)≠0` とする。各座標の絶対値は≤2θ²。平面の方程式は

\[
 n\cdot p=n\cdot p_0=h,\qquad |h|\le2\theta^3. \tag{8}
\]

- `(A,B)≠(0,0)` なら、c=0上で `Ax+By=h`。方向
  
  \[
   (B,-A,0)=u_c v-v_c u\in\Lambda
  \]
  
  に沿って補題5.1を適用できる。従って
  `x′+y′≤2θ³+4θ²≤6θ³`。
- `A=B=0` ならu,vともc成分0で、交点の存在からp₀,cも0。`d=|C|=|u_a v_b−u_b v_a|` は `1≤d≤2θ²`。
  `v_b u−u_b v=(C,0,0)`、`−v_a u+u_a v=(0,C,0)` より、`d e_a,d e_b∈Λ`。
  x,yをそれぞれdを法として `1,…,d` の代表へ減らすと、c=0を保ち、同じ剰余類に留まり、`x′+y′≤2d≤4θ²`。

**k=3。** 独立な生成元u,v,zを列に持つ整数行列Mを作り、`d=|det M|≥1`。行列式の6項展開から `d≤6θ³`。余因子行列の恒等式 `M adj(M)=(det M)I` により `d e_a,d e_b,d e_c∈Mℤ³⊆Λ`。pのa,b座標を独立に `1,…,d` の代表へ減らし、c=0は変えない。従って `x′+y′≤2d≤12θ³`。

全ての場合で非負座標、a,bの正値、c=0、および `p₀+Λ` への所属を保っている。□

**定数と範囲。** 階数0,1,2,3でそれぞれ `θ,3θ²,6θ³,12θ³` を使用した。12は簡明な一様定数であり最良とは主張しない。整数格子の指数を有限と仮定していないため、無限可換群も扱える。

## 6. ベクトルを受理語に戻す：主定理の証明

### 補題6.1：同じ辺支持上の流量の実現 [証明済み／Euler路の標準事実]

一つの s→t 経路が使用する辺の集合をJとする。各辺 `e∈J` に正整数回数 `p_e` を与え、それ以外は0とし、`∂p=1_s−1_t` を満たすなら、各辺eをちょうど `p_e` 回使う s→t 経路がある。

**証明。** 各辺を指定回数だけ複製した有限有向多重グラフを考える。もとの経路がJ全体を使用しているので、非孤立頂点の無向支持は連結で、s,tを含む。

s≠tなら、t→sの特別な辺を一本追加する。すると全頂点で流出数=流入数となり、無向支持の連結性は保たれる。s=tなら追加不要。

この平衡したグラフで、辺を重複使用せずに出発頂点から歩く。未使用の出辺がなくなるまで続けると、出発点以外では停止しない。実際、出発点以外への最後の到着時点では使用入辺数が使用出辺数より1大きく、総入辺数=総出辺数だから未使用の出辺が残る。有限なので出発点で閉じた歩道を得る。

未使用辺があれば、連結性により現在の歩道の頂点に接続する未使用辺が存在する。使用済み閉歩道を除いた残りも各頂点で平衡なので、そこには未使用の出辺も存在する。その頂点から同じ操作で閉歩道を作り、既存の歩道に挿入する。少なくとも一本の新たな辺を使用するので、有限回で全辺を使う閉歩道になる。

特別な辺を追加した場合は、その辺の直後から読み、直前で止めることで元のグラフのs→t経路を得る。追加しなかった場合はsから閉歩道を読む。□

### 定理1.2の証明 [証明済み]

補題4.1で `p₀,Λ` を取る。既存の内容ab語Wのベクトルは `(x,y,0)`、x,y≥1で `p₀+Λ` に属する。補題5.2により、同じ剰余類内に `p′=(x′,y′,0)`、`x′,y′≥1`、`x′+y′≤12θ³` がある。

系4.2により `Φ(p′)∈g+H`、`∂p′=1_s−1_t`。p′の辺支持はWと同じ `{a,b}` なので、補題6.1によってこのベクトルを持つs→t経路w′を作れる。`cont(w′)={a,b}` はWが存在するため𝓜に含まれる。従って(1)の**等号**から `w′∈L`。長さは `|w′|=x′+y′≤12θ³` で、(2)を得る。

Qの節点は比較不能なので、その生成文字位置はWの中で互いに素である。goodの非削除性により、各節点の総生成長が全てWの長さに寄与する。各節点は重いので整数長≥θ+1。従って

\[
 q(\theta+1)\le\sum_{z\in Q}\ell_z\le |W|=\mu_{ab}(L)\le12\theta^3,
\]

から(3)。最後の反鎖評価には、c-強制性や導出の節点数最小性さえ不要である。□

**一般問題との境界。** 証明の中で `w′∈L` を結論する箇所だけは、一般のC₂言語の性質からは導けない。SUB閉包からこの語が生成される証明書は提示していない。(1)を包含に弱めること、可換群条件を任意の非可換条件に変えること、型付き非終端の任意のτにそのまま適用することは、いずれも未証明である。

## 7. 適用検査：既知の有界個数条件を満たさない無限族

### 7.1 無限可換群・非正則の族 [証明済み]

整数 `m≥2` に対し

\[
 L_m=\{w\in\{a,b,c\}^+: |w|_a-|w|_b+m|w|_c=m\}. \tag{9}
\]

一頂点にa,b,cの三ループ、`A=ℤ`、`H=0`、`φ(a)=1,φ(b)=−1,φ(c)=m,g=m`、全非空内容を許す𝓜を取れば(1)になる。命題3.2により全arityで内容型付き代入可能である。

#### 完全な文法 [証明済み]

非終端 `X_k (−m≤k≤m)`、開始 `X_m`、全てarity1とする。規則は次の**全て**である。

\[
 X_k\to X_iX_j\quad(-m\le i,j,k\le m,\ i+j=k),
 \qquad X_1\to a,\ X_{-1}\to b,\ X_m\to c. \tag{10}
\]

各生成語の重みが添字と一致することは規則に関する帰納法から従う。逆を示す。

重みがk∈[−m,m]の非空語wについて、長さに関する帰納法を使う。長さ1は終端規則そのもの。長さ≥2では、非空の真の接頭語の重みPを

\[
 I_k=[\max(-m,k-m),\min(m,k+m)]
\]

に入れれば、その接頭語と残りの接尾語の重みがともに[−m,m]に入るので、帰納法と `X_k→X_P X_{k-P}` を使える。

そのような接頭語が存在することを証明する。第一文字の重みがI_k内ならそれを選ぶ。第一文字の重みがI_kの下なら、各文字の重みは[−m,m]内なのでk>0で、I_kの下端はk−m、上端はmである。接頭語重みの列が初めてk−m以上になる時点を取る。直前はk−m未満で、一回の増加は高々mだから、到達値はk未満、従ってm以下である。この時点は最後の文字ではない。もし最後なら到達値kに反する。よって非空の真の接頭語を得る。

第一文字の重みがI_kの上の場合も対称で、k<0、上端k+m、下端−mとなる。初めてk+m以下になる時点の値は、一回の減少が高々mなのでkより大きく、−m以上である。この時点も最後ではない。これで逆包含が証明でき、(10)は正確に(9)を生成する。

各X_kは、k>0ならa^k、k<0ならb^(−k)、k=0ならabを生成する。X_mから `X_m→X_m X_0→X_m X_{-k}X_k` として全非終端に到達できる。従ってreducedである。全規則は非空、非削除、非置換、非併合でgood、fan-out1、rank2。

二項規則は `3m²+3m+1` 本。正本のサイズ定義で一つ当たり5、終端規則は一つ当たり2なので

\[
 v=2m+1,\qquad \|G_m\|=15m^2+17m+12. \tag{11}
\]

任意のX_kの規則を使用する短い成功導出は、上記の到達文脈で左側X_mをcに、X_{−k}を長さ≤mの生成語にし、当該規則の子をそれぞれ長さ≤mの生成語にすればよい。二項規則の場合は長さ≤`1+m+2m=3m+1`。終端規則の場合はこれ以下。従って

\[
 \bar\theta(G_m)\le3m+1. \tag{12}
\]

全ての表示で定理1.2が適用されるが、(10)は部分クラスの非空性を具体的に保証するための一つの表示である。

#### 既知の仮定では覆われないこと [証明済み]

- c-freeのab語では `#a−#b=m`、`#b≥1` だから `μ_ab=m+2`。`a^{m+1}b` が達成する。
- `L_m∩a*b*={a^{m+k}b^k:k≥0}` は非正則。接頭語 `a^{m+i}` と `a^{m+j}` はi≠jなら接尾語b^iで区別されるため、有限個の右合同類では足りない。従ってL_mも非正則。
- `w_j=(cb^m)^{j-1}cab (j≥1)` は重みm、全文字を含み、cの個数もcの連数もj。従ってc個数、連数、K_c、outer_cの `A_θ` は全て非有界（`h=1` を取れる）。
- `a^m,a^{m+1}b∈L_m`。`λ(a)=λ(b)>0` ならこの二語のλ値が異なるため、λ(c)の選び方によらず言語全体は一水準に入らない。
- 三文字が実際に出現し、標的は全文字型でなくab型。従って二文字の定理や全文字型の上界を、このGの同じθのまま直接適用できない。ab影への制限で厚さが制御できるという仮定も置いていない。
- `c,cab∈L_m` なので、各文字は長さ≤3の成功語に出現する。N10からmに比例する厚さ下界は得られない。`cab,cab ab,cab(ab)^2,…` も受理され、短い語からの大きな長さギャップを利用したN12の設計でもない。

純a語の最短長に関する既知の定理I・II-Bの分類は、本族のab型の上界を直接述べない。本族についてそれらと別の補題を組み合わせたさらに強い個別評価が不可能だとは主張しない。適用検査で必要なのは、依頼§2の列挙されたab上界の追加仮定を満たさない無限族を明示することであり、上記はその検査を満たす。

### 7.2 順序依存・有限群の族 [証明済み]

二頂点0,1を取り、aを0→1、bを1→0、cを0→0の辺とする。`m≥2` に対し

\[
 R_m=\{w\in(ab\mid c)^+: |w|_a-|w|_c\equiv0\pmod m\}. \tag{13}
\]

これは(1)で `A=ℤ/mℤ, φ(a)=1,φ(b)=0,φ(c)=−1,g=0` としたもの。例えばabcは入るがbacは入らないのでParikh-saturatedではない。

完全なgood右線形文法を次で与える。添字はmod m、非終端は `U_j,V_j`、開始 `U_0`。

\[
 U_j\to aV_{j+1}\mid cU_{j-1},\qquad V_j\to bU_j
 \quad(0\le j<m),\qquad V_0\to b,\quad U_1\to c. \tag{14}
\]

Uは頂点0、Vは頂点1、添字は読了部分の `#a−#c`。継続規則はちょうど3種類の遷移、終端規則はU₀に到着して終了できる遷移だけなので、(14)は正確に(13)を生成する。各U_jにはcの反復で到達でき、各V_jにはaを足して到達できる。各状態から頂点0・剰余0に戻れるため全てproductive。非空の右線形規則なのでgood、fan-out1、rank1である。

`v=2m, ||G||=14m+4`。任意の状態への接頭語を長さ≤m、各状態からの非空の受理接尾語を長さ≤mで取れる。継続規則を一回使用してこれらをつなぐと、`θ≤2m+1`。終端規則もこの範囲に入る。

`μ_ab(R_m)=2m`。全文字語 `(abc)^j` は全て受理されるので、cの個数・連数・K_cは非有界。`(ab)^m` と `(ab)^{2m}` の両方を含むため、非負の等a,b重みの単一水準ではない。三文字ともabcという長さ3の語に出現する。

この族単独なら有限状態の直接評価も可能である。本報告の定理は、その特定の文法や状態数に依存せず、任意の表示と任意の群に一様なθの三次式を与える点にある。適用検査の非正則な証人は7.1、順序依存の証人は7.2で役割を分けている。

### 7.3 重い c-強制反鎖が実際に増大する族 [証明済み]

適用例が「そもそもq=0」のものだけでないことも示す。`k≥6, M=k²−1, p=ab` と置き、7.2と同じ二頂点グラフ上で

\[
 B_k=\{w\in(p\mid c)^+: |w|_a-k|w|_c\equiv0\pmod M\}. \tag{17}
\]

全ての剰余g∈ℤ/Mℤに非終端Y_gを置き、開始Y₀、全二項規則

\[
 Y_{i+j}\to Y_iY_j\quad(i,j\in\mathbb Z/M\mathbb Z),
 \qquad Y_1\to ab,\quad Y_{-k}\to c \tag{18}
\]

を置く。p,cというブロックで一意に分解できるため、規則の帰納法とブロック数の二分帰納法で、Y_gは群値gの非空ブロック列をちょうど生成する。

各gを `g=qk+t, 0≤q≤k−1, 0≤t<k` と書く。語 `p^{t+1}c^{k-q}` の値は `t+1−k(k−q)=g−M≡g`、文字長は≤3k。従って全Y_gがproductiveで、`Y_0→Y_{-g}Y_g` により全てreachable。文法はgood、fan-out1、rank2、

\[
 v=M,\qquad \|G_k\|=5M^2+M+5,\qquad\theta\le9k. \tag{19}
\]

厚さの評価は、任意の二項規則を `Y_0→Y_{-g}Y_g→Y_{-g}Y_iY_j` に埋め、三非終端に長さ≤3kの代表を用いることによる。終端規則も長さ≤3k+2の成功語に埋め込める。

c-freeの受理語はpの正のM倍の冪なので、最短Wは `p^M`、`μ_ab=2M`。その全導出では終端葉は全て `Y_1→ab` でちょうどM個、内部節点は二項節点M−1個である。従って全てのWの導出が同じ最小節点数2M−1を持つ。

`h=5k<M` とする。Wをq₀=`⌊M/h⌋` 個の連続した `p^h` ブロックと長さ<hブロックの残余に分け、各長さhブロックをまず一つの部分木にし、それらを上で二項結合する導出Tを選ぶ。これは上記の意味で節点数最小である。各ブロック根はY_hで、実生成長は `2h=10k>θ`。Y_hのc-free生成語は `p^j`、`j≡h mod M` なので最短でも2h文字を要する。従って長さ≤θの生成は全てcを含み、各ブロック根はc-強制かつ重い。これらは反鎖をなすので、Tの最大幅qは

\[
 q\ge q_0=\left\lfloor\frac{k^2-1}{5k}\right\rfloor\longrightarrow\infty. \tag{20}
\]

これは「任意の節点数最小導出でこの下界」という主張ではなく、指定した節点数最小導出での下界である。定理1.2の上界はどの導出にも成立する。

`(p^k c)^j` は全て受理され、c個数と連数はj。WとW²がともに受理されるため、等a,b正重みの単一水準ではない。所属は§3の一般証明による。この族は(54)定理2の可換群の短い代表をブロックpへ移した構成を利用しているが、ここでの役割は**非有界なc-強制重反鎖を実際に持つ適用例**の提示であり、新たな指数反例ではない。

## 8. 同値性検査：条件 (1) は結論の言い換えではない

### 命題8.1 [証明済み]

次の無限言語Jは `C_{1,c}` と `C_{2,c}` に属し、`μ_ab(J)=3` だが、どのグラフ・可換群・剰余類・内容マスクを選んでも(1)の形ではない。

\[
 J=\{w\in\Sigma^+: |w|\equiv\eta(\operatorname{cont}(w))\pmod2\},
 \quad \eta(\{a,b\})=1,\quad \eta(M)=0\ (M\ne\{a,b\}). \tag{15}
\]

**証明：所属。** 同じ成分内容を持つx,yと共通文脈Eでは、完成語の内容も同じ。`E[x],E[y]∈J` なら `∑|y_i|−∑|x_i|` は偶数。どのFでも完成語の内容はx,yで一致し、長さの偶奇も一致するから、`F[x]∈J⇔F[y]∈J`。全arityについて成立する。

Jは、状態として読了内容 `M⊆Σ` と長さの偶奇を保持し、非空の受理状態を定義どおりに選ぶ有限オートマトンで認識できる。これを非空語用の右線形文法にすればCFGである。具体的には各遷移q−x→q′に `Q_q→xQ_{q′}` を、q′が受理状態なら `Q_q→x` も置き、不要な状態を削除する。この文法はε-freeでgood、rank1、有限である。従ってクラスへの実際の所属も得る。ab内容には奇数長が必要で、aabが受理されるため `μ_ab=3`。

**証明：(1)でないこと。** 仮に(1)と表せるとする。群をHで割って、受理値を一つのgとする。`aa,aaaa∈J` なので、aの辺はs=tにあるループで、`2α=g=4α`。従って `2α=0,g=0`。同様にbbからbも同じ頂点のループ、`2β=0`。

`aab,abb∈J` から `2α+β=0` と `α+2β=0`、従って `α=β=0`。するとabは経路条件を満たし、群値0=gも満たす。内容abはaabが受理されるため𝓜に含まれる。従ってab∈Lのはずだが、(15)では偶数長のabは不受理。矛盾。□

これにより、(1)の十分性を「μ_abが多項式である」という結論から逆に取り出すことはできない。短い枠Bridgeのような最短性の言い換えでもない。仮定は言語の全語の構造に関する、独立した制限である。

## 9. 計算機検証

### 検証項目 [計算機による観察（以下の範囲のみ）]

同名の `.py` はPython標準ライブラリのみを使い、次を実行した。

1. 格子補題の階数0–3の構成を検査。階数1の小さい箱はθ=1,2、`||p₀||₁≤θ`、生成元の各座標が[−θ,θ]、係数−12…12を全列挙。加えて固定seedの120,000回の候補生成から、既知の正のab面交点を持つものを検査。大きい係数10⁶の明示例も含む。各変更が選んだ生成元の整数格子に属することも検査した。
2. 文法(10)をCKY型の区間動的計画法で認識し、`m=2,…,6`、全非空三文字語の長さ≤7について、算術的な定義(9)と比較。規則厚さは最短生成長と最短外側長のmin-plus緩和で正確に計算。
3. (18)の文法でk=6,…,12の最短生成長・外側長から厚さを計算し、(19)と指定反鎖の重さを検査。
4. 無限言語の**正確な所属述語**を用いてSUB₁・SUB₂の三前提を有限範囲から列挙し、結論も正確な述語で確認。長さ切りした集合を元の言語と取り違えていない。内部固定部は常に非空、穴も常に非空。

所属の一般証明は§3・§7・§8による。有限範囲で違反がないことを所属の証明にしていない。格子補題の一般証明も§5による。

以下は実際の標準出力である。

```text
LATTICE checked by rank [55, 4534, 7603, 23] total 12215
CFG m 2 v 5 size 106 theta 6 mu_ab 4
CFG m 3 v 7 size 198 theta 7 mu_ab 5
CFG m 4 v 9 size 320 theta 9 mu_ab 6
CFG m 5 v 11 size 472 theta 11 mu_ab 7
CFG m 6 v 13 size 654 theta 13 mu_ab 8
CFG recognition words checked 16395
ANTICHAIN k 6 M 35 theta 32 mu_ab 70 proved width >= 1
ANTICHAIN k 7 M 48 theta 42 mu_ab 96 proved width >= 1
ANTICHAIN k 8 M 63 theta 54 mu_ab 126 proved width >= 1
ANTICHAIN k 9 M 80 theta 60 mu_ab 160 proved width >= 1
ANTICHAIN k 10 M 99 theta 66 mu_ab 198 proved width >= 1
ANTICHAIN k 11 M 120 theta 72 mu_ab 240 proved width >= 2
ANTICHAIN k 12 M 143 theta 78 mu_ab 286 proved width >= 2
SUB integer-fibre-2 premise length <= 6 accepted seeds 123 checks [302683, 193145]
SUB edge-path-mod-2 premise length <= 8 accepted seeds 43 checks [93419, 165634]
SUB integer-fibre-3 premise length <= 6 accepted seeds 53 checks [38298, 13668]
SUB edge-path-mod-3 premise length <= 8 accepted seeds 16 checks [6011, 5038]
SUB integer-fibre-4 premise length <= 6 accepted seeds 59 checks [56152, 36632]
SUB edge-path-mod-4 premise length <= 8 accepted seeds 17 checks [9473, 20573]
SUB support-dependent-parity premise length <= 6 accepted seeds 777 checks [16612139, 10262814]
ALL CHECKS PASSED. Finite tests do not establish C1/C2 membership.
```

## 付録A. 立方体に関する到達限界

### A.1 [証明済み／既知の帰結、主成果に数えない]

Wと各切り替え語W_Sは同じ文法の成功語なので、補題4.1から `π(W_S)−π(W)∈Λ`。特に一節点ずつの差分もΛに入る。

しかし切り替え語だけからΛ全体の短い生成系が得られるとは証明していない。補題4.1が使う短い二成功語は、Wの導出外にある規則厚さの証人も含む。したがって、本報告を「立方体全体のSUB閉包を解いた」と読むことはできない。

### A.2 [条件付き（条件を明示）、新成果に数えない]

一般の言語について、格子で短くしたp′を持つ受理語が存在するという追加仮定を置けば、同じ長さ評価が出る。しかしその仮定を一般のSUBからは導いていない。この形の条件付き主張は主定理として採用せず、実際に受理語へ復元できる閉じた部分クラス(1)だけを主成果とした。

## 付録B. 検証スクリプト全文

実行：`python3 astra_fanout2_core_2026-11-07.py`。乱数seedは固定。有限検査は一般証明の代替ではない。

```python
#!/usr/bin/env python3
"""Finite checks for the report. Standard library only; no membership inference.

Checks explicit lattice reductions, weighted CFG recognition and thickness,
and sound SUB consequences using exact predicates for infinite languages.
"""
from itertools import product
from random import Random
from collections import defaultdict
from heapq import heappop, heappush


def cross(u, v):
    return (u[1]*v[2]-u[2]*v[1], u[2]*v[0]-u[0]*v[2],
            u[0]*v[1]-u[1]*v[0])


def dot(u, v):
    return sum(a*b for a, b in zip(u, v))


def rank_basis(ds):
    bs = []
    for u in ds:
        if not any(u):
            continue
        if not bs or (len(bs) == 1 and any(cross(bs[0], u))) or (
                len(bs) == 2 and dot(cross(*bs), u)):
            bs.append(u)
        if len(bs) == 3:
            break
    return bs


def line_reduce(p, z):
    """Subtract a same-sign direction maximally, keeping a,b positive."""
    z = tuple(z)
    if z[0]*z[1] < 0:
        return tuple(p)
    if min(z[:2]) < 0:
        z = tuple(-x for x in z)
    if not any(z[:2]):
        return tuple(p)
    k = min((p[i]-1)//z[i] for i in (0, 1) if z[i] > 0)
    return tuple(p[i]-k*z[i] for i in range(3))


def reduce_face(p0, ds, p, theta):
    """Input includes an actual p in p0+span_Z(ds), p=(a,b,0)>0.
    The proof ensures the output is in that coset; checks below also verify
    each explicit shift in the selected sublattice without Smith forms.
    """
    bs = rank_basis(ds)
    k = len(bs)
    if k == 0:
        out = tuple(p)
        assert out == tuple(p0)
    elif k == 1:
        u = bs[0]
        out = tuple(p) if u[2] else line_reduce(p, u)
        change = tuple(out[i]-p[i] for i in range(3))
        j = next(i for i in range(3) if u[i])
        assert change[j] % u[j] == 0
        assert change == tuple((change[j]//u[j])*x for x in u)
    elif k == 2:
        u, v = bs
        n = cross(u, v)
        if n[0] == n[1] == 0:
            d = abs(n[2])
            out = ((p[0]-1) % d+1, (p[1]-1) % d+1, 0)
            change = tuple(out[i]-p[i] for i in range(3))
            det = n[2]
            assert (change[0]*v[1]-change[1]*v[0]) % det == 0
            assert (u[0]*change[1]-u[1]*change[0]) % det == 0
        else:
            z = (n[1], -n[0], 0)
            out = line_reduce(p, z)
            change = tuple(out[i]-p[i] for i in range(3))
            j = next(i for i in (0, 1) if z[i])
            assert change[j] % z[j] == 0
            assert change == tuple((change[j]//z[j])*x for x in z)
        assert dot(n, out) == dot(n, p0)
    else:
        u, v, w = bs
        d = abs(dot(cross(u, v), w))
        out = ((p[0]-1) % d+1, (p[1]-1) % d+1, 0)
        change = tuple(out[i]-p[i] for i in range(3))
        assert dot(change, cross(v, w)) % d == 0
        assert dot(u, cross(change, w)) % d == 0
        assert dot(u, cross(v, change)) % d == 0
    assert out[0] >= 1 and out[1] >= 1 and out[2] == 0
    assert sum(out) <= 12*theta**3, (p0, ds, p, out, theta)
    return out, k


def lattice_checks():
    rng = Random(20261107)
    counts = [0]*4
    # Exhaustive rank-one boxes: theta=1,2; p0 L1<=theta; coefficients -12..12.
    for t in (1, 2):
        for p0 in product(range(t+1), repeat=3):
            if sum(p0) > t:
                continue
            for u in product(range(-t, t+1), repeat=3):
                for z in range(-12, 13):
                    p = tuple(p0[i]+z*u[i] for i in range(3))
                    if p[0] > 0 and p[1] > 0 and p[2] == 0:
                        _, k = reduce_face(p0, [u], p, t)
                        counts[k] += 1
    # Deterministic random higher-rank inputs; only witnessed feasible faces tested.
    for trial in range(120000):
        t = rng.randint(1, 12)
        p0 = [rng.randint(0, t), 0, 0]
        p0[1] = rng.randint(0, t-p0[0])
        p0[2] = rng.randint(0, t-p0[0]-p0[1])
        ds = [tuple(rng.randint(-t, t) for _ in range(3))
              for _ in range(rng.randint(1, 4))]
        if trial % 3 == 0:
            ds = [(u[0], u[1], 0) for u in ds]
            p0[2] = 0
        coeff = [rng.randint(-50, 50) for _ in ds]
        p = tuple(p0[i]+sum(z*u[i] for z, u in zip(coeff, ds))
                  for i in range(3))
        if p[0] > 0 and p[1] > 0 and p[2] == 0:
            _, k = reduce_face(p0, ds, p, t)
            counts[k] += 1
    # Explicit rank-two tilted planes, both direction-sign cases, large witnesses.
    for t in range(2, 16):
        for u, v, p0, coeff in [
            ((t, 0, 1), (0, t, -1), (1, 1, 0), (10**6, 10**6)),
            ((t, 0, 0), (0, 0, 1), (0, 1, 0), (10**6, 0)),
            ((1, -1, 0), (0, 0, 1), (t, 0, 0), (-1, 0)),
        ]:
            p = tuple(p0[i]+coeff[0]*u[i]+coeff[1]*v[i] for i in range(3))
            _, k = reduce_face(p0, [u, v], p, t)
            counts[k] += 1
    print('LATTICE checked by rank', counts, 'total', sum(counts))


def grammar(m):
    rules = [(k, (i, j), '') for k in range(-m, m+1)
             for i in range(-m, m+1) for j in range(-m, m+1) if i+j == k]
    rules += [(1, (), 'a'), (-1, (), 'b'), (m, (), 'c')]
    return rules


def metrics(m):
    rules = grammar(m)
    inf = 10**9
    dist = {i: inf for i in range(-m, m+1)}
    while True:
        changed = False
        for k, children, term in rules:
            cost = len(term)+sum(dist[i] for i in children)
            if cost < dist[k]:
                dist[k], changed = cost, True
        if not changed:
            break
    outside = {i: inf for i in dist}
    outside[m] = 0
    while True:
        changed = False
        for k, children, term in rules:
            for at, child in enumerate(children):
                cost = outside[k]+len(term)+sum(dist[x] for j, x in enumerate(children) if j != at)
                if cost < outside[child]:
                    outside[child], changed = cost, True
        if not changed:
            break
    assert all(dist[i] < inf and outside[i] < inf for i in dist)
    theta = max(outside[k]+len(term)+sum(dist[i] for i in children)
                for k, children, term in rules)
    size = 2*m+1+sum(1+len(ch)+len(term)+len(ch) for k, ch, term in rules)
    assert theta <= 3*m+1
    return size, theta


def parses(word, m):
    n = len(word)
    chart = {}
    weights = {'a': 1, 'b': -1, 'c': m}
    for i, letter in enumerate(word):
        chart[i, i+1] = {weights[letter]}
    for length in range(2, n+1):
        for i in range(n-length+1):
            j = i+length
            chart[i, j] = {x+y for k in range(i+1, j)
                           for x in chart[i, k] for y in chart[k, j]
                           if -m <= x+y <= m}
    return m in chart[0, n]


def cfg_checks():
    count = 0
    for m in range(2, 7):
        for n in range(1, 8):
            for w in map(''.join, product('abc', repeat=n)):
                expected = w.count('a')-w.count('b')+m*w.count('c') == m
                assert parses(w, m) == expected, (m, w)
                count += 1
        size, theta = metrics(m)
        print('CFG m', m, 'v', 2*m+1, 'size', size, 'theta', theta, 'mu_ab', m+2)
    print('CFG recognition words checked', count)


def growing_antichain_checks():
    for k in range(6, 13):
        m = k*k-1
        inf = 10**9
        dist = [inf]*m
        heap = []
        for state, cost in ((1, 2), ((-k) % m, 1)):
            dist[state] = min(dist[state], cost)
            heappush(heap, (cost, state))
        while heap:
            cost, state = heappop(heap)
            if cost != dist[state]:
                continue
            for step, extra in ((1, 2), (-k, 1)):
                nxt = (state+step) % m
                if cost+extra < dist[nxt]:
                    dist[nxt] = cost+extra
                    heappush(heap, (dist[nxt], nxt))
        outside = [0 if g == 0 else dist[(-g) % m] for g in range(m)]
        theta = max(outside[(i+j) % m]+dist[i]+dist[j]
                    for i in range(m) for j in range(m))
        theta = max(theta, outside[1]+2, outside[(-k) % m]+1)
        h = 5*k
        assert h < m and 2*h > theta and theta <= 9*k
        assert dist[h] <= theta  # all short alternatives contain c
        print('ANTICHAIN k', k, 'M', m, 'theta', theta,
              'mu_ab', 2*m, 'proved width >=', m//h)


def occurrences(w, d):
    n = len(w)
    for i in range(n):
        for j in range(i+1, n+1):
            if d == 1:
                yield (w[:i], w[j:]), (w[i:j],)
            else:
                for k in range(j+1, n):
                    for ell in range(k+1, n+1):
                        yield (w[:i], w[j:k], w[ell:]), (w[i:j], w[k:ell])


def fill(e, x):
    return ''.join(e[i]+x[i] for i in range(len(x)))+e[-1]


def path_predicate(w, m):
    state, balance = 0, 0
    for c in w:
        if c == 'a' and state == 0:
            state, balance = 1, balance+1
        elif c == 'b' and state == 1:
            state = 0
        elif c == 'c' and state == 0:
            balance -= 1
        else:
            return False
    return bool(w) and state == 0 and balance % m == 0


def sub_checks(name, pred, cap=6):
    # Premises are bounded; conclusions use the EXACT infinite-language predicate.
    # Absence of violations is not used as a membership proof.
    words = {w for n in range(1, cap+1)
             for w in map(''.join, product('abc', repeat=n)) if pred(w)}
    totals = []
    for d in (1, 2):
        by_e = defaultdict(set)
        by_x = defaultdict(set)
        for w in words:
            for e, x in occurrences(w, d):
                sig = tuple(frozenset(t) for t in x)
                by_e[e, sig].add(x)
                by_x[x].add(e)
        ncheck = 0
        for (e, sig), xs in by_e.items():
            for x in xs:
                for y in xs:
                    for f in by_x[x]:
                        out = fill(f, y)
                        assert pred(out), (name, d, e, x, y, f, out)
                        ncheck += 1
        totals.append(ncheck)
    print('SUB', name, 'premise length <=', cap, 'accepted seeds', len(words), 'checks', totals)


def main():
    lattice_checks()
    cfg_checks()
    growing_antichain_checks()
    for m in (2, 3, 4):
        sub_checks('integer-fibre-'+str(m),
                   lambda w, m=m: w.count('a')-w.count('b')+m*w.count('c') == m)
        sub_checks('edge-path-mod-'+str(m), lambda w, m=m: path_predicate(w, m), 8)
    sub_checks('support-dependent-parity',
               lambda w: len(w) % 2 == (1 if set(w) == {'a', 'b'} else 0))
    print('ALL CHECKS PASSED. Finite tests do not establish C1/C2 membership.')


if __name__ == '__main__':
    main()
```

## 10. 最終結果表

| 結果 | 判定 | 分類・限界 |
|---|---|---|
| 経路＋単一可換群剰余類＋内容マスクで `μ_ab≤12θ³` | [証明済み] | (B)。任意のgood MCFG表示、群の大きさや係数に独立 |
| 同じ部分クラスで `q≤⌊12θ³/(θ+1)⌋≤12θ²` | [証明済み] | (B)。最短Wの重い反鎖の長さ計数による |
| この設計では小厚さ・超多項式μ_abを両立できない | [証明済み] | (C)の設計障壁。ただし上の定理の系であり独立成果ではない |
| 全arityの内容型付き代入可能性 | [証明済み] | 既知の経路補題と可換群消去。所属検査のため完全証明を記載 |
| 非正則な無限族(9)、順序依存の無限族(13)、重反鎖が増大する族(17) | [証明済み] | 適用検査を通過。c個数・連数・K_cは非有界 |
| 仮定(1)は多項式結論と同値でない | [証明済み] | (15)がC₁・C₂内の反証、μ_ab=3 |
| 格子・CFG・SUBの有限検査 | [計算機による観察（§9の範囲）] | 一般証明の代用ではない |
| 一般のq上界、反例族、全型付きτへの拡張 | [予想／未解決] | 本報告では成立・不成立のいずれも結論しない |

## 11. 残った穴を一つの命題に限定する

### 命題H：内容ごとに受理剰余類を変える拡張 [予想／未証明]

一文字一辺のグラフD、可換群A、準同型φ、共通部分群Hを固定し、許す各内容 `M∈𝓜` に**別々の**受理剰余類 `g_M+H` を指定する。

\[
 L=\{w\in Path_D(s,t)\cap\Sigma^+:
      \operatorname{cont}(w)\in\mathcal M,
      \varphi(w)\in g_{\operatorname{cont}(w)}+H\}. \tag{16}
\]

固定ランクrに対し多項式P_rが存在し、この形のLの任意のreduced good fan-out≤2表示Gでab型が実現されるなら

\[
 \mu_{ab}(L)\le P_r(|V|,\bar\theta_G)
\]

となるか。

**なぜ空でないか [証明済み]。** (1)は全g_Mを同じにした特例なので、§7の二無限族を含む。さらに(15)は(16)の形だが、命題8.1により(1)には入らない。従って本報告で解いたクラスからの真の拡張である。

**所属の障害はない [証明済み]。** 共通文脈Eでの完成内容はx,yで同じなので、群値の差分はHに入る。別文脈Fでも完成内容はx,yで同じで、Hによる差分はその内容に指定された剰余類を保つ。経路部分は補題3.1で保たれる。従って(16)は全arityで内容型付き代入可能であり、MCFG表示があれば対象クラスに入る。

**どこで現在の証明が止まるか。** 補題4.1の短い二成功語p,p′は、内容が異なる可能性がある。(16)ではその群値差がHに入るとは限らない。そのため、全規則の小さいδを一つの格子にまとめても、その格子移動がabの受理剰余類を保つ保証がない。これが一つの明確な未証明点である。

**なぜ一般問題の言い換えではないか [証明済み]。** (16)は経路と、同じφ・Hに対する高々7つの内容別剰余類という構造条件を課す。一般のC₂言語より狭いことは、単一語言語 `K={abba}` でも分かる。Kはgood CFG `S→abba` を持つ。arity1では共通文脈に対する穴の値が一意なので代入可能。arity2では内部固定部が1文字以上あり、穴長の総和は3以下である。総和2なら穴長は(1,1)に固定され、同じ文脈からの値は一意。総和3で異なる分割があるとすれば(1,2)と(2,1)。成分内容一致のため穴は `(d,ee)` と `(dd,e)` の形でなくてはならない。外側は空、内部固定文字をzとすると、同じ完成語であることから `dzee=ddze`。第2・第3文字の比較でz=d=eとなり、完成語が一文字の4乗になってしまう。abbaでは不可能。従ってKはarity2でも代入可能で、`K∈C_{1,c}∩C_{2,c}`。

一方、abbaを読める一文字一辺のグラフでは、連続bbからbがループ、その前後のaからaも同じ頂点のループになる。従ってaabbも同じs→t経路を与える。abbaとaabbは内容とParikhベクトルが等しいから、どんな可換群・内容別受理剰余類でも区別できない。従ってKを(16)で表すことはできない。これで命題Hは一般問題の単なる再表現でないことを、所属の計算機判定に頼らず示した。

また、(16)を仮定するかどうかは短いab語の存在そのものを述べておらず、短枠Bridgeを仮定する帰着とも異なる。命題Hが解けても一般の `op:fanout-two` が解けたとは言えない。

## 12. 次に試すこと（3件）

1. **型の異なる短証人の差分を分離する。** 補題4.1のδ_Rに、二成功語の内容対を付ける。高々49種類の内容対を持つ有限グラフ上の閉路和がHに入ることを利用し、ab剰余類を保つ小さい生成元を得られるか調べる。閉路を実際の文法導出に対応させる段階は未証明。
2. **(16)の三文字例を先に調べる。** 型ごとのg_Mを小さい有限可換群で変え、全arity所属を一般証明で固定したまま、最小の表示厚さとμ_abの差を探す。有限検査では文法と言語の一致を別途確かめる。
3. **一般の立方体に戻るときは、規則厚さの証人も種に含める。** 立方体だけでなく§4の全規則由来の短い二語を追加し、そのSUB閉包でどの整数格子移動が実際の文字列置換として実現されるかを検査する。単なるParikh一致から所属へ飛躍しない。

以上の定理1.2・系1.3は限定クラスの結果であり、一般のq上界や `op:fanout-two` の解決を主張するものではない。
