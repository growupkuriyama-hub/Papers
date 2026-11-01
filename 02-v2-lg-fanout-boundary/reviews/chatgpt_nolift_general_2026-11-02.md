# ファンアウト2における希少型の長語――冪を用いない二穴剛性と overlap-free 因子の局所障害

**研究日**：2026-11-02　**対象**：栗山貴之 #2 論文（作業版 `02-v2-lg-fanout-boundary/main.tex`）　**判定基準**：「証明済み」は本文中の論証（有限分類の場合は明示的な証明書と完全列挙法）を指し、独立査読・文献的初出性は意味しない。

## 0. 主張と判定（最初に読む）

| ID | 主張 | 判定 | 根拠・条件 |
|---|---|---|---|
| R1 | 希少型に属する語がただ一つ `W` なら `{W}` 自身が `(f,s)`-tuple-substitutable。二穴の「自己衝突」は、標的の他の語をどう加えても修復不能 | **証明済み** | §2、任意の `f≥1`・有限半群型付け、任意の非空 `W` |
| R2 | `U₁` で `a,b↦1`, `c↦ζ` とし `W` が唯一の型 `1` の語なら、`W∈{a,b}*` の各長さ **7** の因子は overlap を含む | **証明済み（24語／6対称類の明示的有限分類）** | §3、表1、§7。`f≥2`、ランク不問 |
| R3 | 内容型付け `c_{\{a,b,c\}}` で `W` が唯一の内容 `{a,b}` の語なら、`W∈{a,b}*` の各長さ **13** の因子は overlap を含む | **証明済み（60語／15対称類の明示的有限分類）** | §4、表2、§7。`f≥2`、ランク不問 |
| R4 | 従って `W` 自身が二元 overlap-free なら、`U₁` の場合 `|W|≤6`、内容型付けの場合 `|W|≤12` | **証明済み** | R2・R3 の系、§3–4 |
| R5 | Thue–Morse の `A_n=μ^n(a)` を唯一の希少型語とする **任意の天井構成**は、`U₁` で `n≥3`、内容型付けで `n≥4` なら `(2,s)` 条件に反する | **証明済み** | §5、R2・R3。文法の分岐・サイズによらない |
| R6 | 素朴な規則 `A_i→A_{i−1}B_{i−1} \mid cA_{i−1}c` と対称な `B_i` は `n=2` で **1穴** 条件から破綻 | **反証** | §6.1、明示的な違反。`U₁` と内容型付け両方 |
| R7 | 原稿の三文字倍増族は `U₁` で `n=2`、内容型付けで `n=3` に既に2穴条件の反例がある | **観察／具体的反例は証明** | §6.2、完全列挙。原稿定理Cはより一般に大きい `n` を除外 |
| R8 | 一元語 `{a^N}` は任意の `f≥1` で `U₁`-tuple-substitutable。ゆえに R2 の局所反復の密度は `|W|` の定数上界を意味しない | **証明済み** | §5.3、全 arity を直接証明 |
| R9 | `f≥2`・固定 `s` の有限 `L∈C_{f,s}` にある型の唯一語 `W` について、`|W|≤poly(‖G‖,θ̄_G)` | **未解決** | §8：R2・R3 からは出ない |
| R10 | `op:fanout-two` およびすべての `f≥2` にわたる LG 境界の決着 | **未解決** | §8–9：本研究は反例族を構成していない |
| R11 | R2–R4 の文献的初出性 | **未確認** | §10、個々の二穴証明書と既知の Thue–Morse 定理は区別 |

**結論**：N1（一般の超多項式反例族）も N2（一般の多項式上界）も未解決。ただし、**冪を含まない語であっても「二穴自己衝突」が希少型の一意性を破る**という、`lem:power-transfer` の冪移行とは別の、定量的な局所禁止因子定理（長さ 7／13）を得た。

## 1. 正本・定義・評価範囲

- **現在確認した論文原稿**：`https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex`、Git blob SHA **`f238b751ea60bfa48a09cef5dd25b8b5327944c0`**。2026-11-02 に GitHub 接続から取得した作業版。旧 `02_fixed-h-mcfg` をこの版の代用にはしない。
- 原稿 §2–§4：`def:standard-mcfg`、`def:grammar-properties`、`def:tuple-occurrence`、`def:tuple-substitutable`、`def:class-cmcf`。**穴は非空であり、2穴の中間固定部も非空**。比較するのは成分ごとの `s` 型である。
- 原稿 `lem:type-deletion`、`lem:no-insertion`、`prop:rare-type`、`prop:three-letter-family`、`cor:typing-level-obstruction`、`lem:power-transfer`、`thm:doubling-no-lift`、`lem:typing-monotone`、`prop:sl-reduction`、`thm:two-letter-content`、`op:fanout-two` を確認した。
- 過去レビュー `reviews/claude_ternary_content_2026-11-01.md`、`reviews/chatgpt_single_neutral_letter_2026-11-02.md`、`reviews/chatgpt_gap_linear_factor_2026-11-02.md` を GitHub から確認した。前者が示す `n≥3` での倍増族の内容型付け違反および「共役移送」と、後二者の既存論点は**独立の新主張として再計上しない**。この報告の中心は「冪なし」の長さ 7／13 の有限証明書とその任意長への移送である。

