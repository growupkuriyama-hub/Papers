# 三文字内容型付け・ファンアウト2における純粋一文字語の短縮問題

**研究報告（2026-11-02）**  
対象：栗山貴之、論文 #2 `02-v2-lg-fanout-boundary`、`op:fanout-two` の一文字語への制限。  
**結論：一般の Q は未解決。** ただし、最小の純粋一文字語／純粋一文字の一穴文脈について、**短い代替生成組の「非一文字骨格」の多様性で制御する条件付き上界**を以下に証明する。これにより、仮に超多項式の反例があれば、短い代替生成組には超対数個の異なる骨格が必要となる。

| 主張 | 判定 | 根拠 |
|---|---|---|
| 主問題 `μ_a(L) ≤ poly(‖G‖, θ̄_G)` の無条件の肯定／否定 | **未解決** | §1、§8 |
| `a^4` が現れたときの `a` 塊再配分と、同じ骨格・異なる `a` 個数からの周期漏れ | **証明済み（既存道具の再証明）** | 補題2.1、2.2 |
| 最短 `C[a^k]` の内側の重い節点：短い代替組の**骨格が同じなら、非終端が異なっても失われる `a` 個数が等しい** | **証明済み（本報告の精密化）** | 定理3.1 |
| 骨格種類数 `M` による `P_a(C)` の条件付き上界 `O_r(v² θ (|C|_fix+5)^3 r^M)` | **証明済み（本報告の条件付き定理）** | 定理4.2 |
| `|C|_fix ≤ θ` かつ `M=O_r(log(‖G‖+θ))` なら `P_a(C)` は多項式 | **証明済み（条件付き帰結）** | 系4.3 |
| 超多項式の純粋一文字最短語族には `M=ω(log(‖G‖+θ))` が必要（固定ランク） | **証明済み（必要条件）** | 系4.4 |
| `K_1,K_2` は `(2,c)`-組代入可能、`K_3` は arity 2 で違反 | **有限全数検査**（前二者は有限言語なので証明、後者は明示違反） | §6、付録A |
| 短い `b,c` 符号を与える単純な倍増文法の候補 | **否定的実験／個別の反証**（候補のみ） | §6、付録A |
| 上記の骨格種類数 `M` が一般に対数以下に抑えられるか | **未解決** | §5、§8 |
| 本報告の定理が文献に既出か | **未確認** | §7 |

## 1. 対象、原稿の確認と定義

2026-11-02 に接続 GitHub から取得した資料：

- [`main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、取得時 Git blob `4b9d1e9d1e8b88ab9a925492814a73fca2cf23a3`。
- [`reviews/claude_ternary_content_2026-11-01.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_ternary_content_2026-11-01.md)、Git blob `658f3744cfdeea54d2566cfbcac3d38049c21e1d`。

原稿 §2–4 の `def:standard-mcfg`、`def:grammar-properties`、`def:tuple-substitutable`、`lem:thickness-equivalence`、`prop:rare-type`、§8–9 の `lem:power-transfer`、`thm:two-letter-content`、`op:fanout-two`、`prop:unique-word-route`、`lem:unique-word-gap` を照合した。レビューの補題3.1–3.5と6.3について、以下で**実際に使う範囲は再証明**する。レビューに「証明済み」とある別の定理の正しさを、本報告だけで一括保証するものではない。

`Σ={a,b,c}`、`c=c_Σ` は語の文字集合を返す内容型付け。`L ∈ C_{2,c}` は `f≤2` の MCFG 言語で、**arity 1 と arity 2 の双方**について内容が成分ごとに等しい、かつ受理する許容文脈を共有する非空語組の分布が一致するもの。arity 2 の穴の間の固定文字列は非空。`G` は `L∩Σ⁺` を生成する reduced good 文法で、ファンアウト `≤2`、規則ランク `≤r`、`r≥2`。`v:=|V|`、`g:=‖G‖`、`θ:=θ̄_G≥1`。

原稿 `lem:thickness-equivalence` (i),(ii) から、**各規則が直接出力する終端は高々 `θ` 文字**であり、**各非終端 `B` に `ω_B∈L_B(G)`、`‖ω_B‖₁≤θ` を選べる**。good なので成分非空・非削除・非順序交換・非結合であり、ファンアウト2の非終端の二成分は成功導出の語中で、非空の固定部分を間に持つ。

