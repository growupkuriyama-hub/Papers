# ファンアウト2・三文字・内容型付けにおける否定方向の二設計と二穴近道障壁

**ファイル**：`chatgpt_negative_design_2026-11-06.md`  
**日付**：2026-11-06  
**判定**：**未解決**。反例族は構成できていない。二つの異なる構成原理のうち、(a) は (1)(2) を満たしながら二穴近道で (3) に失敗し、(b) は (2)(3) を満たしながら (1) の厚さに失敗する。ただし (a) から「倍増バックボーン」の一般的失格定理を得る。  
**凡例**：`[証明済み]` は本文に完全な証明を掲載、`[条件付き]` は条件を併記、`[計算機による観察（範囲）]` は計算のみ、`[予想]` は未証明。

## 0. 正本、照合範囲、原典とのずれ

- 数学的定義の正本：[`parked/2026-11-06_focus/main_before_focus_59pp.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/parked/2026-11-06_focus/main_before_focus_59pp.tex)、Git blob `1bc97358a49b4e80eef96abb0eee6de4ca10eecf`。`def:grammar-properties`、`def:class-cmcf`、`lem:thickness-equivalence`、`prop:rare-type`、`prop:full-content-types`、`op:fanout-two` を直接読んだ。
- 研究履歴：[`README.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/README.md)、Git blob `41ec9e963007ffd3e518a2d613e4db6d93be4453`、特に変更記録 (149)(150)(153)(155)。参照した報告：[`chatgpt_negative_design_2026-11-04.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_negative_design_2026-11-04.md)、[`claude_mu_ab_2026-11-05.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_mu_ab_2026-11-05.md)、[`chatgpt_virtual_length_2026-11-05.md`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_virtual_length_2026-11-05.md)。
- **出典不整合（重要）**：2026-11-06 の閲覧時点で README の **(158) は `prompt_chatgpt_tcs_referee_focus_2026-11-06.md`** を指し、依頼にある `(158) の定理6.2／補題4.1` を指さない。`reviews/chatgpt_shortcut_classification_2026-11-06.md` も指定場所の一覧にはない。したがってこれを**閲覧済み原典としては引用しない**。依頼の N3 の内容は実在する **(153) の補題4（同報告 §2.5）** と照合した。N5・N6 の指定スキーマは依頼から受け取った仮定として扱い、今回の証明書は独立に直接検査する。
- 現行 `main.tex` は集中版であって、指定の59頁版ではない。この混同は避けた。

### 0.1 厳密な SUB 規約

[証明済み・定義照合] `def:class-cmcf` に従い、`d=1,2` の穴の埋め草 `x_i,y_i` はいずれも非空。文脈 `E=v_0□_1v_1...□_dv_d` は両端 `v_0,v_d` が空でよく、`d=2` の中央 `v_1` は**非空**。`cont(x_i)=cont(y_i)` が各成分で一致し、`E[x],E[y],F[x]∈L` のとき `F[y]∈L` を要求する。文脈の固定語に関する内容の一致は要求しない。これを `SUB_d` とする。

[証明済み・定義照合] `good` は λ-free（各出力テンプレート成分非空）、nondeleting、nonpermuting、nonmerging の同時成立。特に**同じ二成分子の第1・第2成分を隣接して結合する** `S→A^{(1)}A^{(2)}` は `nonmerging` に反する。この点を避けるため、候補(a)の開始規則の二成分の間には実際の固定文字 `c` を置く。

[証明済み・定義照合] 文法サイズは

\[
\|G\|=|V|+\sum_{R:A\to\rho(B_1,\dots,B_s)}\left(1+s+\sum_j|\alpha_j|\right).
\]

規則厚さは `θ_G(R)=min{|w| : w は R を使う成功導出を持つ}`、`\bar θ_G=max(1,max_R θ_G(R))` であって、右辺長や非終端の最短生成長そのものではない。

### 0.2 希少型による否定への還元

**命題0 [証明済み・凍結原稿 `prop:rare-type`、`lem:thickness-equivalence`、`op:fanout-two`]** 固定三文字アルファベット、固定ランク `r≥2` に対し reduced good fan-out≤2 の族 `G_n` が

\[
\|G_n\|,\ \bar\theta(G_n)=n^{O(1)},\quad
L_n\in\mathcal C_{2,c_\Sigma},\quad
\mu_m(L_n)=n^{\omega(1)}
\]

を満たすなら、`op:fanout-two` は否定される。ここで `m` は実現される**任意の非空内容型**、とくに `{a,b}`、`{a}`、`{a,c}` でもよい。`\mathcal C_{2,c}` は定義上 arity 1 と2の両方を要求し、余分な `\mathcal C_1` の証明は不要（示してもよい）。