`U₁={1,ζ}` は `ζ²=ζ, 1ζ=ζ1=ζ` とする。`s_U(a)=s_U(b)=1`, `s_U(c)=ζ`。内容型付け `c_Σ(w)` は文字集合。`L∈C_{f,s}` とは `L` がファンアウト `≤f` の MCFL であり、**すべての arity `1≤d≤f`** について、同じ成分型で共通許容文脈を持つ二つの非空タプルの分布が等しいこと。

記号 `E=(p,t,q)` は2穴文脈 `p□₁t□₂q`（**`t≠ε`**）を意味する。`E[x]` は成分 `x=(x₁,x₂)` の挿入後の語である。overlap は `zuzuz`（`z` は一文字、`u` は空でもよい）の形の因子。`aaa` や `ababa` は overlap であり、overlap-free は cube-free より強い。

## 2. 原理：唯一型語の二穴自己衝突と因子への遺伝

### 補題 2.1（唯一型の剛性、任意の arity）【証明済み】

`L∈C_{f,s}`、`m∈S`、`L∩s^{-1}(m)={W}`（`W∈Σ⁺`）とする。`1≤d≤f`、非空成分のタプル `x,y` が `s^(d)(x)=s^(d)(y)` を満たすとする。許容 `d`-文脈 `E,F` が

```
E[x]=E[y]=F[x]=W
```

を満たすなら **`F[y]=W`** が必要である。特に `{W}` はそれ自身 `(f,s)`-tuple-substitutable であり、単語言語は 1-MCFL だから `{W}∈C_{f,s}` である。

**証明**。`E[x],E[y]∈L` と型一致により、代入可能性から `D_L^(d)(x)=D_L^(d)(y)`。`F[x]=W∈L` なら `F[y]∈L`。型付けは半群準同型であり、固定部が空の場合は空語を区別する単位元補完を使えば `s(F[y])=s(F[x])=m`。従って一意性から `F[y]=W`。`{W}` について、共通受理文脈があれば必ずその両方が `W` を作るので、上述の双方向の含意がすべての `F` に対して成立する。`d` は任意だったから全 arity を覆う。□

### 補題 2.2（禁止証明書は因子へ遺伝する）【証明済み】

`v∈Σ⁺` に対し、同型のタプル `x,y` と許容2文脈 `E,F` が

```
E[x]=E[y]=F[x]=v,   F[y]≠v
```

を満たしたとする。そのとき、**`v` を因子として含む語 `W=pvq` は、型 `s(W)` の唯一語として `(2,s)`-tuple-substitutable な言語に現れ得ない**。

**証明**。`E′=pEq`、`F′=pFq` は穴間の非空固定部を保つ許容文脈で、`E′[x]=E′[y]=F′[x]=W` かつ `F′[y]=pF[y]q≠W`。補題2.1に矛盾する。□

これは**全長の単語を小さい `n` だけ試して一般化した推測ではない**。有限個の短因子を禁止すると、補題2.2によって任意長へ移る点が一般部分の証明である。

## 3. 定理U：U₁型には長さ7の overlap-free 因子がない

### 定理 3.1【証明済み：有限の完全な場合分け付き】

`f≥2` とし、`L∈C_{f,s_U}` で `L∩s_U^{-1}(1)={W}` とする。このとき `W` のどの長さ7の因子も overlap-free ではない。従って `W` 自身が overlap-free なら **`|W|≤6`**。

**証明**。文字集合 `{a,b}` 上の長さ7の overlap-free 語は24個。文字交換 `a↔b` および語の反転の下で次の**6軌道**（各4語）に分かれる。表1の各行の `E,x,y,F` は、すべて `E[x]=E[y]=F[x]=v`、`F[y]≠v`、かつ `E,F` の中間固定部は非空である。`a,b` だけからできた全非空成分の `s_U` 型は1なので、成分ごとの型一致も満たす。

**表1：7文字の完全証明書。** 文脈とタプルはセミコロンで区切る。例えば `aa;a;b` は `aa□₁a□₂b` を意味する。

| 因子 v（軌道代表） | E | x | y | F | F[y]（異なる語） |
|---|---|---|---|---|---|
| `aabaabb` | `aa;a;b` | `ba;b` | `b;ab` | `aa;ab;` | `aababab` |
| `aababba` | `aab;b;` | `a;ba` | `ab;a` | `;a;bba` | `abaabba` |
| `aabbaab` | `a;b;ab` | `a;ba` | `ab;a` | `;ab;ab` | `ababaab` |
| `aabbaba` | `a;b;ba` | `a;ba` | `ab;a` | `;ab;ba` | `abababa` |
| `abaabab` | `a;a;ab` | `b;ab` | `ba;b` | `a;aab;` | `abaaabb` |
| `abaabba` | `a;a;ba` | `ba;b` | `b;ab` | `a;ab;a` | `abababa` |

有限分類の**網羅性**は、長さを一文字ずつ延ばす際に新たな末尾 overlap（長さ3,5,7）を拒否する漸化的列挙から確認できる。表の各軌道に4語があり合計24語を尽くすこと、各証明書の4つの等式・不等式・穴の条件は §7 の `verify_certificates(C7,7,'u1')` が直接検証する。反転は2穴の順序を逆に、文字交換は各成分の文字を交換するだけで、いずれも同型条件と非空セパレータを保存する。

任意の長さ7の overlap-free 因子はこの24語のどれかなので補題2.2により `W` に現れない。`W` 全体が overlap-free で長さ7以上なら、その先頭7文字が該当し矛盾。□

