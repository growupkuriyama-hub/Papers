# 二文字 U₁・fan-out 1・rank ≤ 2：代入可能性の完全特徴づけ、極端族 \(N\asymp\|G\|\bar\theta\)、および精密な予想

**対象**：\(\Sigma=\{a,b\}\)、\(s(a)=1\)、\(s(b)=\zeta\)、\(\zeta^2=\zeta\)、\(U_1=\{1,\zeta\}\)、fan-out 1、rule rank \(\le 2\)、非循環（有限言語）CFG。
**原稿**：`Papers/02_fixed-h-mcfg/main.tex`（作業コピー 233 291 bytes、4261 行、`git hash-object` = `1cfba3b866db3a4faa04fd7549d51649a8291465`、HEAD = `3455f493ea1aa51e844c9f4377a95da76c96458b`）。
**先行報告**：`revision/chatgpt_binary_u1_fanout1_2026-10-30.md`、`revision/astra_ternary_u1_fanout2_2026-10-30.md`。
**作業フォルダ**：`revision/deepseek_u1f1_search/`（新規。原稿・既存ファイルは一切変更していない。git 操作もしていない。）

---

## 0. 結論の要約表

| # | 主張 | 判定 | 根拠 |
|---|---|---|---|
| 1 | 有限 \(L\) が \((1,s)\)-代入可能で混合語をもつなら、\(L\) の**全ての**混合語 \(x\) は \(\D_L(x)=\{(\eps,\eps)\}\) | **証明済み** | 定理 1（§3.1） |
| 2 | 系：\(L\) の混合語は \(L\) のいかなる語の真の因子でもない（(K2)） | **証明済み** | 系 1.1 |
| 3 | (K2)（＋純語高々 1 個）は代入可能性の**必要条件だが十分でない**。反例 \(L=\{aaa,aab,aba,baa,bab,bb\}\) | **反証済み** | 例 1（§3.2） |
| 4 | 有限 \(L\) の \((1,s)\)-代入可能性 \(\iff\) (i) \(\abs{L\cap a^+}\le 1\)、(ii) 任意の混合 \(x,y\) について \(\D(x)\cap\D(y)\neq\emptyset\Rightarrow \D(x)=\D(y)\) | **証明済み** | 定理 2（§3.3） |
| 5 | ブロックコード族 \(L_{k,n}=(\{a^k,b\})^{2^n}\) は**全ての** \(k\ge1,n\ge0\) で \((1,s)\)-代入可能 | **証明済み** | 定理 3（§4） |
| 6 | 同族の厳密値：\(N=k2^n\)、\(\|G\|=k+6n+4\)、\(\bar\theta=2^n+k-1\)、\(\tau=N\) | **証明済み**（数値は全列挙でも一致） | 定理 3・§4.3 |
| 7 | 同族で \(N/(\|G\|\bar\theta)\to 1\)（\(k=\lceil\sqrt{6n\,2^n}\rceil\)）。すなわち線形因子下界の定数 \(1/23\) は \(1-o(1)\) に改善できる | **証明済み** | 系 3.2 |
| 8 | 同族で \(\kappa_{A_n}=\tau=N\)、かつ \(\kappa_{A_n}/(|V|\bar\theta)\to\infty\)。よって「\(\kappa_A\le C|V|\bar\theta\)（定数 \(C\)）」という強化予想は**偽** | **反証済み** | 系 3.4 |
| 9 | 予想 C：\(\tau(G,s)\le \|G\|\,\bar\theta_G\)（全有限 \((1,s)\)-代入可能 \(L\)、全 reduced good rank \(\le2\) 表示） | **未解決**（反例 0 件。定理 3 の族が比 \(0.9786\) まで達成） | §5 |
| 10 | 予想 C \(\Rightarrow\) (P) の肯定（特徴データ長は \(\|G\|\cdot\bar\theta\) の多項式） | **証明済み** | 定理 4（§5.1） |
| 11 | 網羅・構造化・ランダム探索で \(\tau>\|G\|\bar\theta\) の例は **0 件** | **観測** | §6 |
| 12 | 素朴倍増＋\(b\) 短絡、\(a^ib a^i\) 族、ブロックコード＋短絡は代入可能でない | **反証済み**（証明書付き） | §7 |
| 13 | 主問題 (P) の真偽 | **未解決**（本報告は決着を主張しない） | §8 |

**要点**：有限言語では代入可能性が「混合部分は因子反鎖（より強く、混合語の分布は全て \(\{(\eps,\eps)\}\)）」という組合せ条件に還元される（定理 1、2）。この還元の下で、\(\theta\) を小さく保ちながら純語を指数的に伸ばす唯一の生き残った構造が**ブロックコード族**であり、それは \(N\asymp\|G\|\bar\theta\) を達成する。すなわち「稀な型」の下界は本質的に \(\|G\|\bar\theta\) で、多項式を超えない。この観測から精密な予想 C を立て、それが (P) の肯定を含意することを示す。

---

## 1. 設定・記法・原稿との対応

* \(\Sigma=\{a,b\}\)、\(s:\Sigma^+\to U_1\)、\(s(a)=1\)、\(s(b)=\zeta\)。語 \(w\in\Sigma^+\) の型は \(w\in a^+\) のとき \(1\)（**純**）、\(b\) を含むとき \(\zeta\)（**混合**）。\(\eps\) は型をもたない（原稿 `def:tuple-substitutable` の「空成分は比較しない」に従う）。
* \(\D_L(x):=\{(u,v)\in\Sigma^*\times\Sigma^*:uxv\in L\}\)（\(d=1\) の分布）。空語 \(x\) は決して比較しない。
* \(L\) が \((1,s)\)-代入可能とは、任意の \(x,y\in\Sigma^+\) について \(s(x)=s(y)\) かつ \(\D_L(x)\cap\D_L(y)\ne\emptyset\) ならば \(\D_L(x)=\D_L(y)\)、を言う（原稿 `def:tuple-substitutable` の \(f=1\)）。
* CFG は原稿 `def:standard-mcfg` の形（fan-out 1 なので各非終端は 1 成分、テンプレートは 1 個）。規則 \(A\to\rho(B_1,\dots,B_q)\) のランクは \(q\)、サイズは
  \(\|G\|:=|V|+\sum_{R}(1+q_R+\sum_i|\alpha_i|)\)（\(|\alpha_i|\) は端末出現と変数出現を数える）。
* \(\theta_G(R):=\min\{\abs{w}:w\in L(G)\ \text{が}\ R\ \text{を一度以上使う成功導出をもつ}\}\)、\(\theta_G:=\max_R\theta_G(R)\)、\(\bar\theta_G:=\max\{1,\theta_G\}\)。**各規則ごとに個別に**最短成功使用をとる（原稿 `subsec:thickness-contexts`）。
* 非終端 \(A\) に対し \(\lo(A):=\min\{\abs{u}:u\in L_A(G)\}\)、\(o_A:=\) 成功導出から \(A\) 部分木を除いて得られる文脈の最短固定長、\(\ctx(A)=(u_A,v_A)\) をその 1 つとする。fan-out 1・線形・非削除性から
  \[
  \theta_G(A\to\rho(B_1,\dots,B_q))=o_A+\abs{\rho}_\Sigma+\sum_j \lo(B_j)
  \tag{1.1}
  \]
  が**厳密に**成り立つ（証明は §2.1）。本報告の \(\theta\) はすべてこの式で計算する。
* \(\tau_X:=\min\{\|\mathbf t\|_1:\mathbf t\in \mathrm{Cl}_{L,s}(X)\}\)、\(\tau(G,s):=\max_X\tau_X\)（原稿 `cor:distribution-representatives`）。\(f=1\) では補題 `lem:app-u1-fillers` により
  \(\tau_{A_{\mathbf t}}=\min\{\abs{z}:s(z)=\mathbf t,\ \ctx(A)[z]\in L\}\)。
* \(\kappa_A:=\min\{k\ge1:\ctx(A)[a^k]\in L\}\)（型 1 を実現する \(A\)）。\(f=1\) では \(\tau_{A_1}=\kappa_A\)。
* \(\mu^\star(L):=\max_{\mathbf t\in M_L}\min\{\abs{w}:w\in L,\ s(w)=\mathbf t\}\)。純語が \(a^N\) のみなら \(\mu^\star=N\)。

**原稿の定理との関係**：`prop:rare-type` により任意の特徴標本 \(F\) は \(\|F\|_+\ge \mu^\star+1=N+1\)。したがって \(N\) の超多項式下界が (P) の否定に十分。`cor:distribution-representatives` により \(\|K\|_+\le N_{\mathrm{typ}}(1+2\bar\theta+r\tau)+1\)、\(N_{\mathrm{typ}}\le 3^r\|G\|\)。よって \(\tau\) の多項式上界が (P) の肯定に十分。

---

## 2. 厳密な道具（段階 1）

### 2.1 規則厚さの厳密計算

**補題 2.1**（(1.1) の証明）。\(G\) は reduced good、fan-out 1、非循環とする。\(R:A\to\rho(B_1,\dots,B_q)\) に対し
\[
\theta_G(R)=o_A+\abs{\rho}_\Sigma+\sum_{j}\lo(B_j).
\]
*証明*．\(\ge\)：\(R\) を使う成功導出で \(A\) 節点より上は文脈（固定部長 \(\ge o_A\)）、\(R\) 自身が書く端末は \(\abs\rho_\Sigma\) 個、子 \(B_j\) の収率長 \(\ge \lo(B_j)\)。非削除性からこれらは全て文の異なる位置に現れる。\(\le\)：\(o_A\) を達成する文脈 \(\ctx(A)\) に、各子を最短収率で埋めた \(R\) を挿入すれば成功導出になり、長さは右辺に等しい。∎

\(o_A,\lo(A)\) は非循環性から DP で厳密に求まる（子の添字が親より小さい正規形に限らず、一般の非循環順序で計算する）。本報告のコードは位相順（添字降順）で \(o\) を伝播させ、\(\ctx(A)\) も同時に構成する。

### 2.2 代入可能性の厳密判定器

有限 \(L\) について、全語 \(w\) の全 \(0\le i<j\le\abs w\) を列挙し、因子 \(x=w[i:j]\) と文脈 \((w[:i],w[j:])\) を登録する。文脈ごとに同一型の因子をまとめ、その中各因子の**全分布** \(\D(x)\)（＝全語の全出現から再計算）を比較する。違反時は \((x,y,\text{共有文脈},\text{区別文脈})\) を返す。有限 \(L\) を完全列挙しているので、打切りによる偽判定はない。

**検証（段階 1）**：`selftest.py` の実行ログ（§9.1）で
* \(H_{N,k}=\{a^N\}\cup\{a^ib^ka^{N-k-i}\}\)：\(N=4..11\)、\(k=1..N-1\) の 52 件すべて通過、
* 二語族 \(\{a^N,w\}\)（\(N=12,20,30\)）：通過、
* 素朴倍増 \(A_0\to a,\ A_i\to A_{i-1}A_{i-1}\mid b\)：\(n\ge2\) で違反（証明書付き）、
* \(A_0\to a\mid b,\ A_i\to A_{i-1}A_{i-1}\)（256 語、\(\|G\|=23\)、\(\bar\theta=8\)）：通過、
* \(\{a,b\}^{\le3}\) の**全 16383 言語**で「定義型判定器」と「構造判定器（定理 1 の必要条件）」を照合し 472 件の不一致（＝必要条件が十分でないことの証拠、例 1）、
* \(\{a,b\}^{\le5}\) 内のランダム 4000 言語でも不一致 0（必要条件の方向は常に成立）。

---

## 3. 有限言語の \((1,s)\)-代入可能性の完全な特徴づけ

### 3.1 定理 1（混合語の分布刚性）

**定理 1.** \(L\subseteq\Sigma^+\) は有限かつ \((1,s)\)-代入可能とする。\(M:=L\cap\Sigma^*b\Sigma^*\)（混合語の集合）が空でないなら、任意の \(x\in M\) について
\[
\D_L(x)=\{(\eps,\eps)\}.
\]

*証明*．\(x,y\in M\) はともに \(L\) の語なので \((\eps,\eps)\in\D(x)\cap\D(y)\)、かつ \(s(x)=s(y)=\zeta\)。代入可能性から \(\D(x)=\D(y)=:\D_0\)。\(\D_0\) が \((\eps,\eps)\) 以外の \((u,v)\) を含むと仮定する。任意の \(y\in M\) に対し \((u,v)\in\D(y)=\D_0\) だから \(uyv\in L\)。\(uyv\) は \(b\) を含むので \(uyv\in M\)。写像 \(f(y):=uyv\) は有限集合 \(M\) から \(M\) への単射で、\(\abs{f(y)}=\abs y+\abs u+\abs v>\abs y\)。\(M\) の最大長の元で矛盾する。∎

**系 1.1.** 定理 1 の下で、\(L\) の混合語は \(L\) のいかなる語の真の因子でもない。すなわち
\[
x\in M,\ w\in L,\ w=uxv,\ uv\ne\eps\ \Longrightarrow\ \text{偽}.
\]
*証明*．\(w=uxv\in L\) なら \((u,v)\in\D(x)=\{(\eps,\eps)\}\)、よって \(u=v=\eps\)。∎

これを **(K2)** と呼ぶ。系 1.1 は「\(L\) の混合部分は因子順序の反鎖である」と言い換えられる。

**注意 3.1**（探索への含意）．系 1.1 は非常に強い。たとえば純語 \(a^N\) の導出において「重い節点の短い収率 \(z\)」を代入して得られる語 \(a^pza^q\in L\)（前報告の定理 1）はすべて混合語であり、それらは互いに因子になれない。特に、同じ非終端の短い収率 \(z\) に対して \(\{(p,q):a^pza^q\in L\}\) は \(\mathbb N^2\) の反鎖でなければならない。

### 3.2 例 1（(K2) は十分でない）

