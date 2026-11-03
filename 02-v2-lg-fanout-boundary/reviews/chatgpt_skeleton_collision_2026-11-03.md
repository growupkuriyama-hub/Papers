# 骨格衝突補題の検討：二文字影文法の厚さ障害と、符号復号型の非衝突模型

**研究日**：2026-11-03  
**対象**：栗山貴之論文 #2、`op:fanout-two`、三文字内容型付け。  
**成果の境界**：**補題Cの一般証明も、`C_{2,c}` に属する超多項式下界族も得ていない**。ただし、二文字への制限に関する定量的な必要条件、および骨格衝突を起こさない反鎖模型を証明した。後者は言語クラス内の反例ではない。

## 0. 主張別判定

| 主張 | 判定 | 根拠 |
|---|---|---|
| 二文字**影文法** $H_b,H_c$ を元の $G$ から単に規則削除と刈込みで構成でき、$\|H_x\|\le\|G\|$ となる | **証明済み** | §2.1 |
| $k=\mu_a(L)$ と $\eta_x=\bar\theta_{H_x}$ について $k\le A_r\|G\|^3\eta_x^4H_{\eta_x}\le A_r\|G\|^3\eta_x^5$（$x=b,c$） | **既存の二文字定理を仮定した厳密な帰結** | §2.2。二文字定理の原稿中の証明を確認したが、その全補題の独立再証明はしていない |
| $\|G_n\|,\bar\theta_{G_n}=n^{O(1)}$ かつ $\mu_a(L_n)=n^{\omega(1)}$ の族があれば、**$\eta_b,\eta_c$ は両方とも $n^{\omega(1)}$** | **同じ条件での証明済みの帰結** | §2.3 |
| 相異なる $m$ 個の一成分逃げ道を長さ $\lceil\log_2m\rceil$ の二元固定長符号で与え、全反鎖の置換において、同一 $a$ 骨格なら $a$ 個数が等しい模型を作れる | **抽象模型内で証明済み** | §3.1–§3.3。$m$ は任意 |
| 逃げ道をすべて $b^*c^*$ 型に制限しても、$m\asymp\theta$ 個の非衝突例ができる | **抽象模型内で証明済み** | §3.4 |
| 再配分・境界交換・$a$ 隙間の合流が、上述の符号模型の復号重み式だけから矛盾を生む | **反証（その推論は成立しない）** | §3.5。これらの操作は $a$ 総数と $bc$ 射影を保存する。ただし言語の閉性は別問題 |
| 模型をそのまま有限言語にした場合の $m=3$：arity 1・2 の両方が成立する | **反証** | §4。両方に具体的違反、完全検査コード付き |
| $a$-塊再配分で飽和した有限模型の $m=3$：arity 1・2 の両方が成立する | **反証** | §4。35語を全検査、両方に違反 |
| **補題C**：$L\in\mathcal C_{2,c}$ の一般の場合、異なる多数の逃げ道から真の骨格衝突を強制 | **未解決** | §5。語の代入可能性を通じた符号境界の破壊が残る |
| $\mu_a(L)\le\mathrm{poly}(\|G\|,\bar\theta_G)$ の一般肯定、または適法な否定族 | **未解決** | §5–§6 |
| 新結果の文献上の優先権 | **未確認** | §7 |

---

## 1. 正本と使用する定義の監査

### 1.1 取得した原典

- [現行 `main.tex`](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex)、取得時 Git blob `b72cd2ed648f802886f0ab7c60a72f9f40c0864b`。確認した箇所：`def:standard-mcfg`、`def:grammar-properties`、`def:tuple-substitutable`、`lem:thickness-equivalence`、`prop:abelian-coset-filter`、`lem:no-insertion`、`prop:rare-type`、`lem:power-transfer`、`thm:two-letter-content`（本文および付録）、`op:fanout-two`。
- [前報・escape branches](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_escape_branches_2026-11-03.md)、blob `9c07d6deaba95556ff594a8b9ad3c0b5fb02a3af`。
- [前報・a-spectrum](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/chatgpt_a_spectrum_2026-11-03.md)、blob `f26e671a61f38b5e587d3d0ad4cd8afd27fea5e5`。
- [Claude・ternary content](https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/claude_ternary_content_2026-11-01.md)、blob `658f3744cfdeea54d2566cfbcac3d38049c21e1d`。