**より一般の型への拡張**：`a,b` が任意の固定型付けで同じ**冪等元** `e` に写り、`W∈{a,b}⁺` が唯一の型 `e` の語であれば、表1の同じ証明が成立する。文字を共有しない非空のコード語 `u,v` が同じ冪等型 `e` を持つ場合にも、表1の文字を `a↦u,b↦v` と置換できる。コードの非空性はセパレータを保ち、文字非共有性は異なるコード語列の像の相異を保証する。これは `cor:typing-level-obstruction` の着想と整合するが、**長い冪を仮定していない**。

## 4. 定理C：内容型にも長さ13の overlap-free 因子がない

### 定理 4.1【証明済み：有限の完全な場合分け付き】

`Σ={a,b,c}`、`f≥2`、`L∈C_{f,c_Σ}` とし、`L∩c_Σ^{-1}({a,b})={W}` とする。このとき `W` のどの長さ13の因子も overlap-free ではない。従って `W` が overlap-free なら **`|W|≤12`**。

**証明**。長さ13の二元 overlap-free 語は60個で、反転と `a↔b` の下で次の15軌道（各4語）に分かれる。表2の各行について

```
c_Σ(x₁)=c_Σ(y₁), c_Σ(x₂)=c_Σ(y₂)
E[x]=E[y]=F[x]=v, F[y]≠v
```

が直接成立する。特に両タプル成分の内容型が**それぞれ**一致するので、`U₁` の粗い型に頼った議論ではない。表の `E,F` の中央固定部はすべて非空である。

**表2：13文字の完全証明書。** 各行は `v | E | x | y | F`。`F[y]` は必ず異なる13文字語であり、§7のコードが全文を再計算する。

| v | E | x | y | F |
|---|---|---|---|---|
| `aabaabbaababb` | `aa;a;abb` | `baabb;ab` | `ba;bbaab` | `aa;aab;b` |
| `aabaabbabaaba` | `aabaabb;a;` | `ab;aba` | `aba;ba` | `a;aabb;aba` |
| `aabaabbabaabb` | `aa;b;aabb` | `baab;ab` | `baa;bab` | `aa;baba;b` |
| `aababbaabbaba` | `a;a;baba` | `ababb;ab` | `ab;bbaab` | `a;aabb;a` |
| `aababbabaabab` | `aa;b;aabab` | `ba;bab` | `bab;ab` | `aa;bbabaa;` |
| `aababbabaabba` | `aa;b;aabba` | `bab;ab` | `ba;bab` | `aa;baba;ba` |
| `aabbaababbaab` | `a;a;bbaab` | `abba;ba` | `abb;aba` | `a;abab;ab` |
| `aabbaababbaba` | `aabbaa;b;a` | `ba;bab` | `bab;ab` | `aab;a;baba` |
| `aabbabaababba` | `aabb;a;bba` | `ab;aba` | `aba;ba` | `a;b;ababba` |
| `aabbabaabbaab` | `a;ba;baab` | `ab;baab` | `abba;ab` | `a;babaab;` |
| `abaababbaabab` | `;a;bbaabab` | `ab;aba` | `aba;ba` | `;aababba;b` |
| `abaababbaabba` | `;a;bbaabba` | `aba;ba` | `ab;aba` | `;abab;abba` |
| `abaababbabaab` | `;a;bbabaab` | `ab;aba` | `aba;ba` | `;aababb;ab` |
| `abaabbaababba` | `;a;ababba` | `ab;abba` | `aba;bba` | `;aabbaab;` |
| `abaabbabaabab` | `abaabb;a;b` | `ab;aba` | `aba;ba` | `;aabb;abab` |

**分類の完全性の理由**：各長さ `k+1` の overlap-free 語は長さ `k` の overlap-free 語に `a` または `b` を付けてでき、末尾に新しくできた `zuzuz` を拒否すれば漏れはない。これを `k=0,...,12` に適用した13文字の集合は60語であり、表2の15軌道がちょうど覆う。`verify_certificates(C13,13,'content')` は**被覆集合の等号**と各行の全条件を assert で検査する。最後は補題2.2により任意長へ拡張する。□

**重要な区別**：R2とR3は「特定の語を全数検査してみたら通らなかった」という有限観察だけではない。**有限個の全可能因子を完全分類して各々に反証明書を与え、因子遺伝補題を使う**ことで、全長にわたる禁止因子定理を証明している。ただし表の網羅性と転記について独立の査読はまだない。

## 5. Thue–Morse 倍増族への帰結と一般的な組合せ制約

### 5.1 両型付けでの非持ち上げ【証明済み】

`A₀=a,B₀=b`、`A_{n+1}=A_nB_n`, `B_{n+1}=B_nA_n`。`A_n=μ^n(a)` で `μ(a)=ab,μ(b)=ba`、`|A_n|=2^n`。古典的に無限 Thue–Morse 語は overlap-free（したがってすべての有限 prefix `A_n` も overlap-free）。

`U₁` で `A_n` が唯一の中立型語なら `2^n≤6`、従って `n≤2`。内容型付けで `A_n` が唯一の `{a,b}`-内容語なら `2^n≤12`、従って `n≤3`。**いずれも他の分岐で作る `c` 入りの語に一切依存しない**。また、どちらも `d=2` の違反なので任意の `f≥2` に適用できる。

