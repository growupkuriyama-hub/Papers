# 骨格の多様性と重みの間隔：三文字内容型付け・ファンアウト2、一文字最短語の検討

**研究日**：2026-11-02  
**対象**：栗山貴之、論文 #2、`op:fanout-two` の純粋一文字語段階  
**結論**：一般の対数骨格多様性、および `μ_a(L)` の無条件多項式上界は **未解決**。以下では (i) 既知の `r^M` を「重みの間隔を空けた個数」で置換する無条件の**パラメータ改良**、(ii) 倍増・短符号スキーマ全体を排除する**arity 2 の偶奇障害**、(iii) 一意復号可能な符号にも課される**離散アフィン重み制約**を証明する。これらは `op:fanout-two` の肯定・否定を決着させない。

| 主張 | 判定 | 根拠 |
|---|---|---|
| 一般に `M(T)=O_r(log(g+θ))` となる代表選択が存在する | **未解決** | §2、§6 |
| 一般に `μ_a(L)≤poly_r(g,θ)`、および全内容型の `op:fanout-two` | **未解決** | §1、§6 |
| `r^M` を、幅 `Δ` で分離した重みの最大個数 `r^{N_Δ(T)}` に置換する上界 | **証明済み** | §2、定理2.2 |
| `a^4` が現れる言語で、全 `a`-塊長が `dℕ` (`d≥2`) なら、受理語に二つの `a`-塊は共存できない | **証明済み** | §3、補題3.1 |
| `E_0→a`, `E_i→E_{i-1}E_{i-1}｜d_i`、任意の `d_i∈{b,c}^+` は `n≥3` で `(2,c)`-代入可能でない | **証明済み・候補スキーマ全体の反証** | §3、定理3.2 |
| `bc^i b` は一意復号でき、連結後も指数重みを復号できる。しかしその事実だけでは言語の代入可能性を保証しない | **証明済み（符号の事実）／論法の限界** | §4.1–§4.2 |
| `bc^i b` をトークンとする豊富な定重み言語が `(2,c)`-代入可能なら、内部の重み列は二階差分ゼロ | **証明済み（必要条件）** | §4、定理4.1 |
| 長さ3以下の `b,c` 符号を用いる倍増族の `n=3` に合格例がない | **有限探索の観察**（探索範囲に限る） | §5、付録A |
| 三文字内容型付けで指数長の純粋 `a` 語を強制する `(2,c)`-代入可能な族の構成 | **未達成** | §6 |
| 新しいパラメータ改良・偶奇障害・アフィン制約が文献上新規か | **未確認** | §7 |

---

## 1. 正本、定義、依存関係

### 1.1 今回実際に照合した資料