純粋一文字語に関して

`μ_a(L)=min{k≥1:a^k∈L}`、

一穴文脈 `C=U □ V` に関して

`P_a(C)=min{k≥1:Ua^kV∈L}`

を用いる（存在しないときは `∞`）。`μ_a(L)=P_a(□)`。以下では `k=P_a(C)≥5` の場合を扱う。`k≤4` の場合の結論は自明である。今回の命題は、**原稿にある特徴標本の長さの無条件上界を示すものではない**。

## 2. 使用する代入可能性の帰結

### 補題2.1（再配分）

`a⁴` が `L` のある語に因子として現れるとする。同じ `a` 骨格 `σ_a(w)` と同じ `a` 個数を持つ二語は、`L` に属するかどうかが一致する。

**証明。** `pa⁴q∈L` から、組 `(a,aa)` と `(aa,a)` は成分内容 `({a},{a})` が一致し、共通の許容文脈 `p □₁ a □₂ q` を持つ。arity 2 の代入可能性から二組の分布が一致する。任意の語の異なる二つの極大 `a` 塊の間には非空の非 `a` 文字列がある。よって一方の塊が長さ2以上なら、そこから一個の `a` を他方の塊へ移す操作は所属を変えない。塊の長さの正の組成は、この操作で互いに連結されている。`a` 塊が高々一つの場合も自明。∎

### 補題2.2（同じ骨格からの個数漏れ）

`a⁴` が出現し、`w,w'∈L` が同じ `a` 骨格を持ち、`|w'|_a−|w|_a=δ>0` なら、

`D_L^(1)(a)=D_L^(1)(a^(1+δ))`。

**証明。** `a` 塊の数を `t≥1` とする。補題2.1 により、両語で第2塊以降をすべて長さ1とし、第1塊のみ長さが `δ` 異なる受理語を作れる。これらを同じ `p □ q` で `a` と `a^(1+δ)` を受理する二語として書ける。両者の内容は `{a}` なので arity 1 の代入可能性を適用する。∎

特に `k=P_a(C)` のとき、`0<δ<k` でこの分布等式が成立すれば、`C[a^k]` 中の `a^(1+δ)` を `a` に置き換え、`C[a^(k−δ)]∈L` が得られるため矛盾する。この**最小性との矛盾**が以下の核心である。

## 3. 新たな比較：異なる非終端の「骨格符号」

`T` を `W=C[a^k]` の導出のうち、節点数が最小のものとする。`C` の固定位置の全ての文字、および穴の `a^k` の先頭と末尾の2文字ずつを**印**とする。印の無い節点 `h` の導出成分はすべて穴の内部の純粋な `a` 列である。`ℓ_h` をその成分の総長とする。`ℓ_h>θ` なら**重い**とする。

各非終端 `B` の前述の短い生成組 `ω_B=(ω_{B,1},…,ω_{B,d})` (`d=fan(B)`) を一つ固定する。以下の語の `a` 骨格を、**短い代替生成組の符号**と呼ぶ：

`κ(B):=σ_a(a ω_{B,1} a … a ω_{B,d} a)`。

ここで各 `a` は1文字であり、`κ(B)` は `a` を含まない文字部分に関する骨格を記録する。ファンアウト2の場合、二つの成分間の `a` は、good 文法に由来する非空の区切りに対応する。`κ(B)` は `B` の名前を**記録しない**ため、異なる非終端でも同じ符号になり得る。

### 定理3.1（異なる非終端をまたぐ骨格剛性）

`h,h'` は `T` の、印の無い重い節点とする。`κ(B_h)=κ(B_{h'})` なら

`ℓ_h−|ω_{B_h}|_a = ℓ_{h'}−|ω_{B_{h'}}|_a`。

したがって `|ℓ_h−ℓ_{h'}|≤θ`。**二節点が比較可能（祖先・子孫）かどうかも、非終端の一致も仮定しない。**

