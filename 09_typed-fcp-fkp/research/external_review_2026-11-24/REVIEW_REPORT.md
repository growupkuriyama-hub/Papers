# 査読報告 — 09_typed-fcp-fkp

2026-11-24 / 判定対象：添付 `manuscript/main.tex`（1003行）

## 1. 結論と推薦

**推薦：major revision。** 核縮約・二つの分離・削除族の表示下界・二つの学習器の収束時データ下界について、主定理を崩す数学的反例は見つからなかった。一方、**Theorem B の中心部分は添付の著者先行稿 Proposition 9.7 と既知の1-FKP学習結果の直接の帰結**である。序論の「既存枠組みは異なる観測を比較しない」という記述も、Yoshinaka 2015 §8 と整合しない。定理の正誤と新規性を切り分けて、論文の主張を再構成すべきである。

判定内訳（29件）：CORRECT 11、CORRECT-WITH-FIX 8、GAP 0、FALSE 0、KNOWN 10。推薦：major revision。

主張別の29判定は `VERDICTS.csv` にある。KNOWN は誤りを意味せず、正しいが指定された意味で既知・直接の帰結という判定である。定義・節見出し・未解決問題そのものは「解決された命題」として数えず、後述の網羅表で扱った。Theorem A–C は元原稿にラベルがないためCSVでは `main:A` 等の監査用IDを使用した。

主な修正点は次のとおり。

1. `thm:uniform` と `rem:uniform-known`（628–687行）：全観測の合併を扱う1-FKP包含も、先行稿 Prop. 9.7 から直ちに従う。これを独立の新しい柱として売り込まない。
2. `sec:intro`（145–147行）、`prop:learners`（405–430行）：Yoshinaka 2015 の §6 だけでなく §8 の signature refinement を比較する。ただし2015年の weak FCP 学習結果から very weak FCP の必要十分性をそのまま引用することもできない。KY2017のSPP議論を別に移植する必要がある。
3. `lem:product`（304行）：右辺の中間 terminal blocks の型が式から抜けている。表示どおりの構成には具体的反例があるが、意図された補題は積の式を直せば成立する。
4. `main:A`（151–161行）：任意の (k\ge1) で strict と読む場合、本文の核側の証人は (k=2) しか示していない。ただし同じ言語を二つの初期記号に分ければ **strong 1-FKP** まで強められる。修正証明を以下に示す。
5. `prop:deletion-upper`（728–734行）：存在しない ((E_0,\zeta)) を参照しないよう、全規則の添字範囲を明記する。
6. 表示サイズ・最大証人長・証人全体の記述サイズを区別する。(r,k) を固定する学習結果と、(k) を自由に増大させる設定を区別する。

Theorem C は、先行稿の「正例のみの識別に必要な distinguishing word」とは異なり、**任意のSPP核表示の下界**と**特定のMQ学習器の候補反駁費用**を述べる。この部分に論文を集中させる価値がある。今回確認した文献に同じ下界は見つからなかった。ただし網羅的な世界初の証明を行ったわけではない。

## 2. 読んだ資料・証拠の境界

- ZIP内 `main.tex` を全1003行読み、正本として使用した。著者のLEDGERは結論の根拠にしなかった。
- KY2017著者版は全12頁を読んだ。Prop. 2(i) の不等式はPDF p.5の画像でも確認した。**(n\le m\le2n)** が正しい。
- KY2023は本文全15頁、特に §§2–3、Lemmas 2–5、Theorem 6、guarded expressions と size の定義を照合した。
- Yoshinaka2015は §§2–8、特に §6.2 Theorem 2、§6.3 Definition 3、§6.4 Theorem 4、§8 を照合した。§9と参考文献も確認した。
- Clark–Yoshinaka2016は主に §§5.1–5.3、§§6–7、MCFG関係の該当節を照合した。概説全体を逐行再証明したという意味ではない。
- 著者先行稿は Definition 2.1、Lemma 2.2、Prop. 3.1、Prop. 5.1、Prop. 6.4、Remark 6.5、**Prop. 9.7** とそれぞれの証明を確認した。元論文全体の再査読は今回の範囲外。
- 追加一次資料：Clark 2013/2015 の著者公開PDF（Props. 3.26, 3.28）、Kanazawa–Kappé2019（Definition 3, Lemma 5）、Leiß2014著者長版（Theorem 2）。詳細URLと確認範囲は `NOVELTY.md`。
- 添付5本の参考文献PDFはすべてテキスト抽出可能だった。文字抽出の数式記号欠落があったため、KY2017の重要な不等式は画像照合した。読めない添付PDFを推測で補った箇所はない。Clark2010 ICGI本文は直接未確認であり、そこでの番号を推測して引用しない。
- ファイル名のR1表示を投稿・公開履歴の証明とは扱わない。今回の「著者先行稿に既出」は、**添付されたそのPDFの内容に対する比較**である。

## 3. 基礎補題と型の定義の逐行監査