原稿の符号化サイズは
\[
\|G\|=|V|+\sum_{A\to\rho(B_1,\dots,B_t)}\left(1+t+\sum_i|\alpha_i|\right).
\]
`good` は λ-free、nondeleting、nonpermuting、nonmerging、`reduced` は全非終端が到達可能かつ生産的であることを表す。$\bar\theta_G$ は各規則を**少なくとも一回使用する成功導出の最短語長**の最大値である。

$\Sigma=\{a,b,c\}$、$c_\Sigma(w)$ は非空語 $w$ の文字集合で、$L\in\mathcal C_{2,c_\Sigma}$ は **fan-out $\le2$ の MCFL であり、arity 1 および arity 2 の両方**について組代入可能性が成立することを意味する。arity 2 の受理文脈は $u\square_1v\square_2z$、$v\in\Sigma^+$（空の中間区切りは不可）である。空の組成分は比較しない。

### 1.2 骨格について独立に使える部分

$k=\min\{j\ge1:a^j\in L\}\ge5$ とし、$\sigma_a(w)$ を極大な $a$-塊を一個の $a$ に縮約した語とする。$a^k$ は $a^4$ を含む。組 $(a,aa)$ と $(aa,a)$ は成分内容が $(\{a\},\{a\})$ で一致し、共通の許容受理文脈 $\square_1a\square_2$ を持つ。したがって組代入可能性により、**異なる二つの $a$-塊の間で、一方の長さが零にならない範囲で一個の $a$ を移す操作**は所属を保存する。正の整数の組成はこの一単位移動で連結するので、同一 $\sigma_a$・同一 $a$ 個数なら同じ所属である。

さらに、同一 $\sigma_a$ の二受理語における $a$ 個数差が $\delta>0$ なら、余剰を一つの塊に集め、共有する一穴文脈で $a$ と $a^{1+\delta}$ を比較できる。よって $\mathcal D_L^{(1)}(a)=\mathcal D_L^{(1)}(a^{1+\delta})$。$1\le\delta<k$ なら $a^k$ の末尾の $a^{1+\delta}$ を $a$ で置換して短い純粋 $a$ 語が生じる。ゆえに
\[
  w,w'\in L,\quad\sigma_a(w)=\sigma_a(w')
  \quad\Longrightarrow\quad
  |w|_a=|w'|_a\ \text{または}\ \bigl||w|_a-|w'|_a\bigr|\ge k.
  \tag{1.1}
\]
これは前報の骨格剛性を用いる際に必要な核心部で、ここでは直接検証した。

$T$ の清浄な重い節点について、短い逃げ道 $\omega_B$ の符号を $\kappa(B)=\sigma_a(a\omega_{B,1}a\cdots a\omega_{B,d}a)$ とすると、同一符号の二節点の $a$ 不足が等しいことは (1.1) と非削除性から従う。また清浄な倍増節点と清浄重い真の子孫では、もう一方の重い子が $>\bar\theta_G$ 個の $a$ を供給するため、長さ差が $>\bar\theta_G$。同符号なら不足等式から長さ差が $\le\bar\theta_G$ となって矛盾する。この前報補題3.3・4.1の**実際に使う部分**は再確認した。

---

## 2. 新しい肯定側の必要条件：二つの二文字「影文法」

### 2.1 文法の文字削除補題

**補題2.1（証明済み）。** $L\in\mathcal C_{2,c_\Sigma}$、$G$ はその正の部分の reduced good な fan-out $\le2$、rank $\le r$ の文法とする。$x\in\{b,c\}$、$\Gamma_x=\{a,x\}$ とする。$G$ から **$\Gamma_x$ 外の終端を規則テンプレートに直接書く規則をすべて削除し、到達不能・非生産的非終端を除いた文法**を $H_x$ と呼ぶ。このとき

1. $L(H_x)=L\cap\Gamma_x^+$。
2. $H_x$ は reduced good、fan-out $\le2$、rank $\le r$ で、$\|H_x\|\le\|G\|$。
3. $L\cap\Gamma_x^+\in\mathcal C_{2,c_{\Gamma_x}}$。

