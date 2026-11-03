# `a` の個数スペクトルと fan-out 2 の未解決問題：補題Sの検証、局所周期の限界、唯一冪語の随伴語

**研究日**：2026-11-03  
**対象**：栗山貴之 #2 `02-v2-lg-fanout-boundary/main.tex`、`op:fanout-two`、`Σ={a,b,c}`、内容型付け `c`。  
**主結論**：**補題Sは正しい**。その上で「局所周期＝全体の可換群不変量」という推論に対する明示的反例を得た。ただし、(α) と (β) のいずれについても `μ_a(L)≤poly(‖G‖,θ̄_G)` の一般証明も、仮定を満たす超多項式の反例族も得られていない。

## 0. 主張別の判定表

| 主張 | 判定 | 根拠 |
|---|---|---|
| 補題S (i)–(iii)：`Δ=∅` または `Δ=gℤ_{>0}` (`g≥k`)、各 `N_σ=n_σ+gℤ_{≥0}` | **証明済み** | §2 |
| **補強**：`Δ≠∅` と純粋 `a` 語が二つ以上あることは同値。さらに `ρ_a(σ)≤n_σ≤ρ_a(σ)+g−1`。`g` は `a` と `a^{1+δ}` の最小の正の分布周期 | **証明済み** | §3 |
| `Δ≠∅` は言語全体に `|w|_a (mod g)` が一定という意味ではない。`g=7` でも言語の `a` 個数差全体の gcd を `1` にできる | **反証例を構成** | §4 |
| 系Sの「不足の加法性」：適切な短縮反鎖 `J` では `k−∑w_h=n_{κ_J}`。実は **(α) と (β) の双方**で成立する | **証明済み（条件を明記）** | §5 |
| (β) で `k>θ̄_G` なら、ある成功語は `b,c` を合計 `k/((r+1)|V|θ̄_G)` 個以上含む | **証明済み**（原稿 `lem:unique-word-gap(ii)` の独立再確認） | §6 |
| `|G_n|,θ̄_{G_n}=O(n)` かつ唯一の純粋 `a` 語が `a^{2^n}` となる縮約的 CFG 候補は、ファンアウト2どころか arity 1 で失敗する | **反証** | §7 |
| 有限言語 `{a^5}`、`(a\|bc)^5` は `(1,c),(2,c)` を満たし、`Δ=∅`。上記縮約的候補は失敗する | **有限全数検査** | §8・付録 |
| (α) で `μ_a(L)=poly(‖G‖,θ̄_G)` または条件を満たす超多項式族 | **未解決** | §9 |
| (β) で同じ結論 | **未解決** | §9 |
| `op:fanout-two` の否定、全作用素に対する新しい超多項式特徴データ下界 | **未達成** | §10 |
| 本報告中の新しい構造観察の文献上の新規性 | **未確認** | §11 |

## 1. 正本、厳密な前提、照合した範囲