**証明**：`prop:rare-type` により `\mathcal B^{≤r}_{2,c}` の特徴標本は型 `m` の語を一つ以上含む。この語は `\mu_m` 文字以上だから、符号長 `\|F\|_+≥\mu_m+1`。さらに型 `m` の削除言語 `L_n^{\setminus m}` は同じ対象クラスに入るので、同命題が扱う**クラス全体で特徴標本を持つ任意の set-driven 演算子**にもこの下界が伝わる。`\|G_n\|,\bar\theta_G` がともに n の多項式なら、いかなる固定多項式 `p(\|G_n\|,\bar\theta_G)` でも最終的に `\mu_m` を上から抑えられない。よって否定となる。□

**注意**：`μ_m` の**唯一語性は不要**。また一つの特定学習器の Gold 収束時間までの下界は言っていない。`prop:full-content-types` の `m=3,f=2` の定数は `294(r+1)|V|\bar\theta_G` なので、全文字型 `{a,b,c}` は標的にできない（同命題の前提どおり）。

## 1. 候補(a)：ファンアウト2で全スロットを初めから生成

`n≥2`、`p=ab`、`M=2^n`、`e_i=a^i c b` (`i≥1`) とする。非終端 `D_0,…,D_n,S` のファンアウトは1、`A_1,…,A_n` のファンアウトは2。以下が**すべての規則**である。右辺の同一非終端を二度書いた場合も**別の子の出現**であり、コピー禁止には違反しない。

\[
\begin{array}{rl}
D_0&\to ab,\\
D_i&\to D_{i-1}D_{i-1}\mid a^icb\quad(1\le i\le n),\\
A_1&\to(ab,ab),\\
A_i&\to (d\,x,y)\quad [d\in D_{i-1},(x,y)\in A_{i-1}],\\
A_i&\to (x,y\,d)\quad [(x,y)\in A_{i-1},d\in D_{i-1}],\\
A_i&\to (d_1,d_2)\quad [d_1,d_2\in D_{i-1}]\quad(2\le i\le n),\\
S&\to D_n\,ab\ \mid\ x\,c\,y\quad[(x,y)\in A_n].
\end{array}
\]

角括弧は言語生成時の代入説明であり、無限個の規則ではない。例えば `A_i→(d x,y)` は2子の linear template `(ξ_D^1 ξ_A^1, ξ_A^2)` を一つ書いた規則である。三つの `A_i` の規則はそれぞれ1本、`D_i` は各2本、`S` は2本。

### 1.1 文法の量的条件

**命題A1 [証明済み]** 各 `G_n` は reduced good、ファンアウト2、最大ランク2で

\[
\boxed{\|G_n\|=\frac{n(n+1)}2+27n+3,\quad
\bar\theta(G_n)\le(n+3)^2.}
\]

**証明**：すべてのテンプレートは各入力成分を一回だけ使用、二成分の順序は維持、同じ子の連続成分は一つの出力成分内で接しない。`S→xcy` も中央に `c` があるので nonmerging。各成分は非空である。`S` から `D_n`,`A_n` に到達し、前者の倍増規則、後者の left/right 規則を辿るとすべての `D_i`,`A_i` に到達する。各 `D_i` は `e_i`、`D_0` は `ab`、各 `A_i` は middle 規則を使って非空二成分を生成するから productive。したがって reduced good。

非終端数は `2n+2`。規則寄与は `S`: `5+5`、`D_0`: `3`、各 `D_i`: `5+(i+3)`、`A_1`: `5`、各 `A_i(i≥2)`: `6+6+5=17`。合計を足すと式どおり。

厚さは各規則を含む**成功導出**を明示して抑える。`D_j` の短い生成として `e_j` (`j≥1`, 長さ `j+2`) と `D_0→ab`（長さ2）を採用する。`D_i` の規則を使う場合、`S→D_n ab` を選び、上の段 `D_j→D_{j-1}D_{j-1}` を一本の道に沿って選び、他方を短い生成にする。指定 `D_i` 規則で得る長さは高々 `2(i+1)`（`D_0` では2）。従って総長は

\[
2+2(i+1)+\sum_{j=i+1}^{n}(j+1)
\le 2+2(n+1)+\sum_{j=1}^{n}(j+1)
=\frac{n^2+7n+8}{2}.
\]

`D_0` にも同じ上界が成り立つ。`A_j` の短い生成は `A_1=(p,p)`（総長4）、`j≥2` では middle 規則で `(e_{j-1},e_{j-1})`（総長 `2(j+1)`）とする。指定 `A_i` 規則の生成は高々 `3i+1` 文字（`A_1` では4）。`S→xcy` を使い、祖先の `A_j` は left/right の片側に短い `D_{j-1}` を置き、もう一方に指定規則までの道を通す。総長は

\[
1+(3i+1)+\sum_{j=i+1}^n(j+1)
\le 3n+2+\sum_{j=2}^n(j+1)
=\frac{n^2+9n}{2}.
\]

