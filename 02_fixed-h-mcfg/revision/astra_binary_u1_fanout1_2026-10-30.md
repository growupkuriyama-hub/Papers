# Binary U₁ / fan-out 1 — 独立検証報告（2026-10-30）

## 0. 結論の要約表

| 主張 | 判定 | 根拠の節 |
|---|---|---|
| (P)：二文字 U₁ 型付け、fan-out 1、固定 rank 上限で一様多項式特徴データが存在する | **未解決** | §1, §6 |
| (N)：同じ対象に超多項式特徴データ下界を与える良形 CFG 族が存在する | **未解決** | §1, §6 |
| **指数欠陥立方体補題**：最短純語 `a^N` が `N>θ` なら、長さ `<N` の相異なる混合語が少なくとも `2^{ceil(N/((r+1)vθ))}-1` 個ある | **証明済み** | §2.1–§2.3 |
| 同じ条件で、長さ `<N` かつ `Ω(N/(rvθ))` 個の b-run を含む受理語が存在する | **証明済み** | §2.4 |
| 有限個 `M` の混合受理語に対し、`t_typ ≤ (r+1)vθ(2+log₂(M+1))` | **証明済み** | §3.1 |
| `M≤2^{q(g,θ)}`（固定多項式 q）を満たす部分クラスでは一様多項式特徴データが存在する | **証明済み**（当該条件下） | §3.2 |
| 有限 `(1,s)`-代入可能言語の型 ζ の受理語は、互いに真の因子にならない | **証明済み** | §4.1 |
| 任意の `t,m≥1` で `(a^t\mid b)^m` は `(1,s)`-代入可能 | **証明済み** | §4.2 |
| `A₀→a`, `Aᵢ→Aᵢ₋₁Aᵢ₋₁\mid b` は `n≥2` で負例族となる | **反証済み**（クラス所属に失敗） | §5.1 |
| レベルを b-run や a-padding で区別する単純短絡族がそのまま (N) を証明する | **未解決**（試した具体例は失敗） | §5.2, §8 |
| h_b 種類の正の b 出現数 ⇒ t_typ≤(r+1)vθ max{1,h_b}（無限言語も可） | **証明済み** | §3.4 |
| M 有限なら t_typ≤(r+1)vθ max{1,log₂(M+1)} | **証明済み** | §3.5 |
| 有限言語の h_len 種類の長さ ⇒ 最大長≤h_len θ | **証明済み**（既知結果の再証明） | §3.6 |
| 一語削除後の代入可能性の必要十分条件と任意作用素への識別下界 | **証明済み** | §4.3 |

**主問題に関する結論：決着していない。** 既報の指数欠陥補題と対数上界を保持したうえで、正の b 出現数のスペクトルによる上界と、一語削除が代入可能性を保つための必要十分条件を追加した。証明は本文に収録したが、一般の (P) の肯定にも否定にも到達していない。

**文献上の新規性：未調査。** 「以前の ChatGPT 報告より強い」ことと「公刊文献に対して新規」であることは異なる。独立査読は未了であり、掲載可能性の保証もしない。

## 1. 最新原稿の照合・量化・定義

### 1.1 取得した GitHub 正本

- Repository: `growupkuriyama-hub/papers`、branch: `main`。
- URL: <https://github.com/growupkuriyama-hub/papers/blob/main/02_fixed-h-mcfg/main.tex>
- **今回取得した `main.tex` の Git blob SHA：`1cfba3b866db3a4faa04fd7549d51649a8291465`**（UTF-8 229,031 bytes）。GitHub のファイル取得 API が返した **blob SHA** であり commit SHA ではない。
- 既報 `revision/chatgpt_binary_u1_fanout1_2026-10-30.md`：blob `d66f45edf797c6d7453fb9c37456a2c99220e4ed`、589 行。
- 既報 `revision/astra_ternary_u1_fanout2_2026-10-30.md`：blob `933df5d0de85d6edcddf1f0604b95d90338bbc8b`、1,155 行。**三文字・fan-out 2 の別問題**として読み、未証明の一般化を輸入していない。
- 2026-10-30 に main を取得し、main の commit `3455f493ea1aa51e844c9f4377a95da76c96458b` に固定した取得でも同じ main.tex blob SHA を確認した。二つの revision 報告はこの commit から取得した。main.tex の生バイトに対して Git の `SHA1(b"blob "+str(len(data)).encode()+b"\0"+data)` で上記 blob SHA と一致することも確認した。blob と commit は別物である。以後の main の変更は反映されない。
- 添付 `project-master-v15-2026-10-28.md` の正本ルーティングを確認した。原稿・リポジトリには変更を加えていない。
- 同名の既存報告（2026-10-30 07:31 UTC 作成）を読み、§2–§5 の証明を保持して照合し直した。指数欠陥補題と対数上界はその既報の結果であり、今回新しく発見した結果として数えない。追補は §3.4–§3.6、§4.3、§7.1 と追加実験である。

### 1.2 原稿中の label と、本報告で使う命題

| label | 照合事項 |
|---|---|
| `def:standard-mcfg` | `‖G‖=|V|+Σ_R(1+rank(R)+テンプレートの端末・変数出現数)`。fan-out 1 は CFG。 |
| `def:grammar-properties` | good = λ-free、nondeleting、nonpermuting、nonmerging。reduced = 全非終端が reachable/productive。fan-out 1 の各子収率は順序を保つ連続因子。 |
| `def:tuple-substitutable`, `def:class-cmcf` | `d=1` のみ。**空因子を比較しない**。等しい `s`-型の非空因子 `x,y` が受理文脈を共有すれば、二側分布 `D_L(x)=D_L(y)`。 |
| `def:reconstruction` | `B^{≤r}_{1,s}` と `B_{1,s}` は Start/Const/Comp/Link による集合駆動型。特徴標本 `K` は任意の有限 `K⊆F⊆L` に対し復元が `L` になる意味。 |
| `lem:thickness-equivalence` | `θ_G(R)` はその規則を**少なくとも一度**使う成功導出の最短**文全体**の長さ。`θ=max(1,max_R θ_G(R))`。各非終端には長さ≤θの収率、成功する固定一穴文脈 `E_A` には固定長≤θのものがある。 |
| `thm:data-from-typed-thickness`, `cor:distribution-representatives` | `μ*≤τ≤t_typ`、特徴データ長 `≤N_typ(1+2θ+rτ)+1_{ε∈L}`。 |
| `prop:rare-type` | 実現した語型は各特徴標本に必要。クラス全域で特徴標本を持つ任意の集合駆動型作用素にも適用。 |
| `rem:fanout-one-data`, `prop:three-letter-family`, `cor:typing-level-obstruction`, `app:three-letter-family` | 中立文字が２個の負例は確定しているが、本件の中立文字１個には直結しない。main は本件を open と明記。 |
| `thm:binary-u1-polydata`, `app:binary-u1` | **fan-out 2** の多項式上界。`lem:app-u1-shallow` と `lem:app-u1-runs` は fan-out 1 にも適用できるが、`lem:app-u1-transfer`, `lem:app-u1-deep` は二穴を使用。 |
| `prop:linear-factor-all-fanout`, `app:linear-factor-fanout` | `lem:app-lf-path` は各文字１辺の経路モデル、`lem:app-lf-descent` は良形文法の長さ下降。二文字への経路符号化には追加検証が必要。 |

以下、`Σ={a,b}`、`s(a)=1`、`s(b)=ζ`、`r≥2` 固定。`G` は `L⁺:=L∩Σ⁺` を生成する reduced good、fan-out 1、rank≤r の CFG、`v=|V|`、`g=‖G‖`、`θ=\bar θ_G≥1`。語が `b` を含めば**混合**、含まなければ**純**。`b`-run は極大連続 `b` 区間。`M(L):=|L⁺∩Σ* b Σ*|` と書き、`M` は無限でもよい。

**量化の注意。** 本報告の上界は**原稿で定義した二つの特定作用素**の特徴標本の存在を示す。下界を任意の集合駆動作用素へ移すには `prop:rare-type` のような識別論法が別途必要。`t_typ` の大きさだけでは一般作用素に対する下界にならない。

## 2. 証明：指数欠陥立方体（substitutability 不要）

### 2.1 定理 A（最短純語から指数個の混合語）

**定理 A.** `G` が上記の reduced good CFG で、`a^N∈L(G)` が `L(G)` 中の最短純語とする。`N>θ` なら、

\[
\left|\{w\in L(G):b\in\mathrm{alph}(w),\ |w|<N\}\right|
\ge 2^{\left\lceil N/((r+1)v\theta)\right\rceil}-1.
\tag{A}
\]

**証明（全 n・全導出について）。** `a^N` を導く木のうち節点数最少の木 `T` を取る。nondeleting により全節点の収率は正の純語である。ある根葉道に同じ非終端 `A` が祖先 `u` と真の子孫 `u'` として現れれば、`u` 以下を `u'` 以下で置換できる。間で消える明示端末や兄弟収率は純で非空（ただし rank-one identity だけの場合は総長不変）だから、完成した純語の長さは `N` 以下。短くなれば `N` の最短性に反し、等しければ `T` の節点最少性に反する。従って全根葉道の節点数は高々 `v`。

