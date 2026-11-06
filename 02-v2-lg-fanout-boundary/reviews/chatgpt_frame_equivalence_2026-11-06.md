# 「枠の同値」による欠損内容型 `{a,b}` の侵入反鎖の解析

**研究日：2026-11-06**  
**対象：** `growupkuriyama-hub/Papers/02-v2-lg-fanout-boundary`、未解決問題 `op:fanout-two`  
**判定：** **未解決**。枠の同値補題Fと枠類の推移性を証明し、別ラベル間の等長剛性、同一ラベルでも文法による交換を超える例、枠アンカーの数量的障壁、および条件付きの肯定方向の明確な帰着を得た。小さな文法と巨大な希少型長を持つ代入可能言語も構成したが、全表示で規則厚さが巨大となる。

**表示規約：** `[証明済み]` はこの報告書内に証明を記載、`[条件付き（…）]` は追加仮定を記載、`[予想]` は未証明、`[計算機による観察（…）]` は指定した有限範囲での計算のみ。既知結果の再定式化は新定理として数えない。

## 0. 正本と既存の結果の照合

1. **定義正本：** [59頁凍結TeX](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/parked/2026-11-06_focus/main_before_focus_59pp.tex)、Git blob `1bc97358a49b4e80eef96abb0eee6de4ca10eecf`。`def:class-cmcf`、`def:grammar-properties`、`lem:thickness-equivalence`、`prop:rare-type`、`prop:full-content-types`、`op:fanout-two` を照合した。
2. [README](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/README.md)（取得時Git blob `567147c7f2fd0a8bca144f9aef556bfc54140fe0`）：(114)「純粋 `a` の最短導出での同名ラベル総長」、(117)「その純粋 `a` 導出の一様化 (U)」、(54)「可換群の指数制約」、(80)「可換剰余フィルタを区別する短い語」を参照した。(114)、(117) の定理を**そのまま一般の `ab` 導出に移植しない**。`ab` では `a`/`b` の保持者での部分木交換が内容を失わせ得る。
3. [Claude (153) 補題1–4、7、7′](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_mu_ab_2026-11-05.md)、[ChatGPT (155) §6.1](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_virtual_length_2026-11-05.md) を確認した。特に (153) 補題1の `N=μ_ab≤3(r+1)vθ(q+2)`、補題2の非保持者の同名等長、補題4の `q/5` 個の `c` 連は**既知**として用いる。
4. 前回の `chatgpt_negative_design_2026-11-06.md` と `.py` は会話添付 `/mnt/data/` の実ファイルを直接閲覧した。前回のN9は本報の枠補題の特例として再生する。**指定された `reviews/chatgpt_shortcut_classification_2026-11-06.md` と `reviews/chatgpt_negative_design_2026-11-06.md` は2026-11-06のGitHub接続で指定パスが404だった。**後者は会話添付で代替しているが、前者の未確認の主張を原典確認済みとして引用しない。
5. 先行研究との比較に [Clark–Eyraud (2007), JMLR 8, 1725–1745](https://jmlr.org/papers/volume8/clark07a/clark07a.pdf) と [Clark (2013 online / 2015 print), *Syntactic concept lattice*](https://doi.org/10.1093/logcom/ext037) を使用した。これらが扱う部分語と文脈の incidence/Galois 双対は標準的である。ただし、本報の「内容輪郭ごとに重なりが一致を意味する」という**同じ文言の補題が原著に掲載されているかは未確認**であり、新規性を主張しない。

**原稿の規約。** `Σ={a,b,c}`, `c(w)=cont(w)`, `cont(ε)=∅`。`C_{2,c}` は非空の穴埋め草について `SUB₁` と `SUB₂` の両方を課す。`SUB₂` の文脈は `v₀ □₁ v₁ □₂ v₂`、`v₁≠ε`、両端は空でもよい。`good` は成分非空、非削除、非置換、非併合。`θ=\barθ_G` は**規則を使用する成功導出語の最短長の最大値**であり、単に非終端の最短生成長ではない。`‖G‖=|V|+∑_R(1+rank(R)+各出力成分の記号数)`。

**否定への十分条件 [既知・原稿 `prop:rare-type`]。** `G_n` が reduced good、fan-out≤2、固定rank、`‖G_n‖,θ_n=poly(n)`、`L(G_n)∈C_{2,c}`、`μ_ab=n^{ω(1)}` なら `op:fanout-two` は否定される。`ab` 型は唯一語である必要はない。`prop:rare-type` によりどの特徴標本にも長さ≥`μ_ab`の `ab` 型語が必要だからである。今回この三条件を同時に満たす族は得られていない。

## 1. 課題0：枠の同値補題F

**定義。** 枠 `f=(u,v)∈Σ*×Σ*` の輪郭 `π(f)=(cont(u),cont(v))`、中心集合

`Z_L(f)={z∈Σ⁺ : u z v∈L}`。

### 定理F（全輪郭版） [証明済み・`def:class-cmcf` の直接の帰結]

`L` が `SUB₁`、`SUB₂` を満たすとする。**枠が空側を持つ場合も含めて**、任意の枠 `f,g` で `π(f)=π(g)` かつ `Z_L(f)∩Z_L(g)≠∅` なら `Z_L(f)=Z_L(g)`。

**証明。** `f=(u,v)`, `g=(u',v')`、共通の中心を `ω∈Σ⁺` とする。輪郭一致から `u=ε ⇔ u'=ε`、`v=ε ⇔ v'=ε` である。任意の `z∈Z_L(f)` に対し `z∈Z_L(g)` を示す。

- `u,v` がともに非空なら `E=□₁ ω □₂`, `F=□₁ z □₂`, `x=(u,v)`, `y=(u',v')`。各穴埋め草は非空、`ω,z` は非空なので二穴の中央条件を満たす。`cont(u)=cont(u')`、`cont(v)=cont(v')`。`E[x]=uωv`, `E[y]=u'ωv'`, `F[x]=uzv` は全て `L` にある。`SUB₂` により `F[y]=u'zv'∈L`。
- `u=u'=ε`、`v,v'` 非空なら `E=ω□`, `F=z□`, `x=v`, `y=v'` として `SUB₁`。
- `v=v'=ε`、`u,u'` 非空なら `E=□ω`, `F=□z`, `x=u`, `y=u'` として `SUB₁`。
- 両端が空なら輪郭一致から両枠は `(ε,ε)` であり、主張は自明。

逆向きは `f,g` の交換で同様。□

**同値関係の注意 [証明済み]。** 輪郭が固定された**活性枠** `\mathfrak F_π(L)={f:π(f)=π, Z_L(f)≠∅}` 上で `f∼g ⇔ Z(f)∩Z(g)≠∅` と置くと、反射・対称・推移が成り立つ。推移性は `Z(f)=Z(g)=Z(h)` から従う。**全枠**にこの「非空交わり」関係をそのまま使うと `Z(f)=∅` に対して `f∼f` が偽であり、同値関係ではない。全枠では `π(f)=π(g) かつ Z(f)=Z(g)` と定義すれば（空の中心集合も含め）同値関係となる。

**定理Fの位置付け。** 原稿の `SUB₂` で「中央を固定して左右を二つの穴とみなす」だけである。したがって**独立の強化条件でも新しい代入可能性公理でもない**。部分語の分布集合と枠の中心集合を転置した incidence という観点は Clark–Eyraud (2007)、Clark (2013) の標準的枠組みと整合する。今回役立つのは、その帰結を**具体的な導出木の外枠と長さの下界へ適用する点**である。

### 系F1（64輪郭・中心集合による類分け） [証明済み]

三文字の輪郭は `2³×2³=64` 通り。しかし**一輪郭内でも中心集合 `Z` の異なる活性類はいくつでもあり得る**。正しい構造は「各輪郭内の非空中心集合は、同じか互いに素」である。類数が64以下になることは導けない。

## 2. 課題A：最短 `ab` 語の枠への適用

`W∈L∩{a,b}⁺` を `N=|W|=μ_ab(L)` の語とする。ファンアウト1の任意の因子分解 `W=u x v` (`x≠ε`) を考える。

### 補題A1（枠の外側最小性） [証明済み]

`f=(u,v)`, `g=(u',v')` が同じ輪郭をもち、ある `ω∈Z(f)∩Z(g)` を共有するなら

`|u'|+|v'| ≥ |u|+|v|`。

**証明。** 定理Fから `x∈Z(g)`、すなわち `u'xv'∈L`。輪郭一致ゆえ `cont(u'xv')=cont(uxv)={a,b}` であり、`c` は含まれない。最短性から `N≤|u'|+|x|+|v'|`。`N=|u|+|x|+|v|` を引いて結論。`u,v` が両方 `ab` を含むという強い仮定は**不要**。□

**注意。** `u'xv'∈L` がもともと直接分かっている場合、同じ下界は SUB を使わずに最短性だけで出る。補題Fの独自の役目は、**共有中心 `ω` から `u'xv'∈L` を導くこと**である。

### 系A2（異なる非終端にも通用する等長性） [証明済み]

`W=u_i x_i v_i=u_j x_j v_j` の二つの因子出現の枠 `f_i,f_j` の輪郭が等しく、`Z(f_i)∩Z(f_j)≠∅` とする。すると `|x_i|=|x_j|`。

**証明。** 補題A1を `f_i,g=f_j` に用いると `N−|x_j|≥N−|x_i|` だから `|x_j|≤|x_i|`。逆方向で `|x_i|≤|x_j|`。□

**唯一の `ab` 型の場合の追加系 [証明済み]。** `W` がその型の唯一語なら、同じ条件で `x_i=x_j` が語として成立する。実際、定理Fによる `u_j x_i v_j` は `ab` 型なので `W=u_jx_jv_j` に等しく、自由モノイドで左右を消去する。

これらは異なる非終端 `B_i≠B_j` にも適用できる。**(114) 補題2.1の証明の単なる再掲ではない適用範囲**は、異なる非終端の二枠が文法に依存しない共通中心で合流する場合である。一方、等長だけで同じ類に属する節点の**出現数**は制限されない。

### 同名ラベルと (114)/(117) (U) の正確な比較

**[証明済み]** 同じファンアウト1非終端 `B` の二出現が `W` にあるとき、そのすべての生成 `L_B(G)` は両方の枠で文法的に許される。特に短い逃げ道 `ρ_B∈L_B` は共通中心である。輪郭が同じなら補題Fによって中心集合は等しくなる。しかし、この結論が文法の差し替えと**完全に同じ**とは限らない。文法は `L_B(G)` の中心しか保証しないのに対し、Fは `Z_L(f)` の**任意の別導出による中心**を運ぶ。

**例A3（同名ラベルでも文法の差し替えを真に超える） [証明済み]。** 次の reduced good CFG（最大ランク2）の全規則を考える：

```
B -> a | c
S -> ab B ab B ab | abbabaab
```

その有限言語は `L={ab X ab Y ab : X,Y∈{a,c}}∪{abbabaab}`、計5語。`W=abaabaab` は最短 `ab` 型語で、`B` が二回現れる。

- 左の `B` の枠 `f=(ab,abaab)`、右の `B` の枠 `g=(abaab,ab)` はともに輪郭 `({a,b},{a,b})`。
- `a,c` は両枠の中心集合にあり、文法的な `B` の交換で運べる。
- しかし `b∈Z(f)` は**直接の別規則** `S→abbabaab` によるもので、`b∉L_B(G)`。`b∉Z(g)` である。

破綻証明書（**一段**）：

```
E = □₁ a □₂       F = □₁ b □₂
x = (ab, abaab)   y = (abaab, ab)
E[x] = abaabaab   ∈ L
E[y] = abaabaab   ∈ L
F[x] = abbabaab   ∈ L
F[y] = abaabbab   ∉ L
```

各穴は非空、中央 `a,b` は非空、成分内容が一致する。つまり `C₂` を仮定すれば `abaabbab` が強制されるが、`B→a|c` の差し替えだけでは作れない。**(α) の「異ラベル」だけが本質ではない。偶然の中心を持つ(β)は、同名ラベルでも強化になる。** この小例は `C₂` 反例を示すための例であり、巨大な侵入反鎖を持つとは主張しない。

**[証明済み・(153)補題2の再利用]** `T` を最短 `ab` 語のうち節点数最小の導出とし、`Q` を `c`-強制の重い節点の反鎖、`Q°⊆Q` を **`a` と `b` のいずれの保持者でもない節点の部分集合**とする（`Q` には保持者が最大2個混ざり得る）。同名の `B` をもつ `Q°` の節点は（ファンアウト1・2とも）全成分の**総長**と部分木の**節点数**が等しい。前者は(153)補題2：これらは非保持者なので一方の部分木を他方の純 `a,b` 生成に替えても最短 `ab` 語が保たれる。節点数が異なれば長さ不変の交換により `T` の節点数が減る。従って、`Q°` の同名・比較不能節点は一種類の部分木に**同時に一様化可能**である。ただし全 `T` に対する (117)(U) は `ab` 型で未証明、成分別長は等しくなくてもよい。

### ファンアウト1の類数 [証明済み]

各ファンアウト1ラベル `B` について短い生成 `ρ_B` を一つ固定する。`W` におけるその `B` 出現の枠は必ず `ρ_B` を受け入れる。輪郭が同じなら互いに類が同じだから、こうした**導出節点の枠**は一つの `B` 当たり高々64類、全ラベルで高々 `64v` 類（他ラベルとの合流は類数をさらに減らす）。ただしこれは **`q≤64v` を意味しない**。一類に任意多数の出現があり得ることを禁止する議論が欠けている。

## 3. ファンアウト2の折り畳みと限界

**[証明済み]** ファンアウト2節点 `t` の組生成を `(x_t¹,x_t²)` とし、語中の配置を

`W=u_t x_t¹ m_t x_t² v_t`（`m_t∈{a,b}⁺`）

とする。規則の `good` 性から二成分間の固定隙間 `m_t` は非空である。短い別生成 `(η_t¹,η_t²)∈L_{B_t}(G)` に置換した語

`u_t η_t¹ m_t η_t² v_t∈L`。

これを一穴の「凸包中心」 `z_t=x_t¹ m_t x_t²` と `ω_t=η_t¹ m_t η_t²` に折り畳めば、**枠 `f_t=(u_t,v_t)` に関する定理Fを合法的に使える**。特に同輪郭の枠 `g=(u',v')` が `ω_t` を受け入れると、`u'z_tv'∈L` まで移送される。

**ただし折り畳みは非終端の生成そのものではない**。中間 `m_t` は `B_t` が生成した文字ではなく上位の文脈に属する。その長さは `θ` により抑えられない。また同じラベル `B` の二出現でも `m_t` が異なれば `ω_t` は異なり得るため、「`64v` 類」の議論はファンアウト2に移植できない。正しい一次データは二穴分布

`D_L^{(2)}(x¹,x²)={u□₁m□₂v : u x¹ m x² v∈L}`

と配置 `m` である。同じ `m` を保った二枠の外側交換はFから得られるが、**異なる `m` の二穴文脈の同値はFだけでは保証されない**。これは `SUB₂` を超える三つの外側スロットを暗黙に導入しないための注意である。

## 4. 枠の「アンカー」：定量的な必要条件と肯定方向の帰着

### 定義（固定の `c` 入り中心に対する最安外枠）

`ω∈Σ⁺`、輪郭 `π` について

`A_L(π,ω)=min{|u|+|v| : π(u,v)=π, uωv∈L}`

と置き、集合が空なら `+∞`。値は有限のとき非負整数である。**`ω` が `c` 入りでも定義できる**。

### 定理A4（最短語の外枠は `c` 入り中心に対しても最安） [証明済み]

`W=u x v` は最短 `ab` 語、`ω∈Z_L(u,v)`、`π=(cont(u),cont(v))` とする。`L∈C_{2,c}` なら

`A_L(π,ω)=|u|+|v|=N−|x|`。

**証明。** 枠 `(u,v)` 自身が `ω` を受け入れるので `A_L≤|u|+|v|`。最小値を実現する `(u',v')` を取る（自然数上で存在）。同輪郭で `ω` を共有するから定理Fを適用でき、`u'xv'∈L`。補題A1により `|u'|+|v'|≥|u|+|v|`。合わせて等号。□

**N11（新しい反例必要条件：外枠アンカー障壁） [証明済み]。** 大きな `N=μ_ab` を維持したいなら、`W` の各因子枠 `f` が受け入れる任意の `c` 入り中心 `ω` に対し、**同じ輪郭で `ω` を受け入れる別枠の外側総長は、必ず `N−|x|` 以上**でなくてはならない。これはファンアウト2の折り畳み中心にもそのまま通用する。`N10` の「短い `c` を含む語がある」だけでは、この `ω` と同輪郭の**短い外枠**を供給しない。

定理A4は (153) の「最短性の伝播」補題3と同じ原理に立ち、Fを用いて**外側の最小性**として言い換えたもの。一般の短い証人の存在は**新しく証明していない**。

### 定理B1（短アンカーがあれば `q` の多項式上界） [条件付き（下記の `Bridge(P)`）]

`G` は reduced good、fan-out≤2、rank≤`r`、`v=|V|`、`θ=\barθ_G`、`L(G)∈C_{2,c}`。`W` は最短 `ab` 語で `N=μ_ab`、`T` はその中で節点数最小、`Q` は `c` 強制の重い節点の最大反鎖、`q=|Q|`。多項式 `P=P_r(v,θ)≥1` について以下を仮定する。

**`Bridge(P)`：** `q≥2` なら、`Q` のうち**組生成の総長が最小**の節点 `t` に対して、(i) `θ` 以下の短い組生成 `η_t` を選び、(ii) 二成分ならその配置隙間を `m_t`、一成分なら `m_t=ε` として、(iii) 折り畳み中心 `ω_t` を受け入れる同輪郭の枠 `(u',v')` が存在し、

`|u'|+|v'|+|m_t|≤P(v,θ)`。

このとき

`N≤max{9(r+1)vθ, 2P(v,θ)}`、さらに `q≤N/(θ+1)`。

**証明。** `q≤1` なら既知の (153) 補題1により `N≤3(r+1)vθ(1+2)=9(r+1)vθ`。`q≥2` とする。`Q` は反鎖で、good の非削除性・線形性により各節点が `W` 内で占める文字位置は互いに素だから `∑_{t∈Q}ℓ_t≤N`。従って最小の `t` は `ℓ_t≤N/q≤N/2`。`t` の凸包因子 `z_t` は一成分なら `ℓ_t`、二成分なら `ℓ_t+|m_t|` 文字を持ち、同じ輪郭の元の枠 `(u_t,v_t)` に `z_t,ω_t` の両方が受理される。`Bridge(P)` の枠 `(u',v')` と定理Fで `u'z_tv'∈L`。内容は `W` と同じ `ab` 型なので最短性から

`N≤|u'|+|v'|+|z_t|=|u'|+|v'|+|m_t|+ℓ_t≤P+N/q≤P+N/2`。

よって `N≤2P`。最後に重い各節点は `ℓ_t≥θ+1` なので `q(θ+1)≤∑ℓ_t≤N`。□

**重要：** `Bridge(P)` は**証明していない**。まさにこれが残る穴である。ファンアウト2では `m_t` が巨大な可能性もあり、この追加前提が原稿の `SUB₁/SUB₂` と小厚さから必然とは分からない。`Bridge(P)` は肯定方向の**十分条件**であって、未解決問題と同値とは主張しない。定理が示したのは、「最大反鎖の最小節点で短いアンカーと短い隙間を一度だけ作る」ことができれば、**定数2で `μ_ab` が抑えられる**という正確な必要作業である。

## 5. 課題C・否定側その1：ファンアウト2倍増族は枠の類で直ちに崩れる

ここでは前回報告の候補(A)を、**枠の観点から独立に再評価**する（候補自体の新規構成とは数えない）。`p=ab`、`M=2^n`、`n≥2`。すべての規則：

```
D0 -> ab
Di -> Di-1 Di-1 | a^i c b             (1<=i<=n)
A1 -> (ab,ab)                       (arity 2)
Ai -> (d x,y) | (x,y d) | (d1,d2)    (2<=i<=n)
        d,d1,d2 from Di-1 (arity 1); (x,y) from Ai-1
S  -> Dn ab | x c y                 (x,y) from An
```

これは各 `Ai` の三つの規則を、左・右・中央それぞれ**別規則**として記した有限の good MCFG である。fan-out2、rank2、reduced good。`S→xcy` では同じ二成分子の間に固定 `c` があるから nonmerging。文法サイズと厚さ：

`‖G_n‖=n(n+1)/2+27n+3,    θ_n≤(n+3)²`。

**詳細な評価 [証明済み]。** `|V|=2n+2`、`D0` 規則のサイズ3、各 `Di` の二規則サイズの和 `i+8`、`A1` 規則は5、各 `Ai (i≥2)` の三規則サイズ合計17、`S` の二規則サイズ合計10。総和が上式となる。すべての規則の子に到達し、全 `Di` は `a^icb`（`D0` は `ab`）、全 `Ai` は左・右・中央の導出によって二つの非空成分を生成するので reduced。厚さでは指定規則から開始記号までの一経路以外を短い `Dj→a^jcb`、`Aj→(a^{j-1}cb,a^{j-1}cb)` 等で埋める。`Di` 指定規則を含む成功語は長さ `≤2+2(i+1)+∑_{j=i+1}^n(j+1)`、`Ai` 指定規則では `≤1+(3i+1)+∑_{j=i+1}^n(j+1)` とできる（`A1` は4）。いずれも `n≥2` で `(n+3)²` 以下、`S` 自身の二規則も同様。これらの短い成功導出は各規則の厚さの**上界証人**である。

**欠損型 [証明済み]。** `S→xcy` は必ず `c` を出す。他方 `S→Dn ab` から `c` を出さないには `Di` の倍増規則しか使えない。よって唯一の `ab` 型語が `W=p^{M+1}`、`μ_ab=2M+2`。二成分 `Ai` は `p` の総 `2^i` 個のブロックの全内部スロットを生成し、N5も満たす（`i=1` を基点に、左規則が右端側、右規則が左端側、中央が中点を作る帰納法）。それでも以下で失格する。

### 枠類衝突と完全な証明書（N9そのもの） [証明済み]

枠を

`f=(a, b p^{M−1}),     g=(a^n,bp)`

とする。ともに輪郭 `({a},{a,b})` で、中心 `c` を受け入れる：

`f[c]=acbp^{M−1}∈L`（完全倍増木の左端の `D1→acb`）、

`g[c]=a^ncbp∈L`（`Dn→a^ncb`）。

しかし `ba∈Z(f)` は `f[ba]=p^{M+1}=W` による。一方 `g[ba]=a^n babab` は `c` を含まないが唯一の純 `ab` 語 `W` ではないから `L` にない。よって定理Fに反し、`G_n` は全 `n≥2` で `C₂` に属さない。

**機械再生可能な一段証明書：**

```
E = □₁ c □₂,             F = □₁ ba □₂
x = (a, b(ab)^(M-1)),    y = (a^n, bab)
E[x] = acb(ab)^(M-1)     ∈ L
E[y] = a^n cbab          ∈ L
F[x] = (ab)^(M+1)        ∈ L
F[y] = a^n babab         ∉ L
```

両穴非空、内部 `c`, `ba` 非空、成分内容一致。従って**この三語を含む任意の `C₂` 言語**には `a^n babab` が強制され、`μ_ab≤n+5`。追加規則やスロット飽和をしても三語を保持する限り指数下界を回復できない。これは前回のN9・定理Dを**枠Fとして読み直したもの**であり、新しい失格定理と数えない。

## 6. 課題C・否定側その2：枠類を完全設計した代入可能族（厚さで失格）

### 構成B（内容別の単一長さ層） [証明済み]

`n≥1`、`M=2^n` とし

`H_n={a,b,c} ∪ {w∈{a,b}^M : cont(w)={a,b}}`。

これは構造的述語「内容型 `T` ごとに許される長さがちょうど一つ」で定義する。具体的には `{a},{b},{c}` は長さ1、`{a,b}` は長さM、それ以外の内容型は実現しない。

**一般補題B1（型別単一長さ層の完全閉包） [証明済み]。** 任意の有限アルファベットと任意の部分関数 `ν:2^Σ\{∅}→ℕ_{>0}` に対し

`L_ν={w∈Σ⁺ : ν(cont(w))が定義され、 |w|=ν(cont(w))}`

は**すべての arity** に関して内容型付き代入可能である。

**証明。** 許容文脈 `E` と非空組 `x,y` が成分ごとに同じ内容型をもち、`E[x],E[y]∈L_ν` とする。完成語の内容は両方とも `T=cont(Eの固定語)∪⋃cont(x_i)` で等しく、両者の長さは `ν(T)` に等しい。文脈固定部分の長さを差し引くと `∑|x_i|=∑|y_i|`。任意の許容文脈 `F` について完成語の内容は両方とも同じ `T'`、長さも等しい。従って `ν(T')` が未定義ならどちらも非所属、定義済みなら長さが `ν(T')` に等しいか否かが両者で同じ。ゆえに `F[x]∈L_ν ⇔ F[y]∈L_ν`。空穴は使わず、いかなる arity にも成立。□

**枠類の完全な設計 [証明済み]。** 任意の枠 `f=(u,v)` の輪郭を `π=(A,B)`、外側総長を `k=|u|+|v|` とすると

`Z_{H_n}(f)={z≠ε : ν(A∪B∪cont(z))が定義され、 k+|z|=ν(A∪B∪cont(z))}`。

従って同じ輪郭で同じ `k` の枠は中心集合が等しい。異なる `k` の枠が中心 `z` を共有すれば `k+|z|=ν(T)=k'+|z|` で `k=k'` に反するから、中心集合は互いに素。すなわち**活性枠の類はちょうど `(輪郭,外側総長)` で分類される**。

`M≥8` のとき、一輪郭 `({a,b},{a,b})` の中に少なくとも `M−4` 個の異なる活性類がある。実際 `k=4,…,M−1` について `u=a^{k−3}b`、`v=ab`、`z=a^{M−k}` とすれば `u z v∈H_n` かつ `|u|+|v|=k`、輪郭は固定である。`k` が違えばクラスが違う。**64輪郭だけでは類数は全く抑えられない**。

### 明示した文法の全規則と量的評価 [証明済み]

`A_{0,a}→a`, `A_{0,b}→b`。`1≤i<n` では `T∈{{a},{b},{a,b}}`、最上段 `i=n` では **`T={a,b}` のみ**置く。存在する `A_{i−1,U}`, `A_{i−1,V}` に対して `U∪V=T` となる**すべての組**につき一規則

`A_{i,T}→A_{i−1,U} A_{i−1,V}`。

開始規則は `S→a | b | c | A_{n,{a,b}}`。`i=1` で内部段なら `(a,a),(b,b),(a,b),(b,a)` の4本、`2≤i<n` なら9本、`i=n≥2` の最上段は和集合が `{a,b}` の7本。`n=1` の最上段には `(a,b),(b,a)` の2本だけを置く。**到達不能な最上段 `A_{n,a}`, `A_{n,b}` は作らない**。これ以外の規則はない。

`A_{i,T}` は帰納法により、長さ `2^i` で内容がちょうど `T` の二文字語をすべて生成する。基底は一文字の `a`,`b`。長さ `2^i` の語を半分に切れば二つの内容集合 `U,V` の和が `T` であり、該当する一規則がある。逆に各規則の完成語は長さが倍になり内容が和集合である。よって `L(G_n)=H_n`。全非終端は productive、開始から（`ab` 段を下り、左右の `a/b` 分岐を使うことで）reachable。テンプレートは一変数ずつを正順に出すので good、fan-out1、rank2。

`|V|=3n+1`、`S` の4規則の寄与は `9`、基底2規則は `4`。`n≥2` で内部第1段は `4×5=20`、内部段 `2≤i<n` は各 `9×5=45`、最上段は `7×5=35`。よって `n≥2` では

`‖G_n‖=(3n+1)+9+4+20+45(n−2)+35=48n−21`。

`n=1` は `|V|=4`、上段2規則が `2×5=10` だから `‖G_1‖=4+9+4+10=27=48−21`。

最短 `ab` 型語は長さMなので `μ_ab(H_n)=M=2^n`。全ての `a,b,c` の一文字語が言語にあり、**前報N10（各文字の短い成功語が存在）は満たす**。しかし、この文法で `S→A_{n,ab}` の規則を使用する成功語は必ず長さMなので `θ≥M`。ほかの全規則も成功語の長さがM以下で実現できるから `θ=M`。

### 定理B2（一般の長さギャップ障壁） [証明済み]

`M≥2`、`L⊆Σ^1∪Σ^{≥M}` に長さM以上の語があり、`G` が `L` を生成する reduced good MCFG（開始 arity1）なら、**どんな表示でも** `\barθ_G≥M`。

**証明。** 逆に `θ<M` とする。reduced なので各規則 `R` には成功導出があり、厚さの定義から `R` を使用する長さ `≤θ<M` の完成語がある。`L` に存在するその長さは必ず1。`R` の右辺が直接書く終端の総個数を `t_R`、子非終端の各 arity を `d_1,…,d_s` とする。good の λ-freeness から子の各成分は1文字以上生成し、nondeleting から各成分は一度ずつ残る。従って `R` を使用する完成語の長さは少なくとも `t_R+∑d_j`。ゆえに `t_R+∑d_j≤1` が**すべての規則**で成立する。左辺各出力成分は非空なので（導出される組の各成分が非空）、実現される非終端は arity1しかあり得ない。さらに規則は終端1個を書き子を持たないもの、または fan-out1 の子を一つだけ受け取り固定終端を書かない単項規則のいずれかしかあり得ない。これらの規則でできる有限の成功導出は、単項規則をいくつ辿っても末端で1文字だけ出すから長さ1である。長い語の存在に矛盾。□

**N12（新しい除外条件：規則厚さに対する長さスペクトルのギャップ） [証明済み]。** 短い語が `a,b,c` それぞれにあっても、`L` の受理語長の集合に `1` と `M` の間の空白があれば、どの reduced good 表示でも `θ≥M`。`N10` とは異なり、**文字ごとの出現ではなく、長さを伸ばす規則の最短成功語**を検査する。構成Bは `‖G_n‖=O(n)` かつ `C₁,C₂` を完全に満たすが、この障壁で否定反例から外れる。

## 7. 計算：枠類と証明書の再生

**実装** `chatgpt_frame_equivalence_2026-11-06.py` は**標準ライブラリのみ**。`goodstep` が「三つの前提の所属、成分ごとの内容一致、二穴の内部固定語の非空、結論の非所属」を確認する。有限言語では**生成語の全体**を使い、任意の長さで打ち切っていない。枠類の計算は各中心 `z` で、同輪郭の活性枠を union–find で結んだ「交わりグラフの連結成分」を数える。**不正な言語**では連結成分の中に異なる `Z` が混在するため、これを合法な等価類とは呼ばない。

| 検査モデル | 完全列挙した言語の語数 | 活性枠数 | 交わり連結成分 | 中心集合が不一致の成分 | 判定 |
|---|---:|---:|---:|---:|---|
| 同名ラベル例A3 | 5 | — | 63 | 11 | SUB₂ 失格 |
| 倍増(A), `n=2` | 13 | 261 | 117 | 21 | SUB₂ 失格 |
| 倍増(A), `n=3` | 131 | 5702 | 290 | 126 | SUB₂ 失格 |
| 層言語(B), `n=1` | 5 | — | 5 | 0 | SUB₁/SUB₂ 全有限検査合格 |
| 層言語(B), `n=2` | 17 | — | 29 | 0 | SUB₁/SUB₂ 全有限検査合格 |

[計算機による観察（上記全語、全許容1穴・2穴出現）] `n=1,2` の層言語について、全 `SUB₁/SUB₂` 一段反例は0だった。ただし**所属の証明は§6の一般補題B1**であり、計算ではない。不正言語については証明書が実際に再生されたので非所属は確定的である。

**代表出力：**

```
SAME_LABEL_CERT: E=("", "a", ""), x=("ab", "abaab"), y=("abaab", "ab"),
                 F=("", "b", "");
                 premises=("abaabaab", "abaabaab", "abbabaab"),
                 missing="abaabbab"
A n=2: |L|=13, frames=261, overlap classes=117, inconsistent=21
A n=2 N9: E=("", "c", ""), x=("a", "bababab"), y=("aa", "bab"),
          F=("", "ba", ""),
          premises=("acbababab", "aacbab", "ababababab"),
          missing="aababab"
A n=3: |L|=131, frames=5702, overlap classes=290, inconsistent=126
B n=4: ‖G‖=171, θ=16, μ_ab=16
```

## 8. 結果一覧・残る穴を一つにまとめる

| 対象 | 判定 | 得られた内容 | 何を証明していないか |
|---|---|---|---|
| 補題F | [証明済み・既存SUBの帰結] | 全ての空枠パターンに拡張、非空中心の枠類が同値関係 | 独立の新規定理ではない |
| 最短語の枠 | [証明済み] | 外側最小性 `A_L(π,ω)=N−|x|`、異ラベルの枠衝突も等長 | 同類の出現数の上界 |
| 同ラベル枠 | [証明済み] | 文法外の「偶然の中身」までFが移送、5語の失格例 | `q` の上界 |
| 二成分 | [証明済み] | 凸包に折ってFを適用可能、ただし gap は自由 | gap の多項式上界 |
| 肯定側 | [条件付き（Bridge(P)）] | `μ_ab≤max(9(r+1)vθ,2P)`、`q≤N/(θ+1)` | Bridge(P) 自体 |
| 候補A | [証明済み失格] | 二成分スロット飽和・小厚さ・指数μを満たすがN9/F違反 | `C₂` 所属 |
| 候補B | [証明済み失格] | **全arity閉包、線形文法サイズ、指数μ、短い全三文字語**。類を `(π,k)` で完全分類 | 全表示で `θ≥2^n` のため必要条件(1) |

### 残った穴：一つの命題

**命題H（短アンカーと二成分隙間の架橋；未証明）。** 固定rank `r` に対するある多項式 `P_r(v,θ)` が存在し、`C_{2,c}` の最短 `ab` 語の最小導出で最大 `c` 強制重反鎖 `Q` が2個以上なら、**最小総長の節点**で `Bridge(P_r)` が成立する。

この命題を示せれば定理B1で直ちに `μ_ab=poly_r(v,θ)` となり、`q` も多項式となる。**命題Hは必要条件とは証明されておらず、強すぎる可能性がある。** 反対に否定を狙うなら、命題Hを避けつつ**小厚さ・小文法・完全なSUB₁/SUB₂**を満たす具体族が必要である。目下、どちらもないので `op:fanout-two` は未解決である。

**次の作業（最大3件）。**

1. 反鎖中の最小節点で、同輪郭・同じ `c` 入り中心をもつ**別ラベル由来の短い外枠**が必ず現れる条件を探す。N11が必要な比較の向きを明確にする。
2. 二成分の `m_t` が長くても、二穴分布のままで短縮できる「gap非依存版」の Bridge を試す。折り畳みFだけでは `|m_t|` が障害になる。
3. 否定族を作るなら、層構造Bの `(π,k)` 分離を利用しつつ、長さギャップN12を避ける**各規則の短い成功導出**を導入する。その導入で生じる別中心との枠類合流を、一般証明書Fで検査する。

---

## 付録：標準ライブラリのみの検証スクリプト全文

別添 `chatgpt_frame_equivalence_2026-11-06.py` と**同一内容**。実行：`python chatgpt_frame_equivalence_2026-11-06.py`、または小例の全一段違反探索を追加するには `python chatgpt_frame_equivalence_2026-11-06.py --scan`。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Frame-equivalence audit for 3-letter content typing; stdlib only.

Run: python chatgpt_frame_equivalence_2026-11-06.py
Optional: --scan (enumerate all first-step SUB1/2 for the small finite examples)
All asserted non-membership certificates concern complete finite languages,
not length-truncated approximations.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from itertools import combinations

ALPHABET = frozenset('abc')


def content(word):
    return frozenset(word)


def fill(context, values):
    assert len(context) == len(values) + 1
    return ''.join(context[i] + values[i] for i in range(len(values))) + context[-1]


def goodstep(L, E, x, y, F):
    """Check exact source premises and a genuine *missing* conclusion."""
    d = len(x)
    assert d in (1, 2) and len(y) == d
    assert len(E) == len(F) == d + 1
    assert all(x) and all(y)
    assert all(content(a) == content(b) for a, b in zip(x, y))
    assert all(E[j] and F[j] for j in range(1, d))
    A, B, C, D = fill(E, x), fill(E, y), fill(F, x), fill(F, y)
    assert A in L, ('first premise', A)
    assert B in L, ('second premise', B)
    assert C in L, ('third premise', C)
    assert D not in L, ('conclusion unexpectedly present', D)
    return dict(d=d, E=E, x=x, y=y, F=F, premises=(A, B, C), missing=D)


def frame_of(w, i, j):
    assert 0 <= i < j <= len(w)
    return w[:i], w[j:], w[i:j]


def all_frames(L):
    """Exact incidence: frame -> all nonempty centers occurring in finite L."""
    ans = defaultdict(set)
    for w in L:
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                ans[(w[:i], w[j:])].add(w[i:j])
    return dict(ans)


def frame_classes(L):
    """For a finite L, compute *actual* active-frame classes.

    If L obeys frame lemma, (outline,Z) is precisely the overlap class.
    For a non-closed L, this exact-Z grouping need not agree with the
    transitive closure of the overlap graph. Both are tested separately.
    """
    incidence = all_frames(L)
    grouped = defaultdict(list)
    for frame, centers in incidence.items():
        outline = (content(frame[0]), content(frame[1]))
        grouped[(outline, frozenset(centers))].append(frame)
    return incidence, grouped




def overlap_components(L):
    """Actual connected components of same-outline overlapping active frames.

    These components need not be valid equivalence classes when the frame
    property fails; ``bad`` counts components having unequal center sets.
    """
    incidence = all_frames(L)
    frames = list(incidence)
    parent = list(range(len(frames)))
    def root(i):
        while parent[i] != i:
            parent[i] = parent[parent[i]]
            i = parent[i]
        return i
    def union(i, j):
        a, b = root(i), root(j)
        if a != b: parent[a] = b
    buckets = {}
    for i, f in enumerate(frames):
        outline = (content(f[0]), content(f[1]))
        for z in incidence[f]:
            key = (outline, z)
            if key in buckets: union(i, buckets[key])
            else: buckets[key] = i
    groups = defaultdict(list)
    for i, f in enumerate(frames): groups[root(i)].append(f)
    bad = sum(len({frozenset(incidence[f]) for f in group}) > 1
              for group in groups.values())
    return len(groups), bad


def exact_layer_words(n):
    from itertools import product
    M = 2 ** n
    assert M <= 8, 'small exact test only'
    return {'a', 'b', 'c'} | {''.join(t) for t in product('ab', repeat=M)
                               if set(t) == {'a','b'}}

def frame_conflict(L):
    """Find one overlap with unequal Z in the same outline (full finite test)."""
    incidence, _ = frame_classes(L)
    by_outline = defaultdict(list)
    for f, Z in incidence.items():
        by_outline[(content(f[0]), content(f[1]))].append((f, Z))
    for outline in sorted(by_outline, key=lambda x: (len(x[0]), len(x[1]), str(x))):
        arr = by_outline[outline]
        # Reverse index over centers: only frames with genuine overlap compete.
        by_center = defaultdict(list)
        for f, Z in arr:
            for z in Z: by_center[z].append(f)
        checked = set()
        for z, frames in by_center.items():
            if len(frames) < 2:
                continue
            for f, g in combinations(sorted(frames), 2):
                if (f, g) in checked: continue
                checked.add((f, g))
                if incidence[f] != incidence[g]:
                    diff = sorted(incidence[f] - incidence[g], key=lambda x:(len(x),x))
                    if diff: return outline, f, g, z, diff[0]
                    diff = sorted(incidence[g] - incidence[f], key=lambda x:(len(x),x))
                    return outline, g, f, z, diff[0]
    return None


def example_same_label():
    """S -> ab B ab B ab | ab b ab a ab, B -> a | c.

    The extra terminal production creates an accidental center 'b'
    in the first B-frame without making b a yield of B.
    """
    L = {'ab' + x + 'ab' + y + 'ab' for x in 'ac' for y in 'ac'}
    accidental = 'ab' + 'b' + 'ab' + 'a' + 'ab'
    L.add(accidental)
    left = ('ab', 'abaab')
    right = ('abaab', 'ab')
    assert left[0] + 'a' + left[1] == right[0] + 'a' + right[1]
    cert = goodstep(L, ('', 'a', ''), left, right, ('', 'b', ''))
    incidence = all_frames(L)
    assert 'a' in incidence[left] & incidence[right]
    assert 'c' in incidence[left] & incidence[right]
    assert 'b' in incidence[left] and 'b' not in incidence[right]
    assert all(content(t) == {'a','b'} for t in left+right)
    return L, cert, left, right, incidence


def candidate_a(n):
    """Exact finite fanout-2 doubled/slotted grammar from preceding report."""
    assert n >= 2
    D = [{'ab'}]
    for i in range(1, n + 1):
        D.append({u + v for u in D[-1] for v in D[-1]} | {'a' * i + 'cb'})
    A = [None, {('ab', 'ab')}]
    for i in range(2, n + 1):
        old, blocks = A[-1], D[i - 1]
        A.append({(d + x, y) for d in blocks for x, y in old}
                 | {(x, y + d) for d in blocks for x, y in old}
                 | {(d, e) for d in blocks for e in blocks})
    L = {w + 'ab' for w in D[n]} | {x + 'c' + y for x, y in A[n]}
    return L


def verify_scissors(n, L):
    M = 2 ** n
    x = ('a', 'b' + 'ab' * (M - 1))
    y = ('a' * n, 'bab')
    cert = goodstep(L, ('', 'c', ''), x, y, ('', 'ba', ''))
    assert {w for w in L if 'c' not in w} == {'ab' * (M + 1)}
    assert len(cert['missing']) == n + 5 < 2 * (M + 1)
    return cert


def layer_language(n, w):
    """Exact membership in {a,b,c} union all full-ab words of length 2**n."""
    M = 2 ** n
    return w in {'a','b','c'} or (len(w) == M and content(w) == {'a','b'})


def layer_grammar_size(n):
    """Exact *reduced* typed-doubling grammar size.

    States are S, A_{0,a}, A_{0,b}, every A_{i,T} for 1<=i<n,
    and only A_{n,ab} at the top. Omitting A_{n,a},A_{n,b}
    is essential for reachability (hence reducedness).
    """
    assert n >= 1
    nonterminals = 3*n + 1
    start_rules = 3*2 + 3
    base_rules = 2*2
    if n == 1:
        binary_rules = 2*5  # only (a,b) or (b,a) at the top
    else:
        binary_rules = 4*5 + (n-2)*9*5 + 7*5
    return nonterminals + start_rules + base_rules + binary_rules


def check_layer(n):
    M = 2 ** n
    assert layer_grammar_size(n) == 48*n - 21
    for c in 'abc': assert layer_language(n, c)
    for w in ['ab'*(M//2), 'a'*(M-1)+'b', 'b'+'a'*(M-1)]:
        assert layer_language(n, w)
    assert not layer_language(n, 'ab'*(M//2)+'a')
    assert not layer_language(n, 'a'*M)
    assert M > 1
    # The general class formula is proved in the report and checked on
    # complete small finite languages in main(); no symbolic tautology here.
    return (layer_grammar_size(n), M, M)


def finite_sub_failure(L, d):
    """Exhaustive finite-language one-step SUB_d search; exact (no cutoff)."""
    incidence = defaultdict(set) # (context, component-content) -> accepted tuples
    contexts_by_tuple = defaultdict(set)
    for w in L:
        N = len(w)
        if d == 1:
            occurrences = (((w[i:j],), (w[:i], w[j:]))
                           for i in range(N) for j in range(i+1,N+1))
        else:
            occurrences = (((w[i:j], w[k:l]), (w[:i], w[j:k], w[l:]))
                           for i in range(N) for j in range(i+1,N)
                           for k in range(j+1,N) for l in range(k+1,N+1))
        for x, E in occurrences:
            incidence[(E, tuple(map(content, x)))].add(x)
            contexts_by_tuple[x].add(E)
    for (E,_), accepted in incidence.items():
        if len(accepted) < 2: continue
        for x in accepted:
            for y in accepted:
                if x == y: continue
                for F in contexts_by_tuple[x]:
                    if fill(F, y) not in L:
                        return goodstep(L, E, x, y, F)
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--scan', action='store_true', help='exact finite SUB1/SUB2 scans for small models')
    args = ap.parse_args()

    L, cert, f, g, Z = example_same_label()
    print('SAME_LABEL |L|=%d f=%r g=%r Zf=%r Zg=%r' %
          (len(L), f, g, sorted(Z[f]), sorted(Z[g])))
    print('SAME_LABEL_CERT',cert)
    assert frame_conflict(L) is not None
    print('SAME_LABEL_OVERLAP_COMPONENTS', overlap_components(L))
    for n in (2,3):
        L = candidate_a(n)
        c = verify_scissors(n,L)
        incidence, classes = frame_classes(L)
        f, g = c['x'], c['y']
        assert content(f[0]) == content(g[0])
        assert content(f[1]) == content(g[1])
        assert 'c' in incidence[f] & incidence[g]
        assert 'ba' in incidence[f] and 'ba' not in incidence[g]
        print('A n=%d |L|=%d active_frames=%d (outline,Z)-groups=%d'
              ' sizes: |Z(f)|=%d |Z(g)|=%d' %
              (n, len(L), len(incidence), len(classes), len(incidence[f]), len(incidence[g])))
        print('A_OVERLAP_COMPONENTS', overlap_components(L))
        print('A_N9_CERT',c)
    for n in (1,2,3,4):
        print('B_LAYER n=%d grammar_size=%d theta=%d mu_ab=%d short_letters=abc'
              % (n, *check_layer(n)))
    for n in (1, 2):
        L = exact_layer_words(n)
        assert frame_conflict(L) is None
        incidence = all_frames(L)
        by_outline = defaultdict(list)
        for f, Z in incidence.items():
            by_outline[(content(f[0]), content(f[1]))].append((f, Z))
        for entries in by_outline.values():
            for (f, Z), (g, Z2) in combinations(entries, 2):
                if len(f[0])+len(f[1]) == len(g[0])+len(g[1]):
                    assert Z == Z2
                else:
                    assert Z.isdisjoint(Z2)
        assert finite_sub_failure(L,1) is None and finite_sub_failure(L,2) is None
        print('B_EXACT n=%d |L|=%d overlap_components=%r' % (n, len(L),overlap_components(L)))
    if args.scan:
        for name, L in (('same_label', example_same_label()[0]),('A2',candidate_a(2))):
            for d in (1,2):
                print('SCAN', name, 'SUB',d,finite_sub_failure(L,d))
    print('PASS: all assertions; no numerical observation was used as a membership proof.')


if __name__ == '__main__':
    main()

```