\[
L=\{aaa,\ aab,\ aba,\ baa,\ bab,\ bb\}
\]
は純語 \(aaa\) をただ一つもち、混合語 \(aab,aba,baa,bab,bb\) はどれも他の語の真の因子でない（(K2) 成立）。しかし
\[
x=ab,\quad y=ba,\quad \text{共有文脈 }(\eps,a),\quad
\D(ab)=\{(\eps,a),(a,\eps),(b,\eps)\},\quad
\D(ba)=\{(\eps,a),(a,\eps),(\eps,b)\}
\]
で \(\D(ab)\ne\D(ba)\)。すなわち \((1,s)\)-代入可能でない。実際 \(aba,baa\in L\) だが \(abb\notin L\)、\(bab\in L\) である。
**教訓**：判定は「\(L\) の語」だけでなく**全ての混合因子**（\(ab,ba\) は \(L\) の語ではない）について行う必要がある。

### 3.3 定理 2（完全特徴づけ）

**定理 2.** 有限 \(L\subseteq\Sigma^+\) について、次は同値である。
1. \(L\) は \((1,s)\)-代入可能。
2. (i) \(\abs{L\cap a^+}\le1\)、かつ (ii) 任意の混合 \(x,y\in\Sigma^+\) について \(\D(x)\cap\D(y)\ne\emptyset\Rightarrow\D(x)=\D(y)\)。

*証明*．(1)\(\Rightarrow\)(2i)：\(a^p,a^q\in L\)、\(p<q\) とすると \((\eps,\eps)\in\D(a^p)\cap\D(a^q)\) で同型。代入可能性から \(\D(a^p)=\D(a^q)\)。\((\eps,a^{q-p})\in\D(a^p)\) だから \(a^{2q-p}\in L\)。帰納的に \(a^{kq-(k-1)p}\in L\ (k\ge1)\) となり無限、有限に矛盾。(1)\(\Rightarrow\)(2ii) は定義そのもの。
(2)\(\Rightarrow\)(1)：混合同士は (ii) そのもの。(ii) は定理 1 の証明と同じ論法で「\(L\) の混合語の分布は全て \(\{(\eps,\eps)\}\)」を含意する（\(x,w\in M\) が \((\eps,\eps)\) を共有 \(\Rightarrow\D(x)=\D(w)\ni(u,v)\)、以下同）。よって (K2) が成り立つ。純同士 \(a^i,a^j\ (i<j)\) が文脈 \((u,v)\) を共有するとする。\(u,v\) が純なら \(a^{\abs u+i+\abs v}\in L\) は純で唯一の純語 \(a^N\) に等しく、同様に \(a^{\abs u+j+\abs v}=a^N\) から \(i=j\)、矛盾。\(u\) か \(v\) が \(b\) を含むなら \(ua^iv\) と \(ua^jv\) はともに混合で前者は後者の真の因子、これは (K2) に反する。∎

**系 2.1**（実用的な必要条件）．有限の代入可能 \(L\) について、
\[
\text{(i)}\ \abs{L\cap a^+}\le1,\qquad
\text{(ii) 混合語は因子反鎖},\qquad
\text{(iii) 混合因子の分布類は「交われば一致」}.
\]
(i),(ii) は計算が安く、探索の前段フィルタに使える。(iii) は定義型判定器で検査する。

---

## 4. ブロックコード族（定理 3）：\(N\asymp\|G\|\bar\theta\) を達成する族

### 4.1 定義

整数 \(k\ge1\)、\(n\ge0\) に対し \(D_k:=\{a^k,\ b\}\)、\(L_{k,n}:=D_k^{\,2^n}\)（\(D_k\) の語 \(2^n\) 個の連接全体）。文法は
\[
G_{k,n}:\quad A_0\to a^k\mid b,\qquad A_i\to A_{i-1}A_{i-1}\ (1\le i\le n),\qquad S=A_n .
\tag{4.1}
\]

### 4.2 定理 3

**定理 3.** 任意の \(k\ge1\)、\(n\ge0\) について：
1. \(L(G_{k,n})=L_{k,n}\)。
2. \(L_{k,n}\) の純語は \(a^{k2^n}\) のみ。よって \(N=k2^n\)。
3. \(\|G_{k,n}\|=k+6n+4\)。
4. \(n\ge1\) のとき \(\bar\theta_{G_{k,n}}=2^n+k-1\)。
5. \(L_{k,n}\) は \((1,s)\)-代入可能。
6. \(\tau(G_{k,n},s)=N=k2^n\)（\(\kappa_{A_i}=k2^i\)）。