収率長が `θ` を超える節点を**重節点**と呼ぶ。重節点 `u` の非終端を `A_u`、元の純収率を `a^{\ell_u}` とする。原稿 `lem:thickness-equivalence(ii)` により `A_u` は長さ高々 `θ` の収率 `z_u` を持つ。`\ell_u>θ≥|z_u|` であり、もし `z_u` まで純なら、当該部分木のみを短い純収率で置換して `a^N` より短い純受理語を得る。従って**全ての重節点について `z_u` は b を含み、`|z_u|<\ell_u`**。

重節点は祖先に関して上方閉である。最も下にある重節点の集合 `F` は反鎖で、その収率は `a^N` の互いに素な非空区間を占める。`h=|F|` とする。`F` の各節点で、その純部分木を `z_u` の導出木に**独立に**置換してよい。good/fan-out-one/nondeleting により、他の部分木を変更しない限り、各置換は元の区間を短い b 入り文字列に取り替える操作そのものであり、構成したすべての木が `G` の適法な成功導出である。

異なる部分集合 `J,J'⊆F` が異なる受理語を生むことを示す。元の語の左から順に `F` の区間を並べ、両集合の所属が最初に異なる区間 `I` を取る。`I` より左の選択は一致するので、両語はその位置まで同一の文字列を出力する。`I` を置換した側では `z_I` 中の**最初の b** が現れる。この相対位置は `|z_I|≤θ<|I|` の範囲内である。他方は `I` を置換しないので、同じ相対位置には依然として文字 `a` がある。以後の区間への変更はこの時点より後ろであり影響しない。従って２語は異なる。これは `2^h` 通りすべての単射性を示す。

空集合を除く `2^h−1` 個の出力は、少なくとも一つの置換によって b を含み、しかも元の `N` から長さが厳密に減少する。これらは全部 `L(G)` に属する。

残るのは `h` の下界である。重節点の総数を `H` とすると、各重節点は `F` のいずれかへ至る根葉道上にあり、道長は高々 `v` なので `H≤vh`。`N>θ` のため根は重い。根の `N` 文字は、(i) 重節点が規則に明記する文字、または (ii) 重節点の**軽い**子の収率、に一意に分類できる（重い子の収率はさらに下で数える）。原稿の thickness lemma (i) により各重節点の明示文字は高々 `θ`、rank≤r の軽い子は高々 `r` 個で各長さ高々 `θ`。従って

\[
 N\le (r+1)\theta H\le (r+1)v\theta h,
\]

よって `h≥ceil(N/((r+1)vθ))`。単射性に代入すると (A) が従う。□

### 2.2 先行する線形個の欠陥補題との比較

従前の `chatgpt_binary_u1_fanout1_2026-10-30.md` §3 は、`F` の各節点を**一つずつ**置換して `h` 個の相異なる混合語を得た。本証明は `F` の各節点を**任意の部分集合にわたり同時に置換**して `2^h−1` 個を得る。CFG 規則の文法的独立性以外を仮定しない。`(1,s)`-代入可能性の一穴性を使わないため、同じ証明は他の型付けでも「b を含む／含まない」という二分に関して成立する。

**重要な限界：** この爆発は矛盾ではない。小さい CFG が二重指数個の有限語を生成することはあり得る。したがって (A) のみから (P) を肯定してはならない。

### 2.3 任意の非終端への局所版

**補題 A′.** 上記 `G` の非終端 `A` が純語を生成し、その最短純収率を `a^{\ell_A}` とする。`\ell_A>θ` なら、`A` の収率集合中に、少なくとも

\[
 2^{\left\lceil\ell_A/((r+1)v\theta)\right\rceil}-1
\]

個の異なる b 入り語がある。さらに、原稿 `lem:thickness-equivalence(iv)` による**一つ固定した**成功文脈 `E_A=(u_A,\square,v_A)` にそれぞれ挿入すると、同数の相異なる **`L(G)` の混合受理語**を得る。

**証明.** 定理 A の証明を「根は `S`」ではなく「根は `A`」として反復する。祖先・子孫が同じ非終端であれば、その置換は `A` の短い純収率になって最短性／節点数最少性に反する。重節点の短縮収率が純なら `A` の純収率を厳密に短縮してしまう。木の他の条件と独立置換の単射性は定理 A と同一である。`E_A` は全ての `A`-収率を `L(G)` に受理させる。固定した `u_A,v_A` の連接は異なる中間語を同一視しない。`z_u` の b が残るから完成語も混合である。□

### 2.4 一語に現れる多数の b-run

**系 A″.** 定理 A の仮定で、長さ `<N` のある混合受理語が少なくとも

\[
\left\lceil\frac12\left\lceil\frac{N}{(r+1)v\theta}\right\rceil\right\rceil
\]

個の異なる b-run を含む。

**証明.** 上の順序付き反鎖 `F` のうち奇数番目の区間だけを `z_u` に置換する。選ばれた二つの区間の間には必ず一つの**置換されない** `F`-区間があり、その収率は非空純語である。よって異なる置換区間の b は同じ極大 b-run に融合できず、選択区間一つにつき少なくとも一つの b-run を数えられる。置換は一つ以上あり全語は短くなる。`|F|=h` と定理 A の `h` の下界を用いる。□

**注記.** b-run の「個数」であり、b の総出現数や各 run の長さではない。原稿 `lem:app-u1-runs` の方向とは独立に、純最短語の**より短い混合語**を具体的に強制する。

## 3. 証明：有限混合切片に対する対数上界

### 3.1 定理 B（`M` に対する logarithmic typed thickness）

**定理 B.** `G` は reduced good、fan-out 1、rank≤r の CFG とする。`M:=|L(G)∩Σ*bΣ*|<∞` とすれば、代入可能性を仮定せず

\[
 t_{\mathrm{typ}}(G,s)\ \le\ (r+1)v\theta\bigl(2+\log_2(M+1)\bigr).
\tag{B}
\]

**証明.** 実現型付き非終端 `A_1` と `A_ζ` の最短収率を別々に考える。

**型 1.** `A` の最短純収率 `a^{\ell_A}` が `\ell_A≤θ` なら終了。`\ell_A>θ` なら補題 A′ と `M` の定義から

\[
 2^{\lceil\ell_A/((r+1)v\theta)\rceil}-1\le M,
 \qquad
 \ell_A\le (r+1)v\theta\log_2(M+1).
\]

ここで `M` は `L(G)` の混合語の**総数**なので、固定文脈 `E_A` を経由してできた全語を含む。ε はこの議論に関係しない。

**型 ζ.** 実現型付き非終端 `A_ζ` の導出木のうち節点数最少の木 `T` を取り、その収率に含まれる b の一文字を印す。`T` の根葉道に同じ `(B,type)` が二度現れれば上位部分木を下位で置き換えて型付き導出を短くでき、節点最少性に反する。従って一つの道の節点数は高々 `2v`。印した b を書いた節点までの一本道を残し、それ以外の各兄弟部分木を `lem:thickness-equivalence(ii)` が保証する元の無型 CFG の長さ高々 `θ` の収率に置き換える。この操作は同一の元非終端の規則を使った正当な導出を保ち、印した b も残すので、得た収率は型 ζ。道上の各節点が書く文字は `≤θ`、道外の子は一節点当たり高々 `r` 個で各 `≤θ`。したがって長さ `≤2v(r+1)θ` の型 ζ 収率がある。これは元原稿の一般的な浅い代表構成とは異なり、単純な一つの b の保持だけを使う。

以上、実現した全ての型付き非終端の最短長の最大は

\[
\max\{\theta,\ (r+1)v\theta\log_2(M+1),\ 2v(r+1)\theta\}
\le(r+1)v\theta(2+\log_2(M+1)).
\]

従って (B)。□

**`M=0` の場合.** b を含む型付き収率があるなら reduced と nondeleting のため成功語にも b が現れるので `M>0`。型 1 の全収率は `≤θ` で短縮できる。上の式はその場合も適用可能。

### 3.2 系 B′（多項式の指数まで多数の混合語を許す）

**系 B′.** 固定 `r≥2`、固定多項式 `q(g,θ)≥0` を選ぶ。`L∈C^{mcf}_{1,s}` とその reduced good、rank≤r 表示 `G` について

\[
M(L)\le2^{q(g,\theta)}
\]

なら、`B^{≤r}_{1,s}` と `B_{1,s}` に共通の特徴標本 `K` が存在し、

\[
 \boxed{\|K\|_+ \le
 3^r g\left[1+2\theta+r(r+1)v\theta\bigl(3+q(g,\theta)\bigr)\right]
 +\mathbf1_{\{\varepsilon\in L\}}.}
\tag{C}
\]

**証明.** `M≤2^q` なので `M+1≤1+2^q≤2^{q+1}`、従って `log₂(M+1)≤q+1` である（ここで `q` は非負）。定理 B から `t_typ≤(r+1)vθ(3+q)` が従う。原稿 `thm:data-from-typed-thickness` にこれと `τ≤t_typ` を代入する。実現型付き非終端は高々 `2v`、各 rank `k` 規則の非空子型の選択は高々 `2^k` 通りなので `N_typ≤2v+2^r|P|≤3^r g`。ゆえに (C)。□