参考出典：Jean Berstel, Aaron Lauve, Christophe Reutenauer, Franco Saliola, *Combinatorics on Words*, Chapter 2, Theorem 2.6（Thue–Morse は overlap-free）<https://webpages.math.luc.edu/~lauve/papers/wordsbook.pdf>。また Brown, Rampersad, Shallit, Vasiga (2006), *Squares and overlaps in the Thue–Morse sequence and some variants*, RAIRO-ITA 40(3), 473–484, <https://www.numdam.org/item/ITA_2006__40_3_473_0/>。

### 5.2 短い明示的な破綻（一般定理に頼らない確認）

**`U₁`、`n=3`**：`A₃=abbabaab`。`x=(a,ba)`、`y=(ab,a)`、`E=□₁b□₂baab`、`F=□₁bba□₂ab` と置く。実際、

```
E[x] = a + b + ba + baab = abbabaab
E[y] = ab + b + a + baab = abbabaab
F[x] = a + bba + ba + ab = abbabaab
F[y] = ab + bba + a + ab = abbbaaab ≠ abbabaab
```

全成分が中立型1で、二つの中央固定部は `b`, `bba` とも非空。唯一の中立語が `A₃` なら矛盾する。**これは大きな冪の移行ではなく、二穴の切断位置をずらす局所衝突**である。

**内容型付け、`n=4`**：`A₄=abbabaabbaababba`。`x=(ab,baab)`、`y=(abba,ab)`、`E=□₁ba□₂baababba`、`F=□₁babaab□₂abba` と置く。各成分の内容は両タプルとも `{a,b}`。また

```
E[x] = E[y] = F[x] = abbabaabbaababba
F[y] = abba + babaab + ab + abba = abbababaabababba
```

で相異なり、しかも `F[y]` は内容 `{a,b}`。最後の等号は文字列の通常の連結である。したがって内容 `{a,b}` の唯一性に反する。

### 5.3 なぜ一般の長さ多項式上界にはならないか

**命題**：任意の `N≥1`、`{a^N}` は `U₁` の下で、**すべての arity `1≤d≤f`** に対して代入可能である（任意の `f`）。

**証明**。任意の共有受理文脈 `E` において `E[x]=E[y]=a^N`。各成分も固定部も `a` の冪なので、`Σ_i |x_i|=Σ_i |y_i|`。別の許容文脈 `F` が `F[x]=a^N` を満たせば、`F` の固定部も `a` のみで、`F[y]` の総長は `N`、よって `F[y]=a^N`。逆向きも同様。`d` は任意。□

従って、局所定理は「長い語そのものを禁止」しない。**長い語には短い overlap が密に存在しなければならない**と主張しているだけで、長い冪のような反復的な構造は許す。`{a^{2^n}}` の straight-line grammar はサイズ `O(n)` でも、最上位の規則が長い受理語にしか使えず `θ̄_G≥2^n`。この例は N2 の所望の `poly(‖G‖,θ̄_G)` 上界を否定しない。

### 5.4 一般化できる「二穴の形の剛性」

`U₁` の下で、唯一中立語 `W` が因子 `abba` を含むとする。`x=(a,ba)`、`y=(ab,a)` は共通文脈 `□₁b□₂` で同じ `abba` を与える。補題2.1・2.2から、もし `W` の別の分解が `W=p a q ba r`（**`q∈{a,b}⁺`**）なら

```
W = p a q ba r = p ab q a r
```

が必要であり、自由モノイドの左右消去により **`q b=b q`**、すなわち `q∈b*`。従って `abba` を含む唯一中立語には、`a ... ba` の二つの穴を隔てる語 `q` に強い制限がかかる。これは `power-transfer` の冪の存在を仮定しない、**明示的な因子配置制約**である。

## 6. 具体的な文法候補の検査

### 6.1 素朴な天井つき Thue–Morse 文法【失敗は証明】

`S→A_n`、`A₀→a`、`B₀→b`、`i≥1` について

```
A_i → A_{i−1} B_{i−1}  |  c A_{i−1} c
B_i → B_{i−1} A_{i−1}  |  c B_{i−1} c
```

とする。生成には `B_n` が不要なので、**reduced な表示では `B_0,...,B_{n-1}` だけを残す**。するとこれは reduced good、ファンアウト1、ランク2、`‖G_n‖=22n−1`（標準 MCFG の式で数える）、`θ̄_G=O(n)` の文法である。各レベルの `c`-wrap は長さ `2i+1` 以下の生成語を持ち、任意のレベルの二分岐を一度使って残りを `c`-wrap にすれば成功語の長さは `O(n)`。`c`-free 語はただ一つ `A_n`。**必要なサイズと厚さは満たすが、代入可能性に失敗する。**

`n=2` では

```
L(A₂) = {abba, abcbc, cacba, caccbc, cabc, ccacc}
```

（辞書順と順序は無関係）。1穴で `x=abc`、`y=ca`、`E=□bc`、`F=c□` とすると、両方の型は `ζ` であり、

```
E[x]=abcbc ∈ L(A₂),  E[y]=cabc ∈ L(A₂)
F[x]=cabc ∈ L(A₂),  F[y]=cca ∉ L(A₂).
```