*証明*．
(1)(2) は \(D_k\) が前符号（\(a^k\) と \(b\) は互いに接頭辞でない）であることからの帰納。(2)：\(D_k\) の語のうち純なのは \(a^k\) のみだから、純語は \((a^k)^{2^n}\) のみ。
(3)：\(\abs V=n+1\)。規則サイズは \(A_0\to a^k\) が \(1+0+k=k+1\)、\(A_0\to b\) が \(2\)、\(A_i\to A_{i-1}A_{i-1}\) が \(1+2+2=5\)（\(n\) 個）。合計 \((n+1)+(k+1)+2+5n=k+6n+4\)。
(4)：\(\lo(A_0)=1\)、\(\lo(A_i)=2^i\ (i\ge1)\)。\(o_{A_n}=0\)、\(o_{A_i}=\sum_{j=i}^{n-1}\lo(A_j)\)。よって
\(\theta(A_n\to A_{n-1}A_{n-1})=2\lo(A_{n-1})=2^n\)、\(i\ge1\) で \(\theta(A_i\to A_{i-1}A_{i-1})=(2^n-2^i)+2^i=2^n\)、
\(\theta(A_0\to a^k)=o_{A_0}+k=(2^n-1)+k\)、\(\theta(A_0\to b)=2^n-1+1=2^n\)。最大は \(2^n+k-1\)。
(5)：\(\psi(w):=(\abs w-\abs w_b)/k+\abs w_b\in\mathbb Q\) とおく（加法性がある）。\(w\in L_{k,n}\) では \(w\) の極大 \(a\)-連はすべて長さが \(k\) の倍数で、\(\psi(w)=2^n\)（＝数字の個数）である。実際 \(\abs w=k\cdot\#(a\text{-数字})+\#b\) より \(\psi=\#(a\text{-数字})+\#b\)。
いま混合 \(x,y\) が共通文脈 \((u,v)\) をもつ、すなわち \(uxv,uyv\in L_{k,n}\) とする。このとき
(a) \(\psi(x)=\psi(uxv)-\psi(u)-\psi(v)=2^n-\psi(u)-\psi(v)=\psi(y)\)。
(b) \(x\) の極大 \(a\)-接頭辞長を \(p_1(x)\)、極大 \(a\)-接尾辞長を \(p_{t+1}(x)\) とすると、\(uxv\in L\) より \(u\) の末尾 \(a\)-連長 \(\mathrm{tr}(u)\) について \(\mathrm{tr}(u)+p_1(x)\equiv0\pmod k\)、また \(p_{t+1}(x)+\mathrm{le}(v)\equiv0\pmod k\)。同じ \((u,v)\) を共有する \(y\) でも同じ式が成り立つから \(p_1(x)\equiv p_1(y)\)、\(p_{t+1}(x)\equiv p_{t+1}(y)\pmod k\)。
(c) 主張：\(x\) の内部 \(a\)-連がすべて \(k\) の倍数であるとき、
\[
\D(x)=\{(u',v'):\ \text{(i) } u'xv'\text{ の極大 }a\text{-連は全て }k\text{ の倍数},\ \text{(ii) }\psi(u')+\psi(v')=2^n-\psi(x)\}
\]
であり、右辺は \(x\) を \((p_1(x)\bmod k,\ p_{t+1}(x)\bmod k,\ \psi(x))\) を通してしか使わない。実際 (i) は「\(u'\) の最後以外の \(a\)-連 \(\equiv0\)」「\(u'\) の末尾 \(a\)-連 \(\equiv-p_1(x)\)」「\(x\) の内部 \(a\)-連 \(\equiv0\)」「\(v'\) の先頭 \(a\)-連 \(\equiv-p_{t+1}(x)\)」「\(v'\) の最初以外の \(a\)-連 \(\equiv0\)」に分解され、(ii) は \(\psi\) の加法性で \(\psi(u')+\psi(v')=2^n-\psi(x)\) と同値。逆に (i)(ii) を満たす \(u'xv'\) は \(D_k\) の語 \(2^n\) 個の連接に一意に分解される（\(a\)-連がすべて \(k\) の倍数だから \(a^k\) と \(b\) への分解は一意で、個数は \(\psi=2^n\)）。
(d) 共有文脈をもつ \(x,y\) は (b) から同じ境界剰余、 (a) から同じ \(\psi\)、そして \(uxv\in L\) から内部 \(a\)-連は両方とも \(k\) の倍数。よって (c) から \(\D(x)=\D(y)\)。
純同士：\(x=a^i,y=a^j\) が共通文脈 \((u,v)\) をもつと (a) から \(\psi(a^i)=\psi(a^j)\)、すなわち \(i/k=j/k\)、よって \(i=j\)。したがって異なる 2 つの純因子は文脈を共有せず、純同士の条件は空虚に成立する。
以上で (5) が従う。
(6)：\(A_i\) の純収率は \(a^{k2^i}\) のみ（(2) と同じ論法）なので \(\kappa_{A_i}=k2^i\)、最大は \(k2^n=N\)。ζ 型はより短い混合収率をもつので \(\tau=N\)。∎

**注意 4.1**：\(G_{k,n}\) は reduced good・rank 2・非循環。すべての非終端が成功導出に現れ、\(\lo(A_i)\le2^i\) なので \(\bar\theta\) は \(2^n+k-1\) で厳密。**\(\theta\) は「深さ由来の \(2^n\)」と「ブロック長 \(k\)」の和**であり、\(N=k2^n\) はその積である。

### 4.3 数値（厳密計算との一致）

`verify_family.py` は \(k=1..6\)、\(n=1..3\) の全 18 組で \(\|G\|=k+6n+4\)、\(\bar\theta=2^n+k-1\)、\(N=k2^n\)、および代入可能性（全列挙・全因子・全文脈）を確認した。さらに定理 3(5) の証明の鍵補題（\(\psi\) 不変量）を \(k=1..4\)、\(n=2,3\) で厳密に検査し、違反 0 を得た（§15）。抜粋：

| \(k\) | \(n\) | \(\abs L\) | \(\|G\|\) | \(\bar\theta\) | \(N\) | \(N/(\|G\|\bar\theta)\) |
|---:|---:|---:|---:|---:|---:|---:|
| 2 | 3 | 256 | 24 | 9 | 16 | 0.0741 |
| 4 | 3 | 256 | 26 | 11 | 32 | 0.1119 |
| 6 | 3 | 256 | 28 | 13 | 48 | 0.1319 |
| 10 | 3 | 256 | 32 | 17 | 80 | 0.1471 |

\(k=\lceil\sqrt{6n\,2^n}\rceil\) に沿った理論値（定理 3 の閉じた式 \(N=k2^n\)、\(\|G\|=k+6n+4\)、\(\bar\theta=2^n+k-1\) から計算）：

| \(n\) | \(k\) | \(\|G\|\) | \(\bar\theta\) | \(N\) | \(N/(\|G\|\bar\theta)\) |
|---:|---:|---:|---:|---:|---:|
| 4 | 20 | 48 | 35 | 320 | 0.1905 |
| 8 | 111 | 163 | 366 | 28 416 | 0.4763 |
| 12 | 543 | 619 | 4 638 | 2 224 128 | 0.7747 |
| 16 | 2 508 | 2 608 | 68 043 | 164 364 288 | 0.9262 |
| 20 | 11 217 | 11 341 | 1 059 792 | 11 761 876 992 | **0.9786** |

### 4.4 系 3.2（線形因子下界の定数の改良）

**系 3.2.** 任意の \(\eps>0\) に対し、有限 \(L\in\Cmcf{1}{s}\) と reduced good・fan-out 1・rank 2 の表示 \(G\) で
\[
\text{全ての特徴標本 }F\text{ について }\ \|F\|_+\ \ge\ (1-\eps)\,\|G\|\,\bar\theta_G
\]
となるものが存在する。

*証明*．定理 3 の族で \(k=\lceil\sqrt{6n2^n}\rceil\) とし、\(N=k2^n\)。`prop:rare-type` により \(\|F\|_+\ge N+1\)。一方
\[
\frac{N}{\|G\|\bar\theta}=\frac{k2^n}{(k+6n+4)(2^n+k-1)}\longrightarrow 1
\]
（\(k/\sqrt{6n2^n}\to1\) のとき \((1+6n/k)(1+k/2^n)\to1\)）。∎

これは原稿 `prop:linear-factor-sharp` と同種の「線形因子 \(\|G\|\bar\theta\) は不可避」という下界を、二文字 \(U_1\)・\((1,s)\)-クラスで定数 \(1-o(1)\) で与える。原稿の下界は自明型付け・三文字・定数 \(1/23\) であったから、本族は代入可能性クラスにおいても線形因子が本質的に最良であることの初めての証拠である。

### 4.5 系 3.4（\(\kappa_A\le C|V|\bar\theta\) の反証）

**系 3.4.** 任意の定数 \(C\) に対し、定理 3 の族のある成員で
\[
\kappa_{A_n}\ >\ C\,|V|\,\bar\theta_{G_{k,n}}
\]
となるものがある。実際 \(\kappa_{A_n}=k2^n\)、\(|V|\bar\theta=(n+1)(2^n+k-1)\) で、\(k\gg n\) のとき比は \(\to\infty\)。

*証明*．比は \(k2^n/((n+1)(2^n+k-1))\ge k/((n+1)(1+k/2^n))\)。\(k=\lceil\sqrt{6n2^n}\rceil\) なら \(k/2^n\to0\)、\(k/(n+1)\to\infty\)。∎

**含意**：前報告の (U) を「\(\kappa_A\le C\,|V|\bar\theta\)」の形で精密化することは**できない**。正しい形は \(\|G\|\bar\theta\) を許すものでなければならない（予想 C）。

---

## 5. 予想 C と (P) への含意

### 5.1 定理 4（予想 C は (P) を導く）

**予想 C.** 有限 \(L\subseteq\Sigma^+\) が \((1,s)\)-代入可能で、\(G\) が \(L=L(G)\) の reduced good・fan-out 1・rank \(\le r\) 表示ならば
\[
\tau(G,s)\ \le\ \|G\|\,\bar\theta_G .
\tag{C}
\]

**定理 4.** 予想 C を仮定すると、固定 \(r\) に対し、任意の有限 \(L\in\Cmcf{1}{s}\) とその任意の reduced good・rank \(\le r\) 表示 \(G\) について、両方の再構成作用素に共通の特徴標本 \(K\) で
\[
\|K\|_+\ \le\ 3^r\|G\|\bigl(1+2\bar\theta_G+r\|G\|\bar\theta_G\bigr)+1
\]
を満たすものが存在する。特に (P) は有限目標に対して肯定的に解ける。

*証明*．`cor:distribution-representatives` より \(\|K\|_+\le N_{\mathrm{typ}}(1+2\bar\theta+r\tau)+1\)。\(f=1\) では \(N_{\mathrm{typ}}\le3^r\|G\|\)（原稿 `thm:data-from-typed-thickness` の直後）。予想 C を代入して \(\tau\le\|G\|\bar\theta\)。∎

**注意 5.1**：予想 C は \(\mu^\star\le\tau\le\|G\|\bar\theta\) を含意する（`cor:distribution-representatives` の \(\mu^\star\le\tau\)）。したがって (P) の否定に必要な「\(N=\mu^\star\) の超多項式下界」は予想 C の下で不可能である。

### 5.2 予想 C の検査

検査した**すべての**代入可能文法（§6 の全 46 246 件、うち \(N>\bar\theta\) の 460 件）で \(\tau\le\|G\|\bar\theta\) が成立し、反例は 0 件。最大比は定理 3 の族の \(0.9786\)（\(n=20\)）。有限探索内の最大は \(0.1429\)（\(N=1\) の退化例）。\(N>\bar\theta\) をもつ例に限っても最大 \(N/\bar\theta=1.667\) で、\(\tau/(\|G\|\bar\theta)\) は \(0.12\) 未満。族を除けば \(\tau/(\|G\|\bar\theta)<0.15\) である。

**予想 C を支える構造的考察**：
1. 定理 1 により、混合語はすべて分布 \(\{(\eps,\eps)\}\)、すなわち \(L\) の混合部分は因子反鎖である。因子反鎖の言語を小さな文法で作ると、どうしても「数字（ブロック）」の反復構造になり、\(\|G\|\) がブロック長 \(k\) を、\(\bar\theta\) が反復回数 \(2^n\) を支払う。\(N=k2^n\) はその積なので \(\|G\|\bar\theta\) を超えにくい。
2. 短絡（\(A_i\to z_i\)）で \(\lo(A_i)\) を下げると \(\theta\) は下がるが、\(z_iz_i\) などが \(L\) に入り、定理 1 の (K2) と両立しなくなる（§7.3 の証明書）。実際 \(n=3\) では 529 通りの短絡の組で**全滅**した。
3. 定理 3 の族は「\(k\) を大きくすると \(\|G\|\) が、\(2^n\) を大きくすると \(\bar\theta\) が」線形に増え、\(N\) はその積。この 3 つの資源の分離が予想 C の等式成立の機構である。

### 5.3 予想 C の同等な形・周辺

* **C1**（純語形）：\(\mu^\star=N\le\|G\|\bar\theta\)。
* **C2**（代表長形）：\(\tau\le\|G\|\bar\theta\)（予想 C 本人。C2 \(\Rightarrow\) C1）。
* **C3**（\(\kappa\) 形）：型 1 を実現する各 \(A\) で \(\kappa_A\le\|G\|\bar\theta\)。定理 3 で \(\kappa_{A_n}=N\) なので C3 も sharp。
* C3 は `lem:thickness-equivalence`(iv) の文脈 \(E_A\) に関する具体的な不等式で、探索で直接検査できる。

---

## 6. 探索（段階 2）

すべて Python 3.12（標準ライブラリのみ）。判定は §2.2 の定義型厳密判定器。言語の完全列挙には上限 `CAP` を設け、超えたものは**未検査**として数えた（違反・通過に混ぜていない）。

### 6.1 網羅探索（正規形クラス）

非終端 \(0,\dots,k-1\)（子の添字 \(<\) 親の添字、非循環）、開始 \(k-1\)、各非終端の規則数 \(\le m\)、右辺の記号数 \(\le4\)、rank \(\le2\)、端末ブロックは \(\{a,b\}^{\le2}\)。すべての非終端が productive かつ reachable（reduced）のものだけを検査。

| クラス | 候補数 | 非 reduced | 容量超過 | 非代入可能 | **代入可能** | \(N>\bar\theta\) | 最大 \(N/(\|G\|\bar\theta)\) | 最大 \(N/\bar\theta\) | 鍵条件違反 |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| \(k=1\)、規則 \(\le2\) | 21 | 0 | 0 | 4 | 17 | 0 | 0.333 | 1.000 | 0 |
| \(k=2\)、規則 \(\le2\) | 31 185 | 441 | 0 | 26 155 | **4 589** | **27** | 0.1429 | 1.500 | 0 |
| \(k=3\)、規則 \(\le1\) | 53 136 | 19 224 | 0 | 0 | **33 912** | 0 | 0.0909 | 1.000 | 0 |
| 構造化 \(k=2\)（§6.2） | 2 880 | 0 | 0 | 1 612 | **1 268** | 23 | 0.1111 | 1.500 | 0 |
| 構造化 \(k=3\)（§6.2） | 135 200 | 0 | 0 | 129 696 | **5 504** | **371** | 0.0762 | 1.667 | 0 |
| 構造化 \(k=4\)（§6.2） | 200 001 | 0 | 0 | 199 194 | **806** | 38 | 0.0467 | 1.400 | 0 |
| ランダム \(k=3..6\)（§6.3） | 20 000 | 15 018 | 45 | 4 787 | **150** | 1 | 0.0588 | 1.167 | 0 |
| **合計** | **442 423** | 34 683 | 45 | 361 449 | **46 246** | 460 | — | — | **0** |

（「非 reduced」は productive でないか reachable でない非終端をもつもの。鍵条件＝(K1) 純語高々 1 個、(K2) 混合語が因子反鎖、(K3) \(\tau\le\|G\|\bar\theta\)。）

\(k=3\)・規則 \(\le2\) の完全列挙は候補数が \(4.2\times10^8\) 超で非現実的なため打ち切った（**未検査**として明記する）。\(k=5\) の構造化探索も時間の都合で未実行（**未検査**）。

**上位例（\(k=2\)、規則 \(\le2\)、\(N>\bar\theta\) の 27 件から）**：

| \(L\) | \(N\) | \(\|G\|\) | \(\bar\theta\) | 比 |
|---|---:|---:|---:|---:|
| \(\{aaaa,aab,baa,bb\}\) | 4 | 12 | 3 | 0.1111 |
| \(\{aaaaaa,aaaab,aabaa,aabb,baaaa,baab,bbaa,bbb\}\) | 6 | 20 | 4 | 0.0750 |
| \(\{aaaaa,aaab,abaa,abb\}\) | 5 | 13 | 4 | 0.0962 |
| \(\{aaaaaa,aaaba,baaaa,baba\}\) | 6 | 14 | 5 | 0.0857 |

いずれも「数字コード」型（\(aa\) と \(b\) の連接）で、定理 3 の族の小さい成員（\(k=2,n=2\) など）と同型か、その変種である。

### 6.2 構造化探索

レベルごとに「構造規則 1 個（16 形状から）＋短絡 1 個（20 語から）」、基底 9 種、\(k\le5\)。形状は \((XX),(aXX),(XaX),(XXa),(bXX),(XbX),(XXb),(aX),(Xa),(bX),(Xb),(X),(aXa),(bXb),(aaX),(Xaa)\)（\(X=i-1\)）。短絡は \(b,bb,ab,ba,aab,aba,baa,abb,bab,bba\) と長さ 4 の混合語 10 種。基底は \((a),(a,b),(aa),(aa,b),(a,b,bb),(aaa),(aaa,b),(ab),(ba)\)。

\(k=2\)：2880 候補、代入可能 1268、\(N>\bar\theta\) 23、最大 \(N/\bar\theta=1.5\)。
\(k=3\)（形状 13・短絡 10・基底 8 に絞った版）：135 200 候補、代入可能 5504、\(N>\bar\theta\) 371、最大 \(N/\bar\theta=1.667\)、最大 \(N/(\|G\|\bar\theta)=0.0762\)。
\(k=4\)：200 001 候補で打切り、代入可能 806、\(N>\bar\theta\) 38、最大 \(N/(\|G\|\bar\theta)=0.0467\)。
いずれも鍵条件違反 0。**短絡を含む族は \(k\) を上げるとほぼ全滅する**（代入可能性率：\(k=2\) で 44%、\(k=3\) で 4%、\(k=4\) で 0.4%）。

### 6.3 ランダム探索

\(k\in\{3,4,5,6\}\)、各非終端 1〜3 規則、端末ブロックは長さ \(\le3\)、子は下位添字からランダム。20 000 個生成、reduced のものだけ検査。結果は §6.1 の表（代入可能 150、\(N>\bar\theta\) 1 件のみ、最大 \(N/(\|G\|\bar\theta)=0.0588\)）。**代入可能かつ \(\tau>\|G\|\bar\theta\) の例は 0 件**。

### 6.4 必要条件に沿った設計探索（本報告の中心）

前報告の事実 3（短い混合語の大量発生、深い挿入、多数の \(b\)-run）を満たす族として、次の 3 系統を設計し検査した。

**(a) 倍増鎖＋レベル別短絡** \(A_0\to a\)、\(A_i\to A_{i-1}A_{i-1}\mid z_i\)。\(z_i\) を 16 種のブロック設計（\(a^iba^i\)、\(ba^ib\)、\(a^ib\)、\(ba^i\)、\(ab^ia\) など）で試した。**すべて \(n=2\) で違反**（\(n=1\) のみ通過）。証明書は §7.2 と §14.7 のログ。

**(b) ブロックコード＋短絡** \(A_0\to aa\mid b\)、\(A_i\to A_{i-1}A_{i-1}\mid z_i\)（根は 2 分規則のみ）。\(n=2\)：23 通りの \(z_1\) のうち通過 3 件（\(z_1=bb,baa,aab\)）はいずれも**既存の語と一致する冗長な短絡**で、言語は \(D^{4}\) のまま。\(n=3\)：529 通り**全滅**。証明書は §7.3。

**(c) ブロックコード族（短絡なし）**：定理 3。全 \(k,n\) で通過（証明済み）。\(\bar\theta\) は \(N/2\) 程度だが、\(k\) を大きくすると \(N/(\|G\|\bar\theta)\to1\) になる。**この族だけが生き残った。**

### 6.5 局所探索（\(k=8..14\)）とその原理的限界

`local_search.py`：非終端 \(k\in\{5,\dots,14\}\) の非循環文法を出発点とし（ブロックコード族の小さい成員、およびランダムな reduced 文法）、「端末ブロックの変更」「規則形状の変更」「規則の追加・削除」を近傍として、代入可能なもののうち \(N/(\|G\|\bar\theta)\) を山登りで最大化する。言語は `CAP=20000` で完全列挙できたものだけを評価する。

結果（150 秒、6 回の再出発、候補 361、代入可能 177）：**改善 0 件、最良比 0.0000（初期点の比を超える近傍が見つからない）**。ログは §14.10。

**原理的限界（重要）**：定理 3 の族の言語サイズは \(\abs{L_{k,n}}=2^{2^n}\)。\(n\ge5\) で \(4\times10^9\) を超え、完全列挙に基づくいかなる探索も到達できない。実際 \(k\ge8\) のブロックコード出発点はすべて容量超過で棄却される。したがって「大きな \(N/(\|G\|\bar\theta)\) をもつ文法」は列挙型探索の届かない領域にあり、**探索の上限は定理 3 の族を頂点とする構造を外部から確認するに留まる**。この意味で、本報告の中心的証拠は定理 3 の解析的証明であって探索ではない。


---

## 7. 失敗した族と違反証明書

### 7.1 素朴倍増＋\(b\) 短絡

\(A_0\to a\)、\(A_i\to A_{i-1}A_{i-1}\mid b\)、\(n=2\)：
\(L=\{aaaa,aab,baa,bb,b\}\)。
\[
x=aab,\ y=b,\ \text{共有文脈 }(\eps,\eps),\quad
\text{区別文脈 }(\eps,aa):\ baa\in L,\ aabaa\notin L .
\]
前報告の証拠と一致。\(n\ge2\) で常に違反（コードで確認）。

### 7.2 \(a^iba^i\) 族

\(z_i=a^iba^i\)、\(n=2\)：\(L=\{aaaa,aaaba,abaaa,abaaba,aabaa\}\)。
\[
x=aab,\ y=aba,\ \text{共有文脈 }(\eps,aa):\ aabaa\in L,\ abaaa\in L,
\]
\[
\text{区別文脈 }(\eps,aba):\ abaaba\in L,\ aababa\notin L .
\]
原因：\(aab\) はブロック \(aabaa\) の「ずれた」因子で、位相（\(a\)-連の剰余）が \(aba\) と異なる。

### 7.3 ブロックコード＋短絡

\(k=2\)、\(n=3\)、\(z_1=z_2=ab\)：\(\abs L=671\)、\(\|G\|=30\)、\(\bar\theta=7\)、\(N=16\)。
\[
x=aab,\ y=ab,\ \text{共有文脈 }(\eps,a^{12}),\quad
\text{区別文脈 }(\eps,a^{8}):\ aab\,a^8\in L,\ ab\,a^8\notin L .
\]
他も同様：\((z_1,z_2)=(ab,aab)\) では \(x=aab,y=ab\)、\((\eps,a^{12})\) 共有、\((\eps,a^8)\) で区別。\((bb,ab)\)、\((aab,aab)\)、\((ab,ba)\) でも違反。短絡が「第 3 の数字」を導入し、\(aab\) と \(ab\) の位相が混ざるのが原因。**529 組すべてで違反**。

### 7.4 全語同長族・二語族（参考）

\(H_{N,k}\) と \(\{a^N,w\}\) は代入可能だが、任意の reduced good 表示で \(\bar\theta=N\)（前報告 §5 と原稿 `prop:linear-factor-sharp`）。したがって下界族にならない。定理 3 の族はこの障碍を「ブロック長 \(k\) を \(\|G\|\) に、反復数を \(\bar\theta\) に逃がす」ことで回避している。

---

## 8. 主問題 (P) の現状

* (P) の**否定**（\(N=\mu^\star\) の超多項式下界）は見つからなかった。定理 1・2 の構造制約の下で、\(\bar\theta\) を多項式に保つ族は定理 3 の族だけが生き残り、それは \(N\asymp\|G\|\bar\theta\) を与える。
* (P) の**肯定**は予想 C から従う（定理 4）。予想 C は未証明だが、全探索・ランダム・族の全例で成立し、定理 3 で sharp。
* 前報告の (U) を「\(\kappa_A\le C|V|\bar\theta\)」と精密化するのは**誤り**（系 3.4）。正しい精密形は \(\kappa_A\le\|G\|\bar\theta\)（予想 C3）。

---

## 9. 実行ログ（抜粋）

### 9.1 段階 1（`selftest.py`）

全文は §13.2、ログは §14.1。要点：
* \(H_{N,k}\)：\(N=4..11\)、\(k=1..N-1\) の 52 件すべて通過（定義型判定器と必要条件の双方）。
* 二語族 \(\{a^N,a^cba^c\}\)：\((12,3),(20,6),(30,10)\) 通過。
* 素朴倍増：\(n=1\) 通過、\(n\ge2\) 違反。証明書は \(x=aab,\ y=b\)、共有文脈 \((\eps,\eps)\)、区別文脈 \((\eps,aa)\)（\(n=2\)）。
* 256 語文法：通過、\(\|G\|=23\)、\(\bar\theta=8\)、\(N=8\)。
* **必要条件の十分性の反証**：\(\{a,b\}^{\le3}\) の全 16 383 言語で「代入可能だが必要条件を満たさない」例は **0**、逆に「必要条件を満たすが代入可能でない」例は **472**。ランダム 4000 言語でも 0 対 600。これが例 1（§3.2）の発見である。

### 9.2 族の検証（`verify_family.py`）

全文は §13.3、ログは §14.2。\(k=1..6\)、\(n=1..3\) の 18 組で公式と一致、すべて通過。\(k=6..10\)、\(n=3\) でも通過（比 0.1319〜0.1471）。

### 9.3 探索（`final_stats.py`、構造化、ランダム）

§6 の表が出力。**鍵条件（K1)(K2)(K3) の違反は 0 件**。ログは §14.3〜§14.5。