**帰結.** `g_nθ_n=n^{O(1)}` の有限負例族で特徴データが `n^{ω(1)}` なら、`log₂ M(L_n)=n^{ω(1)}` が必要である。すなわち、単に指数個 `2^{O(n)}` の混合語を生成するだけでは足りず、**どの固定指数 `c` に対しても最終的に `M(L_n)>2^{n^c}`** となる種類の負例族が必要（適切な漸近列に沿って考える）。また `M=∞` の場合には本系は何も言わない。`μ*(ζ)≤θ` だとしても純型の長さが未解決の核心である。

### 3.3 `κ_A` への適用

原稿 `lem:app-u1-fillers` の fan-out 1 版では、型付き分布類の短い純代表は

\[
\kappa_A=\min\{k\ge1:E_A[a^k]\in L\}.
\]

`A` が型 1 を実現すれば、その元の最短純生成長 `\ell_A` はこの候補の一つなので `κ_A≤\ell_A`。従って `M<∞` のとき (B) は全 `κ_A` に上界を与える。**一般の `M=∞` に対する固定多項式上界は未証明**である。

### 3.4 追加定理 E：b 出現数のスペクトルによる上界

**今回の追補。** §2–§3.3 の指数欠陥と対数上界は同名の先行報告にも含まれていた。以下はその単なる再掲ではなく、同じ反鎖から別の量を取り出す結果である。文献上の新規性は引き続き**未調査**。

混合語の個数 M と区別して

\[
 H_b(L):=\{\,|w|_b:w\in L,\ |w|_b>0\,\},\qquad h_b:=|H_b(L)|
\]

と置く。h_b は b-run 数でも b の最大個数でもなく、**正の b 出現数の異なる値の個数**である。M が無限でも h_b は有限になり得る。

**定理 E.** 代入可能性を仮定しない reduced good CFG G について、h_b<∞ なら

\[
 \boxed{t_{\rm typ}(G,s)\le (r+1)v\theta\max\{1,h_b\}.}\tag{E}
\]

さらに、最短純受理語 a^N が N>θ を満たすなら、**長さ N 未満の混合受理語だけで**少なくとも

\[
 \left\lceil N/((r+1)v\theta)\right\rceil
\]

種類の正の b 出現数を実現する。

**証明。** 型1の最短 A-収率 a^ℓ を取る。ℓ≤θ の場合は (E) で足りる。ℓ>θ の場合、§2.3 の導出木と重節点反鎖 F を使う。その証明は ℓ の最小性と節点最小性から道長≤v、各重節点の短い置換 z_i は b を含むこと、および

\[
 \ell\le (r+1)v\theta m,\qquad m:=|F|
\]

を与える。F の節点を任意の順に i=1,…,m とし、最初の j 個だけを置換した A-収率を w_j とする。t_i:=|z_i|_b≥1 であり、元の全収率は純だから

\[
 |w_j|_b=\sum_{i=1}^{j}t_i\quad(0\le j\le m).
\]

固定した成功文脈 E_A=(u_A,v_A) に挿入すると、完成語の b 個数は

\[
 c+\sum_{i=1}^{j}t_i,\qquad c:=|u_Av_A|_b\ge0.
\]

j=1,…,m の値は全て正で狭義増加し、全て H_b(L(G)) に属する。従って m≤h_b、ℓ≤(r+1)vθh_b。この部分では M<∞ も L の有限性も使っていない。

型ζについては、§3.1 の 2v を v に改善できる。A が混合語を導くなら、A から依存グラフ上で到達可能な非終端 B に b を明記する規則 R がある。A からその B まで最短の依存道を選ぶ。同じ非終端を繰り返さず、B を含めて高々 v 節点である。各道の辺を実現する規則を一つ選び、指定された道の子以外の子には長さ≤θ の元文法の最短収率を入れる。B では R を使い全ての子を同様に完成する。これで b が残る A-導出ができる。各節点の直接端末は≤θ、完成する道外の子は高々 r 個で長さ≤θ。よってこの収率の長さは≤(r+1)vθ。型1と合わせて (E) が得られる。

最後の主張は A=S、E_S=(ε,ε)、ℓ=N とした同じ証明による。j≥1 では少なくとも一つの重い純収率を厳密に短縮するので、完成語長は N 未満である。m≥ceil(N/((r+1)vθ)) と、正の b 個数の狭義増加を用いる。□

**特徴標本への系。** さらに L∈C^{mcf}_{1,s} なら、原稿の `cor:distribution-representatives` に τ≤t_typ と (E) を代入して、両作用素に共通の特徴標本について

\[
 \boxed{\|K\|_+\le3^r g\{1+2\theta+r(r+1)v\theta\max(1,h_b)\}
 +\mathbf1_{\{\varepsilon\in L\}}.}\tag{E-data}
\]

ここでは N_typ≤2v+2^r|P|≤3^r g を用いた。これが系の証明である。特に h_b が g,θ の固定多項式で抑えられる部分クラスでは (P) が肯定される。上記引用は最新原稿の既存の復元定理への依存であり、復元理論全体の独立再証明を主張するものではない。

**適用範囲の例。** L=a*ba* は正則で (1,s)-代入可能、M=∞、h_b=1 である。実際、純因子には全て同じ分布 `{(u,v):|uv|_b=1}`、b を一つ含む因子には全て同じ分布 a*×a*、b を二つ以上含む因子には空分布がある。従って等型因子が文脈を共有した場合の全分布一致が成立する。文法 S→aS | Sa | b がこれを生成するので CFL 条件も満たす。定理 E はこのような無限言語にも、**任意の指定条件を満たす表示 G**に対して適用できる。

**なお、これで一般 (P) は解けない。** 例えば Σ⁺ は h_b=∞ だが代入可能である。h_b を有限にすることは全クラスの性質ではない。有限の下界族については、従来の多数の語長という必要条件に加えて、h_b も超多項式でなければならない、という追加の排除条件を与える。

### 3.5 対数上界の定数改善と局所性

定理 E の型ζの証明を §3.1 に適用すれば、M<∞ について

\[
 t_{\rm typ}(G,s)\le(r+1)v\theta\max\{1,\log_2(M+1)\}
\]

も成立する。純収率 ℓ>θ については §2.3 が与える整数 m と m≤log₂(M+1)、ℓ≤(r+1)vθm を使い、ℓ≤θ と型ζには定理 E の短い導出を使えばよい。これは全ケースを覆う証明である。

各 A の証明に必要なのは E_A に挿入した独立置換語だけなので、M と h_b は、当該 ℓ_A に対して長さ≤|E_A|_fix+ℓ_A の受理語に制限しても、その A の純収率の評価は成立する。ただしこの窓の上端に未知の ℓ_A が含まれるため、それ自体は入力パラメータだけの上界ではない。

### 3.6 既知の長さスペクトル条件の独立確認

有限非空 L(G) の長さの種類が h_len、最短長が μ のとき

\[
 \max_{w\in L(G)}|w|\le\mu+(h_{\rm len}-1)(\theta-\mu)\le h_{\rm len}\theta.
\]

**証明。** 各 B の最短収率長を d_B、成功導出で B-部分木を除いた固定部の最短長を o_B とする。規則 R:B→ρ(B₁,…,B_k) の直接端末数を c_R とすれば、外側と全ての子を独立に選べるので

\[
 \theta_G(R)=o_B+c_R+\sum_jd_{B_j},\qquad o_B+d_B\ge\mu.
\]

長さ>μ の成功導出で、収率長が d_B より大きい節点を最も深く選ぶ。子は全て各々の最短長なので、その部分木を最短 B-導出で置換した語の短縮量は

\[
 c_R+\sum_jd_{B_j}-d_B
 =\theta_G(R)-o_B-d_B\in[1,\theta-\mu].
\]

得た語も受理される。長さを厳密に減らして μ に至るまで繰り返すと、h_len 種類しかないため、最大長からも高々 h_len−1 ステップで済む。各ステップの上界を足して主張を得る。θ=μ なら長さ>μ の語があるという仮定自体が矛盾する。□

これは `lem:app-lf-descent` の CFG 版を再証明したものであり、新規性は主張しない。h_len と h_b は別々のスペクトルである。長さの種類だけを数えるこの証明から、h_b の上界は出ない。


## 4. 有限ターゲットの剛性と、型付けによる正しい非自明例

### 4.1 定理 C（同じ型の受理語の真因子禁止）

**定理 C.** `L` が有限かつ `(1,s)`-代入可能なら、同じ `s`-型を持つ相異なる受理語 `x,y∈L∩Σ⁺` について、`x` は `y` の真の連続因子ではない。従って特に、`L` の**混合受理語全体は factor-antichain** である。

**証明.** `y=u x v` とし `|uv|>0` と仮定する。`x,y` はともに受理語なので、共通受理文脈 `(ε,ε)` を持つ。同型ゆえ `D_L(x)=D_L(y)`。一方 `(u,v)∈D_L(x)` は `uxv=y∈L` によるから、`(u,v)∈D_L(y)`、すなわち `u y v∈L`。`y_0:=y`、`y_{k+1}:=u y_k v` と定める。既に `y_1∈L` である。帰納的に `y_k∈L` とすると、`y_k` と `y` はともに受理語で同じ型（`y` が純なら `u,v` も純、`y` が混合なら `y_k` も混合）なので、空文脈を共有して `D_L(y_k)=D_L(y)`。`(u,v)∈D_L(y)` より `y_{k+1}∈L`。従って全ての `k≥0` で `u^k y v^k∈L`。長さは `|y|+k|uv|` で狭義増加。`L` の有限性に反する。□