**証明。** `h` のみを `ω_{B_h}` の導出に差し替えた成功語を `W^h∈L` と書く。非削除性のため、`h` の全成分は元の `a^k` の互いに交わらない非空区間に現れ、good の nonpermuting/nonmerging 条件により、二成分の場合はその間の元の語に少なくとも一つの `a` がある。印が無いため、最初の成分の前と最後の成分の後にも `a` がある。従って `σ_a(W^h)` は、**印の付いた固定外部部分を除けば** `κ(B_h)` によって一意に定まり、`h` の位置には依存しない。さらに全ての変更は穴の中で起こり、外部は `C` の同じ固定語のままである。ゆえに `κ(B_h)=κ(B_{h'})` なら `σ_a(W^h)=σ_a(W^{h'})`。

`w_h:=ℓ_h−|ω_{B_h}|_a` とおく。`ℓ_h>θ≥‖ω_{B_h}‖₁` なので `w_h≥1`。また `h` は穴の先頭末尾各2文字に触れないから `ℓ_h≤k−4`、従って `w_h<k`。同じことは `h'` にも成り立つ。`|W^h|_a=|W|_a−w_h` と `|W^{h'}|_a=|W|_a−w_{h'}` である。もし `w_h≠w_{h'}` なら、二つの受理語は同じ骨格で、`a` 個数が `δ=|w_h−w_{h'}|∈[1,k−1]` 異なる。補題2.2 と `P_a(C)` の最小性から矛盾。従って `w_h=w_{h'}`。最後に `ℓ_h−ℓ_{h'}=|ω_{B_h}|_a−|ω_{B_{h'}}|_a`、双方 `0,…,θ` の整数なので結論を得る。∎

**Claude 補題6.3 との関係。** 同一非終端の二つの比較不能節点についての長さ一致はレビューの補題6.3(ii) に含まれている。本定理は、**異なる非終端・同じ骨格符号**を比較し、かつ祖先関係があっても利用できる形にしたもの。レビューの構造を使うが、上では必要な論証を独立に記載した。新規性が文献上の新規性かどうかは未確認。

## 4. 骨格多様性 `M` による条件付き最短長上界

以下、`M(T)` を `T` の**印の無い重い節点**に現れる相異なる `κ(B)` の個数とする。`M(T)≤v`。重要なのは、`M` が単なる非終端数 `v` より小さければ上界が改善される点である。

### 補題4.1（印の無い純粋部分木の長さ）

`U` を `T` の印の無い節点を根とする部分木とし、その全ての節点にも印がないとする。`M_U` をその重い節点の符号種類数とする。このとき

`ℓ(U) ≤ (v+1) θ r^(M_U)`。

**証明。** まず `U` の根から、各節点の子のうち成分総長最大のものを選んで下へ進む。`T` の印の無い部分で同じ非終端 `B` が一つのパスに二度現れたら、上側の `B` 部分木を下側の `B` 部分木に差し替えることにより、全ての固定文字は保持したまま `C[a^{k'}]∈L` (`1≤k'≤k`) を作れる。短くなれば `k` の最小性に、同長なら `T` の節点数最小性に反する。ゆえにこのパスの節点は高々 `v` 個。

選んだパスを葉から上へ読む。葉の総長は高々 `θ`。各親の総長は、規則が直接出力する高々 `θ` 個の文字と高々 `r` 個の子の総長の和だから、`ℓ_parent≤θ+rℓ_child`（選択した最大の子）。重くない親は総長 `≤θ`。

重い親の符号がこのパスですでに**下方に現れた**場合、定理3.1 によりその親の総長と当該下方の節点の総長の差は高々 `θ`。非削除性より下方の節点総長は選択子の総長以下なので、この段階での増加は高々 `θ`。初登場の符号の場合のみ `ℓ_parent≤rℓ_child+θ` を用いる。初登場は高々 `M_U` 回、他の段階は合計高々 `v` 回。加算誤差を全て各乗算の前へ繰り上げれば、根は `(v+1)θ r^(M_U)` 以下。∎

### 定理4.2（`P_a(C)` の条件付き上界）

`k=P_a(C)≥5` とし、`m:=|C|_fix+4`、`H:=v(m+1)^2` とおく。前記最小節点導出 `T` の印の無い重い節点の符号種類数を `M=M(T)` とすると

`P_a(C) ≤ m H θ [1+r(v+1)r^M]`

すなわち

`P_a(C) ≤ m v(m+1)^2 θ [1+r(v+1)r^M]`。   **(4.1)**