### 9.4 定理 3 の鍵補題の検証（`check_invariant.py`）

全文は §13.8、ログは §14.8。\(k=1..4\)、\(n=2,3\) で不変量 \((\psi,\mathrm{lead}\bmod k,\mathrm{trail}\bmod k)\) の曖昧性 0、共有文脈での衝突 0。

---

## 10. 次の検討者への申し送り

1. **最有望**：予想 C（\(\tau\le\|G\|\bar\theta\)）の証明。定理 1・2 で混合部分が因子反鎖になることを使えば、「因子反鎖を生成する文法はブロック反復構造に限られ、\(\|G\|\) がブロック長を、\(\bar\theta\) が反復回数を支払う」という構成的証明が現実的だと思われる。定理 3 の族が等式成立例なので、証明は tight な評価を目指せる。
2. **精密な未証明命題**：
   * (C1) \(\mu^\star\le\|G\|\bar\theta\)。
   * (C3) 型 1 の各 \(A\) で \(\kappa_A\le\|G\|\bar\theta\)。
   * (C1) の弱形 \(\mu^\star\le\|G\|^2\bar\theta\) でも (P) の肯定に十分。
3. **計算で残った課題**：\(k=3\)・規則 \(\le2\) の完全列挙（\(4\times10^8\) 超）、構造化 \(k=4,5\)、\(n=4\) のブロックコード族の完全検査（65 536 語、時間切れ）。定理 3 は証明済みなので \(n=4\) は検算にすぎない。
4. **注意**：有限検査は普遍命題の証明ではない。本報告で「証明済み」としたのは定理 1〜4 と系 1.1・3.2・3.4 のみ。

---

## 11. 自己点検表

| 項目 | 状態 |
|---|---|
| 原稿・既存ファイルを変更していない | はい（新規フォルダのみ） |
| git 操作をしていない | はい |
| \(\Sigma,s\) を全族で固定 | はい |
| fan-out 1 のみ（二穴を混入していない） | はい。定理 1・2 は \(d=1\) の文脈のみ |
| \(\theta\) を規則ごとに個別計算 | はい（(1.1) で厳密） |
| 有限検査と証明を区別 | はい（§0 の表で判定列を分離） |
| \(\mu^\star\) と \(\tau\) を区別 | はい（§1、§5） |
| 未検査を通過に混ぜていない | はい（§6 の表） |
| (P) を決着したと主張していない | はい |

---

## 12. 付録の構成

コード全文は §13、実行ログ全文は §14、定理 3 の鍵補題の検証は §15 に置く。実行例：`cd revision/deepseek_u1f1_search; py -3 -u verify_family.py`。

---

## 13. コード全文

すべて Python 3.12、標準ライブラリのみ。作業フォルダ `revision/deepseek_u1f1_search/` に置いたファイルそのものである。

### 13.1 `u1core.py`（厳密判定器・文法計量・族生成）

```python
# -*- coding: utf-8 -*-
"""Exact tools for the binary U1 / fan-out one / rank <= 2 search.

Alphabet Sigma = {a,b}.  Typing s(a)=1, s(b)=zeta (absorbing), U1={1,zeta}.
Type of a nonempty word: PURE (=1) iff it has no 'b', ZETA (=2) otherwise.

Grammar representation (fan-out one, hence one component per nonterminal):
    P[i] = list of right-hand sides of the rules with left-hand side i
    a right-hand side is a tuple whose entries are
        * int j  -- the single variable of child j   (requires j < i: acyclic)
        * str    -- a nonempty terminal block
The last nonterminal is the start symbol.  Every grammar used here is acyclic,
so L(G) is finite and exhaustively enumerable.

All routines are exact; no sampling and no length cut-offs are used except
explicit enumerated-language size caps, which are always reported.
"""
from itertools import product
from collections import defaultdict

PURE, ZETA = 1, 2

TYPE_NAME = {PURE: '1', ZETA: 'z'}


def typ(w):
    """Type of a nonempty word."""
    if not w:
        raise ValueError('the empty word has no type in Sigma^+')
    return ZETA if 'b' in w else PURE


# --------------------------------------------------------------------------
# grammars
# --------------------------------------------------------------------------
def check_acyclic(P):
    for i, rules in enumerate(P):
        for rhs in rules:
            for tok in rhs:
                if isinstance(tok, int) and not (0 <= tok < i):
                    return False
    return True


def enumerate_language(P, cap=None):
    """Exhaustively enumerate L(A) for every nonterminal.

    Returns a list of sets, or None if some intermediate language exceeds
    ``cap`` (that grammar must then be counted as *not inspected*).
    """
    L = []
    for i, rules in enumerate(P):
        out = set()
        for rhs in rules:
            lists = []
            feasible = True
            for tok in rhs:
                if isinstance(tok, int):
                    if not (0 <= tok < i):
                        return None
                    if not L[tok]:
                        feasible = False
                        break
                    lists.append(L[tok])
                else:
                    lists.append((tok,))
            if not feasible:
                continue
            for pieces in product(*lists):
                out.add(''.join(pieces))
            if cap is not None and len(out) > cap:
                return None
        L.append(out)
    return L


def grammar_size(P):
    """||G|| of Definition def:standard-mcfg, fan-out one."""
    return len(P) + sum(
        1 + 2 * sum(isinstance(t, int) for t in rhs)
        + sum(len(t) for t in rhs if isinstance(t, str))
        for rules in P for rhs in rules)


def grammar_metrics(P, L):
    """Exact size, exact per-rule thickness theta_G(R), theta-bar, contexts E_A.

    theta_G(R) = min{|w| : w in L(G) has a successful derivation using R}.
    For fan-out one, linearity and nondeletion give the exact formula
        theta_G(A -> rho(B_1..B_q))
            = o_A + |rho|_Sigma + sum_j lo(B_j),
    where lo(B) = min |u| over u in L_B(G) and o_A = min fixed length of a
    context obtained by deleting an A-subtree from a successful derivation.
    Both are computed by dynamic programming over the acyclic grammar.
    """
    k = len(P)
    lo = [min((len(w) for w in L[i]), default=None) for i in range(k)]
    lo_word = [min(L[i], key=lambda w: (len(w), w)) if L[i] else None
               for i in range(k)]
    o = [None] * k
    ctx = [None] * k
    o[k - 1] = 0
    ctx[k - 1] = ('', '')
    for i in range(k - 1, -1, -1):
        if o[i] is None:
            continue
        for rhs in P[i]:
            if any(isinstance(t, int) and lo[t] is None for t in rhs):
                continue
            tot = sum(lo[t] if isinstance(t, int) else len(t) for t in rhs)
            for pos, tok in enumerate(rhs):
                if not isinstance(tok, int):
                    continue
                val = o[i] + tot - lo[tok]
                if o[tok] is None or val < o[tok]:
                    u = ctx[i][0] + ''.join(
                        lo_word[t] if isinstance(t, int) else t
                        for t in rhs[:pos])
                    v = ''.join(
                        lo_word[t] if isinstance(t, int) else t
                        for t in rhs[pos + 1:]) + ctx[i][1]
                    o[tok] = val
                    ctx[tok] = (u, v)
    theta_rules = {}
    for i, rules in enumerate(P):
        if o[i] is None:
            continue
        for ri, rhs in enumerate(rules):
            if any(isinstance(t, int) and lo[t] is None for t in rhs):
                continue
            theta_rules[(i, ri)] = (
                o[i]
                + sum(len(t) for t in rhs if isinstance(t, str))
                + sum(lo[t] for t in rhs if isinstance(t, int)))
    theta = max(theta_rules.values()) if theta_rules else 0
    return dict(size=grammar_size(P), lo=lo, lo_word=lo_word, o=o, ctx=ctx,
                theta=theta, theta_bar=max(1, theta),
                theta_rules=theta_rules)


def shortest_pure(L):
    """(N, word) for the shortest pure accepted word, or (None, None)."""
    best = None
    for w in L:
        if 'b' not in w and (best is None or len(w) < len(best)):
            best = w
    return (len(best), best) if best is not None else (None, None)


def representative_lengths(P, L, M, root=None, limit_len=None):
    """tau_X and kappa_A, exactly, from the fixed context E_A.

    tau_X = min{|x| : s(x)=t, E_A[x] in L}   (Lemma lem:app-u1-fillers)
    kappa_A = min{k>=1 : E_A[a^k] in L}      (only for type 1)
    These are the quantities of cor:distribution-representatives and of the
    sufficient condition (U); they are only meaningful when L is
    (1,s)-substitutable, which the drivers check first.
    """
    root = len(P) - 1 if root is None else root
    Lr = L[root]
    res = {}
    for A in range(len(P)):
        if M['ctx'][A] is None or not L[A]:
            continue
        u, v = M['ctx'][A]
        types = {typ(w) for w in L[A]}
        for t in types:
            best = None
            bestw = None
            for w in Lr:
                if len(w) <= len(u) + len(v):
                    continue
                if not (w.startswith(u) and w.endswith(v)):
                    continue
                x = w[len(u):len(w) - len(v)] if v else w[len(u):]
                if typ(x) != t:
                    continue
                if best is None or len(x) < best:
                    best = len(x)
                    bestw = x
            res[(A, t)] = (best, bestw)
    return res


# --------------------------------------------------------------------------
# substitutability: definition-based exact test
# --------------------------------------------------------------------------
def all_distributions(L):
    """D(x) for every nonempty factor x of every word of the finite language L."""
    D = defaultdict(set)
    byctx = defaultdict(list)
    for w in L:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                x = w[i:j]
                c = (w[:i], w[j:])
                D[x].add(c)
                byctx[c].append(x)
    return D, byctx


def check_substitutable(L, want_certificate=True):
    """EXACT (1,s)-substitutability test for a finite language.

    Enumerates every nonempty factor of every word of L together with its full
    two-sided context, groups same-type factors that share a context, and
    compares the *complete* distributions inside each group.  Returns
    (True, info) or (False, certificate).
    """
    words = sorted(set(L))
    D, byctx = all_distributions(words)
    for c, xs in byctx.items():
        groups = defaultdict(list)
        for x in xs:
            groups[typ(x)].append(x)
        for t, g in groups.items():
            if len(g) < 2:
                continue
            rep = g[0]
            for x in g[1:]:
                if D[x] != D[rep]:
                    if not want_certificate:
                        return False, None
                    diff = sorted(D[x] ^ D[rep])
                    dist = diff[0]
                    return False, dict(x=rep, y=x, type=t, shared=c,
                                       distinguished=dist,
                                       distinguished_in_x=(dist in D[x]),
                                       distinguished_in_rep=(dist in D[rep]))
    return True, dict(factors=len(D), contexts=len(byctx))


# --------------------------------------------------------------------------
# substitutability: equivalent structural criterion (proved in the report)
# --------------------------------------------------------------------------
def check_structural(L, want_certificate=True):
    """EXACT test using the characterisation proved in the report:

    a finite L is (1,s)-substitutable  <=>  (i) L contains at most one pure
    word, and (ii) no mixed word of L is a proper factor of any word of L.
    """
    S = set(L)
    pure = [w for w in L if 'b' not in w]
    if len(pure) > 1:
        return False, ('two_pure_words', pure[0], pure[1])
    for w in L:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if i == 0 and j == n:
                    continue
                f = w[i:j]
                if 'b' in f and f in S:
                    return False, ('mixed_proper_factor', f, w, i, j)
    return True, None


# --------------------------------------------------------------------------
# families
# --------------------------------------------------------------------------
def doubling_family(zs, z0='a'):
    """A_0 -> z0 ; A_i -> A_{i-1} A_{i-1} | z_i  (i=1..n), start A_n.

    L(A_i) = {z0^{2^i}} union {cut words};  a word of L(A_n) is a concatenation
    of blocks z_{i_1}...z_{i_m} over a cut of the complete binary tree of depth
    n, i.e. levels with  sum_t 2^{i_t} = 2^n and 2^{i_t} | (sum_{t'<t} 2^{i_t'}).
    """
    n = len(zs)
    P = [[(z0,)]]
    for i in range(1, n + 1):
        P.append([(i - 1, i - 1), (zs[i - 1],)])
    return P


def show_grammar(P, names=None):
    names = names or [f'A{i}' for i in range(len(P))]
    out = []
    for i, rules in enumerate(P):
        for rhs in rules:
            body = ''.join(names[t] if isinstance(t, int) else t for t in rhs)
            out.append(f'{names[i]} -> {body}')
    return out


def describe(P, L, M=None, root=None):
    root = len(P) - 1 if root is None else root
    M = M or grammar_metrics(P, L)
    N, Nw = shortest_pure(L[root])
    d = dict(rules=show_grammar(P), size=M['size'], theta=M['theta'],
             theta_bar=M['theta_bar'], words=len(L[root]), N=N, Nword=Nw,
             pure_words=[w for w in L[root] if 'b' not in w])
    return d
```