**注意.** ここで真の因子であることが重要。`x,y` が同長で異なる場合はこの議論を適用できない。また混合**因子**（受理語でない部分語）全体が反鎖とは言っていない。

### 4.2 定理 D（`(a^t|b)^m` の解析的な全面証明）

**定理 D.** 任意の整数 `t,m≥1` に対し

\[
 H_{t,m}:=(\{a^t,b\})^m
\]

は `(1,s)`-代入可能である。

**証明.** 語 `w` の重みを `Q(w):=|w|_b+|w|_a/t` と置く。これは連接に関して加法的であり、`Q(a^t)=Q(b)=1`。`H_{t,m}` に所属することは、(i) **全ての極大 a-run の長さが t の倍数**、(ii) `Q(w)=m`、の二条件と同値である。各極大 a-run を `a^t` に分割し、それと b を左から読むことで逆向きも証明される。

同じ型で、一穴文脈 `(u,v)` により `uxv,uyv∈H_{t,m}` となる非空因子 `x,y` を取る。加法性から `Q(x)=Q(y)`。もし型 1 なら `x=a^p,y=a^q` と書け、`p/t=q/t` だから `x=y`。よって分布一致は自明。

型 ζ の場合、両因子は b を含む。`x` の**最初の b に先行する a-run 長**を `\alpha(x)`、**最後の b に後続する a-run 長**を `\beta(x)` とする（始端・終端が b なら零）。`x` 内部で二つの b の間にある全 a-run は `t` の倍数である。これは `uxv∈H_{t,m}` から従い、`y` についても同じ。さらに左外部語 `u` の末尾 a-run の長さを `c` とすれば、`uxv,uyv` の最初の b の直前で生じる run の長さはそれぞれ `c+\alpha(x)`, `c+\alpha(y)` （u に b があってもこれらは直前の run である）。従って両者の t での剰余は零で、`\alpha(x)≡\alpha(y) (mod t)`。同様に右外部語 v の先頭 a-run を使うと `\beta(x)≡\beta(y) (mod t)`。

いま任意の別文脈 `(p,q)` を取る。`p x q` において `x` の内側の a-run はすでに適切である。外部の内部 a-run は `p,q` にのみ依存し、`x` の左境界・右境界に接する run の剰余は上の `\alpha,\beta` の一致で `y` と等しい。したがって条件 (i) は `p x q` と `p y q` で同時に成立／不成立する。条件 (ii) も `Q(x)=Q(y)` により同時に成立／不成立する。従って任意の `(p,q)` について `p x q∈H_{t,m} ⇔ p y q∈H_{t,m}`、すなわち `D(x)=D(y)`。□

**圧縮と θ の正確値.** `m=2^n` に対して `A₀→a^t\mid b`、`A_i→A_{i-1}A_{i-1}` (`1≤i≤n`)、開始記号 `A_n` は reduced good、rank≤2、`‖G‖=6n+t+4`。全 `A_i` の最短収率は `b^{2^i}`（長さ `2^i`）。各 `A_i` の唯一の二分規則を使う最短成功文長は `2^n`、底の `A₀→b` も `2^n`、`A₀→a^t` の最短成功使用は、残りの `2^n−1` 個の底を全て b にした文なので `2^n−1+t`。よって**各規則の最短成功使用を検討した正確値**は

\[
\bar\theta_G=2^n-1+t\quad(t≥1),\qquad
\mu_1(H_{t,2^n})=t2^n.
\]

`t=1` では `θ=2^n`、式は引き続き正しい。この族には `2^{2^n}` 語があるが、θ も指数的。**(N) の反例にはならない。** また t≥2 なら一般に Clark–Eyraud の無型代入可能性までは主張できない。例えば `H_{2,2}={aaaa,aab,baa,bb}` の `x=aa,y=b` は文脈 `(ε,aa)` を共有するが、区別文脈 `(a,a)` では `aaaa∈H_{2,2}`、`aba∉H_{2,2}`。したがって本定理は**型付き**である。

### 4.3 追加定理 F：一語削除がクラス所属を保つための必要十分条件

文脈 E=(u,v) に対して E[x]=uxv と書く。以下の条件は二穴ではなく、**二つの別々の一穴文脈** E,F に関する。

**定理 F.** L が (1,s)-代入可能で w∈L とする。L\{w} が (1,s)-代入可能でないことと、次を満たす非空因子 x,y と一穴文脈 E,F が存在することは同値である。

\[
 s(x)=s(y),\quad F[y]=w,\quad
 E[x],E[y],F[x]\in L\setminus\{w\}.\tag{F}
\]

三つの受理語 E[x],E[y],F[x] は互いに異なる必要はない。要求されるのは、どれも削除語 w と違うことである。

**証明。** (F) があれば L\{w} で x,y は E を共有するが、F は x のみを受理する。従って代入可能性に反する。

逆に L\{w} が代入可能でなければ、等型の非空 x,y と共有文脈 E、および分布を区別する F が存在する。必要なら x,y を交換して F[x]∈L\{w}、F[y]∉L\{w} とする。一方 E[x],E[y],F[x] は全て L に属し、元の L の代入可能性から F[y]∈L である。除いたのは一語だけなので F[y]=w。これで (F) が得られる。□

L⁺ が CFL なら (L\{w})⁺ も CFL である。これは CFG と、w だけを除く正則言語を受理する有限オートマトンとの積で示せる。具体的には各非終端 A にオートマトンの入出力状態を付した [p,A,q] を作り、規則右辺を通る各状態列を列挙する。端末での状態更新と子の入出力状態を合わせ、開始状態から受理状態へ至る開始規則を選べば、元の導出と受理走行を同時に表す CFG になる。従って本問の L∈C^{mcf}_{1,s} では、(F) の不在は **L\{w}∈C^{mcf}_{1,s} の必要十分条件**でもある。w=ε の場合は非空因子を埋めた文が ε にならないので (F) は起こらず、削除は常に許される。

**識別下界の系。**

\[
 \operatorname{Del}(L):=\{w\in L:L\setminus\{w\}\in C^{mcf}_{1,s}\}
\]

と置く。クラス全域に特徴標本を持つ任意の集合駆動型作用素の L に対する特徴標本 K は Del(L) を含む。

**証明。** w∈Del(L) が K に含まれないと仮定し、L\{w} の特徴標本 K' を取る。有限集合 K∪K' は L と L\{w} の双方に含まれ、それぞれの特徴標本を含む。同一の集合に作用させた出力言語が L と L\{w} の双方に等しくなる必要があり矛盾する。従って各 w∈Del(L) は K に必須である。特に Del(L) は有限で、

\[
 \|K\|_+\ge\sum_{w\in\operatorname{Del}(L)}(|w|+1)
\]

が成立する。□

**検査器としての意味。** 明示的な有限 L なら、w の全非空因子切断 F[y]=w と、L の全因子 x、共通文脈 E を列挙すれば (F) を完全に判定できる。末尾コードではこの判定と L\{w} の直接の代入可能性判定を、長さ1～3の全二文字語からなる全16,384部分集合のうち代入可能なものについて照合する。計算は定理 F の証明の代用ではない。

**小さい障害の手計算。** L=Σ³ は全語長が3なので、共有文脈を持つ因子は同長となり、その同長因子の全分布は一致する。よって (1,s)-代入可能である。しかし w=bba を除くと、x=ab,y=ba、E=(ε,a)、F=(b,ε) は

\[
 E[x]=aba,\quad E[y]=baa,\quad F[x]=bab,\quad F[y]=bba
\]

を与える。x,y はともに型ζ、前の三語は残り最後だけが除かれるため、削除後は代入可能ではない。この四隅を確認せずに「有限言語なら各語を削除できる」とする論法は誤りである。


## 5. 失敗した構成と正確な証明書

### 5.1 `A_i→A_{i-1}A_{i-1}|b` は全 `n≥2` で不適格

`A₀→a`、`A_i→A_{i-1}A_{i-1}\mid b`、開始 `A_n`。`n≥2` では `b∈L_n`（根の短絡）かつ `bb∈L_n`（少なくとも一段を二分して、その両子を b へ短絡できる。n≥2 の場合、より上の段の二分にも b 短絡を配して `bb` とできる）。両語は型 ζ で `b` は `bb` の真因子だから、定理 C により `(1,s)`-代入可能ではない。

**具体的な n=2 証明書（コードでも出力）**：`L₂={aaaa,aab,baa,bb,b}`。`x=aab`, `y=b`, 共通文脈 `E=(ε,ε)` で双方受理、型 ζ。区別文脈 `F=(ε,aa)` では `F[x]=aabaa∉L₂`、`F[y]=baa∈L₂`。従って `D(x)≠D(y)`。

**原文法の θ の正確値.** 任意の `i` の無型最短収率は b（`A₀` だけ a）で長さ 1。`A_i` を根の binary chain で使う最短外部長は `n−i`。`A₀→a` は `θ_G(R)=n+1`、`A_i→A_{i-1}A_{i-1}` は `θ_G(R)=n−i+2`、`A_i→b` は `θ_G(R)=n−i+1`。最大は `θ=n+1`、`g=8n+3`。純語 `a^{2^n}` は指数長。**θ が小さいことは事実だがクラス所属が偽**。