**証明。** good の nondeleting 性により、成功導出で生じた終端はルート語へ必ず現れ、後の規則では消去されない。従って $\Gamma_x$ のみから成る成功語の導出では、どの使用規則も $\Gamma_x$ 外の終端を書かない。逆に残った規則からなる成功導出は $\Gamma_x$ のみを出す。これで 1。規則の部分集合を取り刈り込むだけなので good 性・ファンアウト・ランクは保たれ、サイズは増えない。これで 2。

組 $\vec u,\vec v\in(\Gamma_x^+)^d$ ($d=1,2$) の各成分内容が $\Gamma_x$ で一致し、$\Gamma_x$ 上の許容文脈を共有したとする。それらは $\Sigma$ 上でも内容一致かつ同じ許容文脈を共有する。$L$ の $d$-組代入可能性から、任意の $\Gamma_x$ 上の許容文脈での所属が一致する。よって 3。$H_x$ 自体が fan-out $\le2$ の表示を与えるので、MCFL 性に別の閉包定理は要らない。□

### 2.2 短い影文法なら $\mu_a$ は多項式

**定理2.2（二文字定理への厳密な帰着）。** $r\ge2$ 固定、$g=\|G\|$、$k=\mu_a(L)<\infty$ とする。$\eta_x:=\bar\theta_{H_x}\ge1$、$H_t=\sum_{j=1}^{t}1/j$、
\[
C_{2,r}:=(r+1)(28r+117)+3,\qquad
A_r:=4^{2r}(3+rC_{2,r})
\]
とおけば、$x=b,c$ の**それぞれ**について
\[
\boxed{\quad k\le A_r g^3\eta_x^4H_{\eta_x}
                  \le A_r g^3\eta_x^5.\quad}\tag{2.1}
\]
ここでの「証明」は、**原稿 `thm:two-letter-content` の結果を前提とする**。その定理自体を本報告で独立に再証明したとはしない。

**帰着の証明。** 補題2.1により $L_x:=L\cap\Gamma_x^+$ は二文字の $\mathcal C_{2,c}$ に属し、文法 $H_x$ のサイズは $g$ 以下である。現行原稿の `thm:two-letter-content` は $f=2$ について、$L_x$ に対する集合駆動再構成作用素 $\mathcal B^{\le r}_{2,c_{\Gamma_x}}$、$\mathcal B_{2,c_{\Gamma_x}}$ に共通の特徴標本 $K_x$ が存在し、
\[
 \|K_x\|_+\le A_r\|H_x\|^3\eta_x^4H_{\eta_x}
\]
となることを与える（$L_x$ は空語を含まない）。一方 $a^k\in L_x$ なので内容型 $\{a\}$ が実現する。原稿 `prop:rare-type` の根拠は、$\{a\}$ 型の語を除いた $L_x'$ も同じクラスに属するため、その型を含まない正例集合だけでは $L_x$ と $L_x'$ を区別できない、という識別補題である。これをここでも確認できる。従って $K_x$ には少なくとも一つ純粋 $a$ 語 $a^j$ があり、$j\ge k$。ゆえに $k\le\|K_x\|_+$。最後に $H_t\le1+\ln t\le t$（$t\ge1$）を使う。□

**参照定理の監査範囲。** `thm:two-letter-content` 本文の $D_2=117$、$C_{2,r}$、$4^{2r}$、特徴標本総符号長の式を付録 `app:two-letter-content` の最終証明（原稿 4458–4470 行付近）と突き合わせた。その最終段は非 Parikh 飽和の場合の typed thickness 評価、飽和の場合の代表長評価、および特徴標本の上界から成る。一方、付録のすべての中間補題の新規な完全検証は実施していない。従って定理2.2を「独立の新しい無条件定理」とは位置付けない。

### 2.3 反例族への二重の必要条件

(2.1) から直ちに
\[
\boxed{\quad
\eta_b,\eta_c\ \ge\
\left(\frac{k}{A_r g^3}\right)^{1/5}.\quad}\tag{2.2}
\]
**系2.3。** 固定 $r\ge2$、$g_n,\bar\theta_{G_n}=n^{O(1)}$、$k_n=n^{\omega(1)}$ を満たす **適法な** $L_n\in\mathcal C_{2,c_{\{a,b,c\}}}$ が存在するとすれば、上記の構成で得る **両方**の $H_{b,n}$ と $H_{c,n}$ について
\[
\bar\theta_{H_{b,n}}=n^{\omega(1)},\qquad
\bar\theta_{H_{c,n}}=n^{\omega(1)}.
\]
特に、二文字の一方へ制限しても**各規則が多項式長の成功 witness を持つ**ような族では、$\mu_a$ の超多項式下界は不可能である。