`S` の二規則自体の成功導出長は `n+4` と `2n+3` 以下。以上の各式は `n≥2` で `(n+3)^2` 以下。定義どおり `\bar\theta≤(n+3)^2`。□

### 1.2 指数長の欠損型とスロット飽和

**命題A2 [証明済み]**

\[
L(G_n)\cap\{a,b\}^*=\{p^{M+1}\},\qquad
\boxed{\mu_{ab}(L(G_n))=2M+2=2^{n+1}+2.}
\]

かつ `p^{M+1}∈L` で、全 `1≤h≤M−1` について `p^h c p^{M-h}∈L`。

**証明**：`S→xcy` は必ず `c` を含む。`S→D_n p` で `c` を含まない導出には各 `D_i→e_i` が使えないので、各段は倍増を選び `D_0→p` に到達する。生成は唯一 `p^{2^n}p=p^{M+1}`。逆にそれを導出できる。

`A_1` の c-free 二成分は `(p,p)` であり、総ブロック数2の唯一の内部分割を与える。帰納的に `A_{i-1}` が総 `2^{i-1}` ブロックの全分割 `1≤h<2^{i-1}` を与えるとする。`A_i` の right 規則に c-free `D_{i-1}=p^{2^{i-1}}` を代入すると `1≤h<2^{i-1}`、middle 規則は `h=2^{i-1}`、left 規則は `2^{i-1}<h<2^i` を与える。よって全 `1≤h<2^i` が生成される。これを `S→xcy` に入れれば要求された全スロットが存在する。□

**N1–N5 の検査 [証明済み]**：標的は `c` を欠く三文字上の型で N1 に適合。N2 の (153) 補題1を適用すれば、`v=2n+2,r=2`、上界 `θ≤(n+3)^2` から侵入反鎖幅は

\[
q\ge\frac{2^{n+1}+2}{9(2n+2)(n+3)^2}-2,
\]

従って超多項式（N2 に必要な方向）である。`D_n` の全ての `D_1` 出現で `D_1→acb` を選ぶと、`(acb)^{2^{n-1}}ab∈L` に `2^{n-1}` 個の別々の `c` 連があるため N3 の必要な長い連の個数が実現される。N4 について、`p^{M+1}`、`e_n p`、`e_{n-1}^2p` が同じ非負加法重みの水準にあり `λ(a)=λ(b)=t>0` とすると、前二者から `λ(c)=(2M-n-1)t`、第1・第3から `λ(c)=(M-n)t` が従い、`M>0` に反する（実際、両者は一致しない）。N5 に必要な位置は命題A2の帰納法ですべて生成済み。これらの適合は (3) の証明ではない。

### 1.3 新しい二穴短縮証明書（全 n）

**補題N9（two-slot scissors）[証明済み]** `M≥2,k≥1,p=ab` とする。`L∈\mathcal C_{2,c_\Sigma}` が

\[
acbp^{M-1},\quad a^kcbp,\quad p^{M+1}\in L
\]

を満たすなら、**`a^k babab∈L`**。とくに `μ_ab(L)>k+5` なら、この三つの前提が共存してはいけない。

**証明書**：

\[
E=(\epsilon,c,\epsilon),\quad F=(\epsilon,ba,\epsilon),\quad
x=(a,bp^{M-1}),\quad y=(a^k,bp).
\]

まず穴は全て非空、中央固定語は `c` と `ba` で非空である。第1成分の型は双方 `{a}`、第2成分は双方 `{a,b}`。前提は順に

\[
E[x]=acbp^{M-1},\quad E[y]=a^kcbp,\quad F[x]=p^{M+1};
\]

ゆえに SUB₂ により `F[y]=a^k babab∈L`。長さは正確に `k+5`、内容は `{a,b}`。□

**定理A3（倍増バックボーンの一般失格）[証明済み]** 任意の `n≥2` について `D_0→ab`、`D_i→D_{i-1}D_{i-1}|a^icb`（`1≤i≤n`）、`S→D_n ab` を生成の選択肢として持つ文法の言語 `L` が `\mathcal C_{2,c_\Sigma}` に属するなら

\[
\boxed{\mu_{ab}(L)\le n+5.}
\]

この結論は **他の規則・非終端を追加しても**維持される（ただし指定の規則と開始リンクが保持される）。

**証明**：三つの種を生成する。
(1) 全倍増で `D_n→p^M`、開始から `p^{M+1}`。
(2) 直接 `D_n→a^ncb`、開始から `a^ncbp`。
(3) `D_n` の完全倍増木の左端の `D_1` だけを `D_1→acb`、他の `D_1` を `D_1→p^2` とする。`D_1` は `2^{n-1}` 個現れ、総ブロック数が `M` であることから、開始から `acbp^{M-1}` を得る。
補題N9を `k=n` に適用し `a^n babab∈L`。よって `μ_ab(L)≤n+5`。□