よって `(1,s_U)` に違反し、したがって `(2,s_U)` にも違反する。実際 `c_Σ(abc)=c_Σ(ca)` は**成り立たない**ので、この特定の1穴証明書は内容型付けには転用しない。内容型付けでは別の1穴違反を使う：`x=ca`, `y=cacc`, `E=□bc`, `F=□cba` とすると `c_Σ(x)=c_Σ(y)={a,c}`、`E[x]=cabc`, `E[y]=caccbc`, `F[x]=cacba` はいずれも受理される一方、`F[y]=cacccba` は非受理である。

※ `‖G_n‖` は到達不能な `B_n` とその2規則を削除し、開始規則を一つ、`A₀,B₀` をそれぞれ一つの定数規則として数えた値（`|V|=2n+2`、規則コスト合計 `20n−3`）。`θ̄_G` の評価には、成功導出で対象規則を使用するための外側の `c`-wrap の長さも含めている。

### 6.2 原稿の三文字倍増族との比較

原稿 `G_n` は `S→E_n`, `E₀→a`, `E_i→bE_{i−1}E_{i−1}b | cE_{i−1}c`。`‖G_n‖=13n+7`, `θ̄_G=4n`, 唯一の `c`-free 語は `W_n`、`|W_n|=3·2^n−2`。原稿が証明するのは `(1,s)` の代入可能性と、その希少型からの指数下界である。

有限計算で `n=1,2,3` を調べたところ、`U₁` は `n=2` で2穴違反、内容型付けは `n=3` で2穴違反を確認した。これらは既存のレビュー `claude_ternary_content_2026-11-01.md` の結論と整合する。原稿の `thm:doubling-no-lift` は有限半群型付け**全般**に対して十分大きい `n` を排除する、別の一般定理である。

**`lem:no-insertion` との整合**：本報告の否定証明書では `E[x]=E[y]` なので、タプルの総長は等しい。証明書は穴の中身の「挿入による伸長」ではなく、同じ全長の**非自明な再配分**によるもの。従って `lem:no-insertion` と矛盾しない。むしろ挿入なしでも二穴条件が破れることを示す。

### 6.3 全数検査結果と n=4 の扱い

下の表の「PASS」は対象言語に出現する**全**許容文脈と、各文脈に共通して出現する全同型タプル対を調べて違反がなかったこと。「FAIL」は実際の `E,x,y,F` と `F[y]∉L` を出力した**確定した反例**。「—」は検査していないことを示す。

| 族 | n | 言語サイズ | U₁ d=1 | U₁ d=2 | 内容 d=1 | 内容 d=2 |
|---|---:|---:|---|---|---|---|
| 天井 Thue–Morse | 1 | 2 | PASS | PASS | PASS | PASS |
| 天井 Thue–Morse | 2 | 6 | FAIL | FAIL | FAIL | FAIL |
| 天井 Thue–Morse | 3 | 42 | FAIL | FAIL | FAIL | FAIL |
| 天井 Thue–Morse | 4 | 1806 | — | FAIL（長さ7証明書） | — | FAIL（長さ13証明書） |
| 原稿の倍増族 | 1 | 2 | PASS | PASS | PASS | PASS |
| 原稿の倍増族 | 2 | 6 | PASS | FAIL | PASS | PASS |
| 原稿の倍増族 | 3 | 42 | PASS | FAIL | PASS | FAIL |
| 原稿の倍増族 | 4 | 1806 | — | FAIL（W₂の自己衝突を埋め込み） | — | FAIL（W₃の自己衝突を埋め込み） |

`n≤3` は各言語について `d=1,2` の完全列挙を実行。`n=4` は候補が各1806語に増えるため、**完全列挙したとは主張しない**。代わりに希少語の短い因子に対する明示的な2穴証明書の埋め込みで不合格とした。`n=4` での `PASS` は主張していない。

## 7. 再現用 Python 3 プログラム（標準ライブラリのみ・全文）

保存名：`nolift_exhaustive_2026-11-02.py`。Windows では `py -3 nolift_exhaustive_2026-11-02.py`。プログラムは `(1,s)`,`(2,s)` を全列挙し、**全タプル出現・全許容2文脈・同成分型で共通文脈を持つ組**を辞書に集約して比較する。さらに長さ7／13の**全 overlap-free 語が表の対称軌道に覆われることと、各反例の式を別途検証**する。