**証明。** `T` 内の一節点の**印署名**を、(a) その節点の成分内にある印の識別子の集合、(b) ファンアウト2なら、その集合の印が第1・第2成分のどちらに属するかという順序を保った分割、とする（arity 1 は自明な分割）。固定された印の集合に対し、二成分への順序を保った分割は高々 `m+1` 通りである。

もし一つの祖先・子孫パスで同じ非終端と同じ印署名が再現すれば、上側の部分木を下側に差し替えても、**全ての印の位置と左右の順序、固定文脈 `C` を構成する文字列**がそのまま保たれる。削除され得る印の無い文字は穴の内部の `a` だけである。穴の両端にも印があるので結果は必ず `C[a^{k'}]` (`1≤k'≤k`) となり、`k'<k` は `P_a(C)` の最小性、`k'=k` は節点数の最小性に反する。

任意の根から葉へのパスでは印の集合が包含関係で単調に減る。その集合が厳密に減るのは高々 `m` 回であり、同一集合が続く区間で現れ得る `(非終端,印の分割)` は高々 `v(m+1)` 通り。従って**導出全体の高さ**は `H=v(m+1)^2` 以下。

印付き節点は各印の位置の祖先パスの和集合であるから、その個数は高々 `mH`。根は印付きである。印の無い極大部分木は印付き節点の子として現れるため、その個数は高々 `r mH`。各印付き節点が直接出力する終端文字は高々 `θ`。各印の無い極大部分木の成分総長は補題4.1から `(v+1)θ r^M` 以下。従って

`|C|_fix+k = |W| ≤ mH θ + rmH(v+1)θ r^M`。

`k≤|W|` として (4.1) を得る。∎

### 系4.3（対数骨格多様性なら多項式）

固定ランク `r≥2` について、対象となる最小導出において

`M(T)≤ A log_r(g+θ+2)`

がある固定定数 `A` で成り立ち、かつ `|C|_fix≤θ` とする。このとき

`P_a(C)=O_{r,A}(v² θ (θ+5)^3 (g+θ+2)^A)`。

特に `C=□` なら `μ_a(L)=O_{r,A}(v² θ(g+θ+2)^A)`。**これは無条件の主定理ではなく、骨格多様性の仮定を明記した帰結である。**

### 系4.4（超多項式反例に必要な符号種類数）

固定 `r≥2`、`g_n+θ_n=n^{O(1)}`、`|C_n|_fix≤θ_n` で、`P_a(C_n)=n^{ω(1)}` となる族があれば、最小導出の符号種類数は

`M(T_n)=ω(log n)`。

特に、`μ_a(L_n)=n^{ω(1)}` なら `C_n=□` として同じ結論。定理4.2 の多項式因子は `n^{O(1)}` なので、`r^{M(T_n)}=n^{ω(1)}` が必要である。**短い代替生成組に異なる `a` 骨格が超対数個必要**、という厳密な制約を得る。

## 5. 何がまだ必要か――重み付き符号の残余

定理3.1は同じ骨格の二つの代替を、同じ損失重みへ押し込む。しかし**異なる骨格の重み**の間には依然として制約を与えない。`b,c` を含む骨格が `M=Ω(v)` 種類用意できれば、ランク2の倍増で重み `1,2,4,…` を符号へ割り当てることは、長さ計算の上では可能である。このとき定理4.2は指数上界に留まり、反例を排除しない。

残る本質は、これらの異なる符号を**arity 1 と arity 2 の両方の分布代入可能性の下で共存**させられるか、である。隙間合流（レビュー補題3.4）は符号のつながった骨格を新たに作り、共役移送（レビュー補題3.5）は、同じ重みを保つだけでは避けられない配置替えを強制する。さらに一穴型 `P_a(C)` で内容 `{a}` の代表が必要な場合、外から挿入された `b,c` を単に消すことは一般には許されない。

レビューの `L_○=(a|bc)^+` は、隙間合流後の語が依然受理される例であり、「二文字なら合流即矛盾」という論法が三文字には移らないことを示す。ただしこの言語は `a∈L_○` なので `μ_a=1` であり、主問題の反例ではない。

上界を無条件にするには、例えば**長い純粋語の最小導出に現れる異なる `κ(B)` の種類数が `O(log(g+θ))`** と示す必要がある。本報告ではそれを示せなかった。`κ(B)` の個数は自明には `v` 個まであり、`v=O(g)` は目標には足りない。