**系A4 [証明済み]** 候補(a)は全 `n≥2` で `\mathcal C_{2,c_\Sigma}` に属さない。実際、命題A2から `μ_ab=2^{n+1}+2`、定理A3から所属を仮定すると `μ_ab≤n+5`、しかし `n+5<2^{n+1}+2`。同じ三語を含む**どんな代入可能な拡張言語**も、元の長い `{a,b}` 型最短長を保持できない。

**独立の SUB₁ 証明書 [証明済み]** `u=e_{n-1}`、`t=a` とし、`E=(a,p)`、`x=u`、`y=u[1:]u`、`F=(ε,up)`。このとき `E[x]=e_np`、`E[y]=u^2p`、`F[x]=u^2p` は三つとも `S→D_np` から生成されるが、`F[y]=u[1:]u^2p` は生成されない。後者は全ての `c` の直後が `b` なので `S→xcy` の**挿入された `c`（直後は必ず `a`）**を使えない。他方 `D_n` の各 `c` の直前の連続した `a` の本数は、使用した逃げ道 `e_i` の添字 `i` に等しい（各基本ブロックは `b` で終わる）。`u[1:]u^2` には本数 `n-1` の `c` が二つと追加の `c` が一つある。`D_n` で本数 `n-1` の `c` を二つ作るには、根の左右の `D_{n-1}` が両方 `e_{n-1}` を選ぶしかなく、他の `c` は作れない。矛盾。`n=2` の最初の `c` は語頭だが、同じ議論で扱える。型は `cont(x)=cont(y)={a,b,c}`。よって SUB₁ も一段で破れる。これは既知 `lem:no-insertion` の一例であり、N9 の方が**直接短い欠損型を強制する**点で強い。

**判定 [証明済み]** 候補(a)は N1–N5 を通過したものの、所属 (3) を二穴近道で否定される。N6 の P/PP/V/R/T の**全前提が成立しない**ことを確認したという意味ではなく、独立の一般証明書 N9 により既に失格となった。N7 は CFG 一段一逃げ道に関する観測であり、今回は真の二成分を導入してもなお失敗した。

## 2. 候補(b)：閉包を先に、文法を後に（有限アーベル群）

`M=2^n`、`n≥1` として群 `H_n=(ℤ/Mℤ)^2` と準同型

\[
\phi_n(a)=(1,0),\quad\phi_n(b)=(0,1),\quad\phi_n(c)=(0,0)
\]

を定める。構造的述語は `P_n(w): w≠ε かつ φ_n(w)=(0,0)`、言語