- 現行 [`main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)：Git blob `4b9d1e9d1e8b88ab9a925492814a73fca2cf23a3`。特に `def:standard-mcfg`, `def:grammar-properties`, `def:tuple-substitutable`, `lem:thickness-equivalence`, `prop:rare-type`, `lem:power-transfer`, `op:fanout-two`。
- 前回 [`chatgpt_pure_letter_fanout2_2026-11-02.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_pure_letter_fanout2_2026-11-02.md)：Git blob `063ca391af87e82c5153779b22ecf7d65f09192a`。定理3.1、補題4.1、定理4.2、系4.4。
- [`claude_ternary_content_2026-11-01.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_ternary_content_2026-11-01.md)：Git blob `658f3744cfdeea54d2566cfbcac3d38049c21e1d`。補題3.1–3.5、6.3。

**出典確認について**：この三つは今回 GitHub コネクタで取得した。今回利用するのは、前回の定理3.1と4.2、Claude の再配分（3.1）・個数漏れ（3.2(iii)）・剛性（6.3(ii)）、および任意の二穴を交換する定義である。補題3.3–3.5もその証明・穴間非空の条件を読んだが、**新しい定理2.2、3.2、4.1の証明はそれらを未証明の補助公理として使っていない**。共役移送だけで全コードが同一視されるという追加主張はしない。

### 1.2 記号と前提

`Σ={a,b,c}`、`c=c_Σ` は語の内容（出現文字集合）。`L∈C_{2,c}` は fan-out `≤2` の MCFG 言語で、各 arity `d=1,2`、内容が**成分ごとに等しく**、**共通の許容受理文脈**を持つ非空 `d`-組の分布が一致する。`d=2` の穴の間の固定文字列は必ず非空である。

`G` は `L∩Σ^+` の reduced good 文法、fan-out `≤2`、ランク `≤r` (`r≥2`)、`v=|V|`、`g=‖G‖`、`θ=θ̄_G≥1`。原稿の thickness lemma により、各規則の明示終端文字数は `≤θ`、各非終端 `B` に長さ総計 `≤θ` の生成組 `ω_B` がある。

`C=U□V`、`k=P_a(C)=min{j≥1:Ua^jV∈L}≥5`。`W=C[a^k]` の**節点数最小導出**を `T` とし、固定文脈のすべての文字、および穴の前端2文字・後端2文字を印とする。`h` は印の無い重い (`ℓ_h>θ`) 節点で、`ℓ_h` は導出成分の総長（元の語ではすべて `a`）。

\[
\kappa(B)=\sigma_a(a\omega_{B,1}a\cdots a\omega_{B,d}a),\qquad
w_h=\ell_h-|\omega_{B_h}|_a\in[1,k-1].
\]

`σ_a` は極大 `a`-塊を一文字 `a` にする。`M(T)` は重い印無し節点に現れる相異なる `κ(B)` 数。前回定理3.1は `κ(B_h)=κ(B_{h'})` なら `w_h=w_{h'}` とする。この結果は、**arity 2** による `a`-塊再配分、および **arity 1** による個数漏れと最小性への矛盾を経由する。

**反鎖の加法性（前回・Claude の帰結）**：互いに部分木が重ならない節点集合 `J,J'` の短い生成組への同時差替え語が同じ `a`-骨格なら、`\sum_{h\in J}w_h=\sum_{h\in J'}w_h`。実際、各総損失は非負で `≤k-4`（互いに交わらない穴の内部で生じるため）。異なる場合の差 `0<δ<k` は、再配分→arity 1 の分布一致→`C[a^{k-δ}]` という矛盾を生む。**これは実際に同じ骨格を与える二つの反鎖に対する条件**であって、全符号列の組合せに任意に適用できる等式ではない。

---

## 2. S1：骨格種類数の代わりに「重みの間隔」を数える

前回補題4.1の乗法ステップを、同じ骨格の「初登場」ではなく、**既出重みから十分離れた重みの初登場**だけに課す。

**定義2.1（重みの `Δ`-packing）**。`Δ∈ℕ_0` とする。`T` の印の無い重い節点の重み集合を

\[
\mathcal W(T)=\{w_h:h\text{ は印無し重い節点}\}
\]

とし、

\[
N_\Delta(T)=\max\{|Q|:Q\subseteq\mathcal W(T),\ |x-y|>\Delta\text{ for distinct }x,y\in Q\}.
\]

空集合なら `N_Δ=0`。すべて整数だから `N_0` は**相異なる重みの個数**である。前回定理3.1により

\[
N_\Delta(T)\le N_0(T)\le M(T)\le v.
\tag{2.1}
\]

**定理2.2（重み packing による条件付き上界；証明済み）**。上記設定で `m=|C|_fix+4`、`H=v(m+1)^2` とすると、すべての `Δ∈ℕ_0` に対し

\[
\boxed{
P_a(C)\ \le\ mH\left[\theta+
 r\bigl(\theta+v(\Delta+\theta)\bigr)r^{N_\Delta(T)}\right].}
\tag{2.2}
\]

特に `Δ=0` では

\[
P_a(C)\le mH\theta[1+r(v+1)r^{N_0(T)}],
\tag{2.3}
\]

であり、これは前回の `r^M` を `r^{\#\{w_h\}}` に置換する。`Δ=θ` では `r^{N_θ}` が現れ、前因子の `(v+1)` は `(2v+1)` へ増えるだけである。

**証明**。まず `U` を印の無い極大部分木の任意の一つとする。根から各段で**総長最大の子**を選ぶパスを固定する。前回補題4.1と同じ最小導出の置換 argument により、このパスに同じ非終端は二度現れず、節点数は高々 `v`。同じ `B` を上と下で使うと、上側を下側に差し替えても印が一つも失われない。穴の長さが減れば `k` の最小性、減らなければ導出節点数の最小性に反する。

パスを下から上へたどる。根が非重いとき総長 `≤θ`。重い親 `p` の最大の子 `t` について、規則に現れる終端数が `≤θ` なので、一般に

\[
\ell_p\le r\ell_t+\theta.\tag{2.4}
\]

一方、パス上で `p` より下方に既に訪れた重い節点 `q` があり、`|w_p-w_q|≤Δ` なら、各代表の `a` 個数は `≤θ` であるため

\[
\ell_p=w_p+|\omega_{B_p}|_a
\le w_q+\Delta+\theta
\le \ell_q+\Delta+\theta
\le\ell_t+\Delta+\theta.\tag{2.5}
\]

最後の不等式は非削除性による。したがって `(2.4)` の `r` 倍を使うのは、これより下方の既出重みのすべてから `>Δ` 離れた節点だけでよい。このような「初登場」の重みは互いに `>Δ` 離れているので、その数は `≤N_Δ(T)`。その他の各段は加算 `Δ+θ` のみで済む。葉の総長は `≤θ`、パスの長さは `≤v` だから、加算誤差を乗法ステップの前へ移して

\[
\ell(U)\le[\theta+v(\Delta+\theta)]r^{N_\Delta(T)}.\tag{2.6}
\]

印付き節点は高々 `mH` 個、印無し極大部分木は高々 `rmH` 個である（前回定理4.2の印署名・高さの議論）。印付き節点の明示終端文字数は `≤θ`。ゆえに

\[
|C|_{\rm fix}+k=|W|\le mH\theta+rmH[\theta+v(\Delta+\theta)]r^{N_\Delta(T)},
\]

から `(2.2)`。証明中の**新しい counting 部分は文法の非削除性と長さの算術だけ**を使う。`N_Δ≤M` には前回定理3.1（arity 1 と 2）が必要。□

**系2.3（弱い十分条件）**。固定 `r` で `|C|_fix≤θ` とする。`Δ=poly(g+θ)` に選べて `N_Δ(T)=O_r(log(g+θ+2))` なら `P_a(C)`、特に `C=□` の `μ_a(L)` は `g,θ` の多項式で抑えられる。ただしこの packing 仮定は**まだ証明していない**。

**重要な限界**：`Δ` を非常に大きくすれば `N_Δ=1` にできるが、その際 `(2.2)` の係数自体が `Δ` に比例して大きくなる。したがって、この定理だけで無条件の多項式上界は出ない。指数的に離れた重み `2,4,8,…` では、多項式程度の `Δ` を選んでも `N_Δ` が線形に残り得る。

---

## 3. S2：倍増＋短い非 `a` 符号の**全選択**が失敗する

### 補題3.1（整数格子に縛られた `a`-塊の障害；証明済み）

`L∈C_{2,c}` に `a^4` が因子として出現し、ある整数 `d≥2` について**すべての受理語の極大 `a`-塊の長さが `d` の倍数**であるとする。このとき、`L` の語に二つ以上の極大 `a`-塊は存在しない。

**証明**。二つの `a`-塊があれば、その長さは `p,q≥d≥2`、よってどちらも少なくとも2。Claude 補題3.1（arity 2 で導かれる `a` の再配分）により、最初の塊から次の塊へ `a` を一つ動かし、長さ `(p-1,q+1)` にした語も受理される。塊はどちらも消えない。だが `p-1` は `d` の倍数でなく矛盾。中間に別の `a`-塊があっても、再配分を適用できる。□

### 定理3.2（倍増スキーマの一律反証；証明済み）

任意の `n≥3` と任意の**空でない** `d_1,…,d_n∈{b,c}^+` に対し、fan-out 1・rank 2 の CFG

\[
E_0\to a,\qquad E_i\to E_{i-1}E_{i-1}\mid d_i\quad(1\le i\le n),\qquad S=E_n
\tag{3.1}
\]

の言語 `L_n` は **`(2,c_Σ)`-組代入可能ではない**。この結論は `d_i` の長さ、相異性、符号の一意復号性と無関係である。特に、これまで試した `d_i∈{b,c}^+` の選び直しではこの文法スキーマを救えない。

**証明**。どの導出でも `a` は `E_1→E_0E_0→aa` という部分からしか出ない。`d_i` は `a` を含まないため、任意の受理語の極大 `a`-塊は**偶数長**である（隣り合う塊を結合しても偶数のまま）。一方、全段で二倍化を選ぶと `a^{2^n}∈L_n` で、`a^4` が出現する。

`u=d_1` とし、`N=2^n`。`E_2` は `aa u` を生成し、`E_3` は `(aa u)(aa u)` を生成する。`n>3` では左端の `E_3` 以外の兄弟部分木をすべて純 `a` 語にする。したがって

\[
W=aa\,u\,aa\,u\,a^{N-8}\in L_n.\tag{3.2}
\]

これは二つの `a`-塊を含むので補題3.1だけで矛盾する。**完全に明示した arity 2 違反の証明書**も与える。二組

\[
\mathbf x=(aa,a),\quad\mathbf y=(a,aa)
\]

は成分内容が共に `({a},{a})`。許容文脈

\[
E=\square_1\,a\,\square_2\,a^{N-4}
\]

では `E[\mathbf x]=E[\mathbf y]=a^N∈L_n`。ところが別の許容文脈

\[
F=\square_1\,u\,a\,\square_2\,u\,a^{N-8}
\]

では

\[
F[\mathbf x]=aa\,u\,aa\,u\,a^{N-8}\in L_n,
\quad F[\mathbf y]=a\,u\,aaa\,u\,a^{N-8}\notin L_n.
\]

後者は `u` が `a` を含まないため先頭の `a`-塊長が1（次の塊長が3）になり、偶数塊不変量を破る。`E,F` の二穴間の固定部分はそれぞれ `a`、`ua` で非空である。よって arity 2 の代入可能性に反する。**arity 1 の違反を探す必要はない**。□

**文法条件と規模**：`G_n` は reduced（すべての `E_i` が到達可能・生産可能）、good（定数規則と非削除・非交換の二子連結規則）、fan-out `1≤2`、rank `2`。定義上

\[
\|G_n\|=7n+3+\sum_{i=1}^n|d_i|,
\qquad \mu_a(L_n)=2^n.
\tag{3.3}
\]

`μ_a` の等式は、純 `a` の導出ではどの `d_i` も使えず、二倍化をすべて選ぶほかないことから従う。ただし `L_n\notin C_{2,c}` なので、**これは `op:fanout-two` の下界ではない**。

特に `d_i=bc^i b` とすれば

\[
\|G_n\|=\frac{n(n+1)}2+9n+3,\qquad
\bar\theta_{G_n}=\frac{n(n-1)}2+2n\quad(n\ge2).
\tag{3.4}
\]

後者は原稿通り、**その規則を少なくとも一回使う成功導出の語長の最小値**を各規則で求めた結果である。実際、`E_i` の最短長 `δ_i` は `δ_0=1, δ_1=2, δ_i=i+2 (i≥2)`。`E_i` のある規則を使用する最短文の長さは、その規則の最短出力長に `\sum_{j=i}^{n-1}δ_j`（祖先の兄弟部分木の最短長）を足したものであり、最大は `E_1→bcb` の場合の `3+\sum_{j=1}^{n-1}δ_j=2+\sum_{j=0}^{n-1}δ_j`。`n≥2` でこれを計算すると `(3.4)` となる。`n=1` の厚さは3。この明示的計算は**失敗する候補のサイズ検証**であり、正例の下界ではない。

**意味**：倍増・短符号構成における最初の壁は、長い隙間の一意復号以前に、**短い非 `a` 終端への逃げ道と純 `a` 葉の二倍化が作る、塊長の合同条件**である。二穴の再配分はこの合同条件を許さない。

---

## 4. S1(b)/S2：一意復号できる符号にも残る重み制約

### 4.1 まず、加法性と合流「だけ」では重み `2^i` を排除できない

`D_n={d_i=bc^i b:1≤i≤n}` とする。`D_n` は**接頭符号**：`d_i` と `d_j` (`i<j`) は最初の `i+1` 個の文字まで一致するが、次の文字で前者は終端 `b`、後者は `c` となる。したがって `D_n^*` は左から一意に因子分解でき、隣接する隙間の語を `d_{i_1}\cdots d_{i_t}` に合流させても指数重み

\[
\mathrm{wt}(d_{i_1}\cdots d_{i_t})=\sum_{j=1}^t2^{i_j}
\]

を一意に復号できる。すべての `d_i` の長さは `O(n)`、総符号長は `O(n^2)`、種類数は `n` である。

これは、**「同じ連結語なら重み和が等しい」という抽象的な加法性と、隙間をただ連結する操作だけ**から、`M=O(log(g+θ))` や重み比の多項式性を導くことはできない、と示す**符号レベルの反モデル**である。`D_n` が実際に `C_{2,c}` の言語を実現するとは主張しない。次がまさにその不足条件である。

### 定理4.1（単一文字ラン符号の離散アフィン剛性；証明済み）

任意の正整数重み `t_1,…,t_n` (`n≥4`) と正整数 `N` に対し、トークン集合 `T_n={a}∪D_n` に `wt(a)=1, wt(d_i)=t_i` を与え、**全ての正重み `N` の連結**からなる有限言語

\[
\mathcal L_{N,n}(t)=\{z_1\cdots z_s:z_j\in T_n,\ \sum_jwt(z_j)=N\}
\tag{4.1}
\]

を考える。`t_4≤N`、かつある `2≤i≤n-1` について `2t_i≤N` と仮定する。

もし `\mathcal L_{N,n}(t)` が `(2,c)`-組代入可能なら、

\[
\boxed{t_{i-1}+t_{i+1}=2t_i.}\tag{4.2}
\]

特に `N≥2\max_jt_j` なら、`t_i` は `i` の**アフィン関数**（二階差分ゼロ）でなければならない。

**証明**。`d_4a^{N-t_4}∈\mathcal L_{N,n}(t)` なので `c^4` が受理語に出現する。`2t_i≤N` により

\[
x=d_i d_i a^{N-2t_i}\in\mathcal L_{N,n}(t).
\]

一方、

\[
y=d_{i-1}d_{i+1}a^{N-2t_i}
\]

は `x` と同じ `c` 骨格 `bcb bcb a^{N-2t_i}`（ここで `c` は各極大塊の代表を表す）と同じ `c` 個数 `2i` を持つ。Claude 補題3.1、すなわち**arity 2 の `c`-塊再配分**により `y` も受理されなければならない。`{a}∪D_n` は接頭符号なので `y` のトークン分解は一意であり、その重みは `t_{i-1}+t_{i+1}+N-2t_i`。重み `N` に等しい必要があるため `(4.2)`。各内部 `i` に適用すれば重み列はアフィンである。□

**具体的な `(2,c)` 違反**：`n=4, N=16, t_i=2^i`。`d_4=bccccb` 自体が重み16の受理語。二組 `x=(cc,c)`、`y=(c,cc)` は共に内容 `({c},{c})` で、共通の許容文脈 `E=b□_1c□_2b` において同じ `d_4` を生成する。別文脈 `F=b□_1bbc□_2ba^8` では

\[
F[x]=d_2d_2a^8\in\mathcal L_{16,4}(2^i),\quad
F[y]=d_1d_3a^8\notin\mathcal L_{16,4}(2^i),
\]

なぜなら重みが前者 `4+4+8=16`、後者 `2+8+8=18` だからである。**二穴の区切り `c`、`bbc` はどちらも非空**。

この結果の射程は、(4.1) のように必要な**二つのコードが同時に出現するだけの閉包**を持つモデルまでである。任意の文法の代表組に `bc^i b` があるだけでは、`d_id_i a^p` の受理は保証されない。従って任意の `κ(B)` に対するアフィン性、ひいては一般の `r^M` 排除を主張できない。

---

## 5. 有限検査の結果

付録Aは **Python 3 標準ライブラリのみ**である。有限 `L_n` の**全生成語**について、各一穴・二穴の非空 tuple occurrence を全て列挙し、同じ成分別内容・共通受理文脈を持つ組の全てについて分布一致を検査する。`None` は対象の**有限言語についてのみ**完全な肯定の証明になる。符号長を制限した総当たりでは、その**有限探索領域内だけ**の結果である。

実行結果：

```text
E_n example d1=b, d2=c, d3=bc
n= 1 |L|= 2 mu_a= 2 first violation= None
n= 2 |L|= 5 mu_a= 4 first violation= None
n= 3 |L|= 26 mu_a= 8 first violation= 1
universal arity-2 certificate at n=3: {'arity': 2, 'x': ('aa', 'a'), 'y': ('a', 'aa'), 'shared': ('', 'a', 'aaaa'), 'separating': ('', 'ba', 'b'), 'accepted': 'aabaab', 'rejected': 'abaaab'}
weighted-code arity-2 certificate: {'arity': 2, 'x': ('cc', 'c'), 'y': ('c', 'cc'), 'shared': ('b', 'c', 'b'), 'separating': ('b', 'bbc', 'baaaaaaaa'), 'accepted': 'bccbbccbaaaaaaaa', 'rejected': 'bcbbcccbaaaaaaaa'}
complete code search at E2, E3, code lengths <=3: (14, 130, 0, {1: 1656, 2: 164})
```

最後の行は `b,c` の**長さ1～3**の14個の符号を用いた探索。`n=2` の196通りのうち130組が arity 1,2 とも合格したが、それらに第3符号14種類を追加した1820通りでは合格は0（最初の違反の内訳は arity 1 が1656、arity 2 が164）。`n=2` が既に不合格なら、その任意の生成語を `E_3` に埋め込んだ際に違反が必ず保存されるかは**この探索の数字だけからは主張しない**。しかし定理3.2は、その限定探索とは無関係に、あらゆる符号長の `n≥3` の失敗を証明する。

`n=3` のコード例について、検査が最初に見つけた違反は arity 1 だったが、定理3.2の**arity 2 違反は別途明示**してある。最初に見つかる違反の arity に数学的優先順位はない。

---

## 6. 停止点と次に狙うべき厳密な命題

**S1(a)**：異なる符号の差替えを、再配分・隙間合流・共役移送で**常に同じ** `a` 骨格にできる、という主張は証明できなかった。これらの操作は新しい語の所属を保証するが、任意の二つの `ω_B` の異なる `b,c` 語を同一視するものではない。そもそも異なる骨格のまま同じ文字数を持つ語からは、arity 1 の個数漏れを起動できない。

**S1(b)**：加法性と、隙間が連結しても重みが復号できる条件は、接頭符号 `bc^ib` と重み `2^i` で**抽象的には両立**する。この方針を決着させるには、`bc^i b` に対する定理4.1のような、**符号内部の異なる箇所をまたぐ arity 2 の再配分・共役移送**まで入れなければならない。しかし、一般の短い二文字符号は同じ文字の4乗を含まないこともあり、今回のアフィン化は一般化できなかった。

**S1(c)**：定理2.2は、同じ骨格でない重い節点でも**近い損失重み**なら加法的増加で処理できることを示す。しかし、二倍ずつ離れた重みが実際の `L∈C_{2,c}` に出現しないとは証明できていない。

**S2**：`E_i→E_{i-1}E_{i-1}｜d_i` は `d_i` の選択に**一切依存せず**偶数 `a`-塊障害で失敗する（定理3.2）。実際の反例を作るには、少なくとも **二つの `a`-塊に `1` 文字を再配分した語を受理できる**よう、文法の生成語を大幅に拡張する必要がある。その拡張で新たに短い純 `a` 語が生成されないこと、および arity 1,2 の完全な代入可能性は別途証明が必要である。

**残る、前回より少し絞られた問い**：任意の `L∈C_{2,c}` と最小導出 `T` について、多項式 `Δ=poly(g+θ)` を選び

\[
N_\Delta(T)=O_r(\log(g+\theta+2))
\]

を証明できるか。これは `M=O(log)` より弱い十分条件である。また、`N_Δ` が大きいとき、相互に大きく離れた重みを持つ符号に対し、**どの arity 2 の二穴境界が必ず同じ語・同じ骨格を作るか**が核心となる。

`op:fanout-two` の三文字**全体**（すべての内容型）の代表長は一切抑えられていない。ここで「境界がファンアウトで動く」とは結論しない。

### 下界の射程（今回は下界を得ていない）

仮に将来、固定 `Σ={a,b,c}`、内容型 `c_Σ`、fan-out `≤2`、固定 rank `≤r` (`r≥2`)、reduced good `G_n`、`g_n,θ_n=n^{O(1)}`、`L_n∈C_{2,c}` で `μ_a(L_n)=n^{ω(1)}` を実現できれば、原稿 `prop:rare-type` により、`\mathcal B_{2,c}^{\le r}` と `\mathcal B_{2,c}` の特徴標本には**内容 `{a}` の語が必要**で、その総符号長の寄与は少なくとも `μ_a(L_n)+1`。`C_{2,c}` 全体に特徴標本を持つ任意の**集合駆動作用素**にも同様である（比較対象は `L_n\setminus c^{-1}({a})`）。これは任意の逐次 Gold 学習器の時間や収束時点の下界を意味しない。**本報告には、その前提を満たす反例族はない。**

## 7. 文献上の位置づけ

定義・分布代入可能性の原典として Clark–Eyraud (2007), *JMLR* 8:1725–1745 と Yoshinaka (2011), *Theoretical Computer Science* 412(19):1821–1831（DOI: `10.1016/j.tcs.2010.12.058`）を照合した。有限・無限符号の一意復号性そのものは古典的な符号理論の概念であり、それを本報告の独立した新規成果とはしない。原稿 `main.tex` の `lem:power-transfer` は arity 2 の交換を一般の有限半群に拡張する既存の著者内結果である。

ここで証明した**重み packing の特定上界、偶数塊の倍増スキーマへの一律適用、トークン定重みモデルのアフィン制約**と同一の既発表命題の有無は **未確認**。公開情報を確認した範囲では、これらを原著の新規性として断定する根拠も、既出と断定する根拠もない。

---

## 付録A：検査スクリプト全文（Python 3 標準ライブラリ）

ファイル名例：`skeleton_diversity_check.py`。Windows では `py -3 skeleton_diversity_check.py`。`exact_finite_check` の入力に有限言語の**全語**を与えた場合に限り、違反なしはその言語の代入可能性の完全証明になる。`decode_weight` はトークン言語での**厳密な所属判定**のための復号で、MCFG 一般の所属決定アルゴリズムではない。

```python
#!/usr/bin/env python3
"""Content-typed substitutability: exact finite checks and two certificates.
Run on Windows: py -3 skeleton_diversity_check.py
Only Python 3 standard library is used.
For finite E_n, enumeration is COMPLETE. The finite search over codes is
complete only within the explicitly stated length bound.
"""
from collections import defaultdict, Counter
from itertools import product


def occurrences(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[i:j],), (w[:i], w[j:])
    elif d == 2:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for h in range(k + 1, n + 1):
                        yield (w[i:j], w[k:h]), (w[:i], w[j:k], w[h:])
    else:
        raise ValueError('Only arity 1 or 2 is supported')


def plug(context, tup):
    assert len(context) == len(tup) + 1
    return ''.join(left + piece for left, piece in zip(context, tup)) + context[-1]


def exact_finite_check(words, arities=(1, 2)):
    """Return a genuine witness or None (proof of both properties for finite L).
    Content is checked PER COMPONENT; nonempty inter-hole separators only.
    """
    lang = set(words)
    for d in arities:
        distributions = defaultdict(set)
        grouped = defaultdict(set)
        for w in sorted(lang):
            for tup, ctx in occurrences(w, d):
                distributions[tup].add(ctx)
                typ = tuple(frozenset(x) for x in tup)
                grouped[(typ, ctx)].add(tup)
        checked = set()
        for (_, shared), tups in grouped.items():
            tups = sorted(tups)
            for k, x in enumerate(tups):
                for y in tups[k + 1:]:
                    if (x, y) in checked:
                        continue
                    checked.add((x, y))
                    for left, right in ((x, y), (y, x)):
                        for separating in sorted(distributions[left]):
                            accepted = plug(separating, left)
                            rejected = plug(separating, right)
                            if rejected not in lang:
                                return dict(arity=d, x=left, y=right,
                                            shared=shared, separating=separating,
                                            accepted=accepted, rejected=rejected)
    return None


def doubling_language(codes):
    """E0 -> a; Ei -> Ei-1 Ei-1 | codes[i-1]. Complete FINITE set."""
    current = {'a'}
    for word in codes:
        current = {x + y for x in current for y in current} | {word}
    return current


def parity_certificate(codes):
    """A universal arity-2 violation for every len(codes)>=3 and no-a codes."""
    n = len(codes)
    assert n >= 3 and all(w and set(w) <= {'b', 'c'} for w in codes)
    u = codes[0]
    suffix = 'a' * (2**n - 8)
    E = ('', 'a', 'a' * (2**n - 4))
    F = ('', u + 'a', u + suffix)
    x, y = ('aa', 'a'), ('a', 'aa')
    lang = doubling_language(codes) if n <= 3 else None
    if lang is not None:
        assert plug(E, x) == plug(E, y) == 'a' * 2**n
        assert plug(F, x) in lang and plug(F, y) not in lang
    return dict(arity=2, x=x, y=y, shared=E, separating=F,
                accepted=plug(F, x), rejected=plug(F, y))


def decode_weight(word, n):
    """Prefix decode {a, b c^i b (1<=i<=n)}. Return weight or None."""
    k, total = 0, 0
    while k < len(word):
        if word[k] == 'a':
            total += 1
            k += 1
        elif word[k] == 'b':
            j = k + 1
            while j < len(word) and word[j] == 'c':
                j += 1
            i = j - k - 1
            if not (1 <= i <= n and j < len(word) and word[j] == 'b'):
                return None
            total += 2**i
            k = j + 1
        else:
            return None
    return total


def affine_certificate():
    """Finite weighted token language at N=16, n=4, with exact membership."""
    code = lambda i: 'b' + 'c'*i + 'b'
    N, n = 16, 4
    common = ('b', 'c', 'b')  # both fill to bccccb = code(4)
    separating = ('b', 'bbc', 'b' + 'a'*8)
    x, y = ('cc', 'c'), ('c', 'cc')
    assert plug(common, x) == plug(common, y) == code(4)
    w = plug(separating, x)
    z = plug(separating, y)
    assert decode_weight(code(4), n) == N
    assert decode_weight(w, n) == N
    assert decode_weight(z, n) == 18
    return dict(arity=2, x=x, y=y, shared=common,
                separating=separating, accepted=w, rejected=z)


def bounded_code_search(max_len=3):
    """All codes over {b,c} with length 1..max_len, for E2 and E3."""
    options = [''.join(t) for m in range(1, max_len + 1)
               for t in product('bc', repeat=m)]
    passed2 = []
    passed3 = []
    rejected3 = Counter()
    for u, v in product(options, repeat=2):
        if exact_finite_check(doubling_language((u, v))) is None:
            passed2.append((u, v))
            for w in options:
                hit = exact_finite_check(doubling_language((u, v, w)))
                if hit is None:
                    passed3.append((u, v, w))
                else:
                    rejected3[hit['arity']] += 1
    return len(options), len(passed2), len(passed3), dict(rejected3)


def main():
    print('E_n example d1=b, d2=c, d3=bc')
    for n in (1, 2, 3):
        lang = doubling_language(('b', 'c', 'bc')[:n])
        hit = exact_finite_check(lang)
        print('n=', n, '|L|=', len(lang), 'mu_a=', 2**n,
              'first violation=', None if hit is None else hit['arity'])
    print('universal arity-2 certificate at n=3:',
          parity_certificate(('b', 'c', 'bc')))
    print('weighted-code arity-2 certificate:', affine_certificate())
    print('complete code search at E2, E3, code lengths <=3:',
          bounded_code_search(3))


if __name__ == '__main__':
    main()

```