### 5.2 b-run の長さと a-padding を変える短絡の検査

同じ二分規則で短絡だけを次の５通りにした。`A₀→a`、`A_i→A_{i-1}A_{i-1}|z_i` で `z_i=b`,`b^i`,`ab^ia`,`a^iba^i`,`ab^{2i+1}a`。全て reduced good、rank≤2、生成言語が有限。以下は**実際の n=2 または n=3 における全因子・全文脈の厳密な違反証明書**であり、任意 n の代入可能性の外挿ではない。

| 短絡 | 最初に見つかった失敗 | 共通 E, x, y | 区別 F と判定 |
|---|---:|---|---|
| `b` | n=2 | `E=(ε,ε)`, `x=aab`, `y=b` | `F=(ε,aa)`、x 偽、y 真 |
| `b^i` | n=3 | `E=(ε,ε)`, `x=aaaaaab`, `y=bbb` | `F=(ε,aa)`、x 偽、y 真 |
| `ab^ia` | n=2 | `E=(ε,a)`, `x=aaab`, `y=abaa` | `F=(ε,ba)`、x 偽、y 真 |
| `a^iba^i` | n=2 | `E=(ε,a)`, `x=aaab`, `y=aaba` | `F=(a,ε)`、x 偽、y 真 |
| `ab^{2i+1}a` | n=2 | `E=(ε,a)`, `x=aaabbb`, `y=abbbaa` | `F=(ε,bbba)`、x 偽、y 真 |

各行の真偽は、完全に展開した該当 `L_n` に対する文字列所属の真偽であり、部分サンプル推定ではない。いずれも**同型 ζ**の因子二つが共通文脈を持つので、異なる分布が一件あれば `(1,s)`-代入可能性は厳密に否定される。異なる b-run の隣接・融合を、「標識だから別の辺」と見なすような省略はしていない。

## 6. 未決着の核心と十分な未証明命題

### 6.1 肯定に十分な (U)

> **(U) [未証明].** 固定 `r≥2` に対し固定多項式 `q_r` が存在し、あらゆる `L∈C^{mcf}_{1,s}` と reduced good rank≤r 表示 `G` の、型 1 を実現する任意の非終端 `A` について、導出的文脈 `E_A` に対し `κ_A:=min{k≥1:E_A[a^k]∈L}≤q_r(g,θ)`。

十分性の論証：型 ζ の非終端には §3.1 の**常に成立する** `2(r+1)vθ` の短い型付き収率がある。型 1 の分布類には、原稿 `lem:app-u1-fillers` から長さ `κ_A` の代表がある。よって `τ≤max(2(r+1)vθ,q_r(g,θ))`、`cor:distribution-representatives` で (P) の上界になる。これは証明したことではなく、**(U) ⇒ (P) の論理的十分性**である。

本報告 §3 が (U) を証明するのは、`M` が有限で `log₂(M+1)` を入力パラメータの多項式で抑えられる場合だけ。一般に `M=∞`、あるいは `M` が二重指数級の有限集合の場合を残す。

### 6.2 否定に十分な (N)

> **(N) [未証明].** `n` に依存する reduced good、rank≤2 の CFG `G_n` と有限 `(1,s)`-代入可能言語 `L_n=L(G_n)` が存在し、`‖G_n‖·\bar θ_{G_n}=n^{O(1)}`、`L_n∩a^+={a^{N_n}}`、`N_n=n^{ω(1)}`。

これが成立すれば、原稿 `prop:rare-type` により、型 1 を含む全特徴標本は `a^{N_n}` を含む。したがって二つの固定作用素のみならず、**クラス全域に特徴標本を持つ任意の集合駆動型作用素**に下界が及ぶ。この帰結は正しいが、**(N) 自体は構成できていない**。

**既報から継承する障害.** (N) の有限族なら §2–§3 より `M(L_n)≥2^{N_n/((r+1)v_nθ_n)}−1`。従って長い純語を維持し小さい θ を作るには、superpolynomial な個数どころか**superexponential に多くの混合語**と、短い混合語の b-run の多発を両立させる必要がある。そのうえ §4.1 の受理混合語同士の factor-antichain 条件を満たさねばならない。二文字での位相符号化をこれらすべてに適合させる方法は得られていない。さらに §3.4 から正の b 個数の種類 h_b も超多項式が必要になる。削除型の下界を狙う場合は §4.3 の条件を全 n で証明する必要がある。

### 6.3 一穴と二穴の区別

本報告の §2–§4 の論証は **一穴の因子・文脈のみ**で完結し、二穴で可能な `(a^i,a^j)↔(a^{i'},a^{j'})` の移送を一切利用しない。`lem:app-u1-transfer` と `lem:app-u1-deep` の二穴等価性・Parikh 飽和は、本問題へ適用していない。`{a^{20},a^6ba^6}` は一穴代入可能であっても Parikh 飽和でない、という既報の警告は引き続き有効である。

## 7. 論文挿入用 English LaTeX（証明付き）

本節は証明済みの定理 A と定理 B のみを英語で記す。`\label` は既存 label に重複しないよう仮に付与した。原稿 `lem:thickness-equivalence`、`thm:data-from-typed-thickness` を既知補題として引用する。文献上の新規性は **not investigated**。

```latex
\begin{theorem}[An exponential cube of mixed defects]
\label{thm:binary-u1-exponential-defects}
Let $G$ be a reduced good fan-out-one grammar of rank at most $r$,
with $v$ nonterminals and $\theta=\bar\theta_G$. Suppose $a^N$
is a shortest pure word in $L(G)$ and $N>\theta$. Then
\[
 |\{w\in L(G): b\text{ occurs in }w,\ |w|<N\}|
 \ge 2^{\lceil N/((r+1)v\theta)\rceil}-1.
\]
No substitutability assumption is needed.
\end{theorem}
\begin{proof}
Choose a node-minimal derivation tree $T$ of $a^N$. Every yield
is nonempty and pure. A repeated nonterminal on a root-to-leaf path
could be cut out: this would either give a shorter accepted pure
word or preserve its length with fewer nodes. Thus every path has
at most $v$ nodes. Call a node heavy if its yield has length greater
than $\theta$. By Lemma~\ref{lem:thickness-equivalence}(ii), each
heavy node $u$ admits a replacement yield $z_u$ of length at most
$\theta$. Such a yield must contain $b$, since a pure replacement
would produce an accepted pure word shorter than $a^N$.

Let $F$ be the bottom frontier of heavy nodes, and put $h=|F|$.
Its yield intervals are pairwise disjoint. For every subset $J\subseteq F$,
replace exactly the subtrees at $J$ by derivations of their $z_u$.
All $2^h$ outcomes are accepted. They are pairwise distinct: for
$J\ne J'$, consider the leftmost frontier interval on which the
choices differ. All earlier output is identical. The replaced version
has its first $b$ within at most $\theta$ positions of this interval,
whereas the unreplaced version still has only $a$'s throughout the
original interval of length greater than $\theta$. Therefore their
outputs differ. Every nonempty $J$ yields a mixed word shorter than
$a^N$.

Heavy nodes are ancestor-closed; if $H$ is their number, then
$H\le vh$. Every letter of $a^N$ is written either by a heavy node
or by one of its light children. A heavy node writes at most
$\theta$ terminals and has at most $r$ children of length at most
$\theta$ that are light. Consequently
$N\le(r+1)\theta H\le(r+1)v\theta h$.
Since $N>\theta$, the root is heavy, and hence
$h\ge\lceil N/((r+1)v\theta)\rceil$. The claim follows.
\end{proof}

\begin{theorem}[Logarithmic dependence on the mixed slice]
\label{thm:binary-u1-log-mixed}
Let $G$ be a reduced good rank-at-most-$r$ CFG over
$\{a,b\}$, let $s(a)=1,s(b)=\zeta$, and put
$M=|L(G)\cap\Sigma^*b\Sigma^*|<\infty$,
$v=|V|$ and $\theta=\bar\theta_G$. Then
\[
 t_{\mathrm{typ}}(G,s)
 \le (r+1)v\theta\bigl(2+\log_2(M+1)\bigr).
\]
Consequently, if $L\in\mathcal C^{\mathrm{mcf}}_{1,s}$ has
$L(G)=L\cap\Sigma^+$, the two reconstruction operators have a
common characteristic sample $K$ satisfying
\[
 \|K\|_+\le3^r\|G\|\left(
 1+2\theta+r(r+1)v\theta(2+\log_2(M+1))\right)
 +\mathbf1_{\{\varepsilon\in L\}}.
\]
\end{theorem}
\begin{proof}
Fix a realized type-one nonterminal $A_1$ and choose a shortest
pure $A$-yield $a^\ell$. If $\ell\le\theta$ there is nothing to
prove. Otherwise apply the preceding theorem to a node-minimal
$A$-derivation. All its mixed outputs can be inserted into a single
successful derivational context $E_A$ of
Lemma~\ref{lem:thickness-equivalence}(iv); distinct outputs remain
distinct accepted mixed words. Thus
$2^{\lceil\ell/((r+1)v\theta)\rceil}-1\le M$ and
$\ell\le(r+1)v\theta\log_2(M+1)$.

For each realized type-$\zeta$ nonterminal, take a node-minimal
typed derivation. No typed nonterminal repeats on a path, so paths
have at most $2v$ nodes. Retain one path to a terminal occurrence
of $b$, erase the typing and replace every sibling subtree by an
untyped yield of length at most $\theta$. This is a valid derivation
that retains $b$ and has length at most $2v(r+1)\theta$.
Taking the maximum of these bounds and $\theta$ proves the typed
thickness inequality. The characteristic-sample inequality follows
from Theorem~\ref{thm:data-from-typed-thickness} and
$N_{\mathrm{typ}}\le2v+2^r|P|\le3^r\|G\|$.
\end{proof}
```