## 6. 有限全数検査と倍増候補

付録Aのコードは、有限言語の**全語**からすべての非空一穴／非空二穴（穴の間は正長）の組出現を挙げる。その分布の共通部分と内容型が等しい組の全てに対し、他方の受理文脈でも受理されることを検査する。有限言語の場合、受理分布の全てはその有限言語の語内に現れるため、違反がないことは当該有限言語の代入可能性の証明となる。無限言語の指定長以下の検査では、違反がなければ**観察に過ぎない**。

`K_n` は `E_0→a`, `E_i→bE_{i−1}E_{i−1}b | cE_{i−1}c` の有限言語。`n=1`（2語）、`n=2`（6語）では `(2,c)` 違反なし、`n=3`（42語）では arity 2 の具体的違反を検出した。レビュー §2 の無限族に対する明示的な違反構成と整合する。

検討候補を、`E_0→a`、`E_i→E_{i−1}E_{i−1} | d_i`（`d_i∈{b,c}^+`）とした。各規則は good・rank 2・fanout 1（したがって fanout ≤2）で、文法サイズは符号長総和に線形、通常厚さは短い `d_i` を使って小さくでき、純粋 `a` の語は `a^(2^n)` の一つだけである。しかし例えば `d_1=b,d_2=c,d_3=bc` では、`n=2` は `(2,c)` 違反なしでも、`n=3` は arity 1 で違反する。共通文脈 `(ε,c)` の下で `b` と `bb` が両方受理されるのに、分離文脈 `(ε,a^6)` では `ba^6` が受理され `bba^6` は受理されない。この一例は**候補族の反証**であり、全ての符号族を排除する証明ではない。

符号 `bc,cb` 等も付録Aで検査し、小さい `n` で arity 1 の違反を得た。`(a|bc)^+` は長さ7まで違反が出なかったが、これは無限言語の有限観察に過ぎない（この正則言語についての一般の証明は参照レビュー命題4.1にある）。

## 7. 先行研究・下界の作用素と適用条件

- **代入可能性の原典**：Clark–Eyraud (2007), *Polynomial Identification in the Limit of Substitutable Context-free Languages*, JMLR 8:1725–1745。MCFG の多次元代入可能性は Yoshinaka (2011), *Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*, *Theoretical Computer Science* 412(19):1821–1831, DOI `10.1016/j.tcs.2010.12.058`。新しい骨格剛性の同型結果の有無は**未確認**。
- **既存の三文字資料**：上記 Claude 報告の補題3.1（再配分）、3.3（境界の交換）、3.4（隙間合流）、3.5（共役移送）、6.3（剛性）。本報告は同じ骨格に関する剛性を異なる非終端に拡張し、個数 `M` を導入して一穴文脈の最短長を条件付きで抑える。
- **負の結論がもし得られた場合に必要な量化**：固定アルファベット `Σ={a,b,c}`、内容型付け `c_Σ`、ファンアウト `≤2`、ランク `≤r`（`r≥2` 固定）、`g_n,θ_n=n^{O(1)}`、`μ_a(L_n)=n^{ω(1)}` を満たす reduced good な表示を備える `L_n∈C_{2,c}`。この場合 `prop:rare-type` により、**`B^{≤r}_{2,c}` と `B_{2,c}` の特徴標本**、さらに **`C_{2,c}` 全体に特徴標本を持つ任意の集合駆動作用素**の `L_n` に対する特徴標本に、長さ少なくとも `μ_a(L_n)+1` の寄与が必要となる。これは**任意の Gold 逐次学習器の計算時間や収束時点の下界ではない**。
- **現時点の帰結**：本報告はこのような下界族を構成していない。したがって `prop:sl-reduction` を用いても、ファンアウト2における擬多様体の境界に関する肯定・否定のいずれも確定しない。

## 8. 最終判定と次の厳密な問い

**Q は未解決。** 本報告で証明したのは `a^k`／`C[a^k]` の最小導出に現れる短い代替生成組の**骨格種類数に条件を付けた多項式上界**である。証明の止まった箇所は定理4.2の `r^M` を除去する段階。具体的には「三文字における隙間合流と共役移送が、`M=ω(log(g+θ))` となる重み付き符号系を禁止するか」が残っている。

次に証明または反証すべき小問題を明示する：