```python
#!/usr/bin/env python3
# Python 3 standard library only. Windows: py -3 nolift_exhaustive_2026-11-02.py
from collections import defaultdict

C7 = '''
aabaabb|aa;a;b|ba;b|b;ab|aa;ab;
aababba|aab;b;|a;ba|ab;a|;a;bba
aabbaab|a;b;ab|a;ba|ab;a|;ab;ab
aabbaba|a;b;ba|a;ba|ab;a|;ab;ba
abaabab|a;a;ab|b;ab|ba;b|a;aab;
abaabba|a;a;ba|ba;b|b;ab|a;ab;a
'''
C13 = '''
aabaabbaababb|aa;a;abb|baabb;ab|ba;bbaab|aa;aab;b
aabaabbabaaba|aabaabb;a;|ab;aba|aba;ba|a;aabb;aba
aabaabbabaabb|aa;b;aabb|baab;ab|baa;bab|aa;baba;b
aababbaabbaba|a;a;baba|ababb;ab|ab;bbaab|a;aabb;a
aababbabaabab|aa;b;aabab|ba;bab|bab;ab|aa;bbabaa;
aababbabaabba|aa;b;aabba|bab;ab|ba;bab|aa;baba;ba
aabbaababbaab|a;a;bbaab|abba;ba|abb;aba|a;abab;ab
aabbaababbaba|aabbaa;b;a|ba;bab|bab;ab|aab;a;baba
aabbabaababba|aabb;a;bba|ab;aba|aba;ba|a;b;ababba
aabbabaabbaab|a;ba;baab|ab;baab|abba;ab|a;babaab;
abaababbaabab|;a;bbaabab|ab;aba|aba;ba|;aababba;b
abaababbaabba|;a;bbaabba|aba;ba|ab;aba|;abab;abba
abaababbabaab|;a;bbabaab|ab;aba|aba;ba|;aababb;ab
abaabbaababba|;a;ababba|ab;abba|aba;bba|;aabbaab;
abaabbabaabab|abaabb;a;b|ab;aba|aba;ba|;aabb;abab
'''

def occurrences(w, arity):
    """All occurrences of nonempty holes; separators are strictly nonempty."""
    n = len(w)
    if arity == 1:
        for i in range(n):
            for j in range(i + 1, n + 1):
                yield (w[:i], w[j:]), (w[i:j],)
    elif arity == 2:
        for i in range(n):
            for j in range(i + 1, n):
                for k in range(j + 1, n):
                    for l in range(k + 1, n + 1):
                        yield (w[:i], w[j:k], w[l:]), (w[i:j], w[k:l])
    else:
        raise ValueError('This experiment covers arities 1 and 2.')

def plug(context, components):
    return ''.join(a + b for a, b in zip(context, components)) + context[-1]

def typ(components, typing):
    if typing == 'u1':
        return tuple(1 if 'c' not in component else 0 for component in components)
    if typing == 'content':
        return tuple(frozenset(component) for component in components)
    if typing == 'trivial':
        return tuple(1 for _ in components)
    raise ValueError(typing)

def exhaustive(language, arity, typing):
    """Checks the entire finite language and all admissible occurrences.

    If it fails, returns an exact witness (E,x,y,F,F[x],F[y]).
    Returns None if and only if the arity condition holds.
    """
    language = set(language)
    by_context = defaultdict(set)
    by_tuple = defaultdict(set)
    for w in sorted(language):
        for e, x in occurrences(w, arity):
            by_context[e].add(x)
            by_tuple[x].add(e)
    for e in sorted(by_context):
        grouped = defaultdict(list)
        for x in sorted(by_context[e]):
            grouped[typ(x, typing)].append(x)
        for xs in grouped.values():
            for i, x in enumerate(xs):
                for y in xs[i+1:]:
                    for f in sorted(by_tuple[x] ^ by_tuple[y]):
                        if f in by_tuple[x]:
                            first, second = x, y
                        else:
                            first, second = y, x
                        if plug(f, second) not in language:
                            return (e, first, second, f,
                                    plug(f, first), plug(f, second))
    return None

def thue_morse(n):
    a, b = 'a', 'b'
    for _ in range(n):
        a, b = a + b, b + a
    return a

def ceiling_tm(n):
    a, b = {'a'}, {'b'}
    for _ in range(n):
        a, b = ({u + v for u in a for v in b} |
                {'c' + u + 'c' for u in a},
                {u + v for u in b for v in a} |
                {'c' + v + 'c' for v in b})
    return a

def original_doubling(n):
    words = {'a'}
    for _ in range(n):
        words = ({'b' + x + y + 'b' for x in words for y in words} |
                 {'c' + x + 'c' for x in words})
    return words

def last_overlap(w):
    n = len(w)
    # For k >= 1, an overlap of length 2*k+1 ending at the last letter.
    return any(w[n-2*k-1:n-k] == w[n-k-1:n]
               for k in range(1, (n-1)//2 + 1))

def overlap_free_words(n):
    words = ['']
    for _ in range(n):
        words = [w + ch for w in words for ch in 'ab'
                 if not last_overlap(w + ch)]
    return set(words)

def orbit(w):
    table = str.maketrans('ab', 'ba')
    c = w.translate(table)
    return {w, w[::-1], c, c[::-1]}

def verify_certificates(rows, n, typing):
    words = overlap_free_words(n)
    covered = set()
    for raw in rows.strip().splitlines():
        w, e, x, y, f = raw.split('|')
        e, x, y, f = (tuple(z.split(';')) for z in (e, x, y, f))
        assert len(w) == n
        assert len(e) == len(f) == 3 and len(x) == len(y) == 2
        assert e[1] and f[1] and all(x) and all(y)
        assert typ(x, typing) == typ(y, typing)
        assert plug(e, x) == plug(e, y) == plug(f, x) == w
        assert plug(f, y) != w
        assert w in words
        covered.update(orbit(w))
    assert words == covered, (n, len(words), len(covered))
    print('CERTIFICATES', typing, 'length', n, 'cases', len(rows.strip().splitlines()),
          'total words', len(words), 'verified')

def check_family(name, make, maximum):
    for n in range(1, maximum + 1):
        lang = make(n)
        print('FAMILY', name, 'n', n, 'size', len(lang),
              'longest', max(map(len, lang)))
        for t in ('u1', 'content'):
            for d in (1, 2):
                v = exhaustive(lang, d, t)
                if v is None:
                    print(' ', t, 'arity', d, 'PASS (complete)')
                else:
                    print(' ', t, 'arity', d, 'FAIL (exact certificate)',
                          'E=',v[0], 'x=',v[1], 'y=',v[2],
                          'F=',v[3], 'F[y]=',v[5])

def main():
    verify_certificates(C7, 7, 'u1')
    verify_certificates(C13, 13, 'content')
    for n in range(1, 5):
        w = thue_morse(n)
        print('THUE-MORSE', n, w)
        for t in ('u1','content'):
            v = exhaustive({w}, 2, t)
            print(' ', t, 'arity 2', 'PASS (complete)' if v is None
                  else 'FAIL (exact certificate)',
                  '' if v is None else ('E='+str(v[0])+' x='+str(v[1])+
                                      ' y='+str(v[2])+' F='+str(v[3])))
    check_family('naive-ceiling', ceiling_tm, 3)
    check_family('original-doubling', original_doubling, 3)
    # At n=4 both full ceiling languages are large (1806 strings).
    # Rather than claim an incomplete all-occurrence audit, use the
    # exact 16-letter content certificate: it is inherited by any language
    # whose unique c-free word is thue_morse(4).
    w = thue_morse(4)
    v = exhaustive({w}, 2, 'content')
    assert v is not None and 'c' not in v[5] and v[5] != w
    for name, make in [('naive-ceiling', ceiling_tm)]:
        lang = make(4)
        assert {z for z in lang if 'c' not in z} == {w}
        assert v[5] not in lang
        print('FAMILY', name, 'n 4 size',len(lang),
              'FAIL by exact inherited content certificate; not a full audit')

if __name__ == '__main__':
    main()
```