### 7.1 追補の英語 LaTeX：b-count spectrum と削除判定

```latex
\begin{theorem}[A bound in terms of the positive $b$-count spectrum]
\label{thm:binary-u1-b-count-spectrum}
Let $G$ be a reduced good CFG over $\{a,b\}$ of rank at most $r$,
and put $v=|V|$ and $\theta=\bar\theta_G$. For the typing
$s(a)=1$, $s(b)=\zeta$, suppose
\[
 h=\bigl|\{|w|_b:w\in L(G),\ |w|_b>0\}\bigr|<\infty.
\]
Then $t_{\mathrm{typ}}(G,s)\le(r+1)v\theta\max\{1,h\}$.
No substitutability assumption is required for this inequality.
If additionally $L\in\Cmcf{1}{s}$ and $L(G)=L\cap\Sigma^+$,
the two reconstruction operators admit a common characteristic sample
$K$ with
\[
 \|K\|_+\le3^r\|G\|
 \bigl(1+2\theta+r(r+1)v\theta\max\{1,h\}\bigr)
 +\mathbf1_{\{\varepsilon\in L\}}.
\]
\end{theorem}
\begin{proof}
Fix a nonterminal $A$ having a pure yield and choose a shortest pure
yield $a^\ell$, with a node-minimal derivation $T$. If $\ell\le\theta$,
its length satisfies the required bound. Otherwise every path of $T$
has at most $v$ nodes: cutting between two occurrences of the same
nonterminal either shortens the pure yield or preserves it with fewer
nodes. For each node of yield length greater than $\theta$, fix an
untyped yield of its nonterminal of length at most $\theta$.
It must contain $b$, since otherwise it would shorten $a^\ell$.
Let $F$ be the bottom frontier of these heavy nodes and let $m=|F|$.
Every heavy node lies on a path to $F$, so there are at most $vm$
heavy nodes. Counting their explicit terminals and their light children
gives $\ell\le(r+1)v\theta m$.

List the nodes of $F$ as $u_1,\ldots,u_m$. For $j=1,\ldots,m$,
replace exactly the first $j$ subtrees by the chosen short mixed
yields $z_i$, and insert the result in one fixed successful context
$E_A$. These are accepted words whose $b$-counts are
\[
 |(E_A)_{\mathrm{fix}}|_b+\sum_{i=1}^j|z_i|_b.
\]
The counts are positive and strictly increasing. Hence $m\le h$,
and $\ell\le(r+1)v\theta h$.

If $A$ has a mixed yield, some reachable nonterminal $B$ has a rule
writing $b$. Choose a shortest dependency path from $A$ to $B$,
which has at most $v$ vertices. Use rules realizing this path,
use the $b$-writing rule at its last vertex, and complete every
remaining child by a yield of length at most $\theta$.
This produces a mixed $A$-yield of length at most $(r+1)v\theta$.
The maximum over realized types proves the first assertion.
The second follows from Corollary~\ref{cor:distribution-representatives},
$\tau\le t_{\mathrm{typ}}$, and
$N_{\mathrm{typ}}\le2|V|+2^r|P|\le3^r\|G\|$.
\end{proof}

\begin{proposition}[An exact single-word deletion criterion]
\label{prop:binary-u1-single-deletion}
Let $L$ be $(1,s)$-substitutable and let $w\in L$.
Then $L\setminus\{w\}$ fails to be $(1,s)$-substitutable if and
only if there exist $x,y\in\Sigma^+$ and one-hole contexts $E,F$
such that
\[
 s(x)=s(y),\qquad F[y]=w,\qquad
 E[x],E[y],F[x]\in L\setminus\{w\}.
\]
\end{proposition}
\begin{proof}
Such a quadruple supplies a common accepting context for $x,y$
in the smaller language and another context accepting $x$ but not $y$.
Conversely, take a substitutability violation in the smaller language,
orienting it so that $F[x]$ is accepted and $F[y]$ is not.
The common context $E$ also accepts both factors in $L$.
Substitutability of $L$ therefore gives $F[y]\in L$.
As this word is absent only in $L\setminus\{w\}$, it equals $w$.
\end{proof}
```


## 8. 計算方法と検査範囲

**コード（§9）を実際に実行し、その標準出力をそのまま §10 に転載した。Python 標準ライブラリのみ。** `complete_check(L)` は、**完全に列挙した有限** `L` の各語 `w`、全切断位置 `0≤i<j≤|w|` について、非空因子 `x=w[i:j]` と、それを受理する一穴文脈 `(w[:i],w[j:])` を全て登録する。`D_L(x)` はこれらの集合に厳密に等しい。実際、任意の `uxv∈L` は切断位置 `i=|u|,j=|ux|` から列挙され、その逆は自明である。同型・共通文脈の全因子対について集合比較するので、戻り値の `FAIL` は厳密な反例であり、`PASS` はその**特定の有限言語**についての厳密判定である。無限言語や未列挙の n への外挿は行わない。

実行対象は `H_{t,m}` の `t=1,2,3` と `m=1,…,5` の全 15 個、短絡５方式の `n=1,2,3`（各方式で最初の失敗が出たところで停止）、トークン文法の `n=1,2,3`（`m=2,4,8`、最後は256語）、短絡文法の元規則ごとの `θ_G(R)`、および `n=6` での8個の独立欠陥区間から得られる全256文字列の相異性である。短絡文法の `θ` は、各非終端の最短収率 `d_A`、最短の導出的外部文脈 `o_A` を無向でなく文法依存順に計算して、**各規則 `R:A→ρ(B_1,…,B_k)` に対し `θ_G(R)=o_A+|ρ|_term+Σ_j d_{B_j}`** を使う。この等式は非削除の非循環 CFG で、親の外部完成と子の最短導出を独立に選べるため正確である。`theta` はその**最大**であり、ある一語で全規則を使用する必要はない。

再現条件：`python3 Binary_U1_FanoutOne_Repro.py` と同等の実行。ファイルとしてはこの報告の §9 のコードをその名前で保存して使える。ログはプログラムから標準出力へ出した全文であり、任意の行の省略や手編集はしていない。


### 8.1 今回追加した系統列挙と削除検査

旧プログラムの全検査も今回再実行した。追加では `A₀→a, A_i→A_{i−1}A_{i−1}|z_i` に対し、各レベルの z_i を独立に `{b,bb,ab,ba,bab,baab}` から選び、n=1,2,3 の計258文法を完全生成・完全検査した。打切り・容量超過・未検査は0。縮約済み good、rank≤2 であることは規則形から従う。全258文法について型付き最短収率と定理 E および §3.5 の数値上界を検算した。実数の対数の丸めに頼らず `floor(log₂(M+1))` を整数の bit_length で計算している。

文法パラメータは d₀=1、d_i=min(2d_{i−1},|z_i|)、o_n=0、o_i=o_{i+1}+d_i により厳密計算する。各規則のコストは基底 o₀+1、レベル i の二分規則 o_i+2d_{i−1}、短絡規則 o_i+|z_i|。θ はそれらの最大。サイズは `(n+1)+2+Σ_i(6+|z_i|)`。依存経路はレベルごとに必須で、道外兄弟を最短に完成する選択が実現するため、いずれも下界だけでなく正確値である。

さらに、長さ1～3の二文字語14語の全16,384部分集合を検査し、そのうち代入可能な L の全 w∈L について、定理 F の矩形条件と L\{w} の直接判定が一致することを検査した。結果は代入可能な集合が200、削除照合が578件で、全件一致した。文法の258候補は8件合格・250件不合格で、n=3 の216件は全て不合格だった。この有限検査は全ての n の証明には使わない。個数・成功率・比率は全て**観測**。追加コードの失敗例には因子対・共有文脈・区別文脈を出力する。

## 9. 再現用 Python ソース全文