> **骨格多様性問題：** `Σ={a,b,c}`、`L∈C_{2,c}`、reduced good `G`、`θ̄_G=θ` について、`P_a(C)` の最小節点導出中の、穴の内側の印の無い重い節点に対して短い代替生成組を適切に選んだとき、その相異なる `a` 骨格符号 `κ(B)` の個数を `O_r(log(g+θ))` にできるか。

この小問題の肯定は**本報告の定理4.2を介して**一文字語と `|C|_fix≤θ` の一穴型の多項式短縮を与える。他方、否定だけでは `μ_a` の超多項式性を直ちには与えない。いずれの場合も、二穴型や三文字の全内容型の代表長まで直結するとは主張しない。

---

## 付録A：Python 3 標準ライブラリだけによる検査（全文）

保存名例：`pure_letter_fanout2_check.py`。Windows：`py -3 pure_letter_fanout2_check.py`。この付録の検査には MCFG 決定手続そのものは含めない。`check_finite` は**与えられた有限言語の全語が列挙されているときだけ**全数検査である。

```python
#!/usr/bin/env python3
"""Exact finite (1,c) and (2,c) substitution tests, plus bounded tests.
Run on Windows: py -3 pure_letter_fanout2_check.py
Python standard library only.  Empty tuple components are forbidden and
between the two holes there must be at least one fixed letter.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product


def contexts_in_word(w, arity):
    n = len(w)
    if arity == 1:
        for i in range(n):
            for j in range(i+1, n+1):
                yield (w[i:j],), (w[:i], w[j:])
    elif arity == 2:
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):  # a nonempty inter-hole separator
                    for h in range(k+1, n+1):
                        yield (w[i:j], w[k:h]), (w[:i], w[j:k], w[h:])
    else:
        raise ValueError("arity must be 1 or 2")


def plug(context, pair):
    if len(pair) == 1:
        return context[0] + pair[0] + context[1]
    return context[0] + pair[0] + context[1] + pair[1] + context[2]


def check_from_positive_words(positive_words, belongs, arities=(1,2)):
    """Return an exact substitution counterexample, or None.

    If positive_words lists ALL words of a finite language, None is a proof.
    With a truncated infinite language, None is only a finite observation.
    Every reported witness is genuine if 'belongs' is exact.
    """
    for d in arities:
        distributions = defaultdict(set)
        for w in sorted(set(positive_words)):
            for p, ctx in contexts_in_word(w, d):
                distributions[p].add(ctx)
        by_type_context = defaultdict(list)
        for p, cs in distributions.items():
            typ = tuple(frozenset(t) for t in p)
            for ctx in cs:
                by_type_context[(typ, ctx)].append(p)
        tested = set()
        for (typ, common), words in by_type_context.items():
            words = sorted(set(words))
            if len(words) < 2:
                continue
            for i, p in enumerate(words):
                for q in words[i+1:]:
                    if (p, q) in tested:
                        continue
                    tested.add((p,q))
                    for left, right in ((p,q),(q,p)):
                        for ctx in sorted(distributions[left]):
                            rejected = plug(ctx,right)
                            if not belongs(rejected):
                                return {"arity":d, "x":left, "y":right,
                                        "common":common, "separating":ctx,
                                        "accepted":plug(ctx,left),
                                        "rejected":rejected}
    return None


def check_finite(words):
    words = set(words)
    return check_from_positive_words(words, words.__contains__)


def grammar_finite(n, codes):
    """E_0 -> a; E_i -> E_{i-1} E_{i-1} | codes[i-1]."""
    curr = {"a"}
    for i in range(n):
        curr = {u+v for u in curr for v in curr} | {codes[i]}
    return curr


def K(n):
    curr = {"a"}
    for _ in range(n):
        curr = {"b"+u+v+"b" for u in curr for v in curr} | {"c"+u+"c" for u in curr}
    return curr


def bounded_predicate_test(predicate, length_cap=7, alphabet="abc"):
    accepted = ["".join(s) for n in range(1,length_cap+1)
                for s in product(alphabet, repeat=n)
                if predicate("".join(s))]
    return check_from_positive_words(accepted,predicate)


def main():
    print("FINITE K_n (complete language enumeration):")
    for n in (1,2,3):
        words = K(n)
        witness = check_finite(words)
        print("n", n, "|L|", len(words), "(2,c) witness:", witness)
    print("\nFINITE typed-thickness-friendly doubling candidates:")
    code_sets = [
        ("b","c","bc"),
        ("bc","cb","bcb"),
        ("bc","bcb","cbc"),
        ("bc","bcc","bbc"),
    ]
    for codes in code_sets:
        for n in (2,3):
            words = grammar_finite(n,codes)
            hit = check_finite(words)
            print("codes", codes[:n], "n",n,"|L|",len(words),
                  "mu_a",2**n,"violation",hit)
    print("\nBOUNDED infinite regular candidate (a|bc)^+:")
    import re
    pat = re.compile(r"(?:a|bc)+\Z")
    hit = bounded_predicate_test(lambda w: pat.fullmatch(w) is not None,7)
    print("length<=7:", hit if hit else "no violation (observation only)")

if __name__ == "__main__":
    main()
```