**注意。** 元の $\bar\theta_G$ が小さいからといって $\eta_x$ も小さいとは限らない。元の短い rule witness が削除対象の第三文字を使っている場合、二文字制限後には使えず、最短 witness が極端に長くなり得る。従って (2.2) は元の $\bar\theta_G$ への無条件上界ではない。単に「逃げ道が一成分」「各符号が $b^*c^*$」「$b^4$ または $c^4$ の因子が存在する」だけから $\eta_b,\eta_c$ の多項式性を推論することもできない。

---

## 3. 否定側の設計障害：衝突しない**抽象的**符号模型

### 3.1 重み復号補題

**補題3.1（重み復号、抽象模型）。** $m\ge1$ とし、$q_1,\dots,q_m\in\{b,c\}^+$ は相異なり、その集合 $Q$ は **一意復号可能な符号**だとする。高さ $m$ の完全な順序付き二分木（葉はすべて $a$）を考える。各内部節点 $u$ の高さを $h(u)\in\{1,\ldots,m\}$（その下の葉数は $2^{h(u)}$）とする。内部節点の任意の反鎖 $J$ について、その下の葉の連続区間 $a^{2^{h(u)}}$ を $q_{h(u)}$ に置いた語を $w_J$ とする。$\pi_{bc}$ は $a$ を消す射影とする。このとき、$\pi_{bc}(w_J)$ から $|w_J|_a$ が**一意に定まる**。特に
\[
\sigma_a(w_J)=\sigma_a(w_{J'})
\quad\Longrightarrow\quad
|w_J|_a=|w_{J'}|_a.\tag{3.1}
\]

**証明。** $J$ の節点を葉の左からの順に $u_1,\ldots,u_t$ とする。反鎖なのでそれらの元の葉区間は重ならず、
\[
\pi_{bc}(w_J)=q_{h(u_1)}\cdots q_{h(u_t)}.
\]
一意復号性により、射影から符号語列、従って高さ列 $(h(u_1),\ldots,h(u_t))$ が復元できる。各置換がちょうど $2^{h(u_i)}$ 個の $a$ を失わせ、置換語には $a$ がないから、
\[
\boxed{|w_J|_a=2^m-\sum_{i=1}^t2^{h(u_i)}.}\tag{3.2}
\]
右辺は射影のみで定まる。$\sigma_a$ が等しければ $\pi_{bc}$ も等しい。□

これは**骨格そのものより強い**復号不変量である。同じ $bc$ 射影の語同士ですら $a$ 個数差は生じない。節点の位置、反鎖の大きさ、同じ高さの節点の多重出現には制限を置いていない。重み $2^j$ は任意の高さ依存重み $d_j$ に置き換えても同様である（その場合は総初期葉数から各 $d_j$ を引く）。

### 3.2 長さ $O(\log m)$ の固定長符号

$\ell=\max\{1,\lceil\log_2m\rceil\}$ とし、$j-1$ の $\ell$ 桁二進表示の $0$ を $b$、$1$ を $c$ に置き換えた $q_j\in\{b,c\}^\ell$ を取る。$m\le2^\ell$ で、全 $q_j$ は相異なる同じ長さだから一意復号可能（$\ell$ 文字ずつ区切ればよい）。補題3.1を適用できる。

各逃げ道は**一成分**で長さ $\ell$、抽象的な逃げ道骨格は $\kappa_j=aq_ja$ で相異なる。高さ $j$ の節点の二つの子はともに元の $a^{2^{j-1}}$ に対応し、$2^{j-1}>\ell$ の高さでは両方「重い」。木の根から「左、右」を選んだあとの内側の部分木は、$m\ge4$ で両端の保護位置（最初と最後の二つの $a$）を避ける。そこを下ると $m-O(\log\ell)$ 個の清浄で倍増する高さが並び、それぞれ相異なる符号を持つ。

にもかかわらず、**すべての反鎖について** (3.1) によって要求された重み衝突は起きない。$m$ は $\ell$ に対して指数大にできる。従って「符号数 $>\mathrm{poly}(\theta)$ なので鳩の巣により同骨格・異重み」という**符号論だけの推論**は誤りである。

**厳格な限定**：この木は**抽象的な導出木と交換操作の模型**であり、`reduced good` 文法の表示でも $\mathcal C_{2,c}$ の言語でもない。記述量 $O(m\ell)$ は模型の書式の長さであって、原稿の $\|G\|$ **ではない**。従ってここから補題C全体を反証したり、$\mu_a(L)=2^m$ の合法的な文法族を得たりしてはいけない。

### 3.3 適法性を使う必要がある理由

この模型の全語集合を $\mathsf A_m(Q)$ と呼ぶと、置換をしない場合だけ $a^{2^m}$ が残る。ゆえに**集合として** $\mu_a(\mathsf A_m(Q))=2^m$ である。一方、実際の $L\in\mathcal C_{2,c}$ では、$(a,aa)$ と $(aa,a)$ などが共有文脈を持つことから模型にない語が強制され得る。さらに同じ**成分ごとの内容**の組に対する共役移送や、$b$・$c$ の塊の再配分が非 $a$ 射影の符号の境界を破ることもある。そのため上の $\mu_a$ は元の研究問題の反例ではない。

### 3.4 $b^*c^*$ に順序づけた逃げ道でも同じ障害

$\ell=m-1\ge1$ とし、
\[
q_j=b^{j-1}c^{m-j}\qquad(1\le j\le m)
\]
と置く。すべて $b^*c^*$、長さ $\ell$、相異なる。従って補題3.1がそのまま適用できる。$m=\ell+1$ は $\log(m\ell)$ より十分速く増えるので、少なくとも「$m>C\log(\text{模型の記述量})$ なら骨格衝突」という考えは **$b^*c^*$ の順序だけでは保証されない**。この族は $m>\mathrm{poly}(\ell)$ の任意の多項式を否定するものではない点に注意する。

### 3.5 どの操作なら復号障害を越えられるか

(3.2) の右辺を $\Phi(\pi_{bc}(w))$ と書く。**$\pi_{bc}(w)$ と $|w|_a$ をともに保存する任意の操作**は、$|w|_a=2^m-\Phi(\pi_{bc}(w))$ という等式を破れない。具体的に、$a$ の塊の再配分、$a$ に関する境界交換、$a$ 隙間の合流は、適用されるときには $a$ の総数と非 $a$ 文字の射影を保つ。従って、**これらの操作を行えるという事実だけ**ではこの復号式を矛盾へ運べない。ここで「復号式が保存される」ことと「模型の語集合がその操作で閉じる」ことは**全く違う**。

必要なのは、たとえば $b$ または $c$ に関する再配分や、二成分の内容を合わせた境界横断の共役移送などを通じて、**非 $a$ 射影に異なる一意復号結果を与えながら同一 $a$ 骨格へ合流する**こと、または模型の集合がそのような言語の強制操作に閉じないことを示すことである。後者は次節で有限例から実際に起こる。

---

## 4. 有限全数検査：非衝突だけでは代入可能でない

検査対象は §3 の**抽象模型が作る有限の語集合**であって、文法の合法的な下界候補とはしない。完全な検査手順は付録コード。各語のすべての非空一穴区間、および **正の中間区切り**を持つ非空二穴区間を列挙し、内容ベクトルと共有受理文脈が等しい組の受理文脈集合が一致するかを検査する。従って、ここに限れば単なるランダムテストではなく**有限言語の全数検査**である。

| 模型 | $m$ | 集合の語数 | $a$ 骨格数 | 骨格重み衝突 | $(1,c)$ | $(2,c)$ |
|---|---:|---:|---:|---:|---|---|
| 固定長二元符号 | 2 | 5 | 5 | 0 | **通過** | **通過** |
| 固定長二元符号 | 3 | 26 | 25 | 0 | **違反** | **違反** |
| 固定長二元符号 | 4 | 677 | 499 | 0 | 未検査 | 未検査 |
| 順序つき $b^*c^*$ | 3 | 26 | 25 | 0 | 未検査 | 未検査 |
| 固定長二元符号・$a$ 再配分飽和後 | 3 | 35 | — | 0（構成上） | **違反** | **違反** |

`m=3` の固定長二元符号は $q_1=bb,q_2=bc,q_3=cb$ である。その非飽和集合の **arity 1** の違反として

- $u=cb$、$v=bbbbbc$。内容はどちらも $\{b,c\}$。
- 共有文脈 $E=\square_1$ は $E[u]=cb$、$E[v]=bbbbbc$ をともに受理する。
- 別文脈 $F=b\square_1baa$ は $F[u]=bcbbaa$ を受理するが $F[v]=bbbbbbcbaa$ を受理しない。

**arity 2** の違反はさらに分かりやすい。$u=(a,aa)$、$v=(aa,a)$（内容ベクトルはともに $(\{a\},\{a\})$）は共通文脈 $E=\square_1a\square_2aaaa$ で $a^8$ を与える。しかし $F=\square_1aaabb\square_2$ については $F[u]=aaaabbaa\in\mathsf A_3(Q)$、$F[v]=aaaaabba\notin\mathsf A_3(Q)$ である。この不一致が、短い符号を置いても**二穴の移送による追加語が必要**なことを直接示す。

さらに各 $a$ 骨格・各総 $a$ 個数に属する**すべての正の $a$ 塊長配分**を追加した集合は35語となる。これは $a$ の再配分には閉じるが、なお次の違反を持つ：

- arity 1：$u=aaaaab$、$v=aabbab$、共有 $E=a\square_1b$、食い違い $F=\square_1ba$。
- arity 2：$u=(a,aaab)$、$v=(a,abbb)$、共有 $E=\square_1aa\square_2b$、食い違い $F=\square_1bb\square_2b$。

いずれも受理3例・非受理1例はコードで検証している。したがって、**$a$ 骨格の再配分だけを閉じても、三文字の組代入可能性にはならない**。この失敗は一般 $m$ の不可能性の証明ではない。

---

## 5. 補題Cの現時点での評価と次の数学的焦点

**一般の補題Cは未解決。** §3 は、相異なる符号が $m\gg\log m$ 個あること、各符号が短いこと、符号が一成分であること、あるいは $b^*c^*$ の順序を持つことだけでは、反鎖置換による**重み衝突**が組合せ論的に必然でないと示す。§4 では、それでも実際の $(1,c),(2,c)$ 条件が抽象モデルの語集合を壊すことが分かった。

肯定方向に次に必要な補題は「符号境界の破壊」である。具体的には、clean な倍増経路上の符号列が長いとき、**どこかの二成分の内容ベクトルが一致する許容共通文脈を構成し、共役移送・$b,c$ 再配分・境界交換によって、$bc$ 射影の復号重みと $a$ 個数が食い違う**ことを証明する必要がある。単に2つの非 $a$ 部分語を連結するだけでは、その後の語をすべて同じ長さの符号語に復号できてしまい、(3.2) による無衝突が続く。

別の有望な角度は、系2.3を否定側の設計条件として使うことである。$\mu_a$ を超多項式にするには、$G$ の $\{a,b\}$ への影と $\{a,c\}$ への影の**双方**で、各規則の短い成功 witness が失われなければならない。一方の影だけでも多項式厚さに留まれば、(2.1) が $k$ を抑える。これを実際の fan-out 2／rank 2 の生産規則へ翻訳し、両影での witness 膨張と組代入可能性の同時成立が可能かを調べるのが次の厳密な焦点となる。

### 指定された特殊場合についての判定

- **全逃げ道が一成分**：§3 の符号模型ではなお衝突がない。モデルはクラスに属さないため一般否定にはならないが、仮定だけで肯定の証明も得られていない。
- **すべて $b^*c^*$**：§3.4 で純粋な符号数の鳩の巣論法は使えないと分かる。クラスの代入可能性を追加しての肯定は未証明。
- **$b^4$ または $c^4$ が因子として現れる**：当該文字の塊再配分は可能だが、二成分の内容ベクトル一致や $a$ 骨格衝突は直ちには従わない。追加の証明が必要。
- **どちらかの二文字影文法の厚さが多項式**：系2.3により、既存二文字定理から肯定側の多項式上界が成立する。これは証明済みの**別の条件付き特殊場合**である。

## 6. 学習下界について正確に言えること

本報告は $\Sigma=\{a,b,c\}$、内容型付け $c$、**fan-out $\le2$、rank $\le2$**、$L_n\in\mathcal C_{2,c}$、reduced good $G_n$、$\|G_n\|,\bar\theta_{G_n}=n^{O(1)}$、$\mu_a(L_n)=n^{\omega(1)}$ を**同時に満たす族を作っていない**。ゆえに、いずれの作用素についても新たな超多項式下界は主張しない。

もし将来そのような族ができれば、原稿 `prop:rare-type` により、型 $\{a\}$ を含む標本には長さ $\ge\mu_a(L_n)$ の語が必要となる。下界の対象は固定 rank cap $r\ge2$ の $\mathcal B^{\le r}_{2,c}$、ランク制限なしの $\mathcal B_{2,c}$、および $L_n$ とその $\{a\}$ 型削除部分言語の両方に特徴標本を持つ**集合駆動作用素**（特にクラス全体に特徴標本を持つ集合駆動作用素）である。ファンアウトは 2、アルファベットは明記した三文字であり、任意の Gold 型逐次学習器の収束時点・実行時間には下界を主張しない。

## 7. 既知性の確認範囲

本稿の符号模型は、固定長符号が一意復号可能であるという古典的な符号理論の直接応用である。一般の一意復号可能符号と各種復号性の文献には、たとえば A. Woryna, *On the set of uniquely decodable codes with a given sequence of code word lengths*, *Discrete Mathematics* 340 (2017), 51–57（DOI: 10.1016/j.disc.2016.08.013）がある。ただし**補題3.1のこの導出木への具体的な応用が既知かどうかは未確認**で、新規性の主張をしない。

二文字の組代入可能性の一般的な背景は R. Yoshinaka, *Efficient learning of multiple context-free languages with multidimensional substitutability from positive data*, *Theoretical Computer Science* 412 (2011), 1821–1831（DOI: 10.1016/j.tcs.2010.12.058）。§2の定量的上界は**栗山原稿の現行 `thm:two-letter-content` に依存**し、独立した先行研究として同じ上界が知られていると確認したものではない。

文献検索は限定的であり、**影文法の二重厚さ障害 (2.2) の既知性・優先権も未確認**である。

---

## 付録A：Python 3 標準ライブラリの完全再現コード

下記は外部パッケージを使わず、Windows では `py -3 skeleton_collision_check.py` で実行できる。**模型を文法・言語クラスの合法な族だと宣言するコードではない**。有限に生成した語集合について、全ての許容一穴・二穴区間と共有受理文脈を列挙して判定する。

```python
#!/usr/bin/env python3
"""Abstract escape-code experiment; not a grammar-membership certificate."""
from collections import defaultdict
from itertools import combinations


def sigma_a(w):
    out = []
    for ch in w:
        if ch != 'a' or not out or out[-1] != 'a':
            out.append(ch)
    return ''.join(out)


def binary_codes(m):
    width = max(1, (m - 1).bit_length())
    return [''.join('c' if (j >> k) & 1 else 'b'
                    for k in range(width - 1, -1, -1))
            for j in range(m)]


def ordered_codes(m):
    width = max(1, m - 1)
    return ['b' * j + 'c' * (width - j) for j in range(m)]


def antichain_words(codes):
    # Height j has 2**j leaves. At an internal node one may replace
    # its entire a-leaf interval by codes[j-1], or recurse on both children.
    words = {'a'}
    for code in codes:
        words = {x + y for x in words for y in words} | {code}
    return words


def skeleton_collisions(words):
    counts = defaultdict(set)
    for w in words:
        counts[sigma_a(w)].add(w.count('a'))
    return len(counts), sum(len(vals) > 1 for vals in counts.values())


def saturate_a(words):
    # Closure under reallocation of the positive a-run lengths,
    # preserving the a-skeleton and the total number of a's.
    result = set()
    for word in words:
        sk = sigma_a(word)
        amount = word.count('a')
        runs = sk.count('a')
        if runs == 0:
            result.add(sk)
            continue
        for cuts in combinations(range(1, amount), runs - 1):
            boundaries = (0,) + cuts + (amount,)
            lengths = iter(boundaries[j+1] - boundaries[j]
                           for j in range(runs))
            result.add(''.join('a' * next(lengths) if ch == 'a' else ch
                               for ch in sk))
    return result


def occurrences(w, d):
    n = len(w)
    if d == 1:
        for i in range(n):
            for j in range(i+1, n+1):
                yield (w[i:j],), (w[:i], w[j:])
    elif d == 2:
        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    for t in range(k+1, n+1):
                        yield (w[i:j], w[k:t]), (w[:i], w[j:k], w[t:])
    else:
        raise ValueError('only arity 1 and 2')


def insert(context, tup):
    return ''.join(context[i] + tup[i] for i in range(len(tup))) + context[-1]


def test_substitutability(language, arity):
    # Finite exhaustive test: generate all admissible accepting occurrences.
    distributions = defaultdict(set)
    by_context_and_type = defaultdict(set)
    for w in sorted(language):
        for tup, ctx in occurrences(w, arity):
            distributions[tup].add(ctx)
            content = tuple(frozenset(x) for x in tup)
            by_context_and_type[(ctx, content)].add(tup)
    for (e, content), tups in by_context_and_type.items():
        x = min(tups)
        for y in sorted(tups):
            if distributions[x] == distributions[y]:
                continue
            if distributions[x] - distributions[y]:
                u, v = x, y
            else:
                u, v = y, x
            f = min(distributions[u] - distributions[v])
            assert insert(e, u) in language and insert(e, v) in language
            assert insert(f, u) in language and insert(f, v) not in language
            return {'pass': False, 'arity': arity, 'u': u, 'v': v,
                    'E': e, 'F': f, 'Eu': insert(e, u),
                    'Ev': insert(e, v), 'Fu': insert(f, u),
                    'Fv': insert(f, v), 'tuples': len(distributions)}
    return {'pass': True, 'arity': arity, 'tuples': len(distributions)}


def main():
    for kind, fn in [('binary', binary_codes), ('ordered', ordered_codes)]:
        for m in (2, 3, 4):
            codes = fn(m)
            words = antichain_words(codes)
            s, coll = skeleton_collisions(words)
            print(kind, 'm=', m, 'code_length=', len(codes[0]),
                  'word_count=', len(words), 'skeleton_count=', s,
                  'weight_collisions=', coll)
    for m, saturated in ((2, False), (3, False), (3, True)):
        words = antichain_words(binary_codes(m))
        if saturated:
            words = saturate_a(words)
        print('audit m=', m, 'saturated=', saturated,
              'word_count=', len(words))
        for d in (1, 2):
            print('  ', test_substitutability(words, d))

if __name__ == '__main__':
    main()
```

### 実行ログ（主要部分）

```text
binary m= 2 code_length= 1 word_count= 5 skeleton_count= 5 weight_collisions= 0
binary m= 3 code_length= 2 word_count= 26 skeleton_count= 25 weight_collisions= 0
binary m= 4 code_length= 2 word_count= 677 skeleton_count= 499 weight_collisions= 0
ordered m= 2 code_length= 1 word_count= 5 skeleton_count= 5 weight_collisions= 0
ordered m= 3 code_length= 2 word_count= 26 skeleton_count= 25 weight_collisions= 0
ordered m= 4 code_length= 3 word_count= 677 skeleton_count= 499 weight_collisions= 0
audit m= 2 saturated= False word_count= 5
  arity 1: PASS
  arity 2: PASS
audit m= 3 saturated= False word_count= 26
  arity 1: FAIL (u=cb, v=bbbbbc, E=('', ''), F=('b', 'baa'))
  arity 2: FAIL (u=(a,aa), v=(aa,a), E=('', 'a', 'aaaa'))
audit m= 3 saturated= True word_count= 35
  arity 1: FAIL (u=aaaaab, v=aabbab)
  arity 2: FAIL (u=(a,aaab), v=(a,abbb))
```

**最終判定**：骨格衝突補題Cは未証明。証明できた新しい部分は、(i) 二文字影文法の厚さが**両方**大きくなければ超多項式 $\mu_a$ はあり得ないという定量的制約と、(ii) 長い相異なる逃げ道列からの衝突を**純粋な符号数の論法では引き出せない**という復号補題である。