```python
#!/usr/bin/env python3
"""Reproducible finite checks for binary U1, standard library only.

Every reported substitutability result is an EXHAUSTIVE check of the
explicitly enumerated finite language, not evidence for arbitrary n.
"""
from collections import defaultdict
from itertools import product


def typ(w):
    assert w
    return 'zeta' if 'b' in w else '1'


def complete_check(words):
    """Check all positive factors and ALL two-sided distributions of finite L.

    Return None or a certificate (x,y,common_context,test_context,x_ok,y_ok).
    Both contexts are (left,right), where the test context distinguishes.
    """
    words = frozenset(words)
    dist = defaultdict(set)
    for w in sorted(words):
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                dist[w[i:j]].add((w[:i], w[j:]))
    by_context = defaultdict(set)
    for x, contexts in dist.items():
        for e in contexts:
            by_context[(typ(x), e)].add(x)
    for (t, common), factors in sorted(by_context.items()):
        factors = sorted(factors)
        for i, x in enumerate(factors):
            for y in factors[i + 1:]:
                if dist[x] != dist[y]:
                    witness = sorted(dist[x] ^ dist[y])[0]
                    u, v = witness
                    return x, y, common, witness, (u+x+v in words), (u+y+v in words)
    return None


def tokens(t, m):
    return {''.join(parts) for parts in product(('a'*t, 'b'), repeat=m)}


def shortcuts(n, mode):
    """A0 -> a; Ai -> Ai-1 Ai-1 | shortcut(i)."""
    L = {'a'}
    for i in range(1, n+1):
        options = {
            'b': 'b',
            'b^i': 'b'*i,
            'ab^ia': 'a' + 'b'*i + 'a',
            'a^iba^i': 'a'*i + 'b' + 'a'*i,
            'ab^(2i+1)a': 'a' + 'b'*(2*i+1) + 'a',
        }
        L = {x+y for x in L for y in L} | {options[mode]}
    return L


def grammar(n, mode):
    """Each production: (lhs, sequence of ('T',term) or ('N',name))."""
    p = [('A0', (('T','a'),))]
    for i in range(1,n+1):
        z = {'b':'b', 'b^i':'b'*i,
             'ab^ia':'a'+'b'*i+'a',
             'a^iba^i':'a'*i+'b'+'a'*i,
             'ab^(2i+1)a':'a'+'b'*(2*i+1)+'a'}[mode]
        p.append((f'A{i}', (('N',f'A{i-1}'),('N',f'A{i-1}'))))
        p.append((f'A{i}', (('T',z),)))
    return p


def parameters(n, mode):
    """Exact grammar size and EVERY shortest successful use of every rule.

    Dynamic programming works here because these example grammars are acyclic.
    An outside path chooses shortest sibling yields at each ancestor.
    """
    p = grammar(n,mode)
    nt = [f'A{i}' for i in range(n+1)]
    d = {}
    for A in nt:
        costs = []
        for lhs, rhs in p:
            if lhs != A: continue
            costs.append(sum(len(v) if k=='T' else d[v] for k,v in rhs))
        d[A] = min(costs)
    inf = float('inf')
    outside = {A:inf for A in nt}
    outside[f'A{n}'] = 0
    for i in range(n,-1,-1):
        A=f'A{i}'
        for lhs,rhs in p:
            if lhs!=A: continue
            for j, (k,child) in enumerate(rhs):
                if k!='N': continue
                other = sum(len(v) if k2=='T' else d[v]
                            for h,(k2,v) in enumerate(rhs) if h!=j)
                outside[child] = min(outside[child],outside[A]+other)
    vals=[]
    for lhs,rhs in p:
        cost = outside[lhs]+sum(len(v) if k=='T' else d[v] for k,v in rhs)
        vals.append((lhs, ''.join(v if k=='T' else '{'+v+'}' for k,v in rhs),cost))
    g = len(nt) + sum(1+sum(k=='N' for k,v in rhs)+
                       sum(len(v) if k=='T' else 1 for k,v in rhs)
                       for lhs,rhs in p)
    return g,max(x[2] for x in vals),vals


def witness_str(c):
    if c is None: return 'PASS'
    x,y,e,f,vx,vy=c
    return ('FAIL x=%r y=%r common=%r test=%r acceptance=(%s,%s)'
            % (x,y,e,f,vx,vy))


def cube_check(n=6):
    g,theta,_=parameters(n,'b')
    q=0
    while (1<<q) <= theta: q+=1
    assert q <= n
    blocks=1<<(n-q)
    assert blocks <= 12
    plain='a'*(1<<q)
    seen=set()
    for chosen in product((0,1),repeat=blocks):
        w=''.join('b' if x else plain for x in chosen)
        assert w not in seen
        seen.add(w)
        assert (not any(chosen)) or ('b' in w and len(w)<(1<<n))
        # Explicit derivation: each block is Aq -> b or Aq -> a^(2^q),
        # and the upper n-q levels concatenate the blocks pairwise.
    alternating=tuple(j%2==0 for j in range(blocks))
    w=''.join('b' if x else plain for x in alternating)
    runs=sum(c=='b' and (i==0 or w[i-1]!='b') for i,c in enumerate(w))
    return g,theta,q,blocks,len(seen),runs


def old_main():
    print('Python standard-library exhaustive finite checks; no randomized sampling')
    print('Type: a^+ -> 1; any positive word containing b -> zeta')
    print('Positive factors only; all contexts represented by occurrences in full finite L')
    for t in (1,2,3):
        for m in (1,2,3,4,5):
            L=tokens(t,m)
            result=complete_check(L)
            print('TOKENS t=%d m=%d words=%d %s'%(t,m,len(L),witness_str(result)))
            assert result is None
    for mode in ('b','b^i','ab^ia','a^iba^i','ab^(2i+1)a'):
        for n in (1,2,3):
            L=shortcuts(n,mode)
            result=complete_check(L)
            g,theta,vals=parameters(n,mode)
            print('SHORTCUT mode=%s n=%d words=%d g=%d theta=%d %s' %
                  (mode,n,len(L),g,theta,witness_str(result)))
            if result is not None: break
    for n in (2,3,4,6):
        g,theta,vals=parameters(n,'b')
        print('NAIVE-THICKNESS n=%d g=%d theta=%d pure-N=%d rule-costs=%r'%
              (n,g,theta,1<<n,[p[2] for p in vals]))
        assert g==8*n+3 and theta==n+1
    for n in (1,2,3):
        # A0 -> a^2 | b; Ai -> Ai-1 Ai-1, which generates (aa|b)^(2^n).
        m=1<<n
        g=6*n+2+4  # exact: |V|+binary rules+two terminal rules, t=2
        theta=m+1  # one 'aa' among m tokens, all other tokens 'b'
        L=tokens(2,m)
        assert complete_check(L) is None
        print('TOKEN-GRAMMAR n=%d m=%d words=%d g=%d theta=%d %s'%
              (n,m,len(L),g,theta,'PASS'))
    g,theta,q,h,count,runs=cube_check()
    print('DEFECT-CUBE n=6 g=%d theta=%d frontier-level=%d blocks=%d distinct=%d alternating-b-runs=%d'%
          (g,theta,q,h,count,runs))
    assert count==2**h and runs >= (h+1)//2
    print('ALL ASSERTIONS PASSED; numerical cases are OBSERVATIONS only')



from collections import defaultdict
from itertools import product
from fractions import Fraction


def dist_of(L):
    D=defaultdict(set)
    for w in sorted(L):
        for i in range(len(w)):
            for j in range(i+1,len(w)+1):
                D[w[i:j]].add((w[:i],w[j:]))
    return D


def deletable_by_rectangle(L,w):
    # Precondition: L is substitutable. Return bool, obstruction certificate.
    D=dist_of(L)
    for i in range(len(w)):
        for j in range(i+1,len(w)+1):
            y=w[i:j]; F=(w[:i],w[j:])
            for x in sorted(D):
                if ('b' in x)!=('b' in y) or x==y: continue
                fx=F[0]+x+F[1]
                if fx not in L or fx==w: continue
                for E in sorted(D[x]&D[y]):
                    ex=E[0]+x+E[1]; ey=E[0]+y+E[1]
                    if ex!=w and ey!=w:
                        return False,(x,y,E,F,ex,ey,fx,w)
    return True,None


def grammar_data(codes):
    # A0 -> a, Ai -> Ai-1 Ai-1 | codes[i-1].
    n=len(codes); langs=[{'a'}]; d=[1]
    for z in codes:
        langs.append({x+y for x in langs[-1] for y in langs[-1]}|{z})
        d.append(min(2*d[-1],len(z)))
    o=[0]*(n+1)
    for i in range(n-1,-1,-1): o[i]=o[i+1]+d[i]
    costs=[o[0]+1]
    for i,z in enumerate(codes,1): costs.extend([o[i]+2*d[i-1],o[i]+len(z)])
    g=n+1+2+sum(6+len(z) for z in codes)
    theta=max(costs)
    return langs,g,theta,costs


def extra_main():
    print('ADDITIONAL EXACT CHECKS: no caps, no truncation, no randomness')
    universe=[''.join(t) for n in (1,2,3) for t in product('ab',repeat=n)]
    passed=checks=0
    for mask in range(1<<len(universe)):
        L={w for i,w in enumerate(universe) if mask>>i&1}
        if complete_check(L) is not None: continue
        passed+=1
        for w in sorted(L):
            actual=complete_check(L-{w}) is None
            pred,cert=deletable_by_rectangle(L,w)
            assert actual==pred,(L,w,cert)
            checks+=1
    print('ALL SUBSETS of words of lengths 1..3: total=16384 substitutable=%d deletion-tests=%d'%(passed,checks))
    L={''.join(t) for t in product('ab',repeat=3)}
    print('DELETION certificate for bba from Sigma^3:',deletable_by_rectangle(L,'bba'))
    codeset=('b','bb','ab','ba','bab','baab')
    total=ok=assertions=0; best=Fraction(0); best_data=None
    by_n=[]
    for n in (1,2,3):
        count=good=0
        for codes in product(codeset,repeat=n):
            total+=1; count+=1
            langs,g,theta,costs=grammar_data(codes)
            L=langs[-1]; v=n+1
            M=sum('b' in w for w in L)
            h=len({w.count('b') for w in L if 'b' in w})
            # floor log2(M+1), with exact integer arithmetic
            ellog=(M+1).bit_length()-1
            ttyp=max(min(map(len,[w for w in Q if ('b' in w)==t]))
                      for Q in langs for t in (False,True)
                      if any(('b' in w)==t for w in Q))
            assert ttyp<=3*v*theta*max(1,h)
            assert ttyp<=3*v*theta*max(1,ellog)
            N=2**n
            if N>theta:
                lower=(N+3*v*theta-1)//(3*v*theta)
                short=[w for w in L if 'b' in w and len(w)<N]
                assert len(short)>=2**lower-1
                assert len({w.count('b') for w in short})>=lower
            assertions+=1
            result=complete_check(L)
            if result is None:
                ok+=1; good+=1
                score=Fraction(N,g*theta)
                if score>best: best,best_data=score,(codes,g,theta,N,M,h,costs)
        by_n.append((n,count,good))
    print('SHORTCUT GRID n,total,substitutable:',by_n)
    print('TOTAL=%d PASS=%d FAIL=%d SKIPPED=0 bound-checks=%d'%(total,ok,total-ok,assertions))
    print('MAX mu1/(g theta) among PASS:',str(best),'case=',best_data)
    for codes in [('b','bb','bbb'),('bab','baab','baaab'),('baab','baaab','baaaab')]:
        L,g,theta,costs=grammar_data(codes)
        print('CANDIDATE',codes,'g=',g,'theta=',theta,'all-rule-costs=',costs,
              'certificate=',complete_check(L[-1]))
    print('ADDITIONAL ASSERTIONS PASSED; all numerical outcomes are observations')


if __name__=='__main__':
    old_main()
    extra_main()
```