### 実行結果（この環境で Python 3 を実行）

```text
FINITE K_n (complete language enumeration):
n 1 |L| 2 (2,c) witness: None
n 2 |L| 6 (2,c) witness: None
n 3 |L| 42 (2,c) witness: {'arity': 2, 'x': ('b', 'baab'), 'y': ('bb', 'aab'), 'common': ('', 'b', 'baabbcbaabcb'), 'separating': ('', 'bbaab', 'bbbaabbaabbb'), 'accepted': 'bbbaabbaabbbbaabbaabbb', 'rejected': 'bbbbaabaabbbbaabbaabbb'}

FINITE typed-thickness-friendly doubling candidates:
codes ('b', 'c') n 2 |L| 5 mu_a 4 violation None
codes ('b', 'c', 'bc') n 3 |L| 26 mu_a 8 violation {'arity': 1, 'x': ('b',), 'y': ('bb',), 'common': ('', 'c'), 'separating': ('', 'aaaaaa'), 'accepted': 'baaaaaa', 'rejected': 'bbaaaaaa'}
codes ('bc', 'cb') n 2 |L| 5 mu_a 4 violation {'arity': 1, 'x': ('cb',), 'y': ('bcbc',), 'common': ('', ''), 'separating': ('b', 'c'), 'accepted': 'bcbc', 'rejected': 'bbcbcc'}
codes ('bc', 'cb', 'bcb') n 3 |L| 26 mu_a 8 violation {'arity': 1, 'x': ('aaaabc',), 'y': ('cbaa',), 'common': ('', 'bc'), 'separating': ('aa', ''), 'accepted': 'aaaaaabc', 'rejected': 'aacbaa'}
codes ('bc', 'bcb') n 2 |L| 5 mu_a 4 violation {'arity': 1, 'x': ('bcb',), 'y': ('bcbc',), 'common': ('', ''), 'separating': ('', 'c'), 'accepted': 'bcbc', 'rejected': 'bcbcc'}
codes ('bc', 'bcb', 'cbc') n 3 |L| 26 mu_a 8 violation {'arity': 1, 'x': ('aaaabcb',), 'y': ('aaaaaabc',), 'common': ('', ''), 'separating': ('', 'c'), 'accepted': 'aaaabcbc', 'rejected': 'aaaaaabcc'}
codes ('bc', 'bcc') n 2 |L| 5 mu_a 4 violation {'arity': 1, 'x': ('bc',), 'y': ('bcb',), 'common': ('', 'c'), 'separating': ('', 'aa'), 'accepted': 'bcaa', 'rejected': 'bcbaa'}
codes ('bc', 'bcc', 'bbc') n 3 |L| 26 mu_a 8 violation {'arity': 1, 'x': ('aaaabc',), 'y': ('aabcaa',), 'common': ('', 'aa'), 'separating': ('', 'c'), 'accepted': 'aaaabcc', 'rejected': 'aabcaac'}

BOUNDED infinite regular candidate (a|bc)^+:
length<=7: no violation (observation only)
```

`None` はその検査範囲で違反を発見しなかったことを表す。有限 `K_n` や `grammar_finite` の場合のみ、これを全数検査による肯定と解釈できる。出力中の `x,y,common,separating,accepted,rejected` は、同じ内容の二組を共有文脈で受理しながら別文脈で片方だけ拒否する、検査可能な具体的証明書である。
