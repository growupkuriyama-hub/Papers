# μ_{ab} の独立検証と仮想の長さ：正規化の欠落、長さ増加の障害、加法的場合の二次上界

2026-11-05／ChatGPT／系列の二十七本目。対象：`02-v2-lg-fanout-boundary/`、`op:fanout-two`。

## 0. 主張ごとの判定

| 主張 | 判定 | 正確な射程・注意 |
|---|---|---|
| 前報補題1(i)–(iv)、特に保持者状態の単調性と道の長さ 3v | **独立に確認** | §2。既存の侵入への帰着の特別な場合。新しい多項式上界ではない |
| 前報補題2：比較不能な非保持者・同名節点の総長一致 | **独立に確認** | §2。重いこと自体はこの交換証明に不要 |
| 前報補題3の数式による最小性の主張 | **独立に確認** | 自明に成り立つが目的には足りない |
| 任意の近道証明書の最後の段が必ず元の W を使う、という強い読み | **確認できず** | §2.3。保証できるのは最後の段の第三前提が ab 語であること。元の W とは限らない |
| 命題5(i)–(iii)：重みを既に持つトークンの水準集合 | **独立に確認** | 初等的な加法性の特別な場合 |
| 命題5の、非保持者の短い逃げ道への適用 | **独立に確認** | §3。ラベル付きトークン、長さ ≤θ の逃げ道、c 無し成分の実長と整合する重み分割が必要 |
| 「任意の別生成」「二成分へ任意の重み分割」まで含む適用 | **確認できず** | 条件(ii)との整合性を前報の記述だけでは保証できない。§3の限定版を用いる |
| 前報補題7・7′の**完全な前提付き**主張 | **独立に確認** | §4。実際の生成であること、内容一致、短縮条件を落としてはならない |
| `e_C=sβ` だけで常に一段か二段の近道が出る | **誤り** | §4.3。完全な補題7・7′への反例ではなく、その無条件化への反例 |
| Part A、Part E の二段近道と持ち上げ n=3,…,7、七つの m=3 設計の近道 | **独立に確認** | 自作コードで実行・再生。前報のコードは実行・import していない |
| 2525 件の総数内訳 17/1349/1159 | **確認できず** | 全件の独立再実行は未実施。時間依存の分類でもある。前報の記録としてのみ扱う |
| 前報で停止した三設計には近道がある | **証明済み** | §7。有限の各例について、独立再生可能な証明書を得た |
| 指定の正規化なし差分保存式が近道を防ぐ | **反証** | §5.1。通常の長さが常に解なので、その存在には排除力がない |
| 種をすべて N に正規化した仮想長が存在すれば、閉包の c 無し語はすべて長さ N | **証明済み** | §5.2。初等的帰納法。十分条件として正しい |
| 近道がなければ正規化仮想長が存在する | **反証** | §5.3。唯一の c 無し種を持つ例でも、長い語だけが強制されて不整合になる |
| 最小 SUB 閉包上での正規化仮想長の存在 ⇔ c 無し語が全て長さ N | **証明済み** | 定数関数を使う初等的同値。目的には単独で足りない |
| λ(a)=λ(b)>0、λ(c)≥0 の単一加法水準に入る言語の μ_{ab}≤(r+1)θ² | **証明済み** | §6。代入可能性不要、fan-out 任意。既報(100)の閾値交差法の ab 特殊化 |
| λ(a),λ(b)>0 が不等の場合の μ_{ab}≤(r+1)θ² max(λ(a),λ(b))/min(λ(a),λ(b)) | **証明済み** | 比率依存であり、重み独立の多項式上界ではない |
| 任意の非負文字重みでの、重み独立の ab 版上界 | **未解決** | 本報の定理は同重みの場合。零写像も許す主張は、追加の構造的制限にならない |
| 七設計の m=4 での近道 | **証明済み** | m=3 証明書を導出文脈内へ移した特別な場合。m=4 全閉包の計算ではない |
| 短い逃げ道を持つ深い倍増の、非加法的な正規化仮想長の必然的不整合 | **未解決** | 加法的場合だけ排除。一般の場合の証明・反例族とも未達 |
| 中心の `op:fanout-two`、所属と指数下界を備えた反例族 | **未解決** | 所属未証明の候補に希少型下界を適用していない |
| 文献上の新規性 | **未確認** | 原典の新規探索は未実施。初等的事実・既報の特殊化と区別した |

**主な結論。** 前報の中核的な木の補題と、条件をすべて記した近道補題は確認できた。一方、今回提示された仮想長の式には種の正規化が不足する。正規化を加えても、その不整合から直ちに「短い ab 語」を結論できない。これを、実際に `C_{2,c}` に属する言語で示す。肯定側では、a と b を同じ正の重みにする自然な仮想長の加法的場合に、二次上界を証明した。

## 1. 正本と検証方法

公開 GitHub から以下を取得した。行番号でなくラベルと本文を照合した。取得は同一コミットへの固定ではなくファイル単位なので、再現用に各 blob SHA を示す。