### 実行ログの要約

実行コマンド：`py -3 nolift_exhaustive_2026-11-02.py`。`CERTIFICATES u1 length 7 cases 6 total words 24 verified`、`CERTIFICATES content length 13 cases 15 total words 60 verified` を確認。Thue–Morse 単語言語での arity 2 は `n=1,2` とも U₁・内容とも PASS、`n=3` で U₁ FAIL・内容 PASS、`n=4` で両方 FAIL。天井つき族は `n=1` で両 arity・両型とも PASS、`n=2,3` で全て FAIL。原稿倍増族は §6.3 の表のとおり。

コードが検査するのは全ての出現から作られる**観察分布**。有限言語 `L` の全語を入力した場合、正の分布に現れる文脈は必ずどこかの出現で列挙され、分布が空のタプルは共通文脈を持てない。したがって arity 1,2 のこの方法は対象となる有限言語について完全である。異なるタプルに共通の文脈があり、分布集合が異なるとき、`F[x]∈L`, `F[y]∉L` を明示的に検査する。表1・2の証明書では逆に、*独立して* 諸等式を直接 assert している。

詳細な実行出力は同梱の `nolift_exhaustive_results_2026-11-02.txt` を参照できる。

## 8. N2：一般の多項式上界に何が足りないか

### 8.1 証明できた一般化の正確な範囲

R2 と R3 から、以下の二つの**局所的な必要条件**が従う。

1. `U₁`、唯一の中立型語 `W∈{a,b}⁺`：**どの長さ7の因子にも** `zuzuz` 形の overlap がある。
2. 内容型付け `c_{\{a,b,c\}}`、唯一の内容 `{a,b}` の語 `W`：**どの長さ13の因子にも** overlap がある。

これらは非冪型の交換――同一語に2穴を置く位置のずれ――を直接捉える。「`W` が短い反復を一切持たないために power-transfer を回避する」という方針を強く制限するが、**同じ型の語が真の因子にならないことや、短い周期を密に含むことだけでは `|W|≤poly(‖G‖,θ̄_G)` を導かない**。

一般の有限半群型付けでは、表のタプルの型一致が壊れることもある。内容型付けの場合ですら、長さ13の overlap-free 因子を持たないことは個別の文法の短い導出への変換を保証しない。`r_max` に依存する定数幅の「重い節点」議論へ直接つながるほど強い複雑度評価には至っていない。

### 8.2 N2 の有力な次の補題候補（**未証明**）

原稿付録の `two-letter-content` の `x` 塊の再配分と、先行レビューの「除外文字の消去」を結ぶため、次の形が焦点になる：

> 固定内容型付けで、長さを増大させる導出部分木の類に現れる、短い反復を密に含む成分から、**内容型を変えずに**短い代表を得るための局所短縮規則が存在するか。

二穴自己衝突の排除は、語が短い overlap を**含む**ことを強制する。したがって次は、overlap を一つずつ「強制的な分布等価」に転換できるか、という逆方向の問題になる。これは本報告では解けていない。また、正の特徴標本の上界には `τ(G,s)` などの*意味的代表長*を制御する必要があり、希少な型の最短根語だけを抑えても十分とは限らない。

### 8.3 限界を確認する独立例

`L={a^N}` はすべての `f` において `C_{f,s_U}` に属し、`N` を任意に大きくできる。しかし reduced good な表示で **その唯一の成功語にしか使えない開始規則**の rule thickness は少なくとも `N` である。したがってこれを「小さな厚さで長い語」の反例と数えることはできない。同様に `L={μ^n(a)}` の小さな straight-line grammar は `θ̄` が指数になるため、たとえ二穴条件を満たしたとしても N1 に要求された短い厚さの条件とは別である。

## 9. N3：原稿の境界問題・特徴標本との関係