\[
L_n^B=\{w\in\{a,b,c\}^+: \#a(w)\equiv\#b(w)\equiv0\pmod M\}.
\]

**命題B1（閉包）[証明済み]** `L_n^B` は全ての `d≥1` で `SUB_d` を満たす。特に `\mathcal C_{1,c_\Sigma}\cap\mathcal C_{2,c_\Sigma}` の両方に属する（後述の右線形文法があるので、fan-out 1 の MCFL でもある）。

**証明**：`E[x],E[y]∈L_n^B` なら `φ_n(E[x])=φ_n(E[y])=0`。加法性と可換性から `Σ_i φ_n(x_i)=Σ_i φ_n(y_i)` が得られる。任意の許容文脈 `F` について `φ_n(F[x])=φ_n(F[y])`。各穴が非空なので両完成語も非空であり、`F[x]∈L_n^B⇔F[y]∈L_n^B`。型の一致はこの証明では使っていないので、内容型付けの制限下でも成立する。□

**命題B2（希少型）[証明済み]** `μ_ab(L_n^B)=2M=2^{n+1}`。

**証明**：型 `{a,b}` の語は少なくとも1個ずつ `a,b` を持ち、ゼロ合同条件により `#a,#b` はそれぞれ正の M の倍数。したがって長さは `≥2M`。語 `a^M b^M` が達成する。□

### 2.1 明示的文法（全規則）と厚さ障壁

`i,j∈{0,…,M−1}` ごとにファンアウト1の `Q_{i,j}` を置き、開始記号は `Q_{0,0}`。**すべての規則**は

\[
\begin{aligned}
Q_{i,j}&\to aQ_{(i+1)\bmod M,j}\mid bQ_{i,(j+1)\bmod M}\mid cQ_{i,j}\quad(0\le i,j<M),\\
Q_{M-1,0}&\to a,\qquad Q_{0,M-1}\to b,\qquad Q_{0,0}\to c.
\end{aligned}
\]

この右線形文法は、入力済みの文字数の剰余が `(i,j)` であるときの状態を表す。末尾の文字で剰余0になる場合にのみ終了するので、生成語はちょうど `L_n^B` である。任意の状態には `a,b` を何回か足して `0,0` に戻る経路があり、開始から各状態に到達する。非空の終端文字を全規則が書き、一変数以下であるため reduced good。fan-out 1、ランク1。

**命題B3 [証明済み]** この文法 `H_n` は

\[
\boxed{\|H_n\|=13M^2+6=13\cdot4^n+6,\qquad
M\le\bar\theta(H_n)\le2M+1.}
\]

**証明**：非終端は `M²` 個。各状態の3本の継続規則はランク1、テンプレート長2なので規則寄与各4で `12M²`。末端3本は各2。よってサイズは `13M²+6`。

下界：末端規則 `Q_{M-1,0}→a` を使う成功導出の完成語は `a` を含み、言語の定義上 `a` は少なくとも M 個必要。従ってその規則の厚さは少なくとも M。上界：任意の継続規則の左辺 `Q_{i,j}` へ `a^i b^j` で到達し、当該規則を一度使い、残りの剰余を0にする最短の `a,b` 列を続ける。完成語の `a,b` 個数はそれぞれ 0 または M なので長さは高々 `2M+1`。直後に剰余0になるときでも当該継続規則の子を非空で終わらせる必要があれば `c` を足せばよい。末端3規則は `a^M`、`b^M`、`c` の成功導出で使える。ゆえに θ≤2M+1。□

**命題B4（文字出現による一般障壁）[証明済み]** reduced（少なくとも全規則が使用可能）な文法 `G` が `L` を生成し、文字 `t∈Σ` を含む語が一つ以上あり、全てのそのような語の長さが `≥K` なら、`θ_G≥K`。ファンアウト、ランク、代入可能性には依存しない。

**証明**：`t` を含む語の成功導出を一つ固定する。文法の線形テンプレートで出力された文字 `t` はいずれかの規則に書かれた端末 `t` に由来する。その規則 `R` を使う任意の成功導出の語は `t` を含むので、定義により `θ_G(R)≥K`。したがって `θ_G≥K`。□

候補(b)では `t=a` でも `t=b` でも `K=M` と置けるので、**どんな reduced good 表示を工夫しても `\bar\theta≥M=2^n`**。文法の変更で多項式厚さにできる余地はない。

**追加の N3–N5 検査 [証明済み]**：`(ca^M)^t∈L_n^B` (`t≥1`) なので任意個数の分離した `c` 連を実現できる（N3）。`p^M∈L_n^B`、`p^h c p^{M-h}∈L_n^B` (`0≤h≤M`) であり、スロット移送によって欠けた位置はない（N5）。`a^M,a^{2M}∈L_n^B` なので `λ(a)=λ(b)>0` とする非負加法重みの単一水準には入らない（N4）。ただし厚さ障壁 N10 が決定的である。

**判定 [証明済み]** (b) は「構造 P 上で閉包を先に証明→希少型の長さを下から抑える」を完全に実行した。ただし (iii) を最後に満たせず、任意の表示に厚さの指数下界がある。閉包があることと小さい文法があることは別である。`#a,#b` を固定群の剰余にして M を増す方法は、固定内容型付けでもこの障壁を超えない。

## 3. 計算機検証と再生ログ

**[計算機による観察（n=2,3,4、候補(a)の有限言語全語）]** 付録スクリプトは (a) の全生成語を**長さ切りではなく**非巡回文法の意味評価によって列挙し、規則ごとの最短成功語から θ を正確に計算する。N5 の全スロット `1≤h<2^n` を列挙確認し、N9 の二穴証明書について `E[x],E[y],F[x]∈L`、成分別内容一致、中央固定語非空、`F[y]∉L` を機械的に照合する。したがって有限 n の否定例は真の違反である。**全 n の定理A3の代用として計算を使っていない**。

| n | (a) `\|G_n\|` | (a) 厚さ θ（正確） | (a) μ_ab | `|L(G_n)|` | c の連の証人 | (b) `\|H_n\|` | (b) μ_ab |
|---:|---:|---:|---:|---:|---:|---:|---:|
| 2 | 60 | 8 | 10 | 13 | 2 | 214 | 8 |
| 3 | 90 | 12 | 18 | 131 | 4 | 838 | 16 |
| 4 | 121 | 17 | 34 | 6813 | 8 | 3334 | 32 |

**n=2 の手動再生（SUB₂、一段）**：

```text
E = □1 c □2,       F = □1 ba □2
x = (a, bababab),  y = (aa, bab)
cont(a)=cont(aa)={a}
cont(bababab)=cont(bab)={a,b}
E[x] = acbababab   ∈ L(G_2)
E[y] = aacbab      ∈ L(G_2)
F[x] = ababababab  ∈ L(G_2)
F[y] = aababab     ∉ L(G_2), |F[y]|=7<μ_ab=10
```

`E[x]` は `D_2→D_1D_1` の左の `D_1→acb`、右の `D_1→abab` と `S→D_2ab`。`E[y]` は `D_2→aacb` と同じ開始規則。`F[x]` は完全倍増。`F[y]` の非所属は `c` を含まない完成語が唯一 `p^5` であることから従う。

`--scan` を付けると、`n=2` の全語における許容1穴・2穴出現を列挙して別の一段証明書も見つける。これは[計算機による観察（n=2、全出現）]であり、所属証明とは呼ばない。

## 4. 課題D：失格の一般化と障壁の位置づけ

**定理D [証明済み]** 以下のような「倍増バックボーン」全体は、欠損型 `{a,b}` の指数下界を保持したまま `\mathcal C_{2,c}` に入れることはできない。

> `D_0→ab`、全 `1≤i≤n` について `D_i→D_{i-1}D_{i-1}`、`D_1→acb`、`D_n→a^ncb`、開始側のリンク `S→D_n ab` を保持するすべての拡張文法。

**証明**：定理A3の三種の導出には中間段 `D_2,…,D_{n-1}` の逃げ道は**使われない**。従ってそれらを任意に削除・改変し、新規規則と二成分非終端を自由に足しても、三種 `acbp^{M-1}`, `a^ncbp`, `p^{M+1}` は残る。補題N9は文法ではなく言語の性質なので、その言語が `\mathcal C_{2,c}` に属すれば `μ_ab≤n+5`。□

この定理は N7 より大きい明示的な家族に適用され、**スロット飽和を付け足しても解決しない**。一方 (b) の失格は種の短縮ではなく文字ごとの厚さ下界であるから、両失敗に共通する普遍的な「すべてのファンアウト2の倍増文法は失格」という定理は証明していない。

## 5. 最終表・新必要条件・次の三手

| 候補 | 設計 | 文法サイズ | 厚さ | μ_ab | C₁ | C₂ | 結論 |
|---|---|---|---|---|---|---|---|
| **A** | 二成分 split の全位置スロット | `n(n+1)/2+27n+3` | `≤(n+3)²` | `2^{n+1}+2` | **否**（独立の1段証明書） | **否**（N9の1段短縮） | **失格・閉包での修復も指数下界を破壊** |
| **B** | 群剰余の構造的閉包 | `13·4^n+6`（提示文法） | **全表示で `≥2^n`** | `2^{n+1}` | **是** | **是** | **失格・厚さ下界** |

**N9（二穴 scissors：新たに明示した必要条件）[証明済み]** `acb(ab)^{M-1}, a^kcbab,(ab)^{M+1}` が同居すれば、内容型付き二穴代入可能性は `a^k babab` を強制する。`μ_ab>k+5` を目指す家族はこの3種を同居させられない。**単にすべての位置へ c の逃げ道を移送したことは十分でない。**

**N10（文字ごとの短い成功語：一般障壁）[証明済み]** `\bar\theta(G)≤T` なら、`L(G)` に出現する各文字 `t` について、それを含む長さ `≤T` の語が存在する。ある文字を出すと必ず指数長になる設計（剰余・比率・閾値など）は、規則厚さの時点で失格。

**次の三手 [提案・未証明]**：

1. `D_1→acb` と `D_n→a^ncb` の**二穴 scissors 前提のいずれかを消す**。具体的には逃げ道の直後の `b(ab)^j` を共通成分として認識させない異なる接尾符号を検討する。ただし N6 の P/PP も再チェックする。
2. C₂ 閉包が先に証明できる構造で、すべての文字について長さ `O(poly(n))` の成功語があるものに限定する。群の「零剰余一種類」だけを用いた例は N10 に阻まれるので、型ごとに複数の受理値を認めても substitutability が壊れない条件をまず研究する。
3. トークン段階の閉包では重みを保存すること（(153) 命題5）を維持しながら、**実文字列への埋め込みで N9・P・PP・V・R・T を同時に避ける**符号設計の定理を目指す。現時点では[予想]にも至らず、試験の方針に留まる。

---

## 付録：標準ライブラリのみの検証スクリプト全文

実行：`python chatgpt_negative_design_2026-11-06.py`（全語列挙 `n=2,3,4`）または `python chatgpt_negative_design_2026-11-06.py --scan`（追加の一段証明書探索）。`n>4` の全語列挙は資源膨張を避けるため明示的に禁止しているが、本文の一般定理の証明には影響しない。

```python
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Replayable counterexample-design audit (standard library only).

This script provides genuine non-membership checks by exhaustive generation
of the finite MCFG candidate (a), not by bounded-length overapproximation.
Candidate (b) is infinite and uses an exact modular membership predicate.
"""
from __future__ import annotations
import argparse
from collections import defaultdict
from dataclasses import dataclass
from typing import Tuple

P = 'ab'


def cont(w: str) -> frozenset:
    return frozenset(w)


def fill(ctx: Tuple[str, ...], values: Tuple[str, ...]) -> str:
    assert len(ctx) == len(values) + 1
    return ''.join(ctx[k] + values[k] for k in range(len(values))) + ctx[-1]


def goodstep(L, E, x, y, F):
    """Check the manuscript's typed SUB_d premises, including middle gaps."""
    d = len(x)
    assert d in (1, 2) and len(y) == d
    assert len(E) == len(F) == d + 1
    assert all(z for z in x + y)
    assert all(E[k] and F[k] for k in range(1, d))
    assert all(cont(a) == cont(b) for a, b in zip(x, y))
    p1, p2, p3, conclusion = (fill(E, x), fill(E, y), fill(F, x), fill(F, y))
    assert p1 in L and p2 in L and p3 in L, (p1, p2, p3)
    assert conclusion not in L, conclusion
    return dict(d=d, E=E, x=x, y=y, F=F,
                premises=(p1, p2, p3), absent=conclusion)


@dataclass(frozen=True)
class Rule:
    name: str
    head: str
    children: Tuple[str, ...]
    fixed: int
    variables: int

    @property
    def size(self):
        return 1 + len(self.children) + self.fixed + self.variables


def rules_a(n: int):
    assert n >= 2
    out = [Rule('D0/p', 'D0', (), 2, 0)]
    for i in range(1, n + 1):
        out.extend((
            Rule(f'D{i}/double', f'D{i}', (f'D{i-1}', f'D{i-1}'), 0, 2),
            Rule(f'D{i}/escape', f'D{i}', (), i + 2, 0),
        ))
    out.append(Rule('A1/base', 'A1', (), 4, 0))
    for i in range(2, n + 1):
        out.extend((
            Rule(f'A{i}/left', f'A{i}', (f'D{i-1}', f'A{i-1}'), 0, 3),
            Rule(f'A{i}/right', f'A{i}', (f'A{i-1}', f'D{i-1}'), 0, 3),
            Rule(f'A{i}/middle', f'A{i}', (f'D{i-1}', f'D{i-1}'), 0, 2),
        ))
    out.extend((
        Rule('S/pure', 'S', (f'D{n}',), 2, 1),
        Rule('S/slot', 'S', (f'A{n}',), 1, 2),
    ))
    return out


def metrics_a(n: int):
    rs = rules_a(n)
    nts = [f'D{i}' for i in range(n+1)] + [f'A{i}' for i in range(1,n+1)] + ['S']
    size = len(nts) + sum(r.size for r in rs)
    assert size == n*(n+1)//2 + 27*n + 3
    byhead = defaultdict(list)
    for r in rs:
        byhead[r.head].append(r)
    least = {}
    for h in nts:
        least[h] = min(r.fixed + sum(least[c] for c in r.children)
                       for r in byhead[h])
    # Exact shortest *successful sentence* which uses a designated rule.
    thickness_per_rule = {}
    INF = 10**90
    for target in rs:
        with_target = {}
        for h in nts:
            best = INF
            for r in byhead[h]:
                base = r.fixed + sum(least[c] for c in r.children)
                if r == target:
                    best = min(best, base)
                for c in r.children:
                    best = min(best, base - least[c] + with_target[c])
            with_target[h] = best
        assert with_target['S'] < INF, target.name
        thickness_per_rule[target.name] = with_target['S']
    return size, max(thickness_per_rule.values()), thickness_per_rule


def language_a(n: int):
    """Exact finite L(G_n) by evaluation of all (acyclic) MCFG rules."""
    assert n >= 2
    D = [{'ab'}]
    for i in range(1, n+1):
        old = D[-1]
        D.append({x+y for x in old for y in old} | {'a'*i + 'cb'})
    A = [None, {('ab', 'ab')}]
    for i in range(2, n+1):
        old, block = A[-1], D[i-1]
        A.append({(v+x,y) for (x,y) in old for v in block} |
                 {(x,y+v) for (x,y) in old for v in block} |
                 {(v,w) for v in block for w in block})
    L = {u+'ab' for u in D[n]} | {x+'c'+y for (x,y) in A[n]}
    return L, D, A


def cert_a(n: int, L):
    u = 'a'*(n-1) + 'cb'
    x = (u,)
    y = (u[1:] + u,)
    E = ('a', 'ab')
    F = ('', u+'ab')
    return goodstep(L, E, x, y, F)


def cert_a_scissors(n: int, L):
    """Universal 2-hole shortening certificate, valid for all n>=2."""
    M = 2**n
    x = ('a', 'b' + 'ab'*(M-1))
    y = ('a'*n, 'b'+'ab')
    E = ('', 'c', '')
    F = ('', 'ba', '')
    return goodstep(L, E, x, y, F)


def check_a(n: int):
    L, D, A = language_a(n)
    sz, theta, which = metrics_a(n)
    M = 2**n
    pure = {w for w in L if 'c' not in w}
    assert pure == {'ab'*(M+1)}
    assert min(len(w) for w in L if cont(w) == {'a','b'}) == 2*(M+1)
    # Complete insertion-slot coverage, at every nontrivial position.
    for h in range(1,M):
        assert ('ab'*h)+'c'+('ab'*(M-h)) in L
    # N3: exponentially many disjoint c-runs in a sentence.
    witness_runs = 'acb' * (2**(n-1)) + 'ab'
    assert witness_runs in L and witness_runs.count('c') == 2**(n-1)
    assert 'cc' not in witness_runs
    cert = cert_a(n,L)
    scissors = cert_a_scissors(n,L)
    assert len(scissors['absent']) == n+5 < 2*(M+1)
    assert theta <= (n+3)**2
    return {'n':n,'size':sz,'theta':theta,'mu_ab':2*(M+1),
            'language_size':len(L),'slot_count':M-1,
            'scissors':scissors,
            'c_runs':2**(n-1),'certificate':cert,
            'theta_worst_rules':sorted(which.items(),key=lambda kv:-kv[1])[:3]}


def in_b(w: str, n: int) -> bool:
    M = 2**n
    return bool(w) and len(set(w) - set('abc')) == 0 and w.count('a')%M == 0 and w.count('b')%M == 0


def metrics_b(n: int):
    M = 2**n
    # |V|=M^2; 3M^2 right-linear rules of size 4; 3 terminal rules of size 2.
    size = 13*M*M + 6
    # Any successful derivation with the terminal rule Q_(M-1,0)->a
    # must contain at least M a's.  Every rule has a witness of length
    # <=2M+1 by a shortest residue-prefix and residue-completing suffix.
    return size, M, 2*M+1, 2*M


def check_b(n: int):
    M=2**n
    assert in_b('a'*M+'b'*M,n)
    assert not in_b('a'*(M-1)+'b'*M,n)
    assert in_b('c',n)
    assert in_b('a'*M,n) and in_b('b'*M,n)
    sz,lo,hi,mu = metrics_b(n)
    return {'n':n, 'size':sz, 'theta_lower':lo,
            'theta_upper':hi, 'mu_ab':mu}


def scan_one_step(L, d):
    """Optional exact first-violation search over a FINITE language only."""
    occ = defaultdict(set)
    f_by_x = defaultdict(set)
    for word in sorted(L, key=lambda w:(len(w),w)):
        m=len(word)
        if d == 1:
            ranges=((i,j) for i in range(m) for j in range(i+1,m+1))
            for i,j in ranges:
                E=(word[:i],word[j:]); x=(word[i:j],)
                occ[(E,tuple(map(cont,x)))].add(x)
                f_by_x[x].add(E)
        else:
            for i in range(m):
                for j in range(i+1,m):
                    for k in range(j+1,m):
                        for t in range(k+1,m+1):
                            E=(word[:i],word[j:k],word[t:])
                            x=(word[i:j],word[k:t])
                            occ[(E,tuple(map(cont,x)))].add(x)
                            f_by_x[x].add(E)
    for (E,_),poss in sorted(occ.items(),key=lambda z:sum(map(len,z[0][0]))):
        if len(poss)<2: continue
        for x in sorted(poss):
            for y in sorted(poss):
                if x==y: continue
                for F in sorted(f_by_x[x]):
                    if fill(F,y) not in L:
                        return goodstep(L,E,x,y,F)
    return None


def main():
    arg=argparse.ArgumentParser()
    arg.add_argument('--max-n',type=int,default=4)
    arg.add_argument('--scan',action='store_true',
                     help='run one-step SUB1 and SUB2 search for candidate a, n=2')
    opts=arg.parse_args()
    for n in range(2,opts.max_n+1):
        if n>4: raise ValueError('exact finite enumeration capped at n=4; general certificate is symbolic')
        z=check_a(n)
        print('A n=%d size=%d theta=%d mu_ab=%d |L|=%d slots=%d c_runs=%d' %
              (z['n'],z['size'],z['theta'],z['mu_ab'],z['language_size'],z['slot_count'],z['c_runs']))
        c=z['certificate']
        print('   SUB1 E=%r x=%r y=%r F=%r' % (c['E'],c['x'],c['y'],c['F']))
        print('   SUB1 E[x]=%s E[y]=%s F[x]=%s F[y] (absent)=%s' %
              (*c['premises'],c['absent']))
        c=z['scissors']
        print('   SUB2 E=%r x=%r y=%r F=%r' % (c['E'],c['x'],c['y'],c['F']))
        print('   SUB2 E[x]=%s E[y]=%s F[x]=%s F[y] (absent, SHORT)=%s' %
              (*c['premises'],c['absent']))
    for n in (2,3,4):
        z=check_b(n)
        print('B n=%d size=%d theta in [%d,%d] mu_ab=%d' %
              (z['n'],z['size'],z['theta_lower'],z['theta_upper'],z['mu_ab']))
    if opts.scan:
        L,_,_=language_a(2)
        for d in (1,2):
            print('A n=2 exact SUB_%d scan:'%d,scan_one_step(L,d))

if __name__=='__main__':
    main()

```