基点：[Papers/02-v2-lg-fanout-boundary](https://github.com/growupkuriyama-hub/Papers/tree/main/02-v2-lg-fanout-boundary)。以下のパスはこのディレクトリからの相対パス。

| パス | 取得した blob SHA |
|---|---|
| `main.tex` | `1bc97358a49b4e80eef96abb0eee6de4ca10eecf` |
| `reviews/claude_mu_ab_2026-11-05.md` | `ecce657e701da86b14aaaab407162a3b8ab7de67` |
| `reviews/check_claude_mu_ab_2026-11-05.py` | `d07704b9f0b63c7e28035e3ecc1efcaee74176a7` |
| `reviews/search_m3_escapes.py` | `a636f8ca301da95da42ca604d8196198370e2b70` |
| `reviews/chatgpt_weighted_codes_2026-11-02.md` | `5b624c550441205ad46333e0f7c9c732d928e465` |
| `reviews/chatgpt_negative_design_2026-11-04.md` | `e3b975d0cfb3b3683acb4e12f7c5b58c9eb0cb2b` |
| `reviews/check_claude_negative_shortcut_2026-11-04.py` | `5faca1793122f6950fd8f2a9b810abce172d7e89` |

「独立」は、前報の出力を正解データとして認定したという意味ではない。証明を以下で組み直し、計算の生成・推論・再生を別実装した。ただし前報の証明・スクリプトは仕様確認のため読んだので、盲検ではない。

### 1.1 使用する定義と厚さの確認

`def:class-cmcf` に従い、非空成分だけを比べる。二穴文脈 `p□₁q□₂r` は `q≠ε`。成分ごとの内容が一致する x,y について

\[
 E[x],E[y],F[x]\in L\quad\Longrightarrow\quad F[y]\in L. \tag{SUB}
\]

本報の推論はこれだけを使う。内容が語全体で一致するだけでは二穴推論を許さない。

`G` は reduced good、`θ=θ̄_G≥1`。必要な厚さ補題は次の二項だけで、独立に確認できる。任意の規則を使う最短成功導出の長さは θ 以下であり、非削除性により、規則に直接書かれた終端は全部その文に残る。従って直接終端数は θ 以下。同じ導出の当該非終端の生成組も文の一部なので総長 θ 以下。各非終端に生産規則があるので、各 B に短い代表 ω_B が存在する。

`prop:rare-type` は本報の新しい結論の導出には使用しない。内容型を一つ除いた言語との区別による下界であり、元の言語と比較言語のクラス所属・学習作用素の前提が必要である。今回の候補文法の長い唯一語だけから、この命題を適用することはしない。

## 2. 木の補題を証明し直す

W は最短 ab 語、T はそのうち節点数最小の導出。`ℓ_u` は節点の生成組の総長。位置の集合として生成を扱うため、成分が二つでも以下は変わらない。

### 2.1 保持者と 3v の道長

u が a,b のどちらの保持者でもなければ、その外側に a と b が少なくとも一つずつある。c 無しの短い生成に替えると、外側の a,b は残り、c は増えず、文が短くなる。従ってそのような生成はない。特に重い非保持者は c で強制される。

a の保持者は比較可能である。比較不能な節点の生成位置は互いに素であり、両方が同じ a の全出現を含むことはできない。また保持者の祖先も保持者。従って a 保持者は根からの一本道で、b も同様である。

一本の根から葉への道に状態 `σ(u)=(a保持者か,b保持者か)` を付ける。下に進むと各ビットは 1→0 にしか変わらず、状態の一定区間は高々三つ。

同一区間に同じ非終端 B の節点 u（上）と z（下）があれば、u の導出を z の導出で置換する。非削除性から `ℓ_z≤ℓ_u`。c は出ない。ある文字について u が非保持者なら外にその文字が残り、保持者なら z も保持者なので z 内に残る。従って ab 語で長さは増えず、導出節点数は真に減る。W の最短性と T の選び方に矛盾する。各区間に高々 v 節点、全体で高々 3v 節点である。

同じ深さの重い節点は反鎖で、そのうち保持者は高々二つ、残りは c 強制節点だから高々 q 個。重い節点数 H は `H≤3v(q+2)`。重い節点は祖先閉で、各文字は重い節点の直接終端か、その重くない子の生成内にある。各重い節点は直接終端 ≤θ、重くない子は高々 r 個で各総長 ≤θ。根が重ければ

\[
 |W|\le(r+1)\theta H\le3(r+1)v\theta(q+2).
\]

根が軽ければ `|W|≤θ` で同じ結論。これは q を制御していない帰着である。

### 2.2 同名の非保持者

u,z が非保持者で同じ非終端なら、u を z の生成に替えても ab が外に残る。最短性から `ℓ_z≥ℓ_u`。逆に交換して逆不等式、従って等しい。比較不能なら両方向の交換は特に明瞭である。

さらに**同名の非保持者は入れ子にならない**。入れ子なら上の σ=(0,0) の議論で、長さが増えず節点数が減る。これは重み整合性を論じる際に省略できない。

### 2.3 最小性の伝播と「最後の段」の区別

`W=F[x]` かつ `E[x],E[y]∈L`、成分内容が一致すれば SUB により `F[y]∈L`。その内容は ab、長さは `|W|−‖x‖+‖y‖` だから `‖y‖≥‖x‖`。ここまでは補題3そのものである。

一般の証明書では、一段ごとに `content(F[y])=content(F[x])`。従って短い ab 語の最後の第三前提も ab 語であり、x,y と F は c 無しである。共通文脈 E は c を含んでよい。

ただし第三前提 `F[x]` が**元の W であること**はこの議論から出ない。別の ab 語が先行段で強制されている可能性がある。最初に長さ N=|W| 未満へ到達する段を選べば、`|F[x]|≥N>|F[y]|`、従って `‖x‖>‖y‖` は保証できる。一般論として用いてよいのはこの形である。「W の因子」は二穴では「W 内の二つの非隣接因子の組」と読む必要もある。

## 3. トークン障壁の正しい適用範囲

### 3.1 条件付き命題

Γ の各文字に正の重み λ を与える。`Λ={w:λ(w)=N}` とする。共通文脈 E で `E[x],E[y]∈Λ` なら

\[
 \sum_i\lambda(x_i)=\sum_i\lambda(y_i).
\]

従って任意の F で `F[x]∈Λ ⇔ F[y]∈Λ`。型条件すら使っていないので、すべての arity・すべての型付けに通用する。種が Λ 内なら SUB 閉包も Λ 内である。

さらに非消去写像 h がトークンの意図した内容を保ち、c 無しトークン t には `λ(t)=|h(t)|` を課すと、c 無しのトークン列 w は `|h(w)|=N`。持ち上げた証明書は近道を出さない。

### 3.2 短い逃げ道について重みを構成する

W の非保持者の重い節点を考え、置換は同時に反鎖上で行う。未置換の端末は重み1で残し、生成組の成分をトークン化するときは元の各成分の実長を重みにする。

B の選んだ逃げ道 ω_B は `‖ω_B‖≤θ<ℓ_B`。§2より c を含み、同名節点の ℓ_B は一意で、同名非保持者の入れ子もない。**異なる非終端の逃げ道は、具体的文字列が一致しても別トークンにする**。その一致を忘れるのがまさに抽象模型である。

fan-out 2 で片成分だけ c 無しなら、その成分トークンの重みは実長に固定し、残りを c を含む成分に割り当てる。逃げ道全体が ℓ_B より短いので、残りは正である。両成分とも c を含めば総和 ℓ_B を任意の二つの正の値に分けられる。fan-out 1 は総重み ℓ_B をそのまま割り当てる。

どの置換も重みを保存し、すべての種の重みは |W| になる。異なる反鎖を選んでも、同名節点の総長の一意性が整合性を保証する。これで命題5を**短い逃げ道の近傍**に適用できる。

「二成分に任意に分ける」は、片成分が c 無しの場合には不可。その成分に実長と異なる重みを付けると命題5(ii)が使えない。また、任意の別生成まで無条件に加えると、c 無しの長い生成や、c 無し成分だけで ℓ_B を超える生成があり得るという整合性問題が残る。前報の簡潔な文章はこの点を処理していない。本報はこの拡張を使用しない。

## 4. 因子の一致による近道：前提の確認

### 4.1 補題7

`W=lYY′r`、右の子の別生成 β、`lsβr∈L` を仮定する。文法の部分木交換から `lYβr∈L`。`content(lY)=content(ls)`、`|s|<|Y|` のとき

- `x=lY, y=ls`,
- `E=□βr`, `F=□Y′r`

に SUB₁ を適用して `lsY′r∈L`。これは短い ab 語である。前提 `lsβr∈L` は、親が実際に `sβ` を生成するなら、その親の部分木を交換して得られる。単に文字列が書けることでは足りない。

鏡像も同様。例えば `lβsr∈L`、`content(s)=content(Y′)` なら `E=lβ□r`、`F=lY□r` で短縮する。より広く、右外側を埋め草へ取り込んで内容を一致させてもよい。

### 4.2 補題7′と L_n への適用

`W=UZUZ`、および

\[
 \beta\beta,\quad \beta Ue,\quad UZUZ,\quad UZUe,\quad s\beta\in L
\]

を仮定し、`content(β)=content(Ue)`、`content(UZU)=content(sU)`、`|s|<|UZ|` とする。

第一段：`E=β□`、`x=β,y=Ue`、`F=s□` で `sUe`。

第二段：`E=□e`、`x=UZU,y=sU`、`F=□Z` で `sUZ`。

全前提・内容一致・非空性が明示されている。この五語の所属を仮定せずに「必ず二段」とはいえない。

(149)(150) の文法について n≥3、`i=n−1`、

\[
 U=(ab)^{2^i-2},\quad Z=abab,\quad e=abc,\quad
 \beta=a^icb,\quad s=a
\]

とする。`UZ` は A_i の全倍増生成、`Ue` はその右端 A₁ だけ逃がした生成、β は A_i の逃げ道。従って最初の四語は親の二つの A_i を独立に生成して得られる。`sβ=a^ncb` は親 A_n の逃げ道そのもの。内容一致は双方 abc、双方 ab である。強制語は

\[
 a(ab)^{2^{n-1}},\qquad |a(ab)^{2^{n-1}}|=2^n+1<2^{n+1}.
\]

これは全 n≥3 の証明であり、n=3,…,7 では自作の再帰的完全所属判定でも五前提を確認した。候補 L_n 自体に代入可能性を仮定したのではなく、**L_n を含む任意の代入可能言語で強制される**という条件付き結論である。L_n の唯一の ab 語が W_n なので、候補そのものは所属しない。

### 4.3 因子の一致だけでは足りない具体例

\[
 S\to BB\mid ac,\qquad B\to ab\mid c.
\]

生成言語は `K={abab,abc,cab,cc,ac}`。最短 ab 語は W=abab。親の逃げ道は `ac=sβ`、`s=a`、子の生成 `β=c`、`|s|=1<|ab|=2` である。しかし K 自身が `(2,c)`-代入可能であるため、近道は出ない。

直接の完全検査も短い。arity 1 で共通文脈・同内容を持つ**異なる**埋め草の組は、空の外枠における `abc,cab` だけで、両者の受理文脈はこの空枠のみ。arity 2 にはそのような異なる組がない。従って両 arity の条件を満たす。K は有限・CFG、提示文法も reduced good だから `K∈C_{2,c}`。

付録コードは長さ上限による省略なしにこの閉性を確認する。本例は「重い子を持つ任意深さの反例族」ではない。証明しているのは**補題7′の追加前提を消した要約の誤り**だけである。

## 5. 仮想の長さの定式化と反例

### 5.1 提示された式だけなら常に解がある

提示された条件を (V0) と書く。

\[
 \nu(w)=|w|\quad(c\notin content(w)),\qquad
 \nu(F[y])=\nu(F[x])-\nu(E[x])+\nu(E[y]). \tag{V0}
\]

通常の長さ `ν(w)=|w|` は、任意の語・任意の線形文脈について

\[
 |F[y]|=|F[x]|-|E[x]|+|E[y]|
\]

を満たす。従って (V0) は**常に整合し、どれほど深い倍増でも破れない**。これは反例族の発見ではなく、定式化が目的の制約を表現していないことの指摘である。

例えば近道のある§4.2の最小 SUB 閉包上にも通常の長さが定義できる。したがって「この ν が存在すれば近道は出ない」は、種の値についての仮定なしには誤り。

### 5.2 正規化を加えた定義と完全な同値

S を種集合、N=|W|、`K=Cl_SUB(S)` を長さ制限のない**最小**閉包とする。語は有限回の SUB で得られるものに限る。次を定義する。

**正規化仮想長 (VN)**：`ν:K→R` が (V0) を満たし、さらに `ν(s)=N` を全 s∈S で満たす。

**定理5.1。** (VN) が存在することと、K の c 無し語がすべて実長 N を持つことは同値。

*証明。* 種で値 N、三前提が N なら結論は `N−N+N=N`。導出長の帰納法で全 w∈K に `ν(w)=N`。c 無し語では実長に一致するので長さ N。逆に全 c 無し語が長さ N なら、全 K 上の定数関数 ν≡N が全条件を満たす。□

従って最小閉包上では、非加法的な ν の値そのものに自由度はない。存在問題は「閉包が新しい c 無し長さを作るか」と同値であり、証明方法をまだ与えていない。

周囲の大きな L⊇K 上に ν を要求すると、K 外の語との追加制約が入る。K 上の存在から L 全体への拡張は本定理では主張しない。

### 5.3 「近道なし ⇒ 正規化仮想長あり」は失敗する

\[
 S=\{abab,\ ccab,\ ccababab\},\qquad N=4.
\]

唯一の c 無し種は W=abab。`x=ab,y=ababab,E=cc□,F=□ab` とすると、

\[
 E[x]=ccab,\ E[y]=ccababab,\ F[x]=abab\in S,
 \qquad F[y]=abababab\in K.
\]

一方、`H={w∈{a,b,c}^+ : |w|≡0 (mod 4)}` は正則で、全 arity・全型付けで代入可能。実際、共通文脈があれば二組の総長は mod 4 で等しく、任意の別文脈でも剰余が等しい。従って `H∈C_{2,c}`、S⊆H、K⊆H。

H には長さ4未満の非空語がなく、K には近道が絶対にない。しかし長さ8の c 無し語が強制されるので、(VN) は存在しない。代数的にも種を4にすると `ν(abababab)=4−4+4=4`、実長との一致は8を要求し矛盾する。

この例は、種の中に元から二つの c 無し長さを入れた自明な反例ではない。**唯一の c 無し種から長い方だけが出る**。ただし指定の倍増文法の種そのものではないので、その構成クラスでの逆向きを反証してはいない。

### 5.4 線形方程式による有限証明書とその限界

有限の観察語集合に変数 X_w を置き、全使用 SUB 四角形について

\[
 X_{F[y]}-X_{F[x]}+X_{E[x]}-X_{E[y]}=0,
\]

種には X_s=N、c 無し語には X_w=|w| を課せば、有理数の線形方程式として監査できる。非整合性は有限個の方程式の線形結合 `0=d≠0` で証明できる。無限系についても、自由ベクトル空間で関係の有限線形結合を考えれば、整合性の障害は有限に現れる（整合する部分空間上の線形写像は基底を延長して拡張できる）。

しかしこの証明書は SUB の**有向導出証明書そのものではない**。既知語の線形結合による矛盾から、短い語の所属を逆算してよいわけではない。§5.3 がその危険を具体化する。

正規化の不整合を「近道」と結び付けるには、少なくとも長くなるだけの障害を除く追加定理が必要である。前報§6の「剛性が壊れる、したがって補題3で近道」という移行は、現状では埋まっていない。

## 6. 加法的な場合の肯定結果

### 6.1 a,b が同重みなら二次で足りる

**定理6.1。** G は任意の fan-out の reduced good MCFG、ランク ≤r、`r≥1`、厚さ θ≥1。非負加法写像 λ が `λ(a)=λ(b)>0` を満たし、言語全体が一水準 `L(G)⊆λ^{-1}(Q)` に入るとする。ab 語が存在すれば

\[
 \boxed{\mu_{ab}(L(G))\le(r+1)\theta^2.}
\]

代入可能性は不要である。

*証明。* 共通の正の重みで割って `λ(a)=λ(b)=1`、`λ(c)=t≥0` とする。ab 語 W の成功導出を固定し、その長さを N とする。全節点は c 無しだから、その生成組の λ 値は総長 ℓ_h そのもの。

各節点の B 生成を厚さ補題の短い ω_B へ置換すると、外側の重みは変わらず、文全体は同じ水準 Q に残る。従って

\[
 \ell_h=\lambda(\omega_B),\quad \|\omega_B\|\le\theta. \tag{6.1}
\]

各規則が W に直接書くのは a,b だけなので

\[
 \ell_h\le\theta+\sum_{z\text{ child}}\ell_z. \tag{6.2}
\]

t≤1 なら根の短い代表から N≤θ。t>N なら根の短い代表に c は入れられず、やはり N≤θ。

残る `1<t≤N` を考える。t≤θ なら根で `N≤θt≤θ²`。t>θ なら、長さが t 以上で子はすべて t 未満の節点 h を選べる。葉は長さ θ 以下なので h は内点。各子 z の短い代表は非負重みのため c を含めず、(6.1)より `ℓ_z≤θ`。従って

\[
 t\le\ell_h\le(r+1)\theta.
\]

根の代表から `N≤θt≤(r+1)θ²`。すべての ab 語は同じ λ 値 Q、すなわち同じ実長 N を持つので、これが μ_{ab} の上界。□

この証明は既報(100)定理3.1の非負性・短い代表・閾値交差を再検証して使った特殊化である。今回は単位重みの文字が a,b の二つあり、未知の重い文字が c の一つだけなので、三次でなく二次になる。

### 6.2 不等重みの場合に証明できる範囲

`λ(a),λ(b)>0` とし、最小値を1へ正規化、最大値を ρ≥1 とする。節点の実長の代わりに重み q_h を使うと、直接終端の重み ≤θρ。c の重み t が θρ を超える場合の初交差では、各子の短い代表が c 無しなので `q_z≤θρ`。従って `t≤(r+1)θρ`。t が根の重みを超える場合は根の代表が c 無しであり、その他の場合も根の短い代表により

\[
 |W|\le\lambda(W)\le(r+1)\theta^2\rho.
\]

これは比率に依存する。ρ が入力族に沿って指数的なら目的の多項式上界ではない。**任意の非負重みという依頼を、同重みの定理で全て解決したとはしない。** 特に λ(a)=λ(b)=λ(c)=0 を許せば「一水準に入る」という仮定は任意の言語について成り立ち、制限そのものが消える。

今回の動機である「文字上の加法的仮想長が c 無し語の通常長と一致する」は、a,b に単位重みを課す設定なので、定理6.1が直接対応する。ただし ν を L 上だけで定義し、L に a や b が単独で入らない場合には、その一致だけから λ(a)=λ(b)=1 と推論してはならない。同重みは定理の明示仮定である。

### 6.3 深い倍増について

`A₀→ab`、`A_i→A_{i−1}A_{i−1}|e_i`、各 e_i は c を含み長さ ≤θ とする。文字上で `λ(a)=λ(b)=1`、言語全体が W_m と同じ重みなら、導出部分木の交換から

\[
 \lambda(e_i)=2^{i+1}.
\]

e₁ が c を含むため非負性から t=λ(c)≤4。ゆえに `2^{m+1}=λ(e_m)≤4θ`、すなわち

\[
 m\le\log_2\theta+1.
\]

これは前報の加法的動機を直接再証明したもの。一方、非加法的 (VN) については、短い逃げ道だけから破綻を導く定理は得ていない。通常の長さだけの (V0) にはそもそも破綻がない。

## 7. 独立計算の範囲・結果

### 7.1 方法

付録は Python 3 標準ライブラリのみ。前報の関数を import せず、各ラウンドで `(文脈, 成分型)` の組と、各組の出現文脈を作り直し、共通文脈からの分布移送を列挙する。前報の逐次 partner 更新実装とは別のラウンド方式である。

生成した**すべての追加語**に三前提を持つ証明を内部保存する。報告する近道について依存関係を遡り、必要な段を抽出して独立関数 `replay` で種から検査する。ログの certificate は `(E,x,y,F)` の配列であり、arity は x の成分数。Part E は明示した二段を直接再生する。

探索の制限は決定的：最大8ラウンド、各ラウンドで新規語を最大200個、語長上限 N+1。候補の走査・追加順はソートで固定し、時間では停止しない。近道が見つかれば即座に終了。長い語を捨てたこと、有限ラウンド、arity 制限はすべて「発見なし」側を弱める。

m=3 の探索は **SUB₁ だけ**で実行した。これは健全な規則の部分集合であり、今回すべての必要な近道を得るのに足りた。m=4 は全文法の閉包を構築せず、m=3 の証明を固定右文脈 W₃ に埋め込んだ。二穴を逃げ道周辺へ制限する方式は今回実装していない。

`closed` と出すのは、両 arity を全出現について列挙し、追加される語がなく、語長上限による省略もないときだけ。今回その判定をしたのは二つの小さな有限集合だけであり、七設計や停止例に閉性を宣言していない。

### 7.2 確認した事項

- Part A：L₂ の二穴違反と、L₃ の長さ9の ab 語への二段近道。
- Part E：n=3,…,7 の五前提の厳密所属判定、二段の再生、長さ9,17,33,65,129。
- 七設計：m=3 で全て一段か二段の近道。証明書の内容は前報と同じでなくてよい。
- m=4：七設計の長さ28,29,29,29,29,30,30の近道。m=3 からの文脈内移送という特別な場合。
- 前報の停止リストに実際に載る三組 `(ac,cc,c)`, `(ca,bbc,abc)`, `(cc,ac,c)`：それぞれ6,7,5段で長さ13,13,7の近道。この三件は「判定なし」から「近道あり」へ独立に進んだ。

Part E のうち、無関係な抽象トークン K を使った対照模型の10語閉性や、外側文脈付き・鏡像の各トークン探索ログまでは再現していない。主要な二段証明と n=3,…,7 の持ち上げを独立再生したという範囲である。

m=4 への移送は一般に、SUB の E,F の末尾へ同じ右文脈を加えるだけでよい。内容条件は変わらず、二穴の内側の隙間も変わらない。種 `tW₃` は根の左右の A₃ が t,W₃ を生成するため実際に文法に入る。コードでこの所属も独立確認した。

2525 件全体、17 件の閉性全体、残り1156件の停止例は独立に再判定していない。この三件から他の停止例の結論は推定しない。非退化で閉じた m=4 設計は得ていない。

## 8. 証明できたこと・止まった場所・次の一点

**証明できたこと。** 木の帰着と条件付き近道補題の独立検証、短い逃げ道の正確なトークン重み構成、正規化仮想長の同値定理とその逆向きの反例、同重み加法水準の二次上界。計算では指定の個別例と三件の停止例に証明書を与えた。

**止まった場所。** 非加法的な正規化仮想長の必然的不整合は示していない。しかも不整合を示すだけでは、長い ab 語が出る可能性が残り、短い方への矛盾に届かない。一般の非負不等重みについての重み独立上界も未達である。

**次に絞るべき一点。** 次の、倍増文法の種に限定した「長さ増加から短縮への移行」を証明するか反証する：

> `S_m=L(A_m)` を、A₀→ab、A_i→A_{i−1}A_{i−1}|e_i（c∈content(e_i)）の全生成語とする。`Cl_SUB(S_m)` に長さ N=2^{m+1} を超える ab 語が現れたら、N 未満の ab 語も必ず現れるか。

これは**未解決の補助問**であり、本報で真と予想する根拠を得たわけではない。一般の種集合では§5.3により偽なので、倍増の全置換近傍を本質的に使う必要がある。もしこの限定命題が証明できれば、(VN) の不整合を近道へ接続する欠落が埋まる。その後にも、深さと逃げ道長から不整合を強制する別の仕事が残る。

本報は三文字の開始型 ab の議論に限定する。他の欠けた型や τ の上界、特徴標本の一般下界、ファンアウト境界の移動は結論しない。GitHub の原稿・README は変更していない。

## 付録A. 独立コード全文

以下を `independent.py` として保存して `py -3 independent.py` で実行できる。報告書単体にコードと出力を収録するため、別ファイルを必要としない。

```python
from collections import defaultdict
from functools import lru_cache
from itertools import combinations
import json


def put(e,x):
    return ''.join(e[i]+x[i] for i in range(len(x)))+e[-1]

def typ(x):
    return tuple(tuple(sorted(set(s))) for s in x)

def occ(w,d):
    n=len(w)
    if d==1:
        for i,j in combinations(range(n+1),2):
            yield (w[:i],w[j:]),(w[i:j],)
    else:
        for i,j,k,l in combinations(range(n+1),4):
            yield (w[:i],w[j:k],w[l:]),(w[i:j],w[k:l])

def language(esc):
    s={'ab'}
    for e in esc:
        s={e}|{x+y for x in s for y in s}
    return s

def member(esc,w):
    @lru_cache(None)
    def f(i,s):
        if i==0:return s=='ab'
        return s==esc[i-1] or any(f(i-1,s[:k]) and f(i-1,s[k:]) for k in range(1,len(s)))
    return f(len(esc),w)

def replay(seeds,steps):
    known=set(seeds)
    for e,x,y,f in steps:
        d=len(x)
        assert d in (1,2) and len(y)==d
        assert len(e)==len(f)==d+1 and all(x) and all(y)
        assert d==1 or (e[1] and f[1])
        assert typ(x)==typ(y)
        assert all(put(g,z) in known for g,z in ((e,x),(e,y),(f,x)))
        known.add(put(f,y))
    return known

def trace(seeds,proof,w):
    out=[]; seen=set(seeds)
    def visit(v):
        if v in seen:return
        e,x,y,f=proof[v]
        for g,z in ((e,x),(e,y),(f,x)):visit(put(g,z))
        out.append((e,x,y,f));seen.add(v)
    visit(w)
    assert w in replay(seeds,out)
    return out

def consequences(s,arities):
    # Rebuilt each round: no code or partner engine imported from previous reports.
    for d in arities:
        groups=defaultdict(set); dist=defaultdict(set)
        for w in sorted(s,key=lambda w:(len(w),w)):
            for e,x in occ(w,d):
                groups[e,typ(x)].add(x);dist[x].add(e)
        for (e,t),xs in sorted(groups.items()):
            for x,y in combinations(sorted(xs),2):
                for p,q in ((x,y),(y,x)):
                    for f in sorted(dist[p]-dist[q]):
                        yield put(f,q),(e,p,q,f)

def close(seeds,N,arities=(1,),rounds=8,cap=None,batch=200):
    s=set(seeds);proof={};cap=cap or N+1
    for r in range(rounds):
        pending={}; overflow=False
        for w,st in consequences(s,arities):
            if w in s:continue
            if set(w)==set('ab') and len(w)<N:
                proof[w]=st
                return 'shortcut',w,trace(seeds,proof,w),len(s)
            if len(w)>cap:overflow=True;continue
            if len(pending)<batch:pending.setdefault(w,st)
        if not pending:
            # closed only when BOTH arities were exhaustively scanned, no cap omission
            return ('closed' if arities==(1,2) and not overflow else 'restricted'),None,[],len(s)
        proof.update(pending);s.update(pending)
    return 'round-limit',None,[],len(s)

def report(name,seeds,N,arities=(1,)):
    status,w,tr,size=close(seeds,N,arities)
    print(name,'status='+status,'known='+str(size),'word='+str(w),'steps='+str(len(tr)),flush=True)
    if tr:print('certificate='+json.dumps(tr,ensure_ascii=False),flush=True)
    return status

def main():
    esc=lambda n:['abc' if i==1 else 'a'*i+'cb' for i in range(1,n+1)]
    s=language(esc(2));st=(('', 'ab',''),('ab','abab'),('abab','ab'),('', 'c',''))
    assert put(st[3],st[2]) not in s
    replay(s,[st]);print('A L2: exact violation -> '+put(st[3],st[2]))
    report('A L3',language(esc(3)),16)
    for n in range(3,8):
        u='ab'*(2**(n-1)-2);z='abab';b='a'*(n-1)+'cb';e='abc'
        seeds={b+b,b+u+e,u+z+u+z,u+z+u+e,'a'+b}
        assert all(member(esc(n),w) for w in seeds)
        steps=[((b,''),(b,),(u+e,),('a','')),
               (('',e),(u+z+u,),('a'+u,),('',z))]
        target='a'+u+z
        assert target in replay(seeds,steps)
        print('E n='+str(n)+' exact-premises=True length='+str(len(target))+' steps=2')
    designs=[('c^i',lambda i:'c'*i),('a^(i-1)c',lambda i:'a'*(i-1)+'c'),
        ('ca^(i-1)',lambda i:'c'+'a'*(i-1)),('cb^(i-1)',lambda i:'c'+'b'*(i-1)),
        ('b^(i-1)c',lambda i:'b'*(i-1)+'c'),('c(ab)^(i-1)',lambda i:'c'+'ab'*(i-1)),
        ('ac^ib',lambda i:'a'+'c'*i+'b')]
    for name,f in designs:
        report('F m3 '+name,language([f(i) for i in range(1,4)]),16)
    # m4: sound subset of full grammar, using only a root doubling of L(A3).
    # Keep certificates small by lifting m3 consequences in a fixed suffix W3.
    for name,f in designs:
        es=[f(i) for i in range(1,5)];s3=language(es[:3]);suf='ab'*8
        status,w,tr,size=close(s3,16)
        if status=='shortcut':
            lifted=[(e[:-1]+(e[-1]+suf,),x,y,g[:-1]+(g[-1]+suf,)) for e,x,y,g in tr]
            seeds={t+suf for t in s3}
            assert all(member(es,t) for t in seeds)
            assert w+suf in replay(seeds,lifted)
            print('m4 '+name+' lifted-shortcut length='+str(len(w+suf))+' steps='+str(len(lifted)))
    # Previously stopped concrete cases; deterministic limits, no wall-time stopping.
    for es in [('ac','cc','c'),('ca','bbc','abc'),('cc','ac','c')]:
        report('priority '+repr(es),language(es),16)
    # Independent complete finite closure sanity test.
    report('finite-check',{'ab','c'},2,(1,2))
    small={'abab','abc','cab','cc','ac'}
    report('factor-identity-alone',small,4,(1,2))
    v={'abab','ccab','ccababab'}
    st=(('cc',''),('ab',),('ababab',),('','ab'))
    assert 'abababab' in replay(v,[st])
    print('virtual-counterexample: forced=abababab; 8=4-4+8; normalized 8!=4-4+4')
    print('ALL PRINTED CERTIFICATES REPLAYED')

if __name__=='__main__':main()

```

## 付録B. 実際の標準出力

以下は本環境で上記コードを実行した出力であり、前報からの転載ではない。

```text
A L2: exact violation -> ababcab
A L3 status=shortcut known=127 word=aabababab steps=2
certificate=[[["", "aacb"], ["aacb"], ["abababc"], ["a", ""]], [["", "ababc"], ["ababababab"], ["aab"], ["", "ababab"]]]
E n=3 exact-premises=True length=9 steps=2
E n=4 exact-premises=True length=17 steps=2
E n=5 exact-premises=True length=33 steps=2
E n=6 exact-premises=True length=65 steps=2
E n=7 exact-premises=True length=129 steps=2
F m3 c^i status=shortcut known=43 word=abababababab steps=2
certificate=[[["", "cc"], ["cc"], ["c"], ["abababab", ""]], [["", "abababc"], ["ababab"], ["ab"], ["", "ababababab"]]]
F m3 a^(i-1)c status=shortcut known=26 word=ababababaabab steps=1
certificate=[[["", "c"], ["abababababab"], ["ababababa"], ["", "abab"]]]
F m3 ca^(i-1) status=shortcut known=26 word=aabababababab steps=1
certificate=[[["c", ""], ["abababababab"], ["aabababab"], ["", "abab"]]]
F m3 cb^(i-1) status=shortcut known=26 word=babababababab steps=1
certificate=[[["c", ""], ["abababababab"], ["babababab"], ["", "abab"]]]
F m3 b^(i-1)c status=shortcut known=26 word=ababababbabab steps=1
certificate=[[["", "bc"], ["abababababa"], ["abababab"], ["", "babab"]]]
F m3 c(ab)^(i-1) status=shortcut known=26 word=ababababababab steps=1
certificate=[[["ababababc", ""], ["abab"], ["ab"], ["", "abababababab"]]]
F m3 ac^ib status=shortcut known=166 word=ababababababab steps=2
certificate=[[["ac", ""], ["cbabababab"], ["bababababacb"], ["ababa", ""]], [["", "abababababacb"], ["abab"], ["ab"], ["", "abababababab"]]]
m4 c^i lifted-shortcut length=28 steps=2
m4 a^(i-1)c lifted-shortcut length=29 steps=1
m4 ca^(i-1) lifted-shortcut length=29 steps=1
m4 cb^(i-1) lifted-shortcut length=29 steps=1
m4 b^(i-1)c lifted-shortcut length=29 steps=1
m4 c(ab)^(i-1) lifted-shortcut length=30 steps=1
m4 ac^ib lifted-shortcut length=30 steps=2
priority ('ac', 'cc', 'c') status=shortcut known=290 word=babbababababab steps=6
certificate=[[["", ""], ["c"], ["cccc"], ["ababa", "abababab"]], [["", ""], ["ccabababab"], ["ababacacac"], ["ababacc", ""]], [["", "c"], ["ababababaca"], ["ababacc"], ["", "bab"]], [["", ""], ["c"], ["cccc"], ["ababa", "acac"]], [["", ""], ["ababaccc"], ["ababaccbab"], ["", "cacac"]], [["ababacc", "cacac"], ["ababa"], ["bab"], ["", "bababababab"]]]
priority ('ca', 'bbc', 'abc') status=shortcut known=504 word=ababbbbababab steps=7
certificate=[[["", ""], ["abc"], ["ababababbbc"], ["bbcab", "a"]], [["", ""], ["abc"], ["caababbbc"], ["bbcab", "a"]], [["", "ababbbca"], ["bbcababab"], ["bbcabca"], ["", "ab"]], [["", ""], ["abc"], ["bbcabababab"], ["bbc", "aab"]], [["", "c"], ["ab"], ["ababababbb"], ["bbcca", "ab"]], [["", "abab"], ["caabababab"], ["bbcabab"], ["bbc", "bbab"]], [["bbcbbc", "ab"], ["ababababa"], ["ababbb"], ["", "bababab"]]]
priority ('cc', 'ac', 'c') status=shortcut known=525 word=ababbab steps=5
certificate=[[["abab", ""], ["ababababcc"], ["ababac"], ["", "cc"]], [["", ""], ["c"], ["cccccccc"], ["abab", "cac"]], [["", ""], ["ababcccccc"], ["ababababac"], ["", "cccac"]], [["", ""], ["ababaccc"], ["ababababac"], ["abab", "cac"]], [["", "ccac"], ["ababababababa"], ["abab"], ["", "bab"]]]
finite-check status=closed known=2 word=None steps=0
factor-identity-alone status=closed known=5 word=None steps=0
virtual-counterexample: forced=abababab; 8=4-4+8; normalized 8!=4-4+4
ALL PRINTED CERTIFICATES REPLAYED
```