| 仮定または成果 | 原稿のどの事実へ接続するか | 結論の厳密な範囲 |
|---|---|---|
| **本報告 R2–R5** | `thm:doubling-no-lift` を冪以外の原因で補強 | Thue–Morse 型の**唯一希少語**構成は U₁ `n≥3`、内容型付け `n≥4` で不可能。`op:fanout-two` はなお未解決 |
| N1：例えば固定 `s_U`、`f=2`、ランク `≤r_max` で `L_n∈C_{2,s_U}`、唯一型語 `W_n` が超多項式長、`‖G_n‖,θ̄_{G_n}=poly(n)` **を本当に構成できた場合** | `lem:type-deletion` → `prop:rare-type` | `B^{≤r_max}_{2,s_U}` と `B_{2,s_U}` の全特徴標本、およびクラス全体に特徴標本を持つ任意の集合駆動作用素の全特徴標本は、型1の語を含み、`‖F‖_+≥|W_n|+1`。ランク条件は `G_n` のランクを明記（通常 `r_max≥2` の構成が狙い） |
| 同じ N1 構成 | `lem:typing-monotone`。`s_U≼c_Σ` | **同一対象言語が** `C_{2,c_Σ}` に入る。`B^{≤r_max}_{2,c_Σ}` と `B_{2,c_Σ}` の特徴標本から `s_U` のものに移行し、同じ下界が従う。必要なのは `{a,b}` などへの内容の割当の整合性 |
| 固定 `f=2` の反例によって `SL` が一様多項式データ長を持たないと分かった場合 | `prop:sl-reduction`、`thm:local-group-polydata` | **fan-out 2 における**一様多項式性の擬多様体境界が `LG` であると結論できる |
| **すべての `f≥2`** の LG 境界を言いたい場合 | 各 `f` ごとに `prop:sl-reduction` | `C_{2,s}` の反例は、自動的には `C_{f,s}` (`f>2`) の反例ではない。**全 arity `d≤f`** の代入可能性を別途示すか、反例を各 `f` に供給する一般的な持ち上げ定理が必要 |
| N2 の多項式上界を任意の固定 `s,f≥2` で得た場合 | `prop:rare-type` の機構だけを制限 | 唯一型語による希少型下界が多項式止まりになる。ただし多語・多型の代表長まで制御しない限り `op:fanout-two` 全体の肯定解とはならない |

**作用素／アルファベット／ランクの厳密な区別**：本報告は**新しい超多項式下界を証明していない**。原稿にある既存の `f=1` 指数下界は、`Σ={a,b,c}`・`s_U(a)=s_U(b)=1`, `s_U(c)=ζ`・ランク2・`‖G_n‖=13n+7`, `θ̄_G=4n` という条件に対し、`B^{≤r}_{1,s_U}` (`r≥1`)、`B_{1,s_U}`、および `C_{1,s_U}` 全体に特徴標本を持つ集合駆動作用素に対して `‖F‖_+≥3·2^n−1` を与える。今回の議論でこれを `f=2` に移してはいない。

**N1 の成功を宣言するための検証チェック**：対象族が有限であること、reduced good なファンアウト・ランク・文法サイズ・厚さを正確に評価すること、**全 `d=1,...,f`** の同型タプルと許容文脈について代入可能性を一般の `n` で証明すること、型 `m` の語の一意性または十分大きな `μ_m(L_n)` を証明すること、`lem:no-insertion` と矛盾しないこと、最後に `prop:rare-type` で作用素ごとの下界を導くことが必要である。少数の `n` の PASS だけでは十分ではない。

## 10. 文献的位置づけ・今後の方針・再現性

Thue–Morse の overlap-free 性とその倍増型の表現は古典的（Berstel ほか、前掲）。MCFG の多次元代入可能性、穴間に非空セパレータが必要なことは Yoshinaka (2011)、論文の `def:class-cmcf` 等に従った。原稿の power transfer および先行レビューの共役移送とは異なり、今回の局所定理は**重なる二穴分解を有限分類した**点を使う。

「唯一型語から単語言語を取り出す」補題は、型によるフィルタリングと代入可能性から直ちに出るため、独立の数学的新規性は主張しない。**長さ 7／13 という定数と15軌道の完全証明書が文献で既知かどうかは未確認**。関連した教科書・論文への限定的照合しか行っておらず、網羅的な先行研究調査も第三者の形式検証も済ませていない。

次の探索では、Thue–Morse のような**全長 overlap-free な語は候補から外し**、短い overlap は持つが、U₁・内容型の2穴自己衝突の証明書を含まない長語を探すのが筋である。`θ̄=O(n)` の短い導出を与える `c`-分岐が1穴の分布を壊す事例にも注意が必要。一方、一般的な正の上界に向かうなら、二穴自己衝突の局所剛性を `τ(G,c_Σ)` の短縮へ接続する補題（特に除外文字の消去）が最重要となる。

**実施の限界**：`n≤3` の言語の arity 1/2 全数検査、7文字・13文字の証明書の完全検証、定義・原稿ラベルの照合を実施した。**`n=4` の1806語候補の全分布構築、ファンアウト3以上の候補言語の全数検査、一般の多項式上界の証明は実施していない**。本報告の構成不可定理は `d=2` で否定するため、それだけで全 `f≥2` に及ぶ。新しい反例族も新しい特徴標本下界も発見していない。