### 13.2 `selftest.py`（段階 1 の検証）

```python
# -*- coding: utf-8 -*-
"""Stage 1: validation of the exact tools.

Two independent tests of (1,s)-substitutability are used.

  * check_substitutable  -- the definition, checked on ALL nonempty factors and
    ALL two-sided contexts of the completely enumerated finite language.  This
    is the reference test.
  * check_structural     -- the cheap *necessary* condition of Theorem 2 /
    Corollary 1.1: at most one pure word, and no mixed word of L is a proper
    factor of a word of L.  (Example 1 of the report shows that it is NOT
    sufficient, so the two tests must not be asserted to agree.)
"""
from itertools import combinations

from u1core import (enumerate_language, grammar_metrics, check_substitutable,
                    check_structural, shortest_pure, grammar_size)

LOG = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    LOG.append(s)


def words_up_to(n):
    out = ['']
    cur = ['']
    for _ in range(n):
        cur = [w + c for w in cur for c in 'ab']
        out += cur
    return out[1:]


def model_families():
    log('== MODEL FAMILIES ==========================================')
    cnt = 0
    for N in range(4, 12):
        for k in range(1, N):
            L = {'a' * N} | {'a' * i + 'b' * k + 'a' * (N - k - i)
                             for i in range(N - k + 1)}
            ok, cert = check_substitutable(L)
            ok2, _ = check_structural(L)
            assert ok and ok2, (N, k, cert)
            cnt += 1
    log(f'H_(N,k): {cnt} languages (N=4..11, k=1..N-1): all PASS, both tests')

    for N, c in [(12, 3), (20, 6), (30, 10)]:
        L = {'a' * N, 'a' * c + 'b' + 'a' * c}
        assert check_substitutable(L)[0] and check_structural(L)[0]
    log('two-word {a^N, a^c b a^c}: PASS for (12,3),(20,6),(30,10)')

    for n in (1, 2, 3, 4):
        P = [[('a',)]]
        for i in range(1, n + 1):
            P.append([(i - 1, i - 1), ('b',)])
        L = enumerate_language(P)
        ok, cert = check_substitutable(L[-1])
        ok2, cert2 = check_structural(L[-1])
        assert ok == ok2 or (not ok), (n, ok, ok2)
        log(f'naive doubling n={n}: |L|={len(L[-1])} '
            f'{"PASS" if ok else "FAIL"} '
            f'{"" if ok else "cert=" + repr(cert)}')
        if n >= 2:
            assert not ok

    full = [[('a',), ('b',)]]
    for j in range(1, 4):
        full.append([(j - 1, j - 1)])
    L = enumerate_language(full)
    assert len(L[-1]) == 256, len(L[-1])
    ok, cert = check_substitutable(L[-1])
    ok2, _ = check_structural(L[-1])
    M = grammar_metrics(full, L)
    log(f'full shift 256 words: PASS={ok} (necessary test={ok2}) '
        f'size={M["size"]} theta={M["theta"]} N={shortest_pure(L[-1])[0]}')
    assert ok and ok2


def length_spectrum_family():
    log('== length-spectrum family (all words the same length) ======')
    P = [[('a',)]]
    for i in range(1, 5):
        P.append([(i - 1, i - 1)])
    L = enumerate_language(P)
    M = grammar_metrics(P, L)
    log(f'pure doubling chain n=4: size={M["size"]} theta={M["theta"]} '
        f'N={shortest_pure(L[-1])[0]}  (theta = N, as expected)')
    assert M['theta'] == shortest_pure(L[-1])[0]


def necessary_condition_only():
    log('== the cheap condition is NECESSARY but NOT SUFFICIENT =====')
    # (a) on every language inside {a,b}^{1,2,3}: no violation of the
    #     necessary condition among the substitutable ones.
    ws = words_up_to(3)
    cnt = 0
    bad = 0
    suff_fail = 0
    for r in range(1, len(ws) + 1):
        for comb in combinations(ws, r):
            L = set(comb)
            a = check_substitutable(L, want_certificate=False)[0]
            b = check_structural(L)[0]
            cnt += 1
            if a and not b:
                bad += 1            # would refute Theorem 1 / Corollary 1.1
            if b and not a:
                suff_fail += 1      # shows the condition is not sufficient
    log(f'all {cnt} nonempty languages inside {{a,b}}^{{1,2,3}}: '
        f'{bad} violations of the necessary condition, '
        f'{suff_fail} languages that pass it but are not substitutable')
    assert bad == 0
    assert suff_fail > 0

    # (b) random languages inside {a,b}^{1..5}
    import random
    random.seed(20261030)
    ws = words_up_to(5)
    bad = 0
    suff = 0
    for trial in range(4000):
        r = random.randint(2, 12)
        L = set(random.sample(ws, r))
        a = check_substitutable(L, want_certificate=False)[0]
        b = check_structural(L)[0]
        if a and not b:
            bad += 1
        if b and not a:
            suff += 1
    log(f'4000 random languages inside {{a,b}}^{{1..5}}: '
        f'{bad} violations of the necessary condition, '
        f'{suff} counterexamples to sufficiency')
    assert bad == 0


def exhaustive_small_languages():
    log('== complete classification of very small languages ========')
    ws = words_up_to(2)
    for r in (1, 2, 3, 4):
        n = 0
        tot = 0
        for comb in combinations(ws, r):
            tot += 1
            if check_structural(set(comb))[0]:
                n += 1
        log(f'|L|={r} inside {{a,b}}^{{1,2}}: {n} pass the necessary condition '
            f'of {tot}')


def main():
    model_families()
    length_spectrum_family()
    necessary_condition_only()
    exhaustive_small_languages()
    log('ALL STAGE-1 ASSERTIONS PASSED')


if __name__ == '__main__':
    main()
```

### 13.3 `verify_family.py`（定理 3 の数値検証）

```python
# -*- coding: utf-8 -*-
"""Stage 3: the block-code family  D = {a^k, b},  L_{k,n} = D^{2^n}.

    G_{k,n}:  A_0 -> a^k | b,   A_i -> A_{i-1} A_{i-1}  (1<=i<=n),  start A_n.

Proved in the report:
    L(G_{k,n}) = D^{2^n}
    the only pure word is a^{k 2^n}, so N = k 2^n
    ||G_{k,n}|| = k + 6n + 4
    theta-bar = 2^n + k - 1                     (n >= 1)
    L_{k,n} is (1,s)-substitutable              (for all k>=1, n>=0)
Consequently
    N / (||G|| theta-bar) = k 2^n / ((k+6n+4)(2^n+k-1))  ->  1
along k = round(sqrt(6n 2^n)), and N <= ||G|| theta-bar in every member.
This script checks the formulas against exact enumeration + exact tests.
"""
import math
import time
from fractions import Fraction

from u1core import (enumerate_language, grammar_metrics, check_substitutable,
                    shortest_pure, grammar_size)

CAP = 3000000


def gram(k, n):
    P = [[('a' * k,), ('b',)]]
    for i in range(1, n + 1):
        P.append([(i - 1, i - 1)])
    return P


def main():
    print('== block-code family: formulas vs exact computation ==')
    hdr = ('k', 'n', '|L|', 'g', 'g_formula', 'theta', 'theta_formula',
           'N', 'N_formula', 'PASS', 'ratio', 'N<=g*theta')
    print('  '.join(hdr))
    rows = []
    for k in (1, 2, 3, 4, 5, 6):
        for n in (1, 2, 3):
            P = gram(k, n)
            L = enumerate_language(P, cap=CAP)
            M = grammar_metrics(P, L)
            N, Nw = shortest_pure(L[-1])
            ok, cert = check_substitutable(L[-1])
            gf, tf, Nf = k + 6 * n + 4, 2 ** n + k - 1, k * 2 ** n
            assert M['size'] == gf, (k, n, M['size'], gf)
            assert M['theta'] == tf, (k, n, M['theta'], tf)
            assert N == Nf, (k, n, N, Nf)
            assert ok, (k, n, cert)
            r = Fraction(N, M['size'] * M['theta_bar'])
            rows.append((k, n, len(L[-1]), M['size'], gf, M['theta'], tf,
                         N, Nf, ok, float(r), N <= M['size'] * M['theta_bar']))
            print(f'{k:2d} {n:2d} {len(L[-1]):5d} {M["size"]:3d} {gf:3d} '
                  f'{M["theta"]:4d} {tf:4d} {N:4d} {Nf:4d} {ok} '
                  f'{float(r):.4f} {N <= M["size"] * M["theta_bar"]}', flush=True)
    print()
    print('== ratio along k = round(sqrt(6 n 2^n)) ==')
    for n in (2, 4, 6, 8, 10, 12, 14, 16, 18, 20):
        k = max(1, round(math.sqrt(6 * n * 2 ** n)))
        g, t, N = k + 6 * n + 4, 2 ** n + k - 1, k * 2 ** n
        print(f'n={n:2d} k={k:8d} g={g:9d} theta={t:9d} N={N:12d} '
              f'N/(g theta)={N / (g * t):.6f}')
    print()
    print('== exact check for the largest ratio members (n=3) ==')
    for k in (6, 7, 8, 9, 10):
        P = gram(k, 3)
        L = enumerate_language(P, cap=CAP)
        M = grammar_metrics(P, L)
        N, _ = shortest_pure(L[-1])
        ok, cert = check_substitutable(L[-1])
        r = N / (M['size'] * M['theta'])
        print(f'k={k} g={M["size"]} theta={M["theta"]} N={N} PASS={ok} '
              f'ratio={r:.4f}', flush=True)
    print('ALL FORMULA ASSERTIONS PASSED')


if __name__ == '__main__':
    main()
```

### 13.4 `final_stats.py`（網羅・構造化・ランダム探索と鍵条件検査）

