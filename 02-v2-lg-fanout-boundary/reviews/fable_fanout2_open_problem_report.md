# `op:fanout-two` 独立研究報告（Fable, 2026-11-15）

**結論ラベル：`NEW THEOREM BUT OPEN`**
`op:fanout-two` 自体は解けていない。得られたのは (i) 倍化族に対する no-lift 定理の決定的な強化（機械検証済み証明書つき）、(ii) 薄い文法に対するアーベル型下界の一般的不可能性、(iii) 可換言語における単項希少型の多項式上界（新しい証明法）、(iv) 開問題の単一言明への還元、である。私の現時点の評価は「答えは NO（LG は fan-out 2 では境界でない）の方が見込みが高い」だが、これは**予想**であり証明ではない。

各主張の状態は次の記号で区別する：**[証明]** 本報告内に完全な証明がある／**[検証]** 明示的証明書を独立チェッカで検査済み／**[計算]** ハッシュベースの探索結果で証明書は未抽出／**[予想]**。

---

## 0. 読んだ資料と読んでいない資料

- GitHub を clone して読んだもの：`main.tex` の定義（`def:grammar-properties`, `def:tuple-substitutable`, `def:uniform-polydata`）、`lem:thickness-*`, `lem:distinguishing`, `prop:rare-type`, `prop:three-letter-family`, `thm:fanout-one-data`, `lem:power-transfer`, `thm:doubling-no-lift`, `op:fanout-two`；`HANDOFF_CURRENT.md`；U₂ ノートの定義と主張部分。
- **読んでいないもの**：`reviews/` の各ラウンド報告の本文（定理 L, P, S, L^⊗′ の証明、第九〜十一段の詳細）。したがって §5 の可換定理が既存の定理 L（ℓ=1）と結論の上で重なる可能性は排除していない。証明法は独立に構成した。
- 依頼書の問題設定に誤りは見つからなかった。一点だけ補足がある（§1）。

## 1. 開問題の単一言明への還元 [証明]

**命題 1.** \(f\ge2,\ r_{\max}\ge2\) を固定する。次は同値。
1. `op:fanout-two` の答えが YES。
2. 有限半束の擬多様体 \(\mathbf{SL}\) が fan-out \(f\)・rank \(r_{\max}\) で一様多項式特徴データ長を持たない。
3. ある有限アルファベット \(\Sigma\) とある半束型付け \(s:\Sigma^+\twoheadrightarrow\mathsf S\) について `def:uniform-polydata` の多項式が存在しない。

*証明.* \(\mathbf V\not\subseteq\mathbf{LG}\) なら \(U_1\in\mathbf V\)（`thm:lg-characterization`）で、擬多様体は有限直積・部分・商で閉じるから \(\mathbf{SL}=\langle U_1\rangle\subseteq\mathbf V\)。一様多項式性の失敗は \(\mathbf V\) について単調なので 2⇒1。逆に \(\mathbf{SL}\) 自身が \(\mathbf{LG}\) に含まれないので 1⇒2。2⇔3 は定義。∎

**補足 1′（上界側は内容型付けだけ見ればよい）.** 任意の半束型付け \(s\) は内容型付け \(c_\Sigma\) を経由するので \(\mathcal C^{\mathrm{mcf}}_{f,s}\subseteq\mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}\)。さらに \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) に対し \(\tau(G,s)\le\tau(G,c_\Sigma)\)：\(s\)-型付き非終端 \(B_{\mathbf t}\) の収率を含む内容型付き非終端 \(B_{\mathbf T}\) の類代表は、同じ分布を持ち \(s\)-型も \(\mathbf t\) だから \(\operatorname{Cl}_{L,s}(B_{\mathbf t})\) に入る。よって「全ての \(\Sigma\) で \(\tau(G,c_\Sigma)\) が多項式」が示されれば答えは NO。

つまり問題は U₁ の特定の3文字型付けではなく、**任意アルファベット上の内容型付け**の問題そのものである。下界側は大きなアルファベットを自由に使ってよく、上界側は内容型付けだけ処理すればよい。

## 2. 道具