### `lem:clark`（212–223行）— KNOWN

217行で任意の ((u,v)\in(XY)^\rhd) を取る。218–219行で各 (x'\in X) に対して ((ux',v)\in Y^\rhd) を使い、(y\in Y^{\rhd\lhd}) を代入する。220行で得た全 (x') についての包含から ((u,yv)\in X^\rhd) が従う。ここで (x\in X^{\rhd\lhd}) を使えば結論となる。空の (X,Y) でも全称量化の議論は有効。terminal words をsingletonとして挿入する帰納も成立する。Clark Props. 3.26, 3.28、KY2017 §3 Eq. (1) と重なる。

### `lem:reach`（234–243行）— KNOWN

238–240行の sentential form の解釈は規則1回ごとに包含を反転せず縮小させる。241行で到達列を合成し (uX_Av\subseteq X_S)、242行で soundness を使う。途中の非終端記号の生産性はこの補題には不要。KY2017 p.4のSPP直後の記述、KY2023 Lemma 2そのもの。

### `fact:ky`（256–268行）— KNOWN

(a) は KY2017 Proposition 10 の構成どおり。(b) は Theorems 3–6 の内容を正しくまとめている。収束は**文法の構文的安定化**であり、ある段階でたまたま正しい言語を生成したというだけではない。(c) は Proposition 2(i),(ii) および Theorem 14 の方向と (1,2) の値が一致する。

### 型付け（270–295行、`def:typed`）

fresh identity (1_\sharp\notin S) を追加するため、
(F_{1_\sharp}=\{\lambda\})、(s_0) のもう一つのfiberは (\Sigma^+)。この区別は必要である。279–283行の (pi) はsurjectivityでwell-definedとなり、非空語の像は非空語側の半群に移る。したがって空語fiberが非空語fiberに潰れることはない。291行の型整合式と293–295行の帰納・coarseningは正しい。

### `lem:product`（297–318行）— CORRECT-WITH-FIX

304行の式は

\[
\nu=\widehat h(w_0)\nu_1\widehat h(w_1)\cdots\nu_n\widehat h(w_n)
\]

とする必要がある。印刷どおりの (widehat h(w_0)\nu_1\cdots\nu_n\widehat h(w_n)) には中間 (w_i) がない。例えば (S\to AcB,A\to a,B\to b)、(h=h_{\{c\}}) では、本来 (	au(S)=\zeta) なのに式は1を返す。詳細は `counterexamples/product_formula.md`。

修正後、309–310行は (pi) の乗法性で全terminal blocksも含めて成立。311行の忘却写像で (subseteq)。312–317行では各子の実際のyieldから (
u_i) を選び、その積が親yieldの型となるので逆包含。rankは子非終端記号の数そのものが変わらない。非生産的な型コピーも生成言語が空であるという等式に含まれる。

### `lem:typed-galois`（336–351行）— KNOWN

337–340行はrestricted polarity。345–346行の二つの包含は方向とも正しく、((K^{\rhd\lhd}\cap F_\mu)^\rhd=K^\rhd) を与える。348行では (C^\lhd) が通常閉集合であることを使っている。349–350行の最後の同値は (Y\subseteq F_\mu) の前提を要し、これは340行で明記されている。Yoshinaka2015 §3のsort別concept latticeとLemma 1に対応する。

### `lem:star`（355–369行）— KNOWN

365–366行：(P_X\subseteq P_Y) により (P_Y^\rhd\subseteq P_X^\rhd)。367行：Clarkの積包含で (P_Y\subseteq P_X^{\rhd\lhd})。368行で反変性と三重適用の等式から逆包含。(n=0)、空の (X_i)、空語を含む (X_i)、空の共通文脈集合を含め成立する。KY2017 Eq. (1) / Clark Prop. 3.28 に単調性を挟む直接の帰結であり、新しい代数補題としては数えない。

### `prop:typed-prop1`（371–384行）— KNOWN

377行のfiber帰属は型整合性、378行の文脈包含はpre-fixed不等式の反変像。379–380行でtyped Galoisを適用できる。381–383行では初期成分の各々が (L) に入ることと、least pre-fixed pointの包含が両方向を与える。KY2017 Proposition 1 とfiber制限の直接の帰結。

### `def:typed-props`（386–403行）

強・弱・very weak の区別、kernelの同型性は一貫している。空の (C,K) も許す定義と、学習器の非空 (C,K) の違いは、学習定理で正規化を説明すべき。399–401行の「fiberに制限してもSPP」は、(i)右辺が元の右辺に含まれる、(ii)型整合性で親fiberに入る、(iii)実際のyieldはそのfiber内にある、の三点で正しい。「両辺に交わす」だけより、この説明が正確である。

## 4. 学習器との対応と既知理論

### `prop:learners`（405–430行）— CORRECT-WITH-FIX

結論は支持できるが、「verbatim」「sortsはfibres」で済ませず以下を補う。

**更新条件の照合**：

| KY2017 | 毎段階更新 | 新しい正例集合が前段階の文法に含まれないときのみ更新 | 初期記号 |
|---|---|---|---|
| Algorithm 1 dual | (D_i,E_i=Sub(D_i)) | (J_i=Con(D_i),H_i=Sub^{\le r+1}(D_i)) | (E_i\cap C^\lhd\subseteq L_*) |
| Algorithm 2 primal | (D_i,J_i=Con(D_i)) | (E_i=Sub(D_i),H_i=Sub^{\le r+1}(D_i)) | (K\subseteq L_*) |

413行の (E_i) はこのprimal側の**最後のreset時の集合**であり、常に (Sub(D_i)) と等しいわけではない。原稿の系は包含しか使わないので問題はない。

**有限反駁が存在する理由**：dualの非終端記号は (C\ne\emptyset) なので (C^\lhd\cap F_\mu\subseteq Sub(L_*))。無効な規則には各右辺成分内の有限個の反例文字列があり、それらはいつか (E_i) に入る。無効な初期記号にも同じ議論を適用できる。primalでは (K_0\ne\emptyset) のため、規則を反駁する (c\in K_0^\rhd) は (Con(L_*)) に属し、いつか (J_i) に入る。typed validityは447–468行の同値により、まさに同じテストでよい。

**十分性の有限基底**：対象文法をtrimする。各非終端記号の非空kernelとcontext、その文法の各terminal tupleを含む有限の正例集合が存在する。これらを含めるresetが起これば、対象文法の同型像の全valid規則が以後残る。resetが起きなければ非終端記号とterminal tuplesは既に固定され、有限個の規則・初期記号が反駁によって単調に減る。いずれも安定化し、上記必要性から正解となる。この説明はKY2017 Theorems 3–6の移植である。

**空の証人の正規化**：生産的な (A) で (K_A=\emptyset) なら、yield (w_A\in cl_\mu(\emptyset)) を取り ({w_A}) に置換できる。通常のbottom閉集合に (w_A) が属するので閉包は変わらない。(C_A=\emptyset) なら成分は (F_\mu)。到達文脈 (c_A) とlem:reachから ({c_A}^\lhd\cap F_\mu=F_\mu) である。(k\ge1) を保つ。

**sorted引用の注意**：Yoshinaka2015は distinguished output sort (O_*) を持つ。全fibresを異なるsortにしつつ任意の型を初期記号にする本稿の表記とは、そのままでは一致しない。出力sortと各fiberからの恒等埋込みを付加する対応を説明するか、上記KY2017移植を主証明にする。Yoshinaka2015 Theorem 4はweak FCPの十分性であり、very weak FCPの必要十分性を単独で述べてはいない。結論の反例ではなく、引用・証明の補完で直る。

### `rem:exreg`（432–441行）— KNOWN

KY2023 §§2.1,2.2の定義により、有限 (C) とregular (F_\mu) の交わりはextended regular closure内である。より具体的に、(R_\mu) を (F_\mu) のregular expression、sizeを (b_\mu) とする。(1\le m=|C|\le k) なら

\[
e_{C,\mu}=((u_1,v_1)^\lhd\cap\cdots\cap(u_m,v_m)^\lhd)\cap R_\mu,
\qquad size(e_{C,\mu})=2m+b_\mu.
\]

KY2023 §3.2のguarded定義を満たす。空の (C) は前項の到達文脈で1個に置換する。多初期記号から新たな開始記号 (S\to A (A\in I)) を作り、その解釈を (L=(\lambda,\lambda)^\lhd) とすれば、rankは (max(r,1))、式サイズ上限は (max(1,2k+\max b_\mu))。KY2023 Lemmas 2,4 と Theorem 6 に接続できる。**regular expressionへの変換サイズが型付けの記述サイズに対して多項式とは限らない**ので、固定型の質的包含と量的効率は分ける。

## 5. 核縮約・観測の比較・厳密性

### `lem:reduction`（447–468行）— KNOWN（直接の帰結として）

結論は正しい。新規性の評価は低い。KY2017 §4 p.6には既に、規則validityと (K_0^\rhd\subseteq(w_0K_1\cdots K_nw_n)^\rhd) の同値が明記されている。そこにhomogeneityとrestricted closureを加えた以下の導出は短い。

453–456行：(P_0^\rhd=P_1^\rhd=P_2^\rhd) はlem:starの2回の適用。(P_1\subseteq F_{\tau(A)}) は各子closureがそのfiber内にあるため成立。457–460行：typedとuntypedのいずれの包含も同じ文脈包含に翻訳される。(P_2) 自体のhomogeneityは要求しない。この点に型を忘れることによる穴はない。

462–467行：pre-fixed性が成立した後は実際のyieldが両成分に含まれる。従ってsoundnessの残る条件は全初期 (S) で成分 (subseteq L)。これは両方とも **(K_S\subseteq L)** と同値である。十分性は空文脈が (K_S^\rhd) に属すること、必要性はkernelのextensivity。空kernelにも成立する。複数初期記号でも各成分が (L) に入ることは和集合条件と同値。

この補題を有用な明示化として残すことには賛成だが、既存のclosure calculusから独立した新原理とするのは過大。

### `thm:duality`（475–511行）— CORRECT

(a) 485–486行の弱→very weakはtyped Prop.1で正しい。487–492行ではKY Prop.10のterminal規則を加える際、そのyield (w\in K_A\subseteq F_{\tau(A)}) により型が一致する。通常closureの等式をfiberと交わしてtyped弱性を得る。

(b) 494–500行では、(h)-homogeneousなkernelは (pi) によってcoarsenしても (s)-homogeneous。文法そのものを変えず (	au) を (pi\tau) に置換でき、rank・terminal長・核サイズは不変。fresh identityの扱いも正しい。

(c) 502–510行では、文法積の各copyの成分を (X_A\cap F_\nu^h) とする。右辺は元 (X_A) と新fiberの両方に入り、全開始copyの和は元 (X_S)。strongの場合は生成言語そのものに対するproduct lemmaが使える。untyped→typedには同じ構成で最初のfiber制約を不要とすればよい。**untypedと (s_0)-typedを同一視していない。** weak FCPで同じ証明が動くとは主張していない点も正しい。

### `cor:primal-dominated`（513–525行）— CORRECT

証明で使うcoarsening/reductionは文法を保持するので、同じ (r,k) の学習器を比較できる。結論は「どちらもいずれ収束する」という可学習性の包含であり、収束段階、query数、データ長の大小ではない。この意味を表題付近にも明記した方がよい。

### `prop:strict-context`（533–562行）— CORRECT

上界の2規則群はそれぞれ (a^mcb^{2m})、(a^mdb^n, n\le m\le2n) を生成し、(c)-indicatorが両者を分ける。両初期成分のcontextは空文脈1個でよい。

547–553行：pumpはmarker (c) を含めず両側に伸び、全pump値でc成分に留まるので (j=2i,i>0)。554行：Eはcを含む非空yieldを持つため (s_0)-typedならfiberは必ず (\Sigma^+) であり、(F_{1_\sharp}) ではない。

555–558行：許される文脈は ((a^{q-i_2},b^{2q-j_2}))。(m\ge2q) を全qについて取れば
(2m+2q-j_2\le3m\le3m+q-i_2\le4m\le2(2m+2q-j_2))。従ってd成分の条件「b個数≤a個数≤2b個数」を満たす。559–561行：到達文脈はpump反復を含み、b側が傾き2i、a側がiで増えるので破綻する。非空語を使うため (s_0) にも同じ矛盾が残る。

### `prop:strict-kernel`（564–611行）— CORRECT、さらに強化可能

(Z=\{z\}^{\rhd\lhd})、(Y=\{y\}^{\rhd\lhd})、(T=\{z,y\}^{\rhd\lhd}) とする。実際には

\[
Z=\{a^mb^n:m>n\}\cup\{a^mzb^n:m\ge n\},\quad
Y=\{a^mb^n:m<n\}\cup\{a^myb^n:m\le n\},\quad
T=L_K=Z\cup Y.
\]

空文脈がzとy双方の分布に含まれるためclosureはまず (L_K) の部分集合。z文脈は差 (m-n\ge0) を任意に追加する。unmarked語の差が負なら等しくする文脈で落ち、正なら残る。y-marker語はaを十分追加すれば落ちる。これでZの等式、対称にYの等式が分かる。

**全15規則のpre-fixed確認**：

| 規則 | 必要な包含 | 理由 |
|---|---|---|
| (S\to A), (S\to W) | (Z\subseteq T) | ({z,y}^\rhd\subseteq D(z)) |
| (S\to B), (S\to W') | (Y\subseteq T) | 同じく (D(y)) |
| (S\to aSb) | (aTb\subseteq T) | 両個数差とmarkerを保存 |
| (A\to a) | (a\in Z) | すべてのz文脈で差が正 |
| (A\to aA) | (aZ\subseteq Z) | z文脈のa個数を1増やす |
| (B\to b) | (b\in Y) | 対称 |
| (B\to Bb) | (Yb\subseteq Y) | y文脈のb個数を1増やす |
| (W\to z) | (z\in Z) | extensivity |
| (W\to aW) | (aZ\subseteq Z) | 上記 |
| (W\to aWb) | (aZb\subseteq Z) | 個数差を保存 |
| (W'\to y) | (y\in Y) | extensivity |
| (W'\to W'b), (W'\to aW'b) | (Yb,aYb\subseteq Y) | 対称 |

規則数はSが5、A/B各2、W/W'各3の計15。上表には複数規則を同じ行にまとめた箇所がある。

597–598行のsoundnessは空文脈で成立する。s0への制限では全closureは (L_K\subseteq\Sigma^+) に入るため変わらない。

600–610行の下界は文法内部を調べる必要さえなく、**全てのtype-1初期成分**でPを覆う必要から成立する。(K_S\subseteq P)、有限個の有限kernelについて (|m-n|\le p) と置く。(a^{p+1}) は共通文脈 ((\lambda,b^{p+1})) に失敗する。一方この文脈は全kernel語をPに送る。空kernelにも全称条件は成立し、さらに ((ba,\lambda)) はどんな語も (L_K) に入れないのでbottomは空。この点に初期記号・空kernelの抜けはない。

**k=1への強化**：Sを二つの初期記号に置き換え、
(S_+\to A\mid W\mid aS_+b)、(S_-\to B\mid W'\mid aS_-b)。他の規則はそのまま。
(L(S_+)=Z,L(S_-)=Y)。(S_+,A,W) のkernelを ({z})、(S_-,B,W') を ({y}) とすればvery weak 1-FKP。さらにAとWを統合して (S_+\to a\mid z\mid aS_+\mid aS_+b)、対称な (S_-\to b\mid y\mid S_-b\mid aS_-b) とすれば、各成分の生成言語がZ,Yそのものとなり **s0-typed strong 1-FKP**。h側の下界は不変。これでTheorem Aの任意 (k\ge1) のstrictnessが補える。

### `cor:invariant`（613–620行）— CORRECT

KY2017 Prop.2(ii)のPにtyped SPPがあればreductionで通常SPPが得られ、既知の非存在と矛盾する。有限の任意kについて成立する。

## 6. 全観測に共通のprimal学習器

### `thm:uniform`（628–668行）— KNOWN（添付先行稿＋既知結果の直接の帰結）

**証明の正しさ**：642–646行でbinarizeを先に行い、次に型付き細分化する順序は正しい。CFGなら補助記号を導入してrank≤2にでき、productはrankを保つ。trim後にはyieldとterminal reaching contextがある。空言語は空の初期集合の文法として別扱いすればよい。

649–654行：(mu=1_\sharp) では両語が空語。その他は同型の非空語が同じ到達文脈を共有するのでsubstitutabilityが使える。単に同型であることだけから分布同値を導いていない。singleton closureに入る語は選んだ到達文脈も受け入れるため、中間集合との等式の両方向が成立する。

655–659行：各子の代表yieldを連結した (w') は実際の親yieldであり、親の到達文脈を共有する。starから右辺積の分布が (D(w')=D(w_X)) となるためpre-fixed。660–661行は初期代表がLにあることからsoundness。663–665行では加えるterminal規則のrankは0。667行でKY2017 Theorem 6 のrank2・k1・very weak仮定を全て満たす。

**新規性**：添付著者先行稿 **Prop. 9.7（PDF pp.20–21、印刷行803–816）**は既に (igcup_s\mathcal C_s^{cf}\subseteq CONG) を述べ、その証明はtyped refinement後に各非終端記号のyieldの分布が等しいという、上と同じ論証である。Yoshinaka2015 §6.3 Definition 3 / 直後の記述によりcongruential grammarは1-FKP。先行稿Prop.9.7の入力文法を最初からbinaryにすればrank2であり、KY2017 Theorem 6から同じuntyped learnerが全合併を学習する。観測器を入力に渡す必要はこの導出にもない。

この導出はMAT学習器のequivalence queryを置き換える議論ではない。使用しているのは**positive text＋membership queriesのKY2017 Theorem 6**であり、学習モデルを混同していない。型付きcontext側の(i)の補足はYoshinaka2015 §6.1のsort別substitutabilityにも近い。

### `rem:uniform-known`（670–688行）— CORRECT-WITH-FIX

675–676行の新規性の言い方を修正する。残りの数学は正しい。regular languagesを全て含むことから全有限言語と無限言語を含むので、Goldの正例のみの障壁を適用できる。strict inclusionの証人は、同じ型の (a^i,a^j (i<j)) に対して ((a^\ell,db^\ell))、(ell\ge j) が共通文脈となり、((\lambda,cb^{2i})) は片側しか受け入れない。両語は非空で、どの有限semigroupでも鳩の巣原理が使える。最後の「data量は主張しない」は妥当。

## 7. 削除族と下界

### `lem:nodes`（706–721行）— CORRECT

712–715行：各括弧対は文法節点であり、level-iのyieldのnesting depthはi。716行のj=0ではaはleaf。717–719行のj≥1では最初の開き括弧のmateは最後の括弧で、部分語の内部で対応が完結するため外側の語でも同じ対応となる。従ってその**出現位置**が一つの節点yield。深さjからE_jが決まる。720行のsubtree置換は文法の非終端記号を保つ。「同じ文字列が別の場所の節点yieldである」という弱い主張にすり替えていない。

### `prop:deletion-upper`（723–749行）— CORRECT-WITH-FIX

(a) 738–742行の文脈はleading ceilingsを順に消去するためE_iの言語を正確に切り出す。u_iの任意の出現がE_i節点であることをnodesで示し、同levelのyieldに置換できるので (L(E_i)\subseteq\{u_i\}^{\rhd\lhd})。指定contextで逆包含が従う。S0にもEnと同じkernel u_nと空文脈を使えばよい。n=0でも(a)は成立する。

(b) 型1コピーはi=0,…,n−1、ζコピーはi=1,…,n。floorのtype1規則は **1≤i<n**。ζ-floor規則は **1≤i≤n、既存の子コピーだけ**を取り ((\alpha,\beta)\ne(1,1))。ζ-ceiling規則も既存の子コピーだけを使う。特にi=1のζ-floor規則はなく、ceilingの子は ((E_0,1)) のみ。原稿はこの制約が不明瞭。

修正後、744–745行の帰納はfloorで「片方以上ζ」、ceilingで「子によらず親がζ」により成立。746–748行のi<nの文脈自体がceilingを含むので、削除語を完成させることがない。i=nは空文脈でM_n。文法sizeはO(n)、最大context長O(n)。context証人を各記号に文字列として重複記録した総量はO(n²)。

### `lem:capture`（751–768行）— CORRECT

759–760行：到達文脈に対しkernelもclosure内なので (pK_Bq\subseteq M_n)。761行：xがR内なら右のu_{n−1}は丸ごとq内に残り、その置換で (pxq'=w_n^*)。762–764行：kを入れた語でも同じ末尾の出現はnodes補題によるE_{n−1}節点であり、置換後はL_n内。764–765行：M_nから外れる唯一の可能性は (pkq'=w_n^*)。自由モノイドのcancellationによりk=x。766–767行：(x\in K_B^{\rhd\lhd}) より (K_B^\rhd\subseteq D(x)) だが ((p,q')\notin D(x))。従って同文脈を拒否するkernel語が存在し、それがx。

空kernelが許される場合も、該当するBのkernelは空でないことをこの議論自体が示す。ε-yieldは位置を「R内のgap」と解釈すれば同じ証明が使えるが、cover下界には正長yieldだけが必要。自作計算ではgapも検査した。

### `thm:deletion`（770–798行）— CORRECT

782行の最小node数の木は、自然数の整列性で選べる。783–787行：同じpathにAが繰り返すなら、その間のα,βは選んだ木の固定terminal yields。長さが正ならpump回数で長さが厳密増大し無限に異なる語を生成する。両方空なら上のA-subtreeを下のA-subtreeで置換してzを保ちnode数を減らす。従ってpath上の非終端記号は重複しない。

788–789行：rとr+1を両方含む節点は全て祖先・子孫関係にありterminal leafではない。従って高々|N|個。790–794行：任意のq≤rについてqを含む最深のchain節点が存在する。qがその規則のterminal occurrenceなら1文字を取る。それ以外ではqを含む直下の子はchainでない。その子がr+1まで延びればrとr+1の両方を含み矛盾するため、子yieldはR内。chainの各節点の各RHS occurrenceにpieceを高々一つ対応させ、高々ρ|N|個で覆える。**terminal blockを1記号とは数えず、ρは文字数＋非終端記号数**である。

794–797行：nonterminal pieceにcapture、terminal pieceに長さ1を適用する。rは (1+(3\cdot2^{n-1}-2))。typed版はreductionで文法も核も変えず移る。M_nが非空でcaptureが適用されるため、少なくとも一つのkernel語が存在し最大長κを定義できる。到達不能記号を残しても|N|を大きくするだけ。

この証明は特定のG_nだけでなく、M_nを生成する**任意の有限CFGと任意の有限kernel SPP**に適用する。kernel cardinalityは固定していない。

### `cor:primal-data`（800–816行）— CORRECT

810–811行は安定化したgrammar全体がSPPを持つというKY2017 Theorem 4 / typed版を使う。単なるlanguage equalityでは不十分。812–815行は次のように確認できる。

- primalの (E_i\subseteq Sub(D_i))。全kernel語長≤(|D_i|)。
- (m=|Sub(D_i)|\ge1)。非空でsize≤kのsubsetの個数は (sum_{j=1}^{\min(k,m)}\binom mj\le m^k)。整列した要素列を最小要素の反復で長さkに埋めれば単射となる。
- homogeneousな非空kernelの型は一意。typed版に (|S|) 倍を加える必要はない。
- 長さlの語のsubstringsは高々 ((l+1)^2) 個なので、(|Sub(D_i)|\le\|D_i\|^2)。
- RHSには≤r個のnonterminalsと≤r+1個のterminal blocksがあり、ρ≤((2r+1)|D_i|)。
- 以上の積は≤((2r+1)\|D_i\|^{2k+2})。deletion下界を代入すれば記載の式になる。

r,k固定ならnに指数的。kがnとともに増える場合には、表示された式をそのまま用い、固定指数の指数下界とは言わない。

### `prop:dual-refutation`（818–851行）— CORRECT

827–831行：tは最後のreset。Algorithm 1はその後J,Hを保持しEを毎段階更新する。構文的に安定したgrammarに無効規則があれば、(C\ne\emptyset) により反例yieldはSub(M_n)にあり、いつかEに現れて規則が消えるので矛盾する。typedでも同じ。

833–836行：D_tは非空。任意のdatumはceiling-rootかfloor-root。floor-rootでは右子がζなら左子をhole、左子がζなら右子をholeに選ぶ。外文脈はceilingを含み、許す語は正確に (L(E_{n-1}))。837–839行：limit grammarの全terminal symbolsはH_t由来。M_nにはfloorを含む語があるのでD_tにfloorが必要。同じdatumの後方にcloseもあり、非重複terminal tuple ((\lfloor,\lambda,\rfloor)\in Sub^3(D_t)\subseteq H_t)。ここでr≥2を使う。

841–844行：({(\lambda,\lambda)}) はJ_tのsingletonで、常に初期条件を満たす。右辺の ({c}) もk≥1で候補集合に入る。level-(n−1)語二つのfloor連結は必ずL_nに入り、M_nを外れるのは両方が (w^*_{n-1}) のときだけ。その語がE_iにないと候補を削除できない。

846–850行：typed候補の親はζ、子は1とζ、floor terminalsは1なので整合する。**親は初期記号でなくてよい。** Algorithm 1は到達性による候補削除を行わない。n≥2なのでζのlevel-(n−1)語がある。左子のtype1 denotationはsingleton ({w^*_{n-1}})。実際の右辺yieldはdepth nなので親denotationには入らず無効だが、E_iにこのsingleton語がなければtest右辺は空となり通過する。

従って候補が集合から漏れる、型が違う、初期条件が違う、という穴はない。これは**指定のAlgorithm 1の全候補を保持する実装**の下界。任意のdual learning method・任意のMQ学習器の下界ではない。到達不能・非生産的候補のpruningを加えた別実装への移植は別証明を要する。

### `rem:deletion-table`（853–872行）— CORRECT-WITH-FIX

kernel/context行のO(n)はgrammar sizeと**最大**証人長それぞれの上界と明記する。証人を非共有で全て列挙するサイズはO(n²)。kernel下界はρ|N|max(κ,1)でありgrammar size単独の指数下界ではない。positive-onlyの行は著者先行稿の再構成器またはクラス全体にcharacteristic samplesを持つoperatorに関するもので、MQ学習器のconvergence dataと同一の指標ではない。

## 8. Theorem A–Cの総合判定

- **A：CORRECT-WITH-FIX。** underlying dualityは正しい。k2の証人をk1へ強め、strictnessがs0とindicatorの間を指すことを明示する。untypedとs0間の端点包含まで全てstrictと読む表現は避ける。新規性は基本包含より具体的分離例にある。
- **B：KNOWN。** 結論は正しい。著者先行稿Prop.9.7＋Yoshinaka2015 §6.3＋KY2017 Theorem 6の直接の帰結。
- **C：CORRECT。** productの積・H_nの添字を直せば記載の主張が従う。データ下界を含め、今回の照合範囲では最も独立性の高い結果。

## 9. 計算結果と限界

実行方法と入力hashは `logs/reproducibility.txt`、stdoutは各logに保存した。

| 計算 | 結果 |
|---|---|
| 著者 deletion、n=2,3,4 | 全通過。capture pairs 17、108、1204 |
| 著者 reduction、4000 trials | identity 4000/4000、rule equivalence 2186/2186、反例0 |
| 自作 finite reduction、二文字語長≤2上の全128言語、3型 | star 3,940,992件、規則同値61,636,736件、initial soundness 7,296件、全通過 |
| 自作 L_K | 長さ≤7の全21,845語と下界9例。無限言語の正確なmembershipで検査し全通過 |
| 自作 deletion | 全datum選択文脈5、41、1805個。空yieldも含むcapture 23、120、1228件、全通過 |
| 自作 weak候補 | `logs/weak_candidate.txt`。typed単調性の決着を意味しない |

著者reduction scriptは**trialごとに5型から一つを選ぶ**。4000言語×5型の全走査ではない。nonempty kernel、nonempty common-contextに限定し、εをkernelから除く。自作finite reductionはempty kernel、ε、empty language、無限closure (\Sigma^*) も含めた。無限集合を短い語の集合で代用せず、unboundedな集合として扱っている。

著者scriptはseedが固定でもset→list順序がhash randomizationに依存する。`python3 -I` はPYTHONHASHSEED等を無視するため、rule件数2159は必ずしも再現しない。今回2186という差は反例ではない。再現性にはsortを入れるべき。

これらは全て**計算的証拠**であり、無限言語・全CFG・任意の有限半群に対する証明ではない。一般性は前節までの証明監査による。

## 10. 未解決問題への取り組み・残りの監査範囲

### `op:weak-fcp`（877–888行）

原稿の障害の説明は正しい。(L_A\cap F_\nu) を先に取ると分布が増えてclosureが縮むので、元の有限context集合が同じclosureを表すとは限らない。

追加成果として、second marker候補の**untyped positive half**は全非終端記号を確認できた。KY2017 Lemma 12の言語L'に、L1内のmarkerをfresh @に置換した言語だけを加える。文法はLemma 12の文法に **S1→@** を追加する。さらに@-indicatorではtyped weak FCPが存在しない負側も示した。ただしtyped-to-typed単調性の決着ではない。全12非終端記号についてweak 2-FCPが保たれる証明とcontext表は `WEAK_FCP_PARTIAL.md` に記載した。

ただし**untyped weak FCPからs0-typed weak FCPへの移行は今回未解決**。nullable成分を正長とεに分けるだけでは、問題そのもののclosure交換を仮定する。従ってこの候補をtyped単調性への完成した反例には数えない。

また全有限言語Lは任意のsでtyped strong 1-FCPを持つ。各非空 (L\cap F_\mu) に初期S_μを置き、全 (w\in L\cap F_\mu) についてS_μ→wを列挙する。各成分は空文脈一つで表せる。空言語は初期集合空。このため**有限言語だけの探索で、言語クラスとしてのweak FCP単調性への反例は得られない**。

### `op:robust`（890–897行）

markerを分けるとKY2017 Lemma 13の特定のwitnessが別fiberになるという指摘は正しい。しかしそれだけではtyped weak FCPを実現する文法の存在を証明しない。任意sでの分離は今回解決していない。

### `op:Mn-context` の部分主張（899–906行）— CORRECT-WITH-FIX

single-ζ-nodeを「ceiling規則がちょうど1回で、その節点がlevel j≥1」と定義すると、明確な補題になる。節点yieldは (v=\lceil w^*_{j-1}\rceil)。これを (w^*_j) に替えると (w^*_n) となり、長さ増分は (Delta=|w^*_{j-1}|)。

任意のuntyped context SPP文法で、constituent xがvの出現を丸ごと含むとする。置換後をx'とすれば到達文脈は削除語へ送るので、reachより (x'\notin X_A=C_A^\lhd)。ある (c\in C_A) がxを受け入れx'を拒否する。(c[x]\in M_n\subseteq L_n) で、元のceiling-subwordはnodesにより同level節点。置換後もL_nなので、拒否されるなら (c[x']=w^*_n)。従って最大context長ℓに対し

\[
|x|=|w^*_n|-|c|-\Delta\ge|w^*_n|-\ell-|w^*_{j-1}|.
\]

原稿の曖昧なO項をこの形に置換できる。ただし、このようなconstituentの存在・coverを全体の表示下界へ転換する部分は別問題で、open problem全体を解決してはいない。

### 残りのラベル・無ラベル主張

- `def:typed`, `def:typed-props`：§3で監査済み。定義なので判定件数には含めない。
- `sec:*`：節ID。序論の新規性の問題はISSUES/NOVELTYに記載。
- `app:comp`（924–938行）：sampling範囲・再現条件の補修が必要。CSVに記載。
- filtered kernels（908–914行、無ラベル）：mixed kernelを許すなら、untyped kernel SPPのproduct copiesに同じkernelを保持する構成はpre-fixedかつsound。L_Kの表示にも同じ構成が適用でき、包含は正しい。ただしL_Kは既に通常FKP内なので、この例だけではstrictnessを示さない。
- 最後のopen problems（916–920行、無ラベル）：質問であり肯定命題と数えない。weak kernelの反単調性をstrongへ無根拠に移してはいない。

## 11. 投稿先・文章・構成

**I&C**：任意SPP表示の下界と学習アルゴリズムの限界を中心にすれば適合性が高い。現状はBの既出性と既知補題の多さが弱点。Cを中心、Aを比較原理とstrict witnesses、Bを応用の系とする構成を勧める。

**JoLLI**：sort別concept latticeと分布学習には合う。Yoshinaka2015 §8とKY2023の関係をより正確に整理する必要がある。typed contextとhomogeneous kernelという定義の非対称性を早めに具体例で説明するとよい。

**TCS**：grammar complexityの下界として適合しうるが、著者のTCS先行稿との重複範囲を冒頭で明示することが必要。以上は研究内容との適合性であり、最新の編集方針や採択確率の予測ではない。

`patches/main.tex.diff` は最小限の修正提案。元ZIPの原稿は変更していない。新規性の位置づけ、product式、k1の証人、H_nの添字、学習器とsizeの説明を対象とし、未解決問題の追加成果は別紙に留めた。

差分の検査：`patch --dry-run -p1` は通過し、実適用後のTeXが提案版と一致することを確認した。PDF再ビルドは環境のTeX format/bundle不足で完了していない。数学的検証と差分の適用可能性の検証を、コンパイル成功と同一視しない。