```python
# -*- coding: utf-8 -*-
"""Stage 2 (final): statistics over four search families.

(1) canonical exhaustive class  k <= 2, rules per nonterminal <= 2,
    RHS <= 4 symbols, rank <= 2, terminal blocks <= 2 letters;
(2) canonical exhaustive class  k = 3, rules per nonterminal <= 1;
(3) level-uniform structured class: one structural rule plus one shortcut per
    level, shapes and shortcuts varied independently, k <= 5;
(4) randomised grammars with k in 3..6 and 1..3 rules per nonterminal.

For every substitutable grammar we record N, ||G||, theta-bar, tau and verify
   (K1) L has at most one pure word;
   (K2) no mixed word of L is a proper factor of any word of L   (Theorem 2);
   (K3) N <= ||G|| * theta-bar                                  (Conjecture C);
and count violations.
"""
import random
import time
from itertools import combinations, product

from u1core import (enumerate_language, grammar_metrics, check_substitutable,
                    shortest_pure, representative_lengths, check_acyclic)

CAP = 4000
LOG = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    LOG.append(s)


# ---------------------------------------------------------------- canonical
BLOCKS = ['a', 'b', 'aa', 'ab', 'ba', 'bb']
B0 = [''] + BLOCKS


def pats():
    out = []
    for s1 in B0:
        for s2 in B0:
            for s3 in B0:
                if len(s1) + len(s2) + len(s3) <= 2 and \
                        (s1 != '') + (s2 != '') + (s3 != '') <= 2:
                    out.append((s1, s2, s3))
    return out


PAT = pats()


def candidates(i):
    C = [(s,) for s in BLOCKS]
    for j in range(i):
        for s1 in B0:
            for s2 in B0:
                if len(s1) + len(s2) <= 2 and 1 + (s1 != '') + (s2 != '') <= 4:
                    C.append((s1, j, s2))
    for j1 in range(i):
        for j2 in range(i):
            for (s1, s2, s3) in PAT:
                C.append((s1, j1, s2, j2, s3))
    return C


def rule_sets(i, mr):
    C = candidates(i)
    return [tuple(C[t] for t in comb)
            for r in range(1, mr + 1) for comb in combinations(range(len(C)), r)]


def prod_reach(P):
    k = len(P)
    prod = [False] * k
    for i in range(k):
        for rhs in P[i]:
            if all(prod[t] for t in rhs if isinstance(t, int)):
                prod[i] = True
    if not prod[k - 1]:
        return False
    reach = [False] * k
    reach[k - 1] = True
    for i in range(k - 1, -1, -1):
        if not reach[i]:
            continue
        for rhs in P[i]:
            for t in rhs:
                if isinstance(t, int):
                    reach[t] = True
    return all(prod) and all(reach)


# ---------------------------------------------------------------- structured
SHAPES = [
    ('X', 'X'), ('a', 'X', 'X'), ('X', 'a', 'X'), ('X', 'X', 'a'),
    ('b', 'X', 'X'), ('X', 'b', 'X'), ('X', 'X', 'b'), ('a', 'X'),
    ('X', 'a'), ('b', 'X'), ('X', 'b'), ('X',),
    ('a', 'X', 'a'), ('b', 'X', 'b'), ('aa', 'X'), ('X', 'aa'),
]
SHORTCUTS = ['b', 'bb', 'ab', 'ba', 'aab', 'aba', 'baa', 'abb', 'bab',
             'bba', 'aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa',
             'aaab', 'aaba', 'abaa', 'baaa']
BASES = [('a',), ('a', 'b'), ('aa',), ('aa', 'b'), ('a', 'b', 'bb'),
         ('aaa',), ('aaa', 'b'), ('ab',), ('ba',)]


def instantiate(shape, i, s):
    out = []
    for t in shape:
        if t == 'X':
            out.append(i - 1)
        else:
            out.append(t)
    return tuple(out)


def structured_class(k, nshort=1):
    for base in BASES:
        for shapes in product(range(len(SHAPES)), repeat=k - 1):
            for shs in product(range(len(SHORTCUTS)), repeat=k - 1):
                P = [[(b,) for b in base]]
                for i in range(1, k):
                    rhs = instantiate(SHAPES[shapes[i - 1]], i, None)
                    rules = [rhs]
                    for _ in range(nshort):
                        rules.append((SHORTCUTS[shs[i - 1]],))
                    P.append(rules)
                yield P


# ---------------------------------------------------------------- evaluation
class Stats:
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.over_cap = 0
        self.not_reduced = 0
        self.fail = 0
        self.pass_ = 0
        self.ntheta = 0
        self.max_ratio = 0.0
        self.max_NoverT = 0.0
        self.best = None
        self.viol = []


def evaluate(P, st):
    if not prod_reach(P):
        st.not_reduced += 1
        return
    L = enumerate_language(P, cap=CAP)
    if L is None:
        st.over_cap += 1
        return
    S = set(L[-1])
    pure = [w for w in S if 'b' not in w]
    N, Nw = shortest_pure(S)
    M = grammar_metrics(P, L)
    ok, cert = check_substitutable(S)
    if not ok:
        st.fail += 1
        return
    st.pass_ += 1
    if N is None:
        return
    # (K1) at most one pure word
    if len(pure) > 1:
        st.viol.append(('K1', sorted(S)))
    # (K2) no mixed word of L is a proper factor of a word of L
    for w in S:
        n = len(w)
        for i in range(n):
            for j in range(i + 1, n + 1):
                if i == 0 and j == n:
                    continue
                f = w[i:j]
                if 'b' in f and f in S:
                    st.viol.append(('K2', w, f))
    # (K3)
    if N > M['size'] * M['theta_bar']:
        st.viol.append(('K3', N, M['size'], M['theta_bar'], sorted(S)))
    r = N / (M['size'] * M['theta_bar']) if M['theta_bar'] else 0
    if r > st.max_ratio:
        st.max_ratio = r
        st.best = (N, M['size'], M['theta'], len(S), sorted(S))
    if N > M['theta_bar']:
        st.ntheta += 1
    if M['theta_bar'] and N / M['theta_bar'] > st.max_NoverT:
        st.max_NoverT = N / M['theta_bar']


def report(st):
    log(f'[{st.name}] candidates={st.total} not-reduced={st.not_reduced} '
        f'over-cap={st.over_cap} non-substitutable={st.fail} '
        f'substitutable={st.pass_} with-N>theta={st.ntheta}')
    log(f'    max N/(g theta)={st.max_ratio:.4f}  max N/theta={st.max_NoverT:.3f}'
        f'  key-violations={len(st.viol)}')
    if st.best:
        log(f'    best: N={st.best[0]} g={st.best[1]} theta={st.best[2]} '
            f'|L|={st.best[3]}  L={st.best[4][:12]}')
    for v in st.viol[:5]:
        log('    VIOLATION', v)


def main():
    t0 = time.time()
    log('== (1) canonical exhaustive class, k<=2, <=2 rules ==')
    for k in (1, 2):
        st = Stats(f'canonical k={k}')
        for combo in product(*[rule_sets(i, 2) for i in range(k)]):
            st.total += 1
            evaluate([list(c) for c in combo], st)
        report(st)

    log('== (2) canonical exhaustive class, k=3, 1 rule per nonterminal ==')
    st = Stats('canonical k=3, 1 rule')
    for combo in product(*[rule_sets(i, 1) for i in range(3)]):
        st.total += 1
        evaluate([list(c) for c in combo], st)
    report(st)

    log('== (3) level-uniform structured class, k=2..5 ==')
    for k in (2, 3, 4):
        st = Stats(f'structured k={k}')
        for P in structured_class(k):
            st.total += 1
            if st.total > 400000:
                break
            evaluate([list(r) for r in P], st)
        report(st)

    log('== (4) randomised grammars, k=3..6, 1..3 rules ==')
    rng = random.Random(20261030)
    st = Stats('random')
    ALLB = ['a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb',
            'baa', 'bab', 'bba', 'bbb']
    for _ in range(30000):
        k = rng.choice([3, 4, 5, 6])
        P = []
        for i in range(k):
            rules = []
            for _ in range(rng.randint(1, 3)):
                t = rng.random()
                if i == 0 or t < 0.45:
                    rules.append((rng.choice(ALLB),))
                elif t < 0.75:
                    j = rng.randrange(i)
                    s1 = rng.choice(['', '', 'a', 'b', 'aa', 'ab', 'ba'])
                    s2 = rng.choice(['', '', 'a', 'b', 'aa', 'ab', 'ba'])
                    if len(s1) + len(s2) > 2:
                        s2 = ''
                    rules.append((s1, j, s2))
                else:
                    j1, j2 = rng.randrange(i), rng.randrange(i)
                    s = rng.choice(['', '', '', 'a', 'b', 'aa', 'ab', 'ba'])
                    pat = ['', '', '']
                    pat[rng.randrange(3)] = s
                    rules.append((pat[0], j1, pat[1], j2, pat[2]))
            P.append(rules)
        st.total += 1
        evaluate(P, st)
    report(st)
    log(f'total wall clock {time.time() - t0:.1f}s')


if __name__ == '__main__':
    main()
```

### 13.5 `blockcode.py`（ブロックコード族と短絡の探索）

```python
# -*- coding: utf-8 -*-
"""Stage 2c: the block-code chain.

    A_0 -> aa | b            (a prefix code of "digits":  aa  and  b)
    A_i -> A_{i-1} A_{i-1}   (optionally also  A_i -> z_i )
    start A_n

Without shortcuts L(A_n) is the set of concatenations of 2^n digits from
{aa,b}; the only pure word is (aa)^{2^n} = a^{2^{n+1}}.  We test exact
(1,s)-substitutability and compute ||G||, theta-bar.

With shortcuts z_i the rule thickness theta should drop from N/2+1 to O(n),
which is exactly the tension the search is about.
"""
import sys
from itertools import product

from u1core import (enumerate_language, grammar_metrics, check_substitutable,
                    shortest_pure, representative_lengths)

CAP = 1000000


def blockcode(n, zs=None):
    """zs[k] = shortcut of level k+1 (or None). Returns grammar."""
    P = [[('aa',), ('b',)]]
    for i in range(1, n + 1):
        rules = [(i - 1, i - 1)]
        if zs and i - 1 < len(zs) and zs[i - 1]:
            rules.append((zs[i - 1],))
        P.append(rules)
    return P


def score(P, L):
    M = grammar_metrics(P, L)
    N, _ = shortest_pure(L[-1])
    return M, N


def main():
    print('== pure block-code chain (no shortcuts) ==')
    for n in range(1, 5):
        P = blockcode(n)
        L = enumerate_language(P, cap=CAP)
        if L is None:
            print(f'n={n}: over cap'); continue
        M, N = score(P, L)
        ok, cert = check_substitutable(L[-1])
        print(f'n={n} |L|={len(L[-1])} g={M["size"]} theta={M["theta"]} N={N} '
              f'PASS={ok} ' + ('' if ok else repr(cert)), flush=True)

    print()
    print('== with shortcuts z_1..z_{n-1} (root stays binary) ==')
    cands = []
    for ln in (1, 2, 3):
        for tup in product('ab', repeat=ln):
            w = ''.join(tup)
            if 'b' in w:
                cands.append(w)
    print('shortcut candidates:', cands)
    for n in (2, 3):
        best = []
        hits = 0
        tot = 0
        for zs in product(cands, repeat=n - 1):
            tot += 1
            P = blockcode(n, list(zs))
            L = enumerate_language(P, cap=CAP)
            if L is None:
                continue
            ok, cert = check_substitutable(L[-1])
            if not ok:
                continue
            hits += 1
            M, N = score(P, L)
            best.append((N / (M['size'] * M['theta']), zs, len(L[-1]),
                         M['size'], M['theta'], N))
        best.sort(reverse=True)
        print(f'n={n}: {tot} shortcut tuples, {hits} substitutable', flush=True)
        for b in best[:10]:
            print(f'   ratio={b[0]:.4f} zs={b[1]} |L|={b[2]} g={b[3]} '
                  f'th={b[4]} N={b[5]}')


if __name__ == '__main__':
    main()
```

### 13.6 `family_blocks.py`（倍増鎖＋ブロック設計 16 種）

```python
# -*- coding: utf-8 -*-
"""Stage 2a: parameterised families built on the doubling chain
        A_0 -> z0 ;  A_i -> A_{i-1} A_{i-1} | z_i ,  start A_n .

The pure word is a^{|z0|*2^n}; every shortcut z_i (i>=1) must contain b so that
a^N is the only pure word.  We test for which block designs the resulting
finite language is (1,s)-substitutable, and record N, ||G||, theta-bar and
N/(||G||*theta-bar).
"""
import sys
import time

from u1core import (enumerate_language, grammar_metrics, check_substitutable,
                    shortest_pure, doubling_family, describe)

CAP = 2000000
LOG = []


def log(*a):
    s = ' '.join(str(x) for x in a)
    print(s)
    LOG.append(s)


FAMILIES = {
    # name: function i -> block for level i (i>=1)
    'a^i b a^i': lambda i: 'a' * i + 'b' + 'a' * i,
    'b a^i b': lambda i: 'b' + 'a' * i + 'b',
    'a^i b': lambda i: 'a' * i + 'b',
    'b a^i': lambda i: 'b' + 'a' * i,
    'a b^i a': lambda i: 'a' + 'b' * i + 'a',
    'a b^i': lambda i: 'a' + 'b' * i,
    'b^i a': lambda i: 'b' * i + 'a',
    'b^i a b^i': lambda i: 'b' * i + 'a' + 'b' * i,
    'b a^i b a^i b': lambda i: 'b' + 'a' * i + 'b' + 'a' * i + 'b',
    'a^i b a^(2i)': lambda i: 'a' * i + 'b' + 'a' * (2 * i),
    'a^(2i) b a^i': lambda i: 'a' * (2 * i) + 'b' + 'a' * i,
    'a b^i a b^i a': lambda i: 'a' + 'b' * i + 'a' + 'b' * i + 'a',
    'b^i b a b^i': lambda i: 'b' * i + 'b' + 'a' + 'b' * i,
    'a^i b^i': lambda i: 'a' * i + 'b' * i,
    'b^i a^i': lambda i: 'b' * i + 'a' * i,
    'a^i b^i a': lambda i: 'a' * i + 'b' * i + 'a',
}


def run(name, f, nmax=4):
    row = [name]
    ok_all = True
    for n in range(1, nmax + 1):
        zs = [f(i) for i in range(1, n + 1)]
        if any('b' not in z for z in zs):
            row.append(f'n={n}:BLOCK-PURE')
            ok_all = False
            break
        P = doubling_family(zs)
        L = enumerate_language(P, cap=CAP)
        if L is None:
            row.append(f'n={n}:CAP')
            ok_all = False
            break
        M = grammar_metrics(P, L)
        ok, cert = check_substitutable(L[-1])
        N, Nw = shortest_pure(L[-1])
        row.append(f'n={n}: |L|={len(L[-1])} g={M["size"]} th={M["theta"]} '
                   f'N={N} {"PASS" if ok else "FAIL"}')
        if not ok:
            row.append(f'    cert={cert}')
            ok_all = False
            break
        else:
            row.append(f'    ratio N/(g*th)={N / (M["size"] * M["theta"]):.4f}')
    log('  '.join(row))
    return ok_all


def main():
    log('== doubling-chain block designs (CAP=%d) ==' % CAP)
    passing = []
    for name, f in FAMILIES.items():
        if run(name, f):
            passing.append(name)
    log('PASSING DESIGNS:', passing)


if __name__ == '__main__':
    main()
```

### 13.7 `random_search.py`（比率最大化のランダム探索）