## 10. 実行ログ全文

```text
Python standard-library exhaustive finite checks; no randomized sampling
Type: a^+ -> 1; any positive word containing b -> zeta
Positive factors only; all contexts represented by occurrences in full finite L
TOKENS t=1 m=1 words=2 PASS
TOKENS t=1 m=2 words=4 PASS
TOKENS t=1 m=3 words=8 PASS
TOKENS t=1 m=4 words=16 PASS
TOKENS t=1 m=5 words=32 PASS
TOKENS t=2 m=1 words=2 PASS
TOKENS t=2 m=2 words=4 PASS
TOKENS t=2 m=3 words=8 PASS
TOKENS t=2 m=4 words=16 PASS
TOKENS t=2 m=5 words=32 PASS
TOKENS t=3 m=1 words=2 PASS
TOKENS t=3 m=2 words=4 PASS
TOKENS t=3 m=3 words=8 PASS
TOKENS t=3 m=4 words=16 PASS
TOKENS t=3 m=5 words=32 PASS
SHORTCUT mode=b n=1 words=2 g=11 theta=2 PASS
SHORTCUT mode=b n=2 words=5 g=19 theta=3 FAIL x='aab' y='b' common=('', '') test=('', 'aa') acceptance=(False,True)
SHORTCUT mode=b^i n=1 words=2 g=11 theta=2 PASS
SHORTCUT mode=b^i n=2 words=4 g=20 theta=3 PASS
SHORTCUT mode=b^i n=3 words=17 g=30 theta=5 FAIL x='aaaaaab' y='bbb' common=('', '') test=('', 'aa') acceptance=(False,True)
SHORTCUT mode=ab^ia n=1 words=2 g=13 theta=3 PASS
SHORTCUT mode=ab^ia n=2 words=5 g=24 theta=5 FAIL x='aaab' y='abaa' common=('', 'a') test=('', 'ba') acceptance=(False,True)
SHORTCUT mode=a^iba^i n=1 words=2 g=13 theta=3 PASS
SHORTCUT mode=a^iba^i n=2 words=5 g=25 theta=5 FAIL x='aaab' y='aaba' common=('', 'a') test=('a', '') acceptance=(False,True)
SHORTCUT mode=ab^(2i+1)a n=1 words=2 g=15 theta=5 PASS
SHORTCUT mode=ab^(2i+1)a n=2 words=5 g=29 theta=7 FAIL x='aaabbb' y='abbbaa' common=('', 'a') test=('', 'bbba') acceptance=(False,True)
NAIVE-THICKNESS n=2 g=19 theta=3 pure-N=4 rule-costs=[3, 3, 2, 2, 1]
NAIVE-THICKNESS n=3 g=27 theta=4 pure-N=8 rule-costs=[4, 4, 3, 3, 2, 2, 1]
NAIVE-THICKNESS n=4 g=35 theta=5 pure-N=16 rule-costs=[5, 5, 4, 4, 3, 3, 2, 2, 1]
NAIVE-THICKNESS n=6 g=51 theta=7 pure-N=64 rule-costs=[7, 7, 6, 6, 5, 5, 4, 4, 3, 3, 2, 2, 1]
TOKEN-GRAMMAR n=1 m=2 words=4 g=12 theta=3 PASS
TOKEN-GRAMMAR n=2 m=4 words=16 g=18 theta=5 PASS
TOKEN-GRAMMAR n=3 m=8 words=256 g=24 theta=9 PASS
DEFECT-CUBE n=6 g=51 theta=7 frontier-level=3 blocks=8 distinct=256 alternating-b-runs=4
ALL ASSERTIONS PASSED; numerical cases are OBSERVATIONS only
ADDITIONAL EXACT CHECKS: no caps, no truncation, no randomness
ALL SUBSETS of words of lengths 1..3: total=16384 substitutable=200 deletion-tests=578
DELETION certificate for bba from Sigma^3: (False, ('ab', 'bb', ('', 'b'), ('', 'a'), 'abb', 'bbb', 'aba', 'bba'))
SHORTCUT GRID n,total,substitutable: [(1, 6, 6), (2, 36, 2), (3, 216, 0)]
TOTAL=258 PASS=8 FAIL=250 SKIPPED=0 bound-checks=258
MAX mu1/(g theta) among PASS: 1/11 case= (('b',), 11, 2, 2, 1, 1, [2, 2, 1])
CANDIDATE ('b', 'bb', 'bbb') g= 30 theta= 5 all-rule-costs= [5, 5, 4, 4, 4, 4, 3] certificate= ('aaaaaab', 'bbb', ('', ''), ('', 'aa'), False, True)
CANDIDATE ('bab', 'baab', 'baaab') g= 36 theta= 9 all-rule-costs= [8, 8, 9, 8, 8, 8, 5] certificate= ('aaaabab', 'baabaa', ('', 'aa'), ('aa', ''), True, False)
CANDIDATE ('baab', 'baaab', 'baaaab') g= 39 theta= 10 all-rule-costs= [8, 8, 10, 8, 9, 8, 6] certificate= ('aaaaaabaab', 'baaaab', ('', ''), ('baa', 'aab'), False, True)
ADDITIONAL ASSERTIONS PASSED; all numerical outcomes are observations
```

## 11. 自己点検表（最終）

| 点検項目 | 結果 | 説明 |
|---|---|---|
| 一穴と二穴の論法を混同していないか | **確認済み** | §2–§4 は一穴のみ。定理 F の E,F も各々一穴であり、二穴文脈を意味しない。 |
| `(1,s)`-代入可能性を全 n・全因子・全文脈について証明したか | **定理 D と §3.4 の例について確認済み** | §4.2 は任意の整数 `t,m` に対する解析的全面証明。§3.4 の無限言語例も全分布を列挙して証明。失敗した短絡族については具体的に違反する n の証明書だけを主張。一般の (N) 候補族を証明したと称しない。 |
| `θ̄_G` を元の文法で正確に計算したか（各規則の最短成功使用を個別に） | **確認済み（具体例・列挙文法について）** | §4.2 のトークン文法、§5.1 の b 短絡文法は規則の全種別を場合分け。§8.1 の全規則コスト式と §9 の acyclic DP、ログでも確認。任意の未構成 `G_n` の θ は計算していない。 |
| 下界（任意の集合駆動作用素）と上界（特定の作用素）の量化を混同していないか | **確認済み** | §3 は B 作用素の上界、§6.2 の任意作用素の帰結は未証明 (N) を仮定した `prop:rare-type` の条件文。 |
| 有限検査を普遍命題の根拠にしていないか | **確認済み** | §2–§4 の一般命題は解析的証明。§5 の FAIL は特定の n に対する否定証明書。§10 の PASS は観測範囲限定。 |
| 文献上の新規性を調査したか | **未調査** | 既報・原稿との内容比較のみ。公刊文献に対する新規性は主張しない。 |
| 主問題 (P) または (N) を実際に決着したか | **未解決** | どちらも完全な証明がない。未解決を論文主定理として記さない。 |
| 今回実行したコードと全ログを末尾に収めたか | **確認済み** | §9 に Python 全文、§10 にログ全文。本文の最後はこの自己点検表。 |