以下 \(c(w)=\operatorname{alph}(w)\)、\(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、\(f\ge2\)。

**補題 2.1（滑り補題／共役移送）[証明].** \(l,r\in\Sigma^*\)、\(x_1,y_2,z,z',m\in\Sigma^+\) が \(zm=mz'\)、\(s(x_1z)=s(x_1)\)、\(s(z'y_2)=s(y_2)\)、\(l\,x_1\,z\,m\,y_2\,r\in L\) を満たすなら
\[(x_1z,\;y_2)\ \equiv_{L,s}\ (x_1,\;z'y_2).\]
*証明.* 文脈 \(E=l\,\square_1\,m\,\square_2\,r\)（\(m\neq\varepsilon\)）は両方の組を同じ語 \(l x_1 z m y_2 r=l x_1 m z' y_2 r\) に埋めるので共通の受理文脈であり、成分型は仮定より等しい。∎

`lem:power-transfer` は \(z=z'=u^\delta\), \(m=u\) の特別な場合。内容型付けでは条件は \(c(z)\subseteq c(x_1)\cap c(y_2)\) だけになる。特に：

**系 2.2（単位の移送）.** 内容型付けで、\(L\) のある語が因子 \(x_1\cdot d\kappa\cdot d\cdot y_2\)（\(d\in\Sigma\), \(\kappa\in\Sigma^*\), \(c(d\kappa)\subseteq c(x_1)\cap c(y_2)\)）を持てば、全ての \(l,r\in\Sigma^*\), \(m'\in\Sigma^+\) で
\[l\,x_1\,d\kappa\;m'\;y_2\,r\in L\iff l\,x_1\;m'\;\kappa d\,y_2\,r\in L .\]
同じ文字 \(d\) の連続する二つの出現に挟まれた単位 \(d\kappa\) は、後方の \(y_2\) の出現の直前へ（\(\kappa d\) として）語長と Parikh ベクトルを保ったまま移動できる。長い語では文字が必ず再出現するので、この移動は**避けられない**。

**定義 2.3（導出閉包）.** \(K\subseteq\Sigma^*\) に対し \(\operatorname{Cl}(K)\) を、\(K\) を含み次の規則で閉じた最小集合とする：\(d\in\{1,2\}\)、\(\mathbf x,\mathbf y\in(\Sigma^+)^d\) が成分ごとに同じ内容を持ち、\(E_0,E_1\in\mathcal E_d\) について \(E_0[\mathbf x],E_0[\mathbf y],E_1[\mathbf x]\) が既に入っていれば \(E_1[\mathbf y]\) を入れる。

**補題 2.4（健全性）[証明].** 半束型付け \(s\) と \(f\ge2\) について、\(K\subseteq L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) なら \(\operatorname{Cl}(K)\subseteq L\)。（\(L\in\mathcal C^{\mathrm{mcf}}_{f,c_\Sigma}\) なので各規則適用は定義そのもの。）

**補題 2.5（射による輸送）[証明].** \(\varphi:\Sigma^*\to\Sigma'^*\) を非消去射、\(P,Q\in\Sigma'^*\) とすると \(P\,\varphi(\operatorname{Cl}(K))\,Q\subseteq\operatorname{Cl}(P\varphi(K)Q)\)。
*証明.* 導出の長さの帰納法。\(c(\varphi(u))=\bigcup_{e\in c(u)}c(\varphi(e))\) は \(c(u)\) のみで決まるので、内容が等しい成分は像でも内容が等しい。成分と穴の間の部分は非消去性により非空のまま。文脈 \(E=(l,m,r)\) は \((P\varphi(l),\varphi(m),\varphi(r)Q)\) に移る。∎

内容型付けの本質的な点は、**任意の**非消去射で導出が輸送されることである（文字互いに素である必要はない）。

## 3. 定理 A：倍化族は fan-out 2 で完全に崩壊する

\(L_n,W_n\) は `prop:three-letter-family` のもの（\(W_1=\mathtt{baab}\), \(|W_n|=3\cdot2^n-2\)）。

**定理 A [証明＋検証].** \(\Sigma\supseteq\{a,b,c\}\)、\(s\) を \(\Sigma^+\) 上の任意の半束型付け（\(s_U\)、\(c_\Sigma\) を含む）、\(f\ge2\)、\(n\ge3\) とする。\(L_n\subseteq L\) なる全ての \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) は \(W_1,W_2,\dots,W_n\) を全て含む。特に \(\mathtt{baab}\in L\) であり、\(W_n\) の型の最短語長は \(n\) によらず \(4\) 以下。
より一般に、非消去射 \(\psi\) について \(\psi(L_n)\subseteq L\) なら \(\psi(\mathtt{baab})\in L\)。

これは `thm:doubling-no-lift`（「同じ型・同じ Parikh の別の語がある」）を、半束型付けについて「定数長の語がある」まで強める。語を追加して族を修復する余地は一切ない。

*証明.*
(1) **証明書** [検証]：\(W_2=\mathtt{bbaabbaabb}\in\operatorname{Cl}(L_3)\) かつ \(\mathtt{baab}\in\operatorname{Cl}(L_3)\)。添付 `cert_L3_to_baab_pruned.json` は定義 2.3 の規則 33 回（\(d=1\) が 9 回、\(d=2\) が 24 回）の明示的列で、`verify_cert.py` が各ステップの前提（成分・中間部の非空性、内容の一致、\(E_0[\mathbf x],E_0[\mathbf y],E_1[\mathbf x]\) の所属）を独立に検査する。
(2) \(k\ge0\)、\(\varphi_k:a\mapsto W_k,\ b\mapsto b,\ c\mapsto c\) とすると \(\varphi_k(L_3)\subseteq L^{(k+3)}\)（\(E_{k+3}\) の収率集合）。\(k+3\le n\) なら \(E_{k+3}\) は \(L_n\) の中で文脈 \((P_k,Q_k)\)（例えば \(P_k=b^{\,n-k-3}\)）を持ち、\(P_k\varphi_k(L_3)Q_k\subseteq L_n\subseteq L\)。補題 2.5, 2.4 より \(P_kW_{k+2}Q_k,\ P_kW_{k+1}Q_k\in L\)。
(3) \(W_{k+3},W_{k+2},W_{k+1}\) は内容 \(\{a,b\}\) が等しく文脈 \((P_k,Q_k)\) を共有するので互いに \(\equiv_L\)（分布が一致）。
(4) \(W_n\in L\)。\(j\ge3\) で \(W_j\in L\) なら、\(k=j-3\) の同値 \(W_j\equiv W_{j-1}\) を文脈 \((\varepsilon,\varepsilon)\) に適用して \(W_{j-1}\in L\)。\(W_3\in L\) からは \(k=0\) の \(W_3\equiv W_1\) で \(W_1\in L\)。射版は \(\psi\circ\varphi_k\) で同じ。∎

**崩壊の機構.** 核は系 2.2 の「文字の飛び越し」である。探索で最初に見つかった例では、\(L_3\) の二つの語 \(b\,W_2\,[c\,W_1\,c]\,b\) と \(b\,W_2\,[b\,W_1\,c\,a\,c\,b]\,b\) から、\(b\) が \(c\) を右へ、\(c\) が \(\mathtt{bbaab}\) を左へ飛び越して、**同じ枠** \(b\,W_2\,c\,\square\,c\,bb\) に長さの違う \(c\) なし語 \(\mathtt{baa}\) と \(\mathtt{bbaaba}\) が入る。添付の証明書が実際に使うのは同種の二つの枠で、枠 \((\mathtt{bbcacbaabbc},\mathtt{acbb})\) に \(\mathtt{bbbaa}\) と \(\mathtt{ba}\) が、枠 \((\mathtt{bcbaabcb},\mathtt{cbacbb})\) に \(\mathtt{baabba}\) と \(\mathtt{baa}\) が入る。これと \(b\) の冪移送 \((b,bb)\equiv(bb,b)\) を合わせて \(W_3\) が \((a,2b)\) ずつ縮む（22→19→16→13→10→7→4）。省略記号 \(c\) が可動なので「省略の深さ」を位置で符号化できない、というのが本質である。

**検証の範囲.** `verify_log.txt`：\(L_3\) 上の証明書（刈込み 33 手・完全版 2945 手）に加え、輸送補題に頼らず \(L_4\)（\(k=1\) および \(k=0\) で枠 \((b,W_3b)\)）、\(L_5\)（\(k=2\)、および \(k=0\) で枠 \((bc,\,c^5ac^4b)\)）、\(L_6\)（\(k=1\)）、\(L_7\)（\(k=4\)）の中で同じ 33 手を直接検査し全て通過。所属判定は \(L_n\) の再帰的認識器による（列挙やハッシュに依存しない）。

**命題 A′（括弧を別文字にした変種）[計算].** \(E_i\to b\,E_{i-1}E_{i-1}\,d\mid c\,E_{i-1}\,e\)、\(E_0\to a\)（5文字、内容型付け）の族 \(V_n\) についても、\(\operatorname{Cl}(V_3)\) は \(W_1'=\mathtt{baad}\) と \(W_2'=\mathtt{bbaadbaadd}\) を含む（長さ 22 → 19 → 16 → 13 → 10 → 7 → 4）。これが正しければ定理 A の証明 (2)–(4) がそのまま通り \(V_n\) も定数長に崩壊する。ただしこれは 64 bit ハッシュを用いた打切り閉包＋最良優先探索の結果で、**明示的証明書は抽出していない**。

**観察 [計算].** \(s_U\) 型付けでは \(L_2\) の（長さ 10 打切り）閉包が既に語 \(\mathtt a\) を含む。内容型付けでは \(L_2\) は閉じており、崩壊は \(n=3\) から始まる。

## 4. 定理 B：薄い文法はアーベル不変量を隠せない

**定理 B [証明].** \(G\) を reduced good MCFG（fan-out 任意、rank \(\le r\)）、\(\theta=\bar\theta_G\)、\(g:\Sigma^*\to\mathsf A\) をアーベル群へのモノイド射、\(\mathsf H\le\mathsf A\)、\(\gamma\in\mathsf A\) とする。長さ \(\le(r+2)\theta\) の全ての \(w\in L(G)\) が \(g(w)\in\gamma+\mathsf H\) を満たせば \(L(G)\subseteq g^{-1}(\gamma+\mathsf H)\)。

*証明.* 各非終端 \(A\) に `lem:thickness-equivalence`(ii),(iv) の短い収率 \(\mathbf u_A\)（\(\|\mathbf u_A\|_1\le\theta\)）と文脈 \(E_A\)（固定部 \(\le\theta\)）を取り、\(c_A:=\sum_i g(u_{A,i})\) とおく。主張：全ての \(\mathbf u\in L_A\) で \(\sum_ig(u_i)\equiv c_A\pmod{\mathsf H}\)。導出の高さの帰納法：\(\mathbf u=\rho(\mathbf u^1,\dots,\mathbf u^q)\) なら非削除性と可換性から \(g(\mathbf u)=g(\text{$\rho$ の終端})+\sum_jg(\mathbf u^j)\equiv g(\rho(\mathbf u_{B_1},\dots,\mathbf u_{B_q}))\)。語 \(E_A[\rho(\mathbf u_{B_1},\dots)]\) と \(E_A[\mathbf u_A]\) は共に \(L(G)\) に属し長さ \(\le(q+2)\theta\) なので仮定より \(g\) 値が同じ剰余類にあり、\(g(\rho(\mathbf u_{B_j}))\equiv c_A\)。\(A=S\) では \(c_S=g(u_S)\in\gamma+\mathsf H\)。∎

**帰結.**
- `lem:distinguishing` を \(L'=L\cap g^{-1}(\gamma+\mathsf H)\)（`prop:abelian-coset-filter` の型の部分標的）に適用しても、区別語の長さは高々 \((r_{\max}+2)\bar\theta_G\)。**アーベル剰余類フィルタによる部分標的では超多項式下界は出ない。**
- 例：\(\{w:|w|_a\equiv|w|_c \pmod{2^n}\}\) は全ての型付けで組代入可能だが、多項式サイズ・多項式厚さの reduced good 提示を持たない（持てば上の議論で \(|w|_a=|w|_c\) が \(\mathbb Z\) 上で成立してしまう）。指数的な法や重みを持つ計数は厚さに必ず現れる。

## 5. 単項型の構造と定理 C

以下 \(a\in\Sigma\)、\(s\) は半束型付け、\(a^N\in L\) で \(N=\min\{i\ge1:a^i\in L\}\)。

**補題 5.1 [証明]（非可換・一般の \(L\in\mathcal C^{\mathrm{mcf}}_{2,s}\) で成立）.**
- **(R) 連の再配分.** \(p\,a^i\,q\,a^j\,r\in L\)、\(q\in\Sigma^+\)、\(i,j,i',j'\ge1\)、\(i'+j'=i+j\le N-1\) なら \(p\,a^{i'}q\,a^{j'}r\in L\)。（\(a^N=a^i\cdot a\cdot a^j\cdot a^{N-1-i-j}\) が共通文脈。）
- **(U) 一意性.** \(P a^iQ,\ Pa^{i'}Q\in L\)、\(1\le i<i'\le N\) は起こらない。（起これば \(a^i\equiv a^{i'}\) で \(a^{N-i'+i}\in L\)、最小性に反する。）
- **(E) 交換.** \(V,V'\notin a^*\) が \(aVa^{e},\,aV'a^{e'}\in L\)（\(1\le e,e'\le N-2\)）を満たし \(c(V)\cup\{a\}=c(V')\cup\{a\}\) なら、\(i'-i=e'-e\) なる適当な \(i,i'\ge1\) について \(a^iVa\equiv a^{i'}V'a\)。

(R),(U) から、\(a\) の総数が \(N\) 未満の語では「\(a\) の個数は、\(a\) の連を1文字に潰した骨格の関数」である。すなわち単項希少語 \(a^N\) があると、\(L\) の他の語は**骨格 → 欠損 \(\delta=N-|w|_a\)** という関数のグラフになり、(E) により欠損は同じ内容類の部品の入替えについて加法的に振る舞う。

**定理 C（可換言語では単項型は希少になれない）[証明；独立監査は未実施].** \(\Sigma=\{a\}\sqcup\Delta\)、\(D=|\Delta|\ge1\)。\(L\) を可換（所属が Parikh ベクトルのみで決まる）とし、ある半束型付け \(s\) と \(f\ge1\) で \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、\(G\) を \(L\cap\Sigma^+\) の reduced good 提示（fan-out 任意、rank \(\le r\)、\(v=|V|\)、\(\theta=\bar\theta_G\)）とする。\(a^N\in L\) で \(N\) が最小なら
\[N\ \le\ \max\bigl\{(D+1)BK_0+1,\ \ 2^{D+1}\,v\,(r+1)K_0\bigr\},\quad B=D!\,\theta^{D},\ \rho=2DB,\ K_0=2(r+1)\theta\,\bigl(4(r+1)\rho\bigr)^{D2^{D}} .\]
特に \(N=O_{D,r}\bigl(v\,\theta^{\,1+D+D^22^D}\bigr)\)：固定アルファベットでは多項式。

*証明.* \(P\subseteq\mathbb N\times\mathbb N^\Delta\) を \(L\) の Parikh 像とし、点を \((e,V)\) と書く。
**(0) 木.** \(a^N\) の \(G\) における導出木を節点数最小に取る。同じ非終端の二節点は収率の総長 \(k\) が等しく（違えば短い \(a\) 冪が出る）、入れ子にならない（節点数最小性）。よって深さ \(\le v\)。短い収率 \(\mathbf u_A\) の Parikh を \((\alpha_A,V_A)\) とする。\(k_A>\theta\) の節点を「大」と呼ぶと \(V_A\neq0\)（さもなくば \(a^{N-k_A+\alpha_A}\in L\) が最小性に反する）。欠損 \(\delta_A:=k_A-\alpha_A\in[k_A-\theta,k_A]\)、類 \(T_A:=\operatorname{supp}V_A\)。\(k_A=N\) の節点は根からの単項鎖をなす。
**(1) 実現集合.** \(\mathcal V:=\{V\ne0:\exists e\in[1,N-1],(e,V)\in P\}\)。(U) より \(e\) は一意で \(\delta(V):=N-e\) が定まる。\(k<N\) の大節点を省略すれば \(V_A\in\mathcal V\), \(\delta(V_A)=\delta_A\)。
**(2) 交換.** \(V,V'\in\mathcal V\)、\(\operatorname{supp}V=\operatorname{supp}V'\)、\((e,Q+V)\in P\)、\(e\ge1\)、\(e':=e+\delta(V)-\delta(V')\ge1\) なら \((e',Q+V')\in P\)。（\(i=1+\max(0,\delta(V')-\delta(V))\), \(i'=1+\max(0,\delta(V)-\delta(V'))\) とし、Parikh \((i,V)\) と \((i',V')\) の語は内容が等しく文脈 \((N-\delta(V)-i,0)\) を共有するので同値。\(e\ge i\) は \(e'\ge1\) と同値。）
**(3) 分岐類での完全加法性.** 類 \(T\) が**分岐的**とは、互いに素な大節点 \(B,C\)（\(k<N\)）で \(T_B=T_C=T\)、\(N-\delta_B-\delta_C\ge1\) なるものがあること。このとき、類 \(T\) の大非終端 \(J_1,\dots,J_t\)（各 \(\delta_{J}\le(N-1)/2\)）と \(\sum m_j\delta_{J_j}\le N-1\) なる多重集合 \(m\ne0\) について \(\sum m_jV_{J_j}\in\mathcal V\) で欠損は \(\sum m_j\delta_{J_j}\)。
　\(|m|=2\)：種 \(V_B+V_C\)（欠損 \(\delta_B+\delta_C\)）で \(\delta_B\le\delta_C\) としてよく、(2) で \(V_C\to V_J\)、次に \(V_B\to V_{J'}\) と入れ替える（途中の \(a\) 個数は \(N-\delta_B-\delta_J\ge1\)、\(N-\delta_J-\delta_{J'}\ge1\)）。\(|m|\to|m|+1\)：\(M=\sum m_jV_{J_j}\)（台 \(T\)）、\(m_J\ge1\) とし、\(V_J+V_{J'}\) に (2) を \(V=V_J\), \(V'=M\), \(Q=V_{J'}\) で適用する。
**(4) 分岐類には疎な鎖がない.** 分岐類 \(T\)（\(t=|T|\)）の大非終端 \(J_0,\dots,J_t\) で \(\delta_{J_{i+1}}>\rho\,\delta_{J_i}\)、\(\delta_{J_t}\le N_1:=(N-1)/((D+1)B)\) なるものは存在しない。
　実際 \(t+1\) 個のベクトル \(V_{J_i}\in[0,\theta]^T\) には Cramer の公式から \(|\lambda_i|\le t!\theta^t\le B\) の非自明な整数関係 \(\sum\lambda_iV_{J_i}=0\) があり、\(V_{J_i}\ge0\), \(\neq0\) なので両符号が現れる。\(m^\pm=\lambda^\pm\) は (3) の条件を満たし同じベクトルを実現するから、(U) より \(\sum\lambda_i\delta_{J_i}=0\)。しかし最大の添字 \(i^*\) で \(|\lambda_{i^*}|\delta_{J_{i^*}}\ge\delta_{J_{i^*}}>2Bt\,\delta_{J_{i^*-1}}\ge2\bigl|\sum_{i<i^*}\lambda_i\delta_{J_i}\bigr|\)。矛盾。
　したがって分岐類の欠損のうち \(N_1\) 以下のものは高々 \(D\) 個の区間 \([x,\rho x]\) で覆われる（貪欲法）。全分岐類で区間は \(M_b<D2^D\) 個。
**(5) 非分岐類は高々二本の根道に載る.** 類 \(T\) に互いに素な対がなければ全節点が比較可能で一本の根道上。互いに素な対 \(B,C\) が全て「悪い」（\(k_B+k_C=N\)）なら、\(B\) の下の類 \(T\) 節点は互いに比較可能（互いに素な \(X,Y\subseteq B\) は \(N-\delta_X-\delta_Y\ge k_C\ge1\) で良い対になる）、\(C\) の下も同様、その他は \(B\) か \(C\) と比較可能。\(U\) を、非分岐類の節点が載る根道と \(k=N\) の鎖の和集合とすると \(U\) は上方閉で \(|U|\le2^{D+1}v\)。
**(6) 窓の議論.** \(X\notin U\) を大節点とする。その子孫の大節点は全て分岐類。最重の子を辿る列 \(k_0=k_X\ge k_1\ge\cdots\) は \(k_i>(r+1)\theta\) の間 \(k_{i+1}\ge(k_i-\theta)/r\ge k_i/(r+1)\) を満たす。よって \(\sigma:=2(r+1)\) として、\(y\in[\sigma\theta,k_X]\) なる各窓 \([y/\sigma,y]\) は分岐類の大節点の欠損を含む。\(y_j:=\sigma\theta(2\sigma\rho)^j\)（\(j=0,\dots,M_b\)）の窓は、一つの区間 \([x,\rho x]\) が二つと交わることがないほど離れている。したがって \(\min(k_X,N_1)<K_0=\sigma\theta(2\sigma\rho)^{M_b}\)（\(M_b\le D2^D\)）。
**(7) 集計.** \(N_1<K_0\) なら \(N<(D+1)BK_0+1\)。\(N_1\ge K_0\) なら \(U\) の外の大節点は全て \(k<K_0\) で、\(U\) の各節点は終端 \(\le\theta\) 個と高々 \(r\) 個の子を持つから \(N\le|U|(r+1)K_0\)。∎

**注意.** (a) 証明は \(d=1\) の代入可能性しか使っていない。可換言語では fan-out に関係なく単項型が希少になれない、という主張である。(b) 対照的に非可換・fan-out 1 では `thm:fanout-one-data` の指数的下界がある。fan-out 2 が何を変えるかは次節。(c) `prop:rare-type` 経由の下界のうち「可換言語の単項型」を使うものはこれで閉じられるが、**開問題そのものには届かない**。

## 6. 非可換の場合：見取り図・予想・障壁

**直観.** fan-out 1 の下界は「非可換な剛構造（木）」が希少型の語を長く保つことで成立する。fan-out 2 の代入可能性は系 2.2 により全ての長い語を「単位の移送」で攪拌し、言語を局所データ＋計数データで決まるものへ近づける（先行ラウンドの Euler 付け替えと同じ現象を別方向から見ている）。一方、計数データで決まる部分では定理 B, C の論法（薄さ ⟹ 短い整数関係 ⟹ 疎な重み列が存在しない）が多項式上界を与える。移送に免疫を持つのは文字の順序が剛な有界言語型（例：\(\{a^nb^n\}\) は内容型付けでは 2 次元代入可能）だが、そこではブロック数が固定で次元が有界である。

**予想 U [予想].** 半束型付け \(s\)、\(f\ge2\)、\(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)、reduced good 提示 \(G\) について、\(L\) の最短の \(a\) 冪の長さは \(\|G\|,\bar\theta_G\) の多項式（次数は \(|\Sigma|\) に依存）で抑えられる。

**証明計画と欠けている部分.** 補題 5.1 は非可換でそのまま成立する。定理 C の (3)–(7) を非可換で再現するには、(U) を適用するために**骨格が語として一致する二語**が必要で、ここが唯一の本質的な穴である：
1. 系 2.2 から「交叉」が出る：部品 \(\alpha d\beta\) と \(\alpha'd\beta'\) が、後方に \(\alpha'd\beta'\) の複製を持つ適当な語の中に現れれば、\(\alpha d\beta'\) と \(\alpha'd\beta\) を部品とする語も \(L\) に入り \(a\) の個数は変わらない [証明：系 2.2 の直接の適用]。
2. 交叉は部品の bigram 多重集合（\(a\) との境界 bigram を含む）を保つ。**未証明**：同じ bigram 多重集合を持つ二つの部品多重集合が、常に宿主条件（系 2.2 の因子 \(x_1d\kappa dy_2\) の存在）を満たしたまま交叉と部品の並べ替えで結べること。これは有向多重グラフの Euler 分解の連結性＋「宿主可能性」で、先行ラウンドが HC と呼んだ困難と同種と思われる。部品の複製を自由に増やせる（補題 5.1(E) と定理 C(3) の論法）ので宿主の用意は U₂ より容易だと期待するが、確認していない。
3. これが通れば欠損は bigram 計数ベクトル（次元 \(\le(D+1)^2\)）の加法的関数になり、定理 C の (4)–(7) が次元だけ替えて通る。
4. fan-out 2 の非終端では部品が2成分になり、交換に \(d=2\) の同値が必要。帳簿は増えるが新しい困難は見えていない（未確認）。

**一般の希少型（2文字以上）について.** \(c\) なしの語が \(\{a,b\}\) 上にある場合、(U) の類似は「骨格ごとに \((|w|_a,|w|_b)\) の可能な値が格子の剰余類に入る」になるはずで、可換版ですら未着手である。定理 A の崩壊はこの場合の最初の実例にあたる。

**下界側の候補が残る場所.** 私が排除できていないのは次だけである：(i) 希少型を使わず、非アーベルかつ組代入可能な部分標的 \(L'\subsetneq L\) で区別する経路（定理 B はアーベルな \(L'\) しか殺さない）；(ii) 移送に免疫のある剛構造を、固定アルファベットのまま非有界な深さで実現する未知の符号化。(ii) について、単一ブロックに非線形な重み \(\sigma(j)\) を持たせる有界形 \(\{a^ic^jb^k:i+k=\sigma(j)\}\) を調べたが、\(a^uc^{j_1}\) と \(a^{u'}c^{j_1'}\) の比較から \(\sigma\) は \(j\ge1\) でアフィンに強制され、非線形性は \(j=0\)（別の型）にしか置けず、その場合は薄い提示が作れなかった（議論は概略のみで、定理としては主張しない）。

## 7. 計算の記録

詳細は `experiments_log.txt`。全て決定的で乱数は不使用。閉包は全て長さ打切りなので真の閉包の下からの近似であり、報告した語が閉包に属することだけを主張する。

| 対象 | 型付け | 打切り | 結果 | 状態 |
|---|---|---|---|---|
| \(L_2\)（6語） | \(s_U\) | 10 | 3306語で閉、\(\mathtt a\) を含む | [計算] |
| \(L_2\) | 内容 | 10 | 既に閉（6語） | [計算] |
| \(L_3\)（42語） | 内容 | 22 | 第2巡 \(d=1\) で 644 万語、\(c\) なし長さ16 | [計算] |
| \(L_3\vdash W_2,\ \mathtt{baab}\) | 内容 | — | 33 手の証明書、\(L_4\)–\(L_7\) 内でも直接検査 | [検証] |
| \(V_3\)（42語、5文字） | 内容 | 22、組長/枠長 \(\le7\) | 174 万語、その後 \(\mathtt{baad}\), \(W_2'\) に到達 | [計算] |

失敗・未完：\(L_3,V_3\) の無制限閉包は第2巡以降メモリと時間で完走せず。Python の \(c\) なし語 BFS は 25 分で出力なしのため打ち切り、証明書構成に置き換えた。

## 8. 最も有望な次の一手

1. **予想 U の穴（§6 の 2.）を埋める**か、反例を作る。部品複製が自由な設定での Euler 連結性は、U₂ の宿主問題より扱いやすい特殊化であり、通れば「単項型による下界は fan-out 2 で不可能」という型付け・言語クラスによらない最初の一般上界になる。
2. 定理 C を 2 文字の希少型へ拡張する（可換の場合）。(U) を格子版に置き換える。
3. 定理 A′ の証明書抽出（`build_cert.py` を \(V_3\) 用に書き換えるだけだが計算量が大きい）。
4. 下界を狙うなら §6 の (i) のみが未踏。ただし非アーベルで組代入可能な部分標的の例を私は一つも構成できていない。

## 9. 結論

**`NEW THEOREM BUT OPEN`.**

- **解決したこと（量化込み）.**
  - 全ての \(f\ge2\)、\(n\ge3\)、\(\Sigma\supseteq\{a,b,c\}\)、全ての半束型付け \(s\)、\(L_n\) を含む全ての \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\) について \(\mathtt{baab}\in L\)（定理 A、証明書は機械検査済み）。任意の非消去射像でも同様。
  - 全ての reduced good MCFG \(G\)（rank \(\le r\)）と全てのアーベル剰余類条件について、長さ \((r+2)\bar\theta_G\) 以下の語で成り立てば \(L(G)\) 全体で成り立つ（定理 B）。
  - 全ての可換な \(L\in\mathcal C^{\mathrm{mcf}}_{f,s}\)（\(s\) 半束、\(f\ge1\)）と全ての reduced good 提示について、最短の \(a\) 冪は \(O_{|\Sigma|,r}(|V|\,\bar\theta_G^{\,1+D+D^22^D})\)（定理 C、手証明・未監査）。
  - `op:fanout-two` は「\(\mathbf{SL}\) が fan-out \(f\) で一様多項式データ長を持たないか」と同値（命題 1）。
- **未解決のまま.** ある \(\Sigma\) とある半束型付けについて超多項式族が存在するか（YES）、全ての \(\Sigma\) で \(\tau(G,c_\Sigma)\) が多項式か（NO）。非可換言語では単項希少型すら未決（予想 U）。\(f\ge3\) への移行も未検討。