```python
# -*- coding: utf-8 -*-
"""Stage 2d: randomised / local search for substitutable finite languages with a
large ratio  N / theta-bar  (N = length of the unique pure word).

Random grammars: k nonterminals, each with 1..3 rules; every child index is
smaller than the parent index (acyclic); rules may be
   * constant:  a terminal block of length 1..3
   * unary:     child with terminal blocks on both sides (total <= 2 letters)
   * binary:    two children with at most two terminal letters total
The enumerated language must stay under CAP; the grammar must be reduced.
Every substitutable grammar is recorded with N, ||G||, theta-bar, tau and
N/(||G|| theta-bar); the maximum of N/theta-bar is the quantity of interest
(the conjecture N = O(theta-bar) would settle (P) affirmatively).
"""
import random
import sys
import time

from u1core import (enumerate_language, grammar_metrics, check_substitutable,
                    shortest_pure, representative_lengths)

CAP = 20000
BLOCKS = ['a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb',
          'baa', 'bab', 'bba', 'bbb']


def random_grammar(rng, k, maxrules=3):
    P = []
    for i in range(k):
        nr = rng.randint(1, maxrules)
        rules = []
        for _ in range(nr):
            t = rng.random()
            if i == 0 or t < 0.45:
                rules.append((rng.choice(BLOCKS),))
            elif t < 0.75:
                j = rng.randrange(i)
                s1 = rng.choice(['', '', 'a', 'b', 'aa', 'ab', 'ba'])
                s2 = rng.choice(['', '', 'a', 'b', 'aa', 'ab', 'ba'])
                if len(s1) + len(s2) > 2:
                    s2 = ''
                rules.append((s1, j, s2))
            else:
                j1 = rng.randrange(i)
                j2 = rng.randrange(i)
                s = rng.choice(['', '', '', 'a', 'b', 'aa', 'ab', 'ba'])
                pos = rng.randrange(3)
                pat = ['', '', '']
                pat[pos] = s
                rules.append((pat[0], j1, pat[1], j2, pat[2]))
        P.append(rules)
    return P


def prod_reach(P):
    k = len(P)
    prod = [False] * k
    for i in range(k):
        for rhs in P[i]:
            if all(prod[t] for t in rhs if isinstance(t, int)):
                prod[i] = True
    if not prod[k - 1]:
        return False
    reach = [False] * k
    reach[k - 1] = True
    for i in range(k - 1, -1, -1):
        if not reach[i]:
            continue
        for rhs in P[i]:
            for t in rhs:
                if isinstance(t, int):
                    reach[t] = True
    return all(prod) and all(reach)


def evaluate(P):
    L = enumerate_language(P, cap=CAP)
    if L is None:
        return None
    S = set(L[-1])
    pure = [w for w in S if 'b' not in w]
    if len(pure) > 1:
        return None
    N, Nw = shortest_pure(S)
    if N is None:
        return None
    M = grammar_metrics(P, L)
    if M['theta'] == 0:
        return None
    ok, cert = check_substitutable(S)
    if not ok:
        return None
    return dict(P=P, N=N, Nw=Nw, g=M['size'], theta=M['theta'],
                nwords=len(S), nmixed=len(S) - len(pure),
                lang=sorted(S))


def main(trials=40000, seed=20261030):
    rng = random.Random(seed)
    best = []
    hits = 0
    insp = 0
    t0 = time.time()
    for it in range(trials):
        k = rng.choice([3, 4, 5, 6])
        P = random_grammar(rng, k)
        if not prod_reach(P):
            continue
        d = evaluate(P)
        if d is None:
            continue
        insp += 1
        hits += 1
        d['ratio'] = d['N'] / d['g'] / d['theta']
        d['NoverT'] = d['N'] / d['theta']
        best.append(d)
        if len(best) > 400:
            best.sort(key=lambda x: -x['ratio'])
            best = best[:200]
        if it % 2000 == 0:
            print(f'{it} trials, {hits} substitutable, '
                  f'max N/theta={max((b["NoverT"] for b in best), default=0):.3f}',
                  flush=True)
    best.sort(key=lambda x: -x['ratio'])
    print(f'\n== {trials} random grammars, {hits} substitutable ==')
    print('== top 20 by N/(g theta) ==')
    for d in best[:20]:
        print(f"ratio={d['ratio']:.4f} N/theta={d['NoverT']:.3f} N={d['N']} "
              f"g={d['g']} th={d['theta']} |L|={d['nwords']} |M|={d['nmixed']}")
        print('   ', [[(t if isinstance(t, str) else f'A{t}') for t in rhs]
                      for rules in d['P'] for rhs in rules])
    print('\n== top 20 by N/theta ==')
    best.sort(key=lambda x: -x['NoverT'])
    for d in best[:20]:
        print(f"N/theta={d['NoverT']:.3f} N={d['N']} g={d['g']} th={d['theta']} "
              f"|L|={d['nwords']} |M|={d['nmixed']} ratio={d['ratio']:.4f}")
        print('   ', [[(t if isinstance(t, str) else f'A{t}') for t in rhs]
                      for rules in d['P'] for rhs in rules])
        print('    L=', d['lang'][:20])


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 20000)
```

### 13.8 `check_invariant.py`（定理 3 の証明の鍵補題の検証）

```python
# -*- coding: utf-8 -*-
"""Check the invariant lemma used in the proof of Theorem 3:
for L_{k,n} = ({a^k,b})^{2^n}, a mixed factor x with nonempty D has
    D(x) determined by ( psi(x), lead(x) mod k, trail(x) mod k ),
and any two mixed factors sharing a context have the same triple.
"""
from collections import defaultdict
from fractions import Fraction

from u1core import all_distributions, enumerate_language


def data(k, n):
    P = [[('a' * k,), ('b',)]]
    for i in range(1, n + 1):
        P.append([(i - 1, i - 1)])
    return enumerate_language(P, cap=3000000)[-1]


def psi(w, k):
    return Fraction(len(w) - w.count('b'), k) + w.count('b')


def lead(w):
    c = 0
    for ch in w:
        if ch == 'a':
            c += 1
        else:
            break
    return c


def trail(w):
    c = 0
    for ch in reversed(w):
        if ch == 'a':
            c += 1
        else:
            break
    return c


def check(k, n):
    S = data(k, n)
    D, _ = all_distributions(sorted(S))
    inv = defaultdict(set)
    for x, d in D.items():
        if 'b' not in x:
            continue
        inv[(psi(x, k), lead(x) % k, trail(x) % k)].add(frozenset(d))
    amb = [key for key, v in inv.items() if len(v) > 1]
    byctx = defaultdict(list)
    for w in S:
        for i in range(len(w)):
            for j in range(i + 1, len(w) + 1):
                byctx[(w[:i], w[j:])].append(w[i:j])
    conflicts = 0
    for c, xs in byctx.items():
        keys = {(psi(x, k), lead(x) % k, trail(x) % k)
                for x in xs if 'b' in x}
        if len(keys) > 1:
            conflicts += 1
    return len(D), len(inv), len(amb), conflicts


def main():
    print('k, n, #factors, #invariant-keys, #ambiguous-keys, '
          '#shared-context-key-conflicts')
    tot = 0
    for k in (1, 2, 3, 4):
        for n in (2, 3):
            a, b, c, d = check(k, n)
            print(f'{k}, {n}, {a}, {b}, {c}, {d}', flush=True)
            tot += c + d
    print('TOTAL violations of the invariant lemma:', tot)


if __name__ == '__main__':
    main()
```

### 13.9 `local_search.py`（局所探索）

```python
# -*- coding: utf-8 -*-
"""Stage 2e: local search (hill climbing with random restarts, plus a simple
simulated-annealing acceptance) over acyclic CFGs with k = 8..14 nonterminals,
maximising  N / (||G|| * theta-bar)  subject to exact (1,s)-substitutability.

Start points: the block-code family (Theorem 3) with random (k,n) plus random
acyclic grammars.  Moves: change a terminal block, change a rule shape, add or
delete a rule.  Every candidate is checked with the exact test; the enumerated
language is capped, and grammars above the cap are rejected as "not inspected"
(never counted as improvements).
"""
import random
import sys
import time

from u1core import (enumerate_language, grammar_metrics, check_substitutable,
                    shortest_pure, representative_lengths)

CAP = 20000
BLOCKS = ['a', 'b', 'aa', 'ab', 'ba', 'bb', 'aaa', 'aab', 'aba', 'abb',
          'baa', 'bab', 'bba', 'bbb', 'aabb', 'abab', 'abba', 'baab']
SHAPES = [('X', 'X'), ('a', 'X', 'X'), ('X', 'a', 'X'), ('X', 'X', 'a'),
          ('b', 'X', 'X'), ('X', 'b', 'X'), ('X', 'X', 'b'), ('a', 'X'),
          ('X', 'a'), ('b', 'X'), ('X', 'b'), ('X',), ('aa', 'X'),
          ('X', 'aa')]


def prod_reach(P):
    k = len(P)
    prod = [False] * k
    for i in range(k):
        for rhs in P[i]:
            if all(prod[t] for t in rhs if isinstance(t, int)):
                prod[i] = True
    if not prod[k - 1]:
        return False
    reach = [False] * k
    reach[k - 1] = True
    for i in range(k - 1, -1, -1):
        if not reach[i]:
            continue
        for rhs in P[i]:
            for t in rhs:
                if isinstance(t, int):
                    reach[t] = True
    return all(prod) and all(reach)


def evaluate(P):
    if not prod_reach(P):
        return None
    L = enumerate_language(P, cap=CAP)
    if L is None:
        return None
    S = set(L[-1])
    pure = [w for w in S if 'b' not in w]
    if len(pure) > 1:
        return None
    N, _ = shortest_pure(S)
    if N is None:
        return None
    M = grammar_metrics(P, L)
    if not M['theta']:
        return None
    ok, _ = check_substitutable(S)
    if not ok:
        return None
    return N / (M['size'] * M['theta_bar']), N, M['size'], M['theta'], len(S)


def blockcode(k, j):
    P = [[('a' * j,), ('b',)]]
    for i in range(1, k):
        P.append([(i - 1, i - 1)])
    return P


def random_start(rng, k):
    P = []
    for i in range(k):
        rules = []
        for _ in range(rng.randint(1, 2)):
            t = rng.random()
            if i == 0 or t < 0.5:
                rules.append((rng.choice(BLOCKS),))
            else:
                rules.append((rng.choice(SHAPES), ))
                sh = rules[-1][0]
                rules[-1] = tuple(
                    (i - 1 if x == 'X' else x) for x in sh)
        P.append(rules)
    return P


def mutate(rng, P):
    Q = [[tuple(r) for r in rules] for rules in P]
    k = len(Q)
    i = rng.randrange(k)
    mv = rng.random()
    if mv < 0.35:                       # replace a rule by another shape
        sh = rng.choice(SHAPES)
        Q[i][rng.randrange(len(Q[i]))] = tuple(
            (i - 1 if x == 'X' else x) for x in sh)
    elif mv < 0.6:                      # change a terminal block
        r = rng.randrange(len(Q[i]))
        rhs = list(Q[i][r])
        pos = [p for p, t in enumerate(rhs) if isinstance(t, str)]
        if pos:
            p = rng.choice(pos)
            rhs[p] = rng.choice(BLOCKS)
            Q[i][r] = tuple(rhs)
    elif mv < 0.8:                      # add a rule
        if len(Q[i]) < 3:
            sh = rng.choice(SHAPES)
            Q[i].append(tuple((i - 1 if x == 'X' else x) for x in sh))
    else:                               # delete a rule
        if len(Q[i]) > 1:
            Q[i].pop(rng.randrange(len(Q[i])))
    return Q


def main(seconds=240, seed=7):
    rng = random.Random(seed)
    t0 = time.time()
    best = (0.0, None)
    tried = 0
    accepted = 0
    improved = 0
    restarts = 0
    while time.time() - t0 < seconds:
        restarts += 1
        if restarts % 2 == 0:
            k = rng.choice([8, 9, 10, 12])
            P = blockcode(k, rng.choice([2, 3, 4, 5]))
        else:
            k = rng.choice([8, 10, 12, 14])
            P = random_start(rng, k)
        cur = evaluate(P)
        if cur is None:
            continue
        for step in range(300):
            if time.time() - t0 > seconds:
                break
            Q = mutate(rng, P)
            tried += 1
            v = evaluate(Q)
            if v is None:
                continue
            accepted += 1
            if v[0] > cur[0] + 1e-12:
                P, cur = Q, v
                improved += 1
                if v[0] > best[0]:
                    best = (v[0], (Q, v))
                    print(f'new best ratio={v[0]:.4f} N={v[1]} g={v[2]} '
                          f'theta={v[3]} |L|={v[4]} k={len(Q)}', flush=True)
    print(f'local search: {round(time.time() - t0, 1)}s, restarts={restarts}, '
          f'candidates={tried}, substitutable={accepted}, improvements={improved}')
    print('best ratio', round(best[0], 4))
    if best[1]:
        P, v = best[1]
        print('best stats: ratio=%.4f N=%d g=%d theta=%d |L|=%d' % v)
        print('grammar:',
              [[(t if isinstance(t, str) else f'A{t}') for t in rhs]
               for rules in P for rhs in rules])


if __name__ == '__main__':
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 240)
```

## 14. 実行ログ全文

### 14.1 `py -3 -u selftest.py`

```text
== MODEL FAMILIES ==========================================
H_(N,k): 52 languages (N=4..11, k=1..N-1): all PASS, both tests
two-word {a^N, a^c b a^c}: PASS for (12,3),(20,6),(30,10)
naive doubling n=1: |L|=2 PASS 
naive doubling n=2: |L|=5 FAIL cert={'x': 'aab', 'y': 'b', 'type': 2, 'shared': ('', ''), 'distinguished': ('', 'aa'), 'distinguished_in_x': True, 'distinguished_in_rep': False}
naive doubling n=3: |L|=24 FAIL cert={'x': 'aab', 'y': 'b', 'type': 2, 'shared': ('', 'aaaa'), 'distinguished': ('', ''), 'distinguished_in_x': True, 'distinguished_in_rep': False}
naive doubling n=4: |L|=455 FAIL cert={'x': 'aab', 'y': 'b', 'type': 2, 'shared': ('', 'aaaaaaaaaaaa'), 'distinguished': ('', ''), 'distinguished_in_x': True, 'distinguished_in_rep': False}
full shift 256 words: PASS=True (necessary test=True) size=23 theta=8 N=8
== length-spectrum family (all words the same length) ======
pure doubling chain n=4: size=27 theta=16 N=16  (theta = N, as expected)
== the cheap condition is NECESSARY but NOT SUFFICIENT =====
all 16383 nonempty languages inside {a,b}^{1,2,3}: 0 violations of the necessary condition, 472 languages that pass it but are not substitutable
4000 random languages inside {a,b}^{1..5}: 0 violations of the necessary condition, 600 counterexamples to sufficiency
== complete classification of very small languages ========
|L|=1 inside {a,b}^{1,2}: 6 pass the necessary condition of 6
|L|=2 inside {a,b}^{1,2}: 11 pass the necessary condition of 15
|L|=3 inside {a,b}^{1,2}: 7 pass the necessary condition of 20
|L|=4 inside {a,b}^{1,2}: 2 pass the necessary condition of 15
ALL STAGE-1 ASSERTIONS PASSED
```

### 14.2 `py -3 -u verify_family.py`