参照した公開正本は [現行 `main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex) であり、依頼に列挙された [Claude の三文字報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_ternary_content_2026-11-01.md)、[ChatGPT 純粋文字報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_pure_letter_fanout2_2026-11-02.md)、[ChatGPT 重み付き符号報告](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_weighted_codes_2026-11-02.md) を照合した。数学的に使用する移送は以下で独立に証明する。既往報告の他の補題を未証明の公理として使わない。原稿の `def:tuple-substitutable`、`def:grammar-properties`、`lem:thickness-equivalence`、`lem:no-insertion`、`prop:rare-type`、`lem:unique-word-gap`、`prop:abelian-filter-short`、`op:fanout-two` を確認した。

`c(w)` は非空語 `w` の文字集合。`L∈𝒞_{2,c}` は、**arity 1 と arity 2 の双方**に対し、非空成分の内容型が成分ごとに一致し、受理する許容文脈を共有する二組の全受理文脈が一致する、ファンアウト `≤2` の MCFL を指す。arity 2 の許容文脈は `u □₁ v □₂ z`、`v∈Σ⁺`。任意の一穴分布を `D_L(x)` とする。

`G` は `L∩Σ⁺` の reduced good 文法、fan-out `≤2`、rank `≤r`、`θ=θ̄_G≥1`、`v=|V|`、`s=‖G‖` とする。good は λ-free、nondeleting、nonpermuting、nonmerging。`k=μ_a(L)=min{j≥1:a^j∈L}` は存在するとし、`k≥5` を主に扱う。このとき `a⁴` は `L` の語の因子として現れる。

`σ_a(w)` は極大 `a` ランを一文字に縮約したもの。`a` を含む実現骨格 `σ` に対し `N_σ={|w|_a:w∈L, σ_a(w)=σ}`、`ρ(σ)` はその `a` ラン数、`Δ={n'−n>0:∃σ, n,n'∈N_σ}`。`ℕ₀={0,1,2,…}` と書く。

## 2. 補題S：独立の証明

### 2.1 二穴の一単位移送

**補題2.1**。`L` のある語が `a⁴` を因子に持つなら、`a` 骨格と `a` の総個数が同じ二語の所属は一致する。

**証明**。`p a⁴ q∈L` を取る。`X=(a,aa)`、`Y=(aa,a)` は成分ごとに内容 `{a}` が一致する。許容文脈 `E=p □₁ a □₂ q` において `E[X]=E[Y]=pa⁴q∈L` だから、arity 2 の仮定により両組の分布は等しい。したがって、異なる二つの極大 `a` ランを非空の非 `a` 因子 `z` が隔てているとき、`a^p z a^q` の間で一文字を移動する操作 `(p,q)↔(p−1,q+1)` (`p≥2, q≥1`) は任意の左右文脈中で所属を保存する。`a` ランの長さの正整数組成はこの操作で連結されている。`a` ランが一つの場合はその長さは総数で一意である。□

### 2.2 同一骨格の差から一穴分布等式へ

**補題2.2**。`n,n+δ∈N_σ` (`δ>0`) なら

\[
D_L(a)=D_L(a^{1+δ}).\tag{2.1}
\]

**証明**。補題2.1により、骨格 `σ` の第2ラン以降の長さをすべて1にしたまま、第1ランに余剰の `a` を集中できる。二つの受理語の第1ラン長は `p` と `p+δ` (`p≥1`)、他の部分は同一である。第1ランの先頭 `a^{p−1}` を固定文脈に吸収して二語を `U a V`、`U a^{1+δ} V` と書ける。内容型がともに `{a}` で、共通する受理文脈 `U □ V` が存在するため、arity 1 の代入可能性から (2.1)。□

**補題2.3（全骨格に共通の増減）**。`δ∈Δ` なら、任意の実現骨格 `σ`、任意の `n∈N_σ` について `n+δ∈N_σ`。さらに `n≥ρ(σ)+δ` なら `n−δ∈N_σ`。

**証明**。`σ` を持つ語には必ず `a` がある。(2.1) により、その一つの `a` を `a^{1+δ}` に取り替えれば `+δ` ができる。後半では補題2.1により `a` の余剰を一つのランに集め、そのランを `1+δ` 以上にした後、(2.1)を逆向きに使い `δ` 個縮める。ランは正長のままなので骨格は保たれる。□

### 2.3 スペクトルの定理

**定理S**。依頼文の補題S (i)–(iii) が成立する。

**証明**。(i) `δ∈Δ` に `0<δ<k` を仮定する。(2.1) から、`a^k=a^{k−δ−1}a^{1+δ}` の部分を `a` に置換できる。すると `a^{k−δ}∈L`、最小性に矛盾。従って `δ≥k`。

(ii) 補題2.3により `Δ` は加法で閉じる。さらに `δ>δ'` が共に `Δ` にあれば、任意の実現骨格 `σ` の最小値 `n_σ≥ρ(σ)` から `n_σ+δ∈N_σ` とできる。この値は `ρ(σ)+δ'` より大きいので、補題2.3の減算を用いて `n_σ+δ−δ'∈N_σ`。従って `δ−δ'∈Δ`。非空の正整数集合が加法と正の差に閉じるなら、最小元 `g` でユークリッド除法を繰り返すことで、ちょうど `gℤ_{>0}` である。(i) から `g≥k`。

(iii) `n_σ+g j∈N_σ` は補題2.3による。一方 `n∈N_σ` が `n>n_σ` なら `n−n_σ∈Δ=gℤ_{>0}` なので、他の値は無い。`σ=a` の最小値は `k` だから、純粋 `a` 語は正確に `{a^{k+jg}:j∈ℕ₀}`。`Δ=∅` なら、どの `N_σ` も二点を含められず一点である。□

**確認点**：二つの差 `δ,δ'` が**異なる骨格**から得られていても、補題2.3で両方を任意の一つの骨格に移して引き算できる。ここを省くと「Δが正の差で閉じる」は証明にならない。上の証明はその点を明示した。

## 3. 補強結果：周期の特徴付けと最小個数の幅

**命題3.1（より強い二分法）**。上記の前提で次が成り立つ。

1. `Δ≠∅` と `L∩a⁺` に相異なる二語があることは同値。従って **有限言語は必ず (β)**。逆に `(α)` は必ず無限言語。
2. `(α)` の周期 `g` は
   \[
   g=\min\{δ≥1:D_L(a)=D_L(a^{1+δ})\};\tag{3.1}
   \]
   最小の正の**一穴分布周期**である。
3. `(α)` では全ての実現骨格 `σ` について
   \[
   \rho(σ)\le n_σ\le \rho(σ)+g-1.\tag{3.2}
   \]

**証明**。(1) `Δ≠∅` なら定理S(iii)により `a^k,a^{k+g}∈L`。逆向きは `σ=a` で二点があれば定義から従う。(2) `δ∈Δ` なら補題2.2で分布等式。一方、分布等式が任意の `δ≥1` について成立すれば `a^k` 中の `a` を `a^{1+δ}` に変えて `a^{k+δ}∈L`、ゆえに `δ∈Δ`。従って等式を満たす正整数の集合は `Δ=gℤ_{>0}`。(3) `n_σ≥ρ(σ)` は各ランが非空だから。もし `n_σ≥ρ(σ)+g` なら補題2.3で `n_σ−g∈N_σ` となって最小性に反する。□

この上界は `n_σ` を **ラン数 `ρ(σ)` と周期 `g` で**抑えたものであり、`g` 自体や `k` を文法サイズ・厚さで抑えたわけではない。また `(β)` は言語の有限性を意味しない。例えば `{a^k}∪b⁺` は無限・正則・全arityで内容代入可能であり、`Δ=∅` である（§4 の同じ一文字分岐の議論を参照）。

## 4. (α) の重要な障害：スペクトルの `mod g` は全体の可換群不変量ではない

**命題4.1（周期と global Parikh-gcd の乖離）**。`1≤k≤g` とし

\[
U_{k,g}=\{a^{k+jg}:j≥0\},\qquad L_{k,g}=U_{k,g}\cup\{b\}\subseteq\{a,b,c\}^*.
\]

この言語は正則で、任意の `f≥1` について `(f,c)`-tuple-substitutable である。`μ_a(L_{k,g})=k`、`Δ=gℤ_{>0}` である。しかし `gcd(k,g)=1` なら、言語全体の `a` 個数の差が生成する加法部分群は **`ℤ` 全体**であって `gℤ` ではない。特に `k=5,g=7` は `k≥5` での明示例となる。

**証明**。`U_{k,g}` の任意の非空 `d`-成分組は純粋な `a` の組であり、全成分長の和を `p` とする。二組 `X,Y` が共通の受理文脈を持つなら、その文脈にも `a` しか現れず、固定部分の長さを `t` として `p+t,q+t∈k+gℕ₀`。よって `p≡q (mod g)`。任意の別の許容文脈が純粋な `a` からなり、その固定部分長を `t'` とすると、`p+t'` と `q+t'` はともに正整数で合同である。`1≤k≤g` より、**正の整数で `k (mod g)` に合同であることと `k+gℕ₀` に属することは同値**。従って両組は全ての許容文脈で同時に受理される。文脈に他の文字があれば双方とも不受理。

`{b}` から観察できるのは一穴組 `(b)` だけで、純粋な `a` の組と内容型が異なる。`a` と `b` の混合を含む受理語は無いので、混合組の分布は空。したがって和集合 `L_{k,g}` でも全arityで代入可能性が成り立つ。言語は正則だから任意の `f≥1` で `f`-MCFL でもある。

実現する `a` 骨格は `σ=a` だけで、`N_a=k+gℕ₀`。ゆえに `Δ=gℤ_{>0}`。一方、言語の `a` 個数には `0` (`b`) と `k`、`k+g` があり、これらの差の gcd は `gcd(k,g)`。`k=5,g=7` なら 1。□

**意義と制限**：`g` は `a` ランの**同一骨格内**の周期であり、`|w|_a≡const (mod g)` を言語全体で主張することはできない。そのため、原稿 `prop:abelian-filter-short` の規則差 `δ_R` に**機械的に** `mod g` を課して `g≤poly(s,θ)` を示す論法は成立しない。あの命題は全言語の Parikh 差が一つの有限アーベル群の部分群に入る**global な**条件を検出するものである。

同様に `(β)` の `{a^5}` と `(a\|bc)^5` は `Δ=∅` を共有するが、後者の言語全体の `a` 個数は `0,1,…,5` を取る。「骨格差が無い」ことと「Parikh 差が無い」ことも別である。

## 5. 系Sの精密化：不足は両場合で加法的

`a^k` の節点数最小の成功導出 `T` を一つ取り、最初と最後に保護された `a` の位置を印とする（既往の純粋文字報告の手順では先頭末尾各2位置）。非終端 `B_h` の節点 `h` が印を含まず、全成分の元の総長を `ℓ_h` とする。各非終端について `‖ω_B‖₁≤θ` の生成組を固定し、`ℓ_h>θ` の節点を「重い」と呼ぶ。`h` は純粋 `a` の位置のみを占めるので、元の `a` 個数は `ℓ_h` である。`w_h:=ℓ_h−|ω_{B_h}|_a>0`。

**命題5.1**。印の無い重い節点の任意の非空反鎖 `J` を同時に `ω_{B_h}` へ差し替えて得る語を `W_J`、その骨格を `κ_J` とする。印の配置により少なくとも一つの `a` が残るとき、

\[
1\le |W_J|_a=k-\sum_{h\in J}w_h<k,
\qquad |W_J|_a=n_{κ_J},\qquad
k-n_{κ_J}=\sum_{h\in J}w_h.\tag{5.1}
\]

これは **(α)・(β) の双方**で成立する。特に `κ_J=κ_{J'}` なら `∑_{h∈J}w_h=∑_{h∈J'}w_h` である。

**証明**。good 文法の非削除性から、相異なる反鎖節点の全成分は根の語の互いに重ならない位置に出力される。従って同時置換の `a` 個数減少は `∑w_h` に等しく、成功導出のままである。印のある `a` を消さないから結果の `a` 個数は正。`J` が非空で各重みは正だから `k` 未満。`W_J` より小さい同骨格の受理語 `W'` があったなら、`0<|W_J|_a−|W'|_a<k` は `Δ` に入って定理S(i)に反する。従って `|W_J|_a=n_{κ_J}`。残りは算術的に従う。□

**注意**：「骨格に対する不足 `e_κ=k−n_κ`」の加法性は、**同じ最短導出 `T` における、同時に差し替え可能な反鎖 `J` が実現した骨格**に限る。任意の抽象骨格を自由に乗算できるとか、異なる導出にまたがって骨格が加法群をなす、という主張ではない。実際、この命題に必要なのは定理S(i)だけであり、非空の周期 `g` は必要ない。この意味で、系Sは正しいが `(α)` 固有の強化ではない。

## 6. (β) の必要条件：指数的 `a` 語には長い非 `a` 随伴語が必要

`Δ=∅` の場合は、定理Sにより `a^k` が `L` の唯一の純粋 `a` 語である。これを使うと以下の原稿の結論を独立に確認できる。

**命題6.1（`lem:unique-word-gap(ii)` の再証明）**。`k>θ` なら、ある `W∈L(G)` が存在し、

\[
|W|_b+|W|_c\ \ge\ \frac{k}{(r+1)v\,θ}.\tag{6.1}
\]

**証明**。`a^k` の節点数最小導出 `T` の一本の根から葉への経路上で、同じ非終端が二回現れることはできない。現れれば、上位部分木を下位の同名非終端の部分木で置き換えられ、全体はなお純粋な `a` 語となる。唯一性から再び `a^k` となるが節点数が減り、最小性と矛盾する。ゆえに `T` の高さは高々 `v`。

節点の生成組総長が `θ` を超えるとき「重い」とする。原稿の厚さ補題から各規則が直接書く終端数は高々 `θ`。重い節点の直下の軽い各子の総出力長も `θ` 以下、子は高々 `r` 個。従って全体の `k` 文字を負担する重い節点は少なくとも `k/((r+1)θ)` 個ある。深さは高々 `v` だから、ある深さには少なくとも `k/((r+1)vθ)` 個の重い節点があり、互いに反鎖である。各節点 `h` を `‖ω_{B_h}‖₁≤θ` の生成組へ置き換える。その生成組が純粋 `a` なら、元の `a` だけの生成組（長さ `>θ`）より短いので、全体に `a^j∈L` (`1≤j<k`) を生成してしまう。したがって各 `ω_{B_h}` は少なくとも一つ `b` または `c` を含む。全てを同時置換すると、非削除性により別々の `b,c` が根に残り、(6.1)。□

**帰結**：固定ランク `r` に対し `s=‖G‖`、`θ` がともに `poly(n)` で `k` が超多項式なら、`b,c` が超多項式個ある受理語を同時に含まなければならない。単に `a^k` を圧縮文法で作り、他の受理語を短く少数加えるだけでは反例にならない。しかし、この随伴語の存在は `k` の多項式上界を与えない。

## 7. (β) に対する自然な指数候補と一般的な失敗証明

**候補**：非終端 `A_0,…,A_n`（開始 `A_n`）、全てファンアウト1、規則ランク高々2とし、

```text
A_0 -> a | bc
A_i -> A_(i-1) A_(i-1) | bc       (1 <= i <= n)
```

これは有限の reduced good CFG。`‖G_n‖=O(n)`、`θ̄_{G_n}=O(n)`（実際、直接出力した終端と、ある規則まで至る各先祖の最小生成兄弟を数えれば `θ̄_{G_n}≤2n+2`）。唯一の純粋 `a` 語は `a^{2^n}` で、`μ_a=2^n`。したがって **もし** `(2,c)`-代入可能なら求める否定例になる。しかし以下で一律に失敗する。

**命題7.1（失敗）**。全 `n≥1` について `L(G_n)` は **arity 1 で**内容代入可能でない。

**証明**。どの `n≥1` でも根の規則 `A_n→bc` から `bc∈L(G_n)`、規則 `A_n→A_{n−1}A_{n−1}` と各子の `bc` 生成から `bcbc∈L(G_n)`。`x=bc`、`y=bcbc` は同じ内容 `{b,c}` で、一穴文脈 `□` で共に受理される。arity 1 の仮定なら `D(x)=D(y)`。すると `bc`, `bcbc`, `bcbcbc`, … が帰納的に全て受理される。しかし `G_n` は非再帰的な有限文法なので生成言語は有限。矛盾する（原稿 `lem:no-insertion` のこの場合を直接証明した）。□

`n=1` の最小証明書は `x=bc, y=bcbc`、共通文脈 `E=□`、相違文脈 `F=□bc`：`F[x]=bcbc∈L(G_1)`、`F[y]=bcbcbc∉L(G_1)`。有限言語の全数検査でも確認した。**この候補は結果的に `𝒞_{2,c}` に属さないため下界の構成ではない**。

## 8. 有限計算と正確な読み方

付録の Python 3 スクリプトは、**入力が有限言語の全要素の列挙**である場合に限り `(1,c)`、`(2,c)` の全非空成分・全許容出現文脈を列挙し、相違文脈を返す。`Δ` の算出も同じ有限集合を対象とする。`(a|bc)^5` は全32語、`G_1` は全5語、`G_2` は全24語を対象にした。

```text
singleton a^5 size= 1 pure= [5] Delta= []
  substitutability: PASS certificate= None
(a|bc)^5 size= 32 pure= [5] Delta= []
  substitutability: PASS certificate= None
compressed G1 size= 5 pure= [2] Delta= []
  substitutability: FAIL certificate= (1, ('bc',), ('bcbc',), ('', ''), ('', 'bc'), 'bcbc', 'bcbcbc')
compressed G2 size= 24 pure= [4] Delta= [1]
  substitutability: FAIL certificate= (1, ('a',), ('aa',), ('', 'abc'), ('bcbc', 'bc'), 'bcbcabc', 'bcbcaabc')
Note: finite samples of infinite L_{k,g} are NOT tested as whole languages.
```

`G_2` に `Δ={1}` が出ることは**定理Sとの矛盾ではない**：代入可能性が失敗しているため、定理Sの仮定から外れる。`L_{5,7}` など無限言語の所属は付録の有限試験ではなく、§4の一般の証明による。

## 9. 二つの場合で止まった正確な地点

### (α) `Δ=gℤ_{>0}`

定理Sは `a^{k+jg}∈L` を強制し、`g≥k` と、全骨格の最小 `a` 個数に対する (3.2) を与えた。一方、§4 は **全受理語の `a` 個数 modulo `g` を規則差に落とす操作が一般には正当化できない**ことを示す。従って原稿 `prop:abelian-filter-short` のアーベル群法では、さらに「骨格変更に対する剰余の伝播」またはそれに代わる局所的な規則差制約が必要である。

未証明なのは、`g`（または `k`）が短い mixed-content 導出の間接作用により多項式以下に抑えられるという、**文法と骨格間をまたぐ**部分である。`a^{k+g}` の導出から周期 `g` の一部だけを再現できる小さな導出変更を常に見つけられるかは未証明。逆に、`g` が超多項式でありながら `θ,s` が多項式の対象言語族も構成できていない。

### (β) `Δ=∅`

純粋 `a` 語の唯一性が成立する。§6 から `k` が大きければ大量の `b,c` を含む随伴語が必要。§5 から同一骨格に落ちる短縮反鎖の総不足は一致しなければならない。しかし相異なる短縮骨格が無制限に多くなる可能性を排除できない。§7 は、文法サイズと厚さを小さくするために `bc` の短い枝を加える最も単純な案を arity 1 で排除するが、**全ての符号化案を排除していない**。

### 次に絞る一点

`a^k` の最小導出で、多数の重い反鎖節点の短い代替が作る **`b,c` を含む骨格 `κ_J` の実現可能性**を、同一の `b,c` 配置を共有する **二つの異なる反鎖**に結びつける。その際に、§5 の等式 `e_{κ_J}=∑w_h` と、(α) なら `+g` の作用を、**一穴ないし非空区切りを持つ二穴の実際の共通受理文脈**で接続する必要がある。

具体的な証明課題は次のどちらかである：同じ骨格 `κ` を作る二つの反鎖で `0<|∑_{J}w_h−∑_{J'}w_h|<k` を強制するか、そうした衝突を防ぐ全ての骨格符号が、短い受理語中に同じ内容の proper factor を作って `lem:no-insertion` に反することを示す。これが出来なければ、矛盾を避ける実現可能な多層符号を記述し、反例に用いる。

## 10. 特徴標本、作用素、fan-out とランクの射程

本報告には **`L_n∈𝒞_{2,c}`、`Σ={a,b,c}`、reduced good、fan-out `≤2`、rank `≤2`、`‖G_n‖,θ̄_{G_n}=poly(n)`、`μ_a(L_n)=n^{ω(1)}`** を同時に満たす族はない。従って `prop:rare-type` からの新しい超多項式／指数特徴標本下界は示していない。これは以下のすべてに共通する：

- ランク `≤r` の標準集合駆動作用素 `𝓑^{≤r}_{2,c}`（特に `r=2`）。
- ランクを限定しない作用素 `𝓑_{2,c}`。
- `𝒞_{2,c}` **全体**について特徴標本を持つ任意の集合駆動作用素。

原稿 `prop:rare-type` は、同じ内容型の語が一つだけである場合に限らず、その型の任意の語が長い場合に下界を与える。一方、本報告の `μ_a` は、型 `{a}` の最短語長であり、**言語全体の特徴標本総符号長の多項式上界を証明する量ではない**。`op:fanout-two` は三文字の純 `a` 語だけでは解決しない。ファンアウトの境界が移動したという結論も出していない。

## 11. 既知性の監査と関連文献

- R. Yoshinaka, *Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*, **Theoretical Computer Science 412(19)** (2011), pp. 1821–1831, DOI [10.1016/j.tcs.2010.12.058](https://doi.org/10.1016/j.tcs.2010.12.058)。多次元代入可能性と学習法の直接の先行研究。
- 栗山論文の `main.tex`：`lem:thickness-equivalence`、`lem:no-insertion`、`lem:unique-word-gap(ii)`、`prop:abelian-filter-short`、`op:fanout-two`。§6 の命題は**原稿既出**であり、新規結果とは呼ばない。
- Claude 2026-11-01 三文字報告：`a` ラン再配分と個数漏れの先行する本研究内証明。§2は使用範囲について独立に再証明。
- ChatGPT 2026-11-02 重み付き符号報告：単一の非負加法重みレベルに対する上界 `μ_a≤(r+1)^2 θ^3` を報告しているが、**今回の一般 (α)/(β) にその仮定が自動的に成り立つわけではない**ので使用していない。

§3 の分布周期の特徴付け、§4 の local/global 乖離例、§5 の修正版と数値計算の組み合わせが文献上初出であるかは**未確認**。今回の探索で一致する文献を確認できなかったというだけで、新規性の証明ではない。

---

## 付録A：Python 3 標準ライブラリによる完全な有限言語検査（全文）

以下を `a_spectrum_check_2026_11_03.py` として保存。Windows では `py -3 a_spectrum_check_2026_11_03.py` で実行できる。

```python
#!/usr/bin/env python3
"""Finite (1,c)/(2,c) exhaustive test, plus a-spectrum audit.
Python standard library only. Windows: py -3 a_spectrum_check_2026_11_03.py
Requires complete enumeration of a FINITE language for an exact pass.
The interval between two holes is always nonempty.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import product


def occurrences(word, arity):
    n = len(word)
    if arity == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield ((word[i:j],), (word[:i], word[j:]))
    elif arity == 2:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for ell in range(k + 1, n + 1):
                        yield ((word[i:j], word[k:ell]),
                               (word[:i], word[j:k], word[ell:]))
    else:
        raise ValueError('arity must be 1 or 2')


def fill(ctx, tup):
    return ''.join(ctx[i] + tup[i] for i in range(len(tup))) + ctx[-1]


def check_finite(words):
    lang = set(words)
    for arity in (1, 2):
        dist = defaultdict(set)
        for w in lang:
            for tup, ctx in occurrences(w, arity):
                dist[tup].add(ctx)
        common = {}
        for tup, contexts in dist.items():
            typ = tuple(frozenset(s) for s in tup)
            for ctx in contexts:
                key = (typ, ctx)
                if key in common:
                    other = common[key]
                    if dist[other] != dist[tup]:
                        for x, y in ((other, tup), (tup, other)):
                            for different_ctx in dist[x] - dist[y]:
                                return (arity, x, y, ctx, different_ctx,
                                        fill(different_ctx, x), fill(different_ctx, y))
                else:
                    common[key] = tup
    return None


def a_skeleton(w):
    out = []
    for ch in w:
        if ch != 'a' or not out or out[-1] != 'a':
            out.append(ch)
    return ''.join(out)


def spectrum(words):
    ns = defaultdict(set)
    for w in words:
        if 'a' in w:
            ns[a_skeleton(w)].add(w.count('a'))
    delta = set()
    for values in ns.values():
        for x, y in product(values, repeat=2):
            if x > y:
                delta.add(x - y)
    return dict(ns), sorted(delta)


@lru_cache(None)
def compressed(n):
    if n == 0:
        return frozenset(('a', 'bc'))
    prev = compressed(n - 1)
    return frozenset(('bc',) + tuple(x + y for x in prev for y in prev))


def code_fiber(t):
    return frozenset(''.join(tokens)
                     for tokens in product(('a', 'bc'), repeat=t))


def main():
    for label, lang in [
        ('singleton a^5', {'a' * 5}),
        ('(a|bc)^5', code_fiber(5)),
        ('compressed G1', compressed(1)),
        ('compressed G2', compressed(2)),
    ]:
        ns, delta = spectrum(lang)
        pure = sorted((len(w) for w in lang if set(w) == {'a'}))
        print(label, 'size=', len(lang), 'pure=', pure, 'Delta=', delta)
        cert = check_finite(lang)
        print('  substitutability:', 'PASS' if cert is None else 'FAIL',
              'certificate=', cert)
        if cert is None:
            assert delta == [], 'finite passing target would contradict spectrum S'
    assert 'bc' in compressed(2) and 'bcbc' in compressed(2)
    print('Note: finite samples of infinite L_{k,g} are NOT tested as whole languages.')


if __name__ == '__main__':
    main()
```

**最終判定**：補題S・系Sの適切な形は成立し、`(α)⇔a` の純粋語が複数あること、各骨格の最小数の幅、局所周期と global Parikh 条件の乖離を確定した。`(β)` での随伴語条件を再証明し、自然な指数候補を一律に排除した。しかし `μ_a` の一般多項式上界も、`𝒞_{2,c}` 内の超多項式族も未解決であり、`op:fanout-two` は未解決のままである。
