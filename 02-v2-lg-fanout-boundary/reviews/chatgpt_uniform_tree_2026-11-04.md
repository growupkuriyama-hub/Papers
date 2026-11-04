# 一様な最小導出と両文字型ラベルの出現数：三文字内容型付け・第九報

**研究日**：2026-11-04　**対象**：栗山貴之論文 #2、`op:fanout-two`  
**正本**：[`02-v2-lg-fanout-boundary/main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、Git blob SHA `b72cd2ed648f802886f0ab7c60a72f9f40c0864b`。添付ZIPの `main.tex` とGitHub取得結果はバイト数・内容長が一致し、GitHubで上記SHAを確認した。先行の `chatgpt_spectrum_m_2026-11-03.md`、`chatgpt_bc_escapes_2026-11-03.md`、`chatgpt_escape_branches_2026-11-03.md` を併読した。  
**重要**：以下の数学的証明は、出典を引用するだけでなく必要な内容を再構成する。結果は原稿未採用の研究ノートであり、独立査読を経ていない。

## 0. 主張別の判定

| 主張 | 判定 | 根拠・射程 |
|---|---|---|
| (U) 節点数最小の `a^k` 導出を、各ラベルの部分木が全て同じ導出木である形へ取り直せる | **証明済み** | §2、定理2.3 |
| 同名ラベルの総生成長および部分木の節点数はそれぞれ一定 | **証明済み** | §2.1–2.2 |
| 同名ラベルのファンアウト2の**成分別**生成長も一定 | **反証** | §3、3節点の具体例 |
| 元の最小導出に現れるラベル間の子依存グラフも非巡回 | **証明済み** | §2.2（節点数による厳密減少） |
| `a` だけの二成分組について、同じ総長の全分割は分布同値、異なる総長の分布は交わらない | **証明済み** | §4、補題4.1 |
| 一様DAGの `B` 出現数を依存グラフ上の `B` 分岐深さで `N_B≤r^{D_B}` と抑える | **証明済み** | §5、命題5.1（構文的・条件付き） |
| 交差置換による `b,c` 個数の一致に必要な整数核、損失の線形価格条件 | **証明済み** | §6、命題6.1–6.2 |
| `aa` の存在と、`b,c` 個数が等しく `a` 個数が違う二語から、全内容のParikh飽和を強制できる | **反証** | §7、`L_k={a^k,abc,acab}`、全 `k≥5` |
| 上記 `L_k` が arity 1 と 2 の内容代入可能性を満たす | **証明済み** | §7の全場合証明；§10の小例の厳密全数検査は補助 |
| 先行の補題D、清浄な倍増節点に関する補題4.1の必要部分 | **再証明済み** | §8（ただし一般の `N_B` 上界を与えない） |
| 一ラベルの両文字型 `B` の `N_B≤poly(v,θ)`、その fan-out=1、祖先一色型を含む場合 | **未解決** | §9.1 |
| 条件をすべて満たす `G_n` による超多項式の `μ_a(L_n)` | **未解決** | §9.2；既報のnear-missはarity 1で失敗 |
| 新しい命題が文献上既知ではない | **未確認** | §11 |

**今回の主成果は (U) の完全な肯定証明**である。依存関係が非巡回であることは、一様化した後だけでなく、**元の最小導出の段階ですでに成り立つ**。一方、そのDAGは長さ指数的な純粋 `a` 語を容易に展開できる。文法の短い逃げ道と内容代入可能性からDAGの分岐を制限する最後の論証は未完成である。

## 1. 設定と原稿の定義の再確認

アルファベットを `Σ={a,b,c}` とし、非空語の内容型付けを `c(w)={x∈Σ:x が w に出現する}` とする。`L∈𝒞_{2,c}` は fan-out `≤2` のMCFLで、**arity 1 と 2 の双方**について、成分ごとの内容が等しい非空組 `x,y` が一つの許容受理文脈を共有すれば、両者の受理文脈集合が一致するものとする。arity 2の文脈 `u□₁v□₂z` では **`v≠ε`** が必須である。

`G=(V,Σ,P,S,fan)` は `L∩Σ⁺` の reduced good 表示、`fan≤2`、規則ランク `≤r`、`r≥2` は固定、`v=|V|`、`g=||G||`、`θ=θ̄_G≥1`。good は λ-free、nondeleting、nonpermuting、nonmerging を同時に意味する。各導出組の成分は非空である。`k=μ_a(L)=min{j≥1:a^j∈L}≥5` とし、`T` を **`a^k` を出す導出のうち節点数が最小**のものとする。節点 `u` の生成組の総長を `ℓ(u)`、その節点を根とする導出木の節点数を `s(u)` とする。`ℓ(u)>θ` を重いと呼ぶ。

### 1.1 厚さの使い方

原稿 `lem:thickness-equivalence` の必要部分を次のように確認する。ある規則 `R` を含む最短の成功導出は長さ `≤θ` の語を出す。nondeleting なので、`R` が直接出力する終端はこの語に全て残る。よって一規則の終端書込み数は `≤θ`。reduced なので各ラベル `X` は成功導出に現れる。その成功導出内の `X` 部分木は根語の部分位置を占めるため、長さ `≤θ` の生成組 `ρ_X∈L_X(G)` を選べる。good の nonmerging と各成分非空から、ファンアウト2の部分木を抜いた文脈は穴間に非空の固定語を持つ。この確認に型付き文法への置換は要らない。

任意の部分木の総長は、そこにある直書き終端数と子部分木の**総長**の和である。これは非削除性による。**各成分の長さが親子で単純に足し合わされるとは限らない**ので、§2.4では成分ごとの変数配置も別記する。

## 2. (U)：一様な最小導出の構成的証明

### 2.1 補題：同名ラベルの総長は等しい

**補題2.1。** `T` に現れる同名ラベル `X` の任意の二出現 `u,u'` に対し `ℓ(u)=ℓ(u')`。

**証明。** 両部分木の出力は全成分が `a` だけの組である。もし `ℓ(u)>ℓ(u')` なら、`u` の部分導出を `u'` の部分導出に差し替えられる。ラベルとファンアウトは同じなので、外側の規則はそのまま合法であり、nondeleting により根の出力は `a^{k−ℓ(u)+ℓ(u')}` となる。指数は正で `k` より小さい。`k=μ_a(L)` に矛盾。逆の場合も対称。従って共通の総長 `ℓ_X` が存在する。□

**付記。** `T` に現れる `X` について、`ℓ_X` は `X` が生成可能な**純粋 `a` 組の最小総長**でもある。もしより短い純粋組があれば、`X` の一出現をそれへ差し替えれば同じ矛盾が生じる。ただし長い純粋組の存在までは排除しない。

### 2.2 補題：同名ラベルの節点数は等しい

**補題2.2。** `T` に現れる同名ラベル `X` の任意の二出現 `u,u'` に対し `s(u)=s(u')`。また、元の `T` に現れる親子ラベルの有向グラフは非巡回である。

**証明。** 補題2.1により総長は等しい。もし `s(u)>s(u')` なら `u` を `u'` の導出に差し替えても根語は `a^k` のままだが、節点数は減る。`T` の選択に矛盾する。ゆえに各ラベル `X` に共通節点数 `s_X` がある。さらに `X` の節点が `Y` の節点を直接の子として持つなら、**真の部分木**なので `s_X>s_Y`。従って同じラベルが根葉経路で再出現することはないし、もっと強く、元の `T` の**全出現を合わせて作った**ラベル間依存グラフの各辺で正整数 `s_X` が厳密に減る。向き付き閉路は存在しない。□

ここでは別々の枝で `X→Y` と `Y→X` が現れる可能性さえ排除された。単なる「一経路でラベルを繰り返さない」より強い。

### 2.3 定理：各ラベルにただ一つの導出部分木を選べる

**定理2.3（一様化）。** `a^k` の節点数最小の成功導出 `T` から、根語と節点数を変えずに、同じラベルの全出現が**同一の規則・同一の子部分木を持つ**成功導出 `T^{unif}` を構成できる。`T^{unif}` はラベル数 `≤v` の非巡回DAGを展開した導出木である。

**証明。** 元の `T` に現れる各ラベル `X` に対し、`X` の出現を一つ固定し、その出現で用いられた規則 `R_X` を記録する。補題2.2により、この規則の子ラベル `Y` は全て `s_Y<s_X` を満たす。

各 `X` の標準部分木 `t_X` を `s_X` の昇順に定義する。`R_X` がランク0なら、その規則単独を `t_X` とする。ランク正なら、`R_X` の各子スロット `Y` に、既に構成した `t_Y` の**コピー**を入れる。非巡回なので構成は停止し、同じラベルの子には常に同一の `t_Y` を入れられる。

帰納的に、`t_Y` の出力は純粋 `a` の非空組で総長 `ℓ_Y`、節点数 `s_Y` と仮定する。`R_X` の元の出現で使われていた全ての子も、補題2.1–2.2によってそれぞれ同じ `ℓ_Y,s_Y` を持つ。`R_X` は線形・非削除だから、子の**成分別長さが変わっても**、親が出す終端総数と子の総長和は同じである。親の生成組の各成分は good 性によって非空で、全て `a` だけである。節点数も `1+Σ_{子スロット}s_Y=s_X`。よって `t_X` の総長は `ℓ_X`、節点数は `s_X` である。

根の `t_S` はしたがって `a^{ℓ_S}=a^k` を出し、節点数 `s_S=|T|`。それを `T^{unif}` とすれば、ラベルごとに一意の規則・部分木を持つ。`s_X` が辺に沿って減る依存グラフをDAGとして共有化すると、頂点数は元の `T` に現れたラベル数以下、従って `≤v` である。□

**注意**：この構成は各ラベルの**出現数** `N_X` や各非終端の**成分別**生成長を元の `T` から保存するとは主張しない。保存するのは `a^k`、総節点数、各採用ラベルの総長と局所節点数である。以降は一様化後の `T` を改めて `T` とする。

### 2.4 DAGの厳密な計数式

`T` に現れるラベル `X` の採用規則 `R_X` の直接書込み数を `c_X≤θ`、子スロットのうちラベル `Y` を持つものの重複度を `m_{X,Y}` とする。このとき

\[
\ell_X=c_X+\sum_Y m_{X,Y}\ell_Y,\qquad
s_X=1+\sum_Y m_{X,Y}s_Y,\qquad
N_X=\mathbf1_{X=S}+\sum_P N_Pm_{P,X}.
\tag{2.1}
\]

最後の式は `N_S=1` を含む形で書いた。右辺はトポロジカル順序で計算され、ラベルが複数回右辺に現れれば重複して数える。`ℓ_S=k`。

fan-out2の成分別には、規則 `R_X=(α_{X,1},…,α_{X,d_X})` とし、`m_{X,i;Y,j}` を**ラベル `Y` を持つ子スロットの第 `j` 成分が親の第 `i` 成分に配置される回数**とする（スロットの重複を数える）。`c_{X,i}` を `α_{X,i}` の終端数とすると

\[
\ell_{X,i}=c_{X,i}+\sum_{Y,j}m_{X,i;Y,j}\ell_{Y,j},
\qquad \ell_X=\sum_{i=1}^{d_X}\ell_{X,i}.
\tag{2.2}
\]

`m_{X,i;Y,j}` は非負整数で、非削除性により各子スロット成分は親のどれか一成分に**ちょうど一度**現れる。`Σ_i c_{X,i}=c_X`、`Σ_i m_{X,i;Y,j}` はその子スロットの本数である。これが総長式 (2.1) を保証する。**原稿の MCFG は文字列の直線的プログラムというより、非巡回なタプル直線プログラムである**。全ての採用規則が一つずつ、という意味でSLP類似であり、CFGの通常の文字列SLPに同一視してはいけない。

## 3. ファンアウト2の成分長一致は不要・実際に偽

次のgood MCFGを考える。`fan(S)=1`、`fan(B)=2`、ランク上限2。

```text
S -> (x_1^1 a x_1^2 x_2^1 a x_2^2)(B,B)
B -> (a,aa)
B -> (aa,a)
```

`S` の二つの `B` 子スロットの間は異なる子の変数が隣接するが、同じ子の二成分 `x_j^1,x_j^2` の間には明示 `a` があるので nonmerging。全成分非空、全変数一回、順序保存でgood。両ラベルが到達可能・生産的なのでreduced。四つの規則選択のいずれでも生成語は `a^8` だけであり、成功導出は必ず `S` と二つの `B` の**3節点**からなる。従って全て節点数最小である。

左の `B` を `(a,aa)`、右の `B` を `(aa,a)` とすれば、**同名の部分木が両方とも総長3・節点数1でありながら、成分長は `(1,2)` と `(2,1)` で違う**。その一方、右も `(a,aa)` に取り直せば一様化できる。

この例は `L={a^8}∈𝒞_{2,c}` でもある。実際、arity 1では共有する受理文脈があれば同じ純粋 `a` 長、arity 2では非空セパレータ付きで共有する文脈があれば両成分の長さの和が一致し、その分布は総長だけで決まる（次節）。

## 4. 純粋 `a` 組の分布は「総長」で完全に層別化される

**補題4.1（pure-`a` fiber）**。`L∈𝒞_{2,c}`、`μ_a(L)=k≥5` とする。

1. arity 1では `a^t`（`1≤t≤k`）の分布は、相異なる `t` どうしで**交わらない**。
2. arity 2では `2≤t≤k−1` の各 `p=1,…,t−1` に対し
   `x_{t,p}=(a^p,a^{t−p})` と置くと、**同じ `t` の全ての `x_{t,p}` は分布同値**である。
3. arity 2で `2≤t<t'≤k−1` なら、任意の `p,p'` について `D_L^{(2)}(x_{t,p})` と `D_L^{(2)}(x_{t',p'})` は**交わらない**。

**証明。** (2) `E_t=□₁a^{k−t}□₂` は `k−t≥1` により許容され、どの `x_{t,p}` を入れても `a^k∈L`。成分型は共に `({a},{a})` なので代入可能性から分布は全て等しい。

(3) 異なる総長 `t<t'` の組がある許容文脈を共有すると、同じ成分型であるため分布が一致する。しかし `E_{t'}` は `x_{t',p'}` を受理するから `x_{t,p}` も受理する。すると `a^{k−(t'−t)}∈L` となり、指数は正で `k` より小さい。矛盾。(1) も同じ議論で、一穴文脈 `a^{k−t'}□` を使えばよい。□

**系4.2。** 節点数最小の `a^k` 導出中の fan-out2ラベル `B` について `2≤ℓ_B≤k−1`。上限は穴間の非空固定語のためである。従って、同じラベルの純粋 `a` 生成組は、成分長が違っても **`L` の受理分布上は同値**である。ただし、同値な組が全て文法 `G` の `B` から導出可能だとは限らない。この区別が重要である。

## 5. 一様DAGからの `B` 出現数と分岐深さ

`B` を一様導出 `T` に現れるラベルとする。各DAG頂点 `X` について、標準部分木 `t_X` に現れる `B` ラベルの節点数を `t_{X,B}` とする。`B` は自身の真下に現れないので `t_{B,B}=1`。`X≠B` では

\[
t_{X,B}=\sum_Y m_{X,Y}\,t_{Y,B},\qquad q_B=N_B=t_{S,B}.
\tag{5.1}
\]

これは非巡回グラフ上で厳密に計算できる。**同名ラベルの全出現の下に含まれる `B` の個数も常に同一**となり、ユーザーの (X) にある `P` 一出現中の `t` は実際にラベルのみの関数 `t_{P,B}` となる。

**命題5.1（`B`-分岐深さ）。** `X` の子スロットで `B` の子孫を持つものを **`B`-有効な子** と呼ぶ。`X→B` の経路上で `B`-有効な子が少なくとも二つある頂点の最大個数を `D_B(X)` とする。`r≥2` なら

\[
 t_{X,B}\le r^{D_B(X)}\quad(t_{X,B}>0),\qquad
 q_B\le r^{D_B(S)}.
\tag{5.2}
\]

**証明。** `X=B` では1=\(r^0\)。`X≠B` の有効な子が一つなら (5.1) はその子の `t` をそのまま引き継ぎ、深さは増えない。二つ以上なら最大 `r` 個の子の和で、`t_{X,B}≤r max_Y t_{Y,B}`。そこで分岐深さが1増える。非巡回順の帰納法で式 (5.2)。□

**系5.2。** ランク `r` 固定で `q_B=(v+θ)^{\omega(1)}` なら、どの一様 `T` も `D_B(S)=\omega(\log(v+θ))` を持つ。逆に `D_B(S)≤C\log_r(v+θ+2)` のような**追加仮定**があれば `q_B≤(v+θ+2)^C`。これは条件付きの純構文的な多項式上界であり、内容代入可能性からその追加仮定を導けたわけではない。

さらに `B` が重いなら、`B`-分岐頂点 `X` は少なくとも二つの子にそれぞれ長さ `≥ℓ_B>θ` の `B` 部分木を持つ。よって `X` は**重い倍増節点**である。したがって本問題の巨大な `q_B` は、同じ `B` を共有するDAG内の**多数の重い倍増**を必要とする。

## 6. 交差 (X) の算術的障害と有限の「価格」

### 6.1 平坦置換の厳密な加法式

重いラベル `X` に総長 `≤θ` の短い生成組 `ρ_X` を固定し、`p_X=|ρ_X|_a`、`β_X=|ρ_X|_b`、`γ_X=|ρ_X|_c`、`d_X=ℓ_X−p_X>0` とする。同じラベルの総長は一様化の前から一定である。`T` の任意の**反鎖** `J` に含まれる各節点をそのラベルの `ρ_X` に置き換える（先頭の `a` を保護できるときはそれを残す）。`n_X(J)` をラベル別選択数とすれば、生成語 `W_J∈L` に対し

\[
 \bigl(|W_J|_a,|W_J|_b,|W_J|_c\bigr)
 =\Bigl(k-\sum_X n_X(J)d_X,\ 
          \sum_X n_X(J)\beta_X,\ 
          \sum_X n_X(J)\gamma_X\Bigr).
\tag{6.1}
\]

異なる反鎖 `J,J'` の差 `z_X=n_X(J)−n_X(J')` に対し、`b,c` のParikh数が一致する必要十分条件は

\[
 \sum_X z_X\beta_X=0,\qquad\sum_X z_X\gamma_X=0.
\tag{6.2}
\]

そのときの `a` 個数差は `−Σ_X z_Xd_X` である。これは**整数核**の問題だが、核の解が実際の反鎖選択として実現できるとは限らない。

### 6.2 命題：Parikh衝突を生まない線形価格条件

**命題6.1。** 平坦置換に使用するラベル群 `H` に対し、実数 `λ_b,λ_c` が存在して

\[
 d_X=\lambda_b\beta_X+\lambda_c\gamma_X\qquad (X\in H)
\tag{6.3}
\]

を満たすなら、`H` のラベルだけを使ったどんな二つの反鎖置換も、`b,c` 個数が同じであれば `a` 個数も同じである。

**証明。** 式 (6.2) に (6.3) を掛けて足すと `Σ_Xz_Xd_X=0`。式 (6.1) から結論。□

**重要な二ラベル帰結**：混合型 `B` が `(β_B,γ_B)`（両方正）、一色型 `C` が `(β_C,0)`（`β_C>0`）なら二つのベクトルは一次独立である。式 (6.2) の解は `z_B=z_C=0` のみ。従って **`B` と `b`-only `C` の二種類だけを交差させても、`a` の個数が異なる同一 `b,c` Parikhの二語は作れない**。`c`-onlyとの二種類も同様。`b`-onlyが複数ラベルあっても全て同じ損失比 `d_X/β_X=λ_b` を持つなら、混合型 `B` と合わせて (6.3) を満たし、この方法では衝突しない。これは一色型の共通損失比が得られる既報の飽和側解析と整合する。

### 6.3 三ラベルでの「価格欠損」

一つの両文字型 `B`、一つの `b`-only `C`、一つの `c`-only `D` があり、その短い代表の非 `a` 個数が

\[
 (\beta_B,\gamma_B),\quad (\beta_C,0),\quad (0,\gamma_D),
\qquad\beta_B,\gamma_B,\beta_C,\gamma_D>0
\]

であるとする。正整数

\[
 m=\beta_C\gamma_D,\quad
 h_C=\gamma_D\beta_B,\quad
 h_D=\beta_C\gamma_B
\tag{6.4}
\]

は全て `≤θ²` で、

\[
 m(\beta_B,\gamma_B)
 =h_C(\beta_C,0)+h_D(0,\gamma_D).
\tag{6.5}
\]

**命題6.2（算術的交差証明書）。** 保護する `a` の外側で、`m` 個の `B` 出現を選べる反鎖と、`h_C` 個の `C` および `h_D` 個の `D` を**互いにも比較不能に**選べる別の反鎖があると仮定する。それぞれの置換後に残る `a` 数が `1,…,k−1` に入るとする。この二つの受理語は同一の `b,c` 個数を持ち、その `a` 個数の差は符号を別にして

\[
 \Delta=m d_B-h_Cd_C-h_Dd_D
 =\beta_C\gamma_D
 \left(d_B-\frac{d_C}{\beta_C}\beta_B
            -\frac{d_D}{\gamma_D}\gamma_B\right).
\tag{6.6}
\]

**証明。** 反鎖置換の合法性から二語とも受理される。式 (6.1)、(6.4) を代入すれば (6.5) と (6.6)。□

括弧の中を **`B` の価格欠損** と呼んでよい。これが非零なら**算術的には** `a` 個数差が生じる。しかし二語の **`a`-骨格の一致は式 (6.5) から導けない**。それが一致する場合に限り、§8.1で再証明する定理Sから矛盾となる。反鎖の選択可能性・骨格整列・非空セパレータを同時に満たすことは、なお研究の核心である。

**祖先 `P` との比較**についても、`P` 自身への一回の短縮と、その下の `t_{P,B}` 個の `B` への平坦置換を比較して、非 `a` 個数が一致する条件は `(β_P,γ_P)=t_{P,B}(β_B,γ_B)` である。そこから `d_P=t_{P,B}d_B` は一般には出ないし、骨格一致も出ない。`P` と `B` を同じ反鎖で置き換えられると誤認してはならない。

## 7. 三文字の全内容に対する安易な飽和二分法は成立しない

**命題7.1（全 `k≥5` の厳密な反例）。**

\[
 L_k:=\{a^k,\ abc,\ acab\}\subseteq\{a,b,c\}^+.
\tag{7.1}
\]

とする。このとき `μ_a(L_k)=k`、`aa` は `L_k` の受理語の因子であり、`abc,acab` は `b,c` の個数がそれぞれ `(1,1)` で等しいが `a` の個数は1と2で違う。それでも **`L_k∈𝒞_{2,c}`** であり、Parikh-saturatedではない。

**証明。** 有限言語なのでCFG、従って fan-out≤2 MCFLである。`S→a^k | abc | acab` の3つのランク0規則による一ラベル文法は reduced goodであり、`||G||=k+11`、`θ=k`。`μ_a=k` は直接明らか。`abc∈L_k` だが `acb∉L_k` なのでParikh非飽和。

**arity 1**：一つの文脈 `u□v` に同じ内容の二つの語 `x,y` を埋めて両方受理されるとする。完成語の一方が `a^k` なら、`u,v,x` は全て `a` だけで、`y` も同じ内容 `{a}` だから、他方も `a^k`。固定 `u,v` から `x=y`。完成語が双方とも同じ混合語なら、同じ理由で `x=y`。完成語が `abc` と `acab` の別々の場合、共通する語頭は `a` のみ、語末には非空の共通接尾辞がない。従って共通文脈は `□`、または `a□` のみ。`□` では `x=abc,y=acab` で、両者は他のどの受理語の因子でもないので分布は共に `{□}`。`a□` では `x=bc,y=cab` となり、内容が `{b,c}` と `{a,b,c}` で異なる。よってarity 1の条件を満たす。

**arity 2**：一方が `a^k` なら固定部も穴埋めの組も全て純粋 `a` であり、もう一方も `a^k`。同じ総長の純粋 `a` 二成分組の分布一致については、`L_k` に適用した補題4.1(2)から従う（`k−t` は穴間に少なくとも1文字必要なので正）。一方と他方の完成語がともに混合語の場合、`abc` に二つの非空穴を置くと、非空の固定穴間語は**必ず中央の `b`** を含む（長さ3なので実際に `b`）。これに対し `acab` では `b` は末尾にしか現れず、後ろの穴を非空に保つ固定穴間語は `b` を含めない。従って**同一の許容二穴文脈**が `abc` と `acab` の両方を完成させることはない。同じ混合語を二通りに完成させる場合、固定穴間語の出現位置は一意である：`abc` には内部の `b` が一回、`acab` には内部の `c` と `a` が一回ずつで、内部固定語として可能な `c`、`a`、`ca` はそれぞれ一度しか現れない。固定された前後部分も考えれば穴の中身は一意。ゆえにarity 2の条件も成立。□

**帰結と限界**。`aa` と、等しい `b,c` 個数・異なる `a` 個数をもつ二つの**全内容語**の存在から、Parikh飽和や `a^{<k}` の存在は導けない。二文字の影の「飽和／非飽和」を、そのまま三文字に延ばす案はこの形では失敗する。ただしこの有限例の厚さは `θ=k` であり、**小さい厚さの下での `N_B` の多項式上界を反証していない**。

## 8. 先行補題D・補題4.1・定理Sの必要部分の自己点検

### 8.1 定理S（同じ `a` 骨格の異なる総 `a` 数は禁止）

`σ_a(w)` を各極大 `a` ランを1文字に縮めた骨格とする。`a^k∈L`、`k≥5` なので `(a,aa)` と `(aa,a)` は、許容二穴文脈 `□₁a□₂a^{k−4}` を共有してともに `a^k` を完成させる。成分内容が一致し `L∈𝒞_{2,c}` だから、両組の分布は等しい。従って異なる `a` ランの間で、各ランの長さを正に保ちながら一文字ずつ `a` を移す操作は受理性を保存する。

`w,w'∈L` が同じ `a` 骨格を持ち、`0<|w|_a<|w'|_a<k` とする。`δ=|w'|_a−|w|_a`。双方の `a` を第一ランに集め、残る全ての `a` ランを長さ1にできる。その結果、同じ固定一穴文脈 `u□v` に `a` と `a^{1+δ}` を埋めた二語がともに `L` に属する。arity 1により `D_L(a)=D_L(a^{1+δ})`。特に `a^k=a^{k−1−δ}a^{1+δ}` から、後半を `a` に換えると `a^{k−δ}∈L`。`1≤k−δ<k` となって矛盾。従って

\[
 \sigma_a(w)=\sigma_a(w'),\quad
 0<|w|_a,|w'|_a<k
 \quad\Longrightarrow\quad |w|_a=|w'|_a.
\tag{S}
\]

ランが一つしかない場合も同じ一穴議論で済む。異なるランの交換には、必ず非空の非 `a` 区切りがあるため、arity 2文脈の許容条件を満たす。

### 8.2 補題Dの再証明

各根葉経路は、補題2.2により長さ `≤v`。最大総長の子を選ぶ経路を取り、その経路のうち**重い子が二つ以上**ある節点を `D` 個とする。重い子が高々一つなら親長は最大子の長さ `x` と、直書きおよび高々 `r−1` 個の軽い子から `≤x+rθ`（より粗く `≤x+(r+1)θ` でもよい）。重い子が二つ以上なら `≤r x+θ≤r x+rθ`。葉の長さは `≤θ`。最大 `v−1` 段を戻ると、乗数 `r` が現れるのは `D` 箇所だけであり

\[
 k\le[1+r(v−1)]\,θ\,r^D.
\tag{D}
\]

よって `v,θ` が多項式で `r` が固定、`k` が超多項式なら `D=ω(log n)`。これは算術的に正しい。ただし `D` の上界を別途証明しなければ `k` は抑えられない。

### 8.3 清浄な倍増節点の逃げ道符号（既報補題4.1）

`a^k` の先頭2文字・末尾2文字を保護し、それらの位置を所有しない部分木を**清浄**とする。重いラベル `X` の短い代表 `ρ_X=(ρ_{X,1},…,ρ_{X,d})` は、そうでなければ純粋 `a` の短縮で `μ_a` に反するので、`b` または `c` を含む。清浄な重い節点の一つだけを短縮した語は、保護した `a` を残し、`a` の損失 `d_X=ℓ_X−|ρ_X|_a` が `0<d_X<k` である。

その完成語の骨格は、文字の並びとしての

\[
 \kappa(X)=\sigma_a(a\,ρ_{X,1}\,a\cdots a\,ρ_{X,d}\,a)
\]

だけで決まる。ここでは各成分外側と穴間に元の `a` が**一文字以上残る**ことが必要であり、good の nonmerging と清浄性を使う。同じ `κ` を持つ二つの清浄重い節点 `h,u` の単独短縮語は同じ `a` 骨格を持つため、(S) により損失が同じ。従って `|ℓ(h)−ℓ(u)|≤θ`。一方 `h` が二つの重い子を持ち、`u` が `h` の重い真の子孫なら、`u` 以外の重い子が出力する長さ `>θ` のため `ℓ(h)>ℓ(u)+θ`。矛盾。よって**清浄な倍増節点とその清浄重い真の子孫は、同じ逃げ道骨格符号を持てない**。

この自己点検により既報の補題4.1の必要部分は確認できる。**ただし符号 `κ(X)` はラベルごとに最大 `v` 種類を取り得る**ので、これだけでは `D_B=O(log(v+θ))` とならない。一様化しても、異なる祖先ラベルがそれぞれ異なる逃げ道骨格を使い分ける余地は残る。

## 9. 肯定・否定の到達点と止まった場所

### 9.1 肯定側

(U) は完全に証明できた。`B` の出現数は構文的に `q_B=t_{S,B}` と計算でき、さらに `q_B≤r^{D_B(S)}`。そのため **一様DAGの深い `B` 分岐列を禁じることが最後の問題**として抽出される。短い代表による損失 `d_X` と、他ラベルの `b,c` 個数を線形価格にまとめると、交差 (X) における算術的な衝突可能性は式 (6.2)–(6.6) へ縮約される。

しかし、`q_B≤poly(v,θ)` を以下のどれについても示せなかった：一般の両文字型、**両文字型が一ラベルのみ**、そのラベルの **fan-out=1**、そのラベルの全重い祖先が **一色型**。とくに最後の状況で一色型が `b` のみかつ共通損失比を持つなら、命題6.1により**平坦置換のParikh計算だけでは**衝突を作れない。この観察を「したがってその場合は多項式」という主張へ飛躍させてはならない。

前回の定理3.2にある `k≤poly_r(v,θ,N_{bc})` および `h_T` 上界は**研究の背景**として参照したが、今回の新しい定理の証明にはその複雑な飽和側・二段刈込みの推論をブラックボックスとして用いていない。従って本報告の独立した新しい多項式上界は式 (5.2) の**追加の分岐深さ制限付き**のものだけである。

### 9.2 否定側

必要な全条件を満たす族 `G_n` は今回構成できなかった。既報の近接族

```text
start A_n
A_0 -> a | D
A_i -> A_(i-1) A_(i-1) | D   (1 <= i <= n)
D -> bc | bc D
```

は reduced good、fan-out1、rank2、`||G_n||=9n+15`、`θ̄_G=2n+1`、`μ_a(L_n)=2^n` を満たすが、**`L_2∉𝒞_{2,c}`**。正確な所属判定では `bc,bcbc,bcbca∈L_2`、`bca∉L_2`。共通文脈 `E=□` において同じ内容 `{b,c}` の `bc,bcbc` が受理されるが、`F=□a` は `bcbc` を受理し `bc` を拒否する。arity 1 の完全な違反証明書であり、有限探索の推測ではない。`a` の個数が漏れる問題を本質的に回避する設計は得られなかった。

### 9.3 下界の正確な作用素・資源指定

**新しい特徴標本の超多項式下界は証明していない。** 将来もし、**アルファベット `Σ={a,b,c}`、ファンアウト≤2、ランク≤固定 `r≥2`、reduced good `G_n`、`L_n∈𝒞_{2,c}`、`||G_n||,θ̄_{G_n}=poly(n)`、`μ_a(L_n)=n^{ω(1)}`** の族が得られれば、型 `{a}` を消した部分言語 `L'_n=L_n\setminus c^{-1}({a})` も `𝒞_{2,c}` に属する。なぜならそのフィルタは正規言語であり、MCFLは正規言語との交叉で閉じ、固定文脈で成分内容が等しい二組に対して完成語の内容は等しいので、代入可能性が保たれるからである。

`L'_n⊊L_n`。両言語に特徴標本を持つ**集合駆動作用素**について、`L_n` の特徴標本が `{a}` 型を含まないと `L'_n` の特徴標本との和集合で両言語を再構成させる矛盾が生じる。同じ下界は原稿 `prop:rare-type` とそのsoundnessにより、**`\mathcal B^{≤r}_{2,c}` と `\mathcal B_{2,c}`** にも及ぶ。したがって初めて、特徴標本の**総符号長** `≥μ_a(L_n)` が従う。これは**任意のGold学習器**の実行時間・収束段階の下界ではない。現在、その仮定を満たす族は未構成なので**条件文以上の主張はしない**。「最大の特徴標本」という表現も使用しない。

## 10. Python 3 標準ライブラリによる厳密検査

付録コードはWindowsで `py -3 uniform_tree_checks.py` として実行できる。**全文**を下に掲載する。`finite_substitution_certificate` は有限言語の全受理語の全切り出しから、許容 `d` 穴文脈を正確に列挙し、共通受理文脈が存在して分布が異なる組を返す。有限言語に対しては**判定そのものが厳密**であり、無限言語の未検査部分には拡張しない。`near_miss_member` は無限言語に対する正確な所属判定（`D=(bc)^+` と有限分割のメモ化再帰）である。near-missは実際に得た **反例証明書の4語**にこの判定器を適用する。

```python
"""Exact small-instance checks for chatgpt_uniform_tree_2026-11-04.md.
Only Python 3 standard library; on Windows: py -3 uniform_tree_checks.py
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product


def content_tuple(xs):
    return tuple(frozenset(x) for x in xs)


def contexts_of_finite_language(words, arity):
    """All accepting d-hole contexts, exhaustive for the finite language.
    An arity-two context has a nonempty fixed word between its holes.
    Components/holes are required to be nonempty.
    """
    distributions = defaultdict(set)
    for word in words:
        n = len(word)
        if arity == 1:
            for i in range(n):
                for j in range(i + 1, n + 1):
                    xs = (word[i:j],)
                    E = (word[:i], word[j:])
                    distributions[xs].add(E)
        elif arity == 2:
            for i in range(n):
                for j in range(i + 1, n):
                    for p in range(j + 1, n):
                        for q in range(p + 1, n + 1):
                            xs = (word[i:j], word[p:q])
                            E = (word[:i], word[j:p], word[q:])
                            assert E[1]
                            distributions[xs].add(E)
        else:
            raise ValueError('only arity 1 or 2')
    return distributions


def finite_substitution_certificate(words):
    """Returns None iff the finite language is exactly (2,content)-substitutable.
    Otherwise returns (d, x, y, common E, discriminating F).
    Every relevant context arises by cutting a word in the finite language.
    """
    for d in (1, 2):
        distributions = contexts_of_finite_language(words, d)
        by_type = defaultdict(list)
        for xs in distributions:
            by_type[content_tuple(xs)].append(xs)
        for group in by_type.values():
            for index, xs in enumerate(group):
                for ys in group[index + 1:]:
                    Cx, Cy = distributions[xs], distributions[ys]
                    if Cx & Cy and Cx != Cy:
                        E = min(Cx & Cy)
                        F = min(Cx ^ Cy)
                        return d, xs, ys, E, F
    return None


def render_context(E, xs):
    assert len(E) == len(xs) + 1
    return ''.join(s for pair in zip(E, xs + ('',)) for s in pair)


def is_bc_plus(word):
    return len(word) >= 2 and len(word) % 2 == 0 and word == 'bc' * (len(word) // 2)


def near_miss_member(n, word):
    """Exact membership for the infinite language generated by
    A_0 -> a | D; A_i -> A_(i-1) A_(i-1) | D;
    D -> bc | bc D.  Computes on the COMPLETE input word.
    """
    @lru_cache(maxsize=None)
    def A(i, w):
        if is_bc_plus(w):
            return True
        if i == 0:
            return w == 'a'
        return any(A(i - 1, w[:j]) and A(i - 1, w[j:])
                   for j in range(1, len(w)))
    return A(n, word)


def verify():
    # Two fan-out-two B nodes, each with two different 3-letter split rules.
    b_rules = (('a', 'aa'), ('aa', 'a'))
    distinct = (b_rules[0], b_rules[1])
    assert distinct[0] != distinct[1]
    assert all(sum(map(len, t)) == 3 for t in b_rules)
    yields = set()
    for left, right in product(b_rules, repeat=2):
        w = left[0] + 'a' + left[1] + right[0] + 'a' + right[1]
        yields.add(w)
        assert len(w) == 8
    assert yields == {'a' * 8}
    assert finite_substitution_certificate(yields) is None
    print('Toy fan-out-2: all four rule choices produce a^8;')
    print('  distinct component splits coexist in a node-minimal 3-node tree.')

    # The finite family has a paper proof for ALL k>=5; these are exact checks
    # of finite instances, not an extrapolation to arbitrary k.
    for k in (5, 6, 7, 8, 9):
        L = {'a' * k, 'abc', 'acab'}
        cert = finite_substitution_certificate(L)
        assert cert is None, (k, cert)
        assert 'abc'.count('b') == 'acab'.count('b') == 1
        assert 'abc'.count('c') == 'acab'.count('c') == 1
        assert 'abc'.count('a') == 1 and 'acab'.count('a') == 2
        print('Exact finite tuple test: k=', k, ', arities 1,2: PASS', sep='')

    n = 2
    for w, expected in (('bc', True), ('bcbc', True),
                        ('bcbca', True), ('bca', False),
                        ('aaaa', True), ('aaa', False)):
        observed = near_miss_member(n, w)
        assert observed == expected, (w, observed, expected)
        print('Near-miss n=2:', repr(w), observed)
    assert render_context(('', ''), ('bc',)) == 'bc'
    assert render_context(('', ''), ('bcbc',)) == 'bcbc'
    assert render_context(('', 'a'), ('bcbc',)) == 'bcbca'
    assert render_context(('', 'a'), ('bc',)) == 'bca'
    print('Near-miss arity-1 certificate: E=hole, F=hole+a: VERIFIED')


if __name__ == '__main__':
    verify()
```

実行結果（2026-11-04、Python 3、標準ライブラリのみ）：

```text
Toy fan-out-2: all four rule choices produce a^8;
  distinct component splits coexist in a node-minimal 3-node tree.
Exact finite tuple test: k=5, arities 1,2: PASS
Exact finite tuple test: k=6, arities 1,2: PASS
Exact finite tuple test: k=7, arities 1,2: PASS
Exact finite tuple test: k=8, arities 1,2: PASS
Exact finite tuple test: k=9, arities 1,2: PASS
Near-miss n=2: 'bc' True
Near-miss n=2: 'bcbc' True
Near-miss n=2: 'bcbca' True
Near-miss n=2: 'bca' False
Near-miss n=2: 'aaaa' True
Near-miss n=2: 'aaa' False
Near-miss arity-1 certificate: E=hole, F=hole+a: VERIFIED
```

**計算の位置づけ**：`L_k` の全 `k≥5` の代入可能性は§7の**紙上証明**による。計算は `k=5,…,9` の個別の厳密な検算であり、族全体の証明ではない。near-missの否定は `n=2` の明示的な4語からの直接反証である。

## 11. 文献との関係・新規性

* **原稿**：栗山貴之、#2 の上記GitHub SHA。主要箇所は §2–§4、`lem:thickness-equivalence`、`prop:rare-type`、`op:fanout-two`、付録 `app:two-letter-content`。
* **先行系列**：`reviews/chatgpt_spectrum_m_2026-11-03.md`（第八報）、`chatgpt_bc_escapes_2026-11-03.md`、`chatgpt_escape_branches_2026-11-03.md`。ここでの (U) の構成的証明、ラベル節点数ランキング、価格欠損の整理、`L_k` の反例は今回の報告として明示した。
* **文献で確認できる一般背景**：Ryo Yoshinaka, *Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*, Theoretical Computer Science 412 (2011), 1821–1831, [DOI 10.1016/j.tcs.2010.12.058](https://doi.org/10.1016/j.tcs.2010.12.058)。MCFGの多次元代入可能性と学習が主題であり、今回の `N_B` の問題を解決したとする資料ではない。Markus Lohrey らの [*Balancing Straight-Line Programs for Strings and Trees*](https://pmc.ncbi.nlm.nih.gov/articles/PMC7309493/) ではSLP・DAGによる圧縮が一般的な既知概念として扱われている。従って本報告で**「DAGを用いること自体」を新規と主張しない**。
* **同等定理の有無**：最小純粋語導出の同名ラベル節点数剛性、元の依存グラフの非巡回性、pure-`a` fiber、価格欠損命題が既刊文献に同形式で存在するかは**未確認**。限定的な文献検索から「新規性が証明された」とは書かない。

## 12. 終了時の三点

1. **証明できたこと**：一様な最小導出 (U) を、**元の最小木のラベル依存グラフが既に非巡回**という強化つきで厳密に証明した。成分長一致は偽。純粋二成分組の分布層別化、`B`-分岐深さ、算術的交差条件、三文字の安易な飽和二分法への具体的反例を得た。
2. **止まった場所**：算術的に `b,c` 個数を整えた二つの短縮語を、**同じ `a` 骨格**へ整列させる機構がない。さらに両文字型 `B` の重複出現が、実際に深い倍増DAGで実現され得ることを内容代入可能性が排除するか証明できない。完全適格な下界族も未構成。
3. **次に絞る一点**：**単一の重い両文字型 `B` を数多く含む一様DAGの「一つの倍増規則」を固定し、その両方の子に現れる `B` の短縮を、祖先の一色短縮または非空セパレータを持つ二穴文脈と交差させたとき、骨格整列が不可避になるための必要十分条件を求める。** まず `fan(B)=1`、`rank=2`、混合型は `B` 一つだけの局所模型に限定する。三文字全内容の一般二分法を先に仮定しない。

**最終判定**：一様化 (U) は成立。中心の `op:fanout-two` について**一般肯定も適格な否定族も未解決**。「境界がファンアウトで動く」とは主張しない。