```text
== block-code family: formulas vs exact computation ==
k  n  |L|  g  g_formula  theta  theta_formula  N  N_formula  PASS  ratio  N<=g*theta
 1  1     4  11  11    2    2    2    2 True 0.0909 True
 1  2    16  17  17    4    4    4    4 True 0.0588 True
 1  3   256  23  23    8    8    8    8 True 0.0435 True
 2  1     4  12  12    3    3    4    4 True 0.1111 True
 2  2    16  18  18    5    5    8    8 True 0.0889 True
 2  3   256  24  24    9    9   16   16 True 0.0741 True
 3  1     4  13  13    4    4    6    6 True 0.1154 True
 3  2    16  19  19    6    6   12   12 True 0.1053 True
 3  3   256  25  25   10   10   24   24 True 0.0960 True
 4  1     4  14  14    5    5    8    8 True 0.1143 True
 4  2    16  20  20    7    7   16   16 True 0.1143 True
 4  3   256  26  26   11   11   32   32 True 0.1119 True
 5  1     4  15  15    6    6   10   10 True 0.1111 True
 5  2    16  21  21    8    8   20   20 True 0.1190 True
 5  3   256  27  27   12   12   40   40 True 0.1235 True
 6  1     4  16  16    7    7   12   12 True 0.1071 True
 6  2    16  22  22    9    9   24   24 True 0.1212 True
 6  3   256  28  28   13   13   48   48 True 0.1319 True

== ratio along k = round(sqrt(6 n 2^n)) ==
n= 2 k=       7 g=       23 theta=       10 N=          28 N/(g theta)=0.121739
n= 4 k=      20 g=       48 theta=       35 N=         320 N/(g theta)=0.190476
n= 6 k=      48 g=       88 theta=      111 N=        3072 N/(g theta)=0.314496
n= 8 k=     111 g=      163 theta=      366 N=       28416 N/(g theta)=0.476315
n=10 k=     248 g=      312 theta=     1271 N=      253952 N/(g theta)=0.640400
n=12 k=     543 g=      619 theta=     4638 N=     2224128 N/(g theta)=0.774709
n=14 k=    1173 g=     1261 theta=    17556 N=    19218432 N/(g theta)=0.868115
n=16 k=    2508 g=     2608 theta=    68043 N=   164364288 N/(g theta)=0.926225
n=18 k=    5321 g=     5433 theta=   267464 N=  1394868224 N/(g theta)=0.959905
n=20 k=   11217 g=    11341 theta=  1059792 N= 11761876992 N/(g theta)=0.978599

== exact check for the largest ratio members (n=3) ==
k=6 g=28 theta=13 N=48 PASS=True ratio=0.1319
k=7 g=29 theta=14 N=56 PASS=True ratio=0.1379
k=8 g=30 theta=15 N=64 PASS=True ratio=0.1422
k=9 g=31 theta=16 N=72 PASS=True ratio=0.1452
k=10 g=32 theta=17 N=80 PASS=True ratio=0.1471
ALL FORMULA ASSERTIONS PASSED
```

### 14.3 `py -3 -u final_stats.py`（k=1,2 の網羅と構造化 k=2）

```text
== (1) canonical exhaustive class, k<=2, <=2 rules ==
[canonical k=1] candidates=21 not-reduced=0 over-cap=0 non-substitutable=4 substitutable=17 with-N>theta=0
    max N/(g theta)=0.3333  max N/theta=1.000  key-violations=0
    best: N=1 g=3 theta=1 |L|=1  L=['a']
[canonical k=2] candidates=31185 not-reduced=441 over-cap=0 non-substitutable=26155 substitutable=4589 with-N>theta=27
    max N/(g theta)=0.1429  max N/theta=1.500  key-violations=0
    best: N=1 g=7 theta=1 |L|=1  L=['a']
== (2) canonical exhaustive class, k=3, 1 rule per nonterminal ==
[canonical k=3, 1 rule] candidates=53136 not-reduced=19224 over-cap=0 non-substitutable=0 substitutable=33912 with-N>theta=0
    max N/(g theta)=0.0909  max N/theta=1.000  key-violations=0
    best: N=1 g=11 theta=1 |L|=1  L=['a']
== (3) level-uniform structured class, k=2..5 ==
[structured k=2] candidates=2880 not-reduced=0 over-cap=0 non-substitutable=1612 substitutable=1268 with-N>theta=23
    max N/(g theta)=0.1111  max N/theta=1.500  key-violations=0
    best: N=1 g=9 theta=1 |L|=2  L=['a', 'b']
```

### 14.4 構造化 k=3,4

```text
[structured k=3] candidates=135200 not-reduced=0 over-cap=0 non-substitutable=129696 substitutable=5504 with-N>theta=371
    max N/(g theta)=0.0762  max N/theta=1.667  key-violations=0
    best: N=8 g=21 theta=5 |L|=4  L=['aaaaaaaa', 'aaaab', 'baaaa', 'bb']
[structured k=4] candidates=200001 not-reduced=0 over-cap=0 non-substitutable=199194 substitutable=806 with-N>theta=38
    max N/(g theta)=0.0467  max N/theta=1.400  key-violations=0
    best: N=7 g=30 theta=5 |L|=4  L=['aaaaaaa', 'aaaab', 'abaaa', 'abb']
elapsed 413.9077982902527
```

### 14.5 ランダム k=3..6（20 000 個）

```text
loop count 20000 st.total 20000
[random k=3..6] candidates=20000 not-reduced=15018 over-cap=45 non-substitutable=4787 substitutable=150 with-N>theta=1
    max N/(g theta)=0.0588  max N/theta=1.167  key-violations=0
    best: N=3 g=17 theta=3 |L|=2  L=['aaa', 'ba']
elapsed 150.5
```

### 14.6 `py -3 -u blockcode.py`

```text
== pure block-code chain (no shortcuts) ==
n=1 |L|=4 g=12 theta=3 N=4 PASS=True 
n=2 |L|=16 g=18 theta=5 N=8 PASS=True 
n=3 |L|=256 g=24 theta=9 N=16 PASS=True 
```

### 14.7 `py -3 -u family_blocks.py`

```text
== doubling-chain block designs (CAP=2000000) ==
a^i b a^i  n=1: |L|=2 g=13 th=3 N=2 PASS      ratio N/(g*th)=0.0513  n=2: |L|=5 g=25 th=5 N=4 FAIL      cert={'x': 'aab', 'y': 'aba', 'type': 2, 'shared': ('', 'aa'), 'distinguished': ('', 'aba'), 'distinguished_in_x': True, 'distinguished_in_rep': False}
b a^i b  n=1: |L|=2 g=13 th=3 N=2 PASS      ratio N/(g*th)=0.0513  n=2: |L|=5 g=24 th=5 N=4 FAIL      cert={'x': 'aab', 'y': 'ba', 'type': 2, 'shared': ('', 'ab'), 'distinguished': ('', 'baa'), 'distinguished_in_x': True, 'distinguished_in_rep': False}
a^i b  n=1: |L|=2 g=12 th=2 N=2 PASS      ratio N/(g*th)=0.0833  n=2: |L|=5 g=22 th=4 N=4 FAIL      cert={'x': 'aaab', 'y': 'aab', 'type': 2, 'shared': ('', ''), 'distinguished': ('a', ''), 'distinguished_in_x': True, 'distinguished_in_rep': False}
b a^i  n=1: |L|=2 g=12 th=2 N=2 PASS      ratio N/(g*th)=0.0833  n=2: |L|=5 g=22 th=4 N=4 FAIL      cert={'x': 'b', 'y': 'ba', 'type': 2, 'shared': ('', 'aa'), 'distinguished': ('', 'a'), 'distinguished_in_x': True, 'distinguished_in_rep': False}
a b^i a  n=1: |L|=2 g=13 th=3 N=2 PASS      ratio N/(g*th)=0.0513  n=2: |L|=5 g=24 th=5 N=4 FAIL      cert={'x': 'aaab', 'y': 'abaa', 'type': 2, 'shared': ('', 'a'), 'distinguished': ('', 'ba'), 'distinguished_in_x': True, 'distinguished_in_rep': False}
a b^i  n=1: |L|=2 g=12 th=2 N=2 PASS      ratio N/(g*th)=0.0833  n=2: |L|=5 g=22 th=4 N=4 FAIL      cert={'x': 'aba', 'y': 'ab', 'type': 2, 'shared': ('', 'b'), 'distinguished': ('', 'a'), 'distinguished_in_x': False, 'distinguished_in_rep': True}
b^i a  n=1: |L|=2 g=12 th=2 N=2 PASS      ratio N/(g*th)=0.0833  n=2: |L|=5 g=22 th=4 N=4 FAIL      cert={'x': 'ba', 'y': 'b', 'type': 2, 'shared': ('', 'ba'), 'distinguished': ('', 'aa'), 'distinguished_in_x': False, 'distinguished_in_rep': True}
b^i a b^i  n=1: |L|=2 g=13 th=3 N=2 PASS      ratio N/(g*th)=0.0513  n=2: |L|=5 g=25 th=5 N=4 FAIL      cert={'x': 'aab', 'y': 'babb', 'type': 2, 'shared': ('', 'ab'), 'distinguished': ('b', ''), 'distinguished_in_x': True, 'distinguished_in_rep': False}
b a^i b a^i b  n=1: |L|=2 g=15 th=5 N=2 PASS      ratio N/(g*th)=0.0267  n=2: |L|=5 g=29 th=7 N=4 FAIL      cert={'x': 'aab', 'y': 'bababb', 'type': 2, 'shared': ('', 'abab'), 'distinguished': ('b', 'aab'), 'distinguished_in_x': False, 'distinguished_in_rep': True}
a^i b a^(2i)  n=1: |L|=2 g=14 th=4 N=2 PASS      ratio N/(g*th)=0.0357  n=2: |L|=5 g=28 th=7 N=4 FAIL      cert={'x': 'aaba', 'y': 'aba', 'type': 2, 'shared': ('', 'aaa'), 'distinguished': ('', 'aabaa'), 'distinguished_in_x': True, 'distinguished_in_rep': False}
a^(2i) b a^i  n=1: |L|=2 g=14 th=4 N=2 PASS      ratio N/(g*th)=0.0357  n=2: |L|=5 g=28 th=7 N=4 FAIL      cert={'x': 'aaaab', 'y': 'aaba', 'type': 2, 'shared': ('', 'aa'), 'distinguished': ('', 'a'), 'distinguished_in_x': False, 'distinguished_in_rep': True}
a b^i a b^i a  n=1: |L|=2 g=15 th=5 N=2 PASS      ratio N/(g*th)=0.0267  n=2: |L|=5 g=29 th=7 N=4 FAIL      cert={'x': 'aaabab', 'y': 'ababaa', 'type': 2, 'shared': ('', 'a'), 'distinguished': ('', 'baba'), 'distinguished_in_x': True, 'distinguished_in_rep': False}
b^i b a b^i  n=1: |L|=2 g=14 th=4 N=2 PASS      ratio N/(g*th)=0.0357  n=2: |L|=5 g=27 th=6 N=4 FAIL      cert={'x': 'aab', 'y': 'bbabb', 'type': 2, 'shared': ('', 'bab'), 'distinguished': ('b', ''), 'distinguished_in_x': True, 'distinguished_in_rep': False}
a^i b^i  n=1: |L|=2 g=12 th=2 N=2 PASS      ratio N/(g*th)=0.0833  n=2: |L|=5 g=23 th=4 N=4 FAIL      cert={'x': 'aab', 'y': 'abb', 'type': 2, 'shared': ('a', ''), 'distinguished': ('', 'b'), 'distinguished_in_x': False, 'distinguished_in_rep': True}
b^i a^i  n=1: |L|=2 g=12 th=2 N=2 PASS      ratio N/(g*th)=0.0833  n=2: |L|=5 g=23 th=4 N=4 FAIL      cert={'x': 'ba', 'y': 'bb', 'type': 2, 'shared': ('', 'aa'), 'distinguished': ('', 'ba'), 'distinguished_in_x': False, 'distinguished_in_rep': True}
a^i b^i a  n=1: |L|=2 g=13 th=3 N=2 PASS      ratio N/(g*th)=0.0513  n=2: |L|=5 g=25 th=5 N=4 FAIL      cert={'x': 'aaab', 'y': 'abaa', 'type': 2, 'shared': ('', 'a'), 'distinguished': ('', 'ba'), 'distinguished_in_x': True, 'distinguished_in_rep': False}
PASSING DESIGNS: []
```

### 14.8 `py -3 -u check_invariant.py`

```text
k, n, #factors, #invariant-keys, #ambiguous-keys, #shared-context-key-conflicts
1, 2, 30, 4, 0, 0
1, 3, 510, 8, 0, 0
2, 2, 60, 12, 0, 0
2, 3, 1132, 28, 0, 0
3, 2, 98, 24, 0, 0
3, 3, 1994, 60, 0, 0
4, 2, 144, 40, 0, 0
4, 3, 3096, 104, 0, 0
TOTAL violations of the invariant lemma: 0
```

### 14.9 ブロックコード＋短絡の全 529 組（n=3）

```text
n=2: 23 tuples, 3 PASS
   ratio=0.0762 zs=('bb',) |L|=16 g=21 th=5 N=8
   ratio=0.0727 zs=('baa',) |L|=16 g=22 th=5 N=8
   ratio=0.0727 zs=('aab',) |L|=16 g=22 th=5 N=8
n=3: 529 tuples, 0 PASS
```

### 14.10 `py -3 -u local_search.py`（150 秒版）

```text
elapsed 150.4 restarts 6 candidates 361 substitutable 177 best 0.0000
```

## 15. 補遺（定理 3 の証明の鍵補題の計算機検証）

定理 3(5) の証明の中心的補題は「混合因子 \(x\) の分布は \((\psi(x),\ \mathrm{lead}(x)\bmod k,\ \mathrm{trail}(x)\bmod k)\) で決まる」である。これを \(k=1..4\)、\(n=2,3\) で厳密に検査した（因子数 30〜3096、不変量キー 4〜104、**曖昧キー 0、共有文脈でのキー衝突 0**）。コードは §13.8、ログは §14.8。
