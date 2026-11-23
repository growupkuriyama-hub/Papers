# R15　方向C：Strahler 数で切った部分クラスでの型付けの境界 — 報告（Claude Opus 5.5、2026-11-23）

**ラベルはすべて自己判定である。** 確認も同じモデル系列（Claude）の読み直しであり、独立した監査ではない。VALID は「自分で証明を書き、別の観点から読み直し、有限検査とも矛盾しない」という意味でしかない。

**結論（3 行）**
1. **上界（C2）**：どの有限半群型付けでも、どの fan-out でも、次元（全導出木の Strahler 数の上限）が $b$ 以下の reduced good な提示なら、特徴データは $O_{f,r,|\mathsf S|,b}(\|G\|^{b+2}\bar\theta_G)$ である。証明は RV1 (ii) の論法をラベル $(B,\widehat s^{(d)}(\mathbf u))$ に読み替え、`thm:data-from-typed-thickness` に代入するだけで済む（C0）。〔VALID〕
2. **下界（C3、fan-out 1）**：$U_1$ への型付け $s_{U,3}$ では、次元 $b$・$\|G\|=(13b+11)n+3$・$\bar\theta_G=(4b+2)n+2$ の Clark–Eyraud 代入可能な有限言語 $L_{n,b}$ が、どの特徴標本にも長さ $(n+1)^b(2n+3)-2$ の語を強いる。したがって次数は $(b+1)/2\le\delta_{s_{U,3}}(b)\le b+2$ となり、$b$ とともに増える。LG なら $\delta\le2$ で一様。fan-out 1 では「LG の境界は次元が有界でなくなる極限で初めて現れる」という閉じた二分法になる。〔VALID〕
3. **fan-out 2**：$L_{n,b}$ は冪移送（`lem:power-transfer`）で倒れ、持ち上がらない（具体的な二穴 Rect 違反あり）〔VALID〕。fan-out 2 で次数が $b$ とともに増える族があるかどうかは **OPEN**。ただし、この問いは内容型付け $c_\Sigma$（$|\Sigma|\ge3$）に帰着する〔VALID〕。C2 から、`op:fanout-two` を肯定する族は次元 $\to\infty$ でなければならない（構造的な必要条件）〔VALID〕。

---

## 1. 読了表

| 資料 | 読んだ範囲 | 未読・注記 |
|---|---|---|
| `02-v4/research/README.md` | 全文 | — |
| `02-v4/v2/reviews/PAUSE_FALSE_ROUTES_2026-11-16.md` | 全文 | 参照先の監査ファイルは未読 |
| `02-v4/main.tex` | l.520–780（定義、`def:tuple-substitutable`、`def:class-cmcf`、`lem:filling-identity` 付近）、l.1050–1470（`lem:thickness-equivalence`、`lem:witness-length-template`、`thm:data-from-typed-thickness`、`prop:rare-type`、`prop:typed-thickness-exponential`、`cor:distribution-representatives`、`lem:heavy-node-count`）、l.1680–1740（`thm:local-group-polydata` と定数）、l.1975–2025（`def:uniform-polydata`、`thm:fanout-one-data`）、l.2296 付近（`cor:two-letter-fanout-one` の主張）、l.2570–2850（`lem:power-transfer`、`thm:doubling-no-lift`、`lem:typing-monotone`、`prop:sl-reduction`、`thm:two-letter-content` の主張、`op:fanout-two` と直後の段落、`prop:zeta-capacity` の主張）、l.3688–3810（`thm:rankone-polydata` **証明全文**、`thm:binary-u1-polydata` の主張）、l.5100–5175（`lem:rank-one-edt0l` と証明）、l.8225–8275（`conj:rare-types` と注記）、l.9285–9346（R8：H1〜H4）、l.9540–9740（`rr:RV1-crossing`、`rr:RV1-audit`、`rr:RV1-wn`、R13、`sec:p4-open`） | `prop:good-normalization`、`lem:normalization-stages`、`prop:pattern-thickness-transfer`、第 IV 部の R1〜R7・R9〜R11 の節、付録はすべて未読 |
| RV1 `deliverable/report.md` | §4 全文（一般 $m$ の限定上界とその証明を含む）、§5 | §1〜§3、§6〜§9 は見出しのみ |
| RV1 確認メモ | 項目 6 | 他の項目は未読 |
| R1 報告 | 定理 2 の主張・完結部分・照合表（grep による部分読み） | 証明本体は未読 |
| R2 報告 | 結論、定理 B・C の主張と照合部分（grep による部分読み） | 証明本体は未読 |
| `01_fixed-h-cfg/main.tex`（#1） | §6（`lem:typed-thickness-bound`、`cor:typed-thickness-data`、括弧付き倍増族と `prop:typed-thickness-gap` の主張）、`prop:thick-bunf-normal` の主張、§8（`prop:linear-normal` の主張、`lem:linear-short` と証明、`thm:linear-poly` と証明） | 付録 C（括弧付き族の代入可能性）は未読（02-v3 付録 B で代用）。**Cor. 6.3＝`cor:typed-thickness-data`、Prop. 6.4＝`prop:typed-thickness-gap`、Prop. 7.3＝`prop:thick-bunf-normal`、Thm 8.3＝`thm:linear-poly` という対応は、節の順序から推定した。PDF の番号は確認していない** |
| `02-v3/main.tex` | 導入（Theorem A〜C）、§2、§3（`lem:rep-witness`、`lem:lambda-elimination`、`cor:master`、`prop:rare-type`）、§5（`thm:pseudovariety-boundary`、`rem:scope`）、§6（`prop:three-letter-family`、`cor:typing-level-obstruction`、`def:isolated-letter`、`thm:isolated-letter` の主張、`cor:isolated-data`、`cor:u1-classification`）、§7 の主張（`prop:linear-factor` とその後の注記、`prop:binary-quadratic`）、付録 B 全文（三文字倍増族の代入可能性）、付録 D.1（`lem:app-u1-insertion`、`lem:app-u1-code`） | §4（LG の証明）、付録 A・C・D.2・E は未読 |
| Ginsburg–Spanier (1966)（Core C） | プロジェクト検索で得た原頁：pp.429（序）、436、438（ultralinear の定義、Lemma 3.1）、439（Theorem 3.1）、443–444（§4：nonterminal bounded の定義、**Theorem 4.1**、rank の定義）、448–449（Theorem 5.1） | pp.430–435、437、440–442、445–447、450–453 は未読 |
| Esparza–Luttenberger–Schlund (LATA 2014) | **WebFetch の要約で**、index と Strahler 数の関係（CNF では「index $k$ ⟺ Strahler 数 $k-1$」）、tree dimension＝Strahler 数、caterpillar を確認。**全文は精読していない** | 有限指数・nonexpansive への言及はない、と要約は述べる |
| Ganardi–Lohrey, arXiv:2512.19060 | 検索結果の抜粋のみ（CNF の導出木で「st+1＝最小の index」） | 本文は未読 |
| Denkinger (DLT 2016, arXiv:1606.02975) | 要旨と目次のみ（制限つき tree-stack automata ⟺ MCFG、$k$-restricted ⟺ $k$-MCFG） | ターンや次元の制限は見つからなかった |
| Salomaa、Gruska、Brainerd（有限指数）、Gallot (2021)、Villemonte de la Clergerie（thread automata）、Vijay-Shanker（EPDA）、Yoshinaka (2011)、Yoshinaka (2015, MoL) | **未読** | 言及はすべて「記憶による。未確認」か「compendium の引用による」と明記した |

---

## 2. C0　既知との照合

**判定：C2 の上界は、既存の二つの結果を組み合わせると数行で従う。** 一行で済ませるには、三点の確認が要る。

> RV1 (ii) の論法（路の上で同じラベルが繰り返したら、子孫の部分木を祖先の位置へ代入する。Strahler 数は増えない。その後、分岐を数える）を、ラベル $(B,\widehat s^{(\mathrm{fan}\,B)}(\mathbf u))$ に対して使うと $t_{\rm typ}(G,s)\le\theta_G\cdot\mathrm{Nd}_r(|V||\mathsf S|^f,b)$ が得られる。これを `thm:data-from-typed-thickness` に代入すればよい。$b=0$ の場合が `thm:rankone-polydata` である。

確認すべき三点（§4 で扱う）は次のとおり。

- RV1 (ii) のラベルは（非終端、成分の内容の和集合）である。これは内容型付けの**根の型**には十分だが、一般の型付けでは成分ごとの型ベクトルが要る。ラベルの数は $|V|2^{|m|}$ から $|V||\mathsf S|^f$ に増える。
- 特徴標本の文脈 $\chi(X)=E_B$ は**型によらない**導出文脈であり、$|E_B|_{\rm fix}\le\theta_G$ を満たす（`lem:thickness-equivalence`(iv)）。到達文脈の長さには次数が付かない。
- 代入による置換は文法の上の操作（文脈自由性）であり、代入可能性は使わない。

**使えない近道が二つある（どちらも確認済み）。**

1. **言語の水準での潰し込み。** 次元 $b$・rank $r$・fan-out $f$ の MCFL は、fan-out $((r-1)b+1)f$ の rank 1 の MCFL になる（§3.2 の命題 M3。スケッチ）。しかし `thm:rankone-polydata` を高い fan-out で使うには、$L\in\mathcal C^{\mathrm{mcf}}_{((r-1)b+1)f,s}$ が要る。クラスは $f$ について単調でない（`def:class-cmcf` の後の注記 (b)）。実際、§5.3 の $L_{n,b}$ は $\mathcal C^{\mathrm{mcf}}_{1,s}$ に入るが $\mathcal C^{\mathrm{mcf}}_{2,s}$ には入らない。したがってこの近道は使えない。
2. **#1 の BUNF 経由（Cor. 6.3＋Prop. 7.3）。** 二分化は次元を上げることがある。rank 3 の規則 $A\to BCD$ の子の Strahler 数が $(m,m-1,m-1)$ なら、元の値は $m$ である。右くし型の二分化 $A\to BA'$, $A'\to CD$ では $A'=m$、$A=m+1$ になる。子の値は導出ごとに変わるので、規則ごとに固定した二分化でこれを避けられるとは限らない（一般の不可能性は示していない）。そこで、提示の次元で定理を述べるには、正規化をしない compendium 第 I 部の枠組み（reduced good・rank $\le r$ の提示に直接 `thm:data-from-typed-thickness` を使う）を用いる。

**残る本当の問いは C3（下界）である。**

---

## 3. C1　定義、判定条件、機械との対応、部分クラスの問題

### 3.1 定義

Strahler 数 $\mathrm{St}$ の規約は RV1 と同じにする。葉は 0、内部の節点は子の最大値をとり、最大値を取る子が二つ以上あれば 1 を加える。$g(v_1,\dots,v_k)$ をこの結合関数とする（$g()=0$）。$g$ は各引数について単調である。

**定義 D1（次元）。** reduced な MCFG $G$ に対して
\[
 \dim(G):=\sup\{\mathrm{St}(T): T \text{ は } G \text{ の（任意の非終端からの）導出木}\}\in\mathbb N\cup\{\infty\}.
\]
reduced なら、$B$ からの導出木はどれも成功導出の部分木になる（$B$ は到達可能）。Strahler 数は部分木について単調なので、成功導出だけで上限を取っても同じ値になる。

**定義 D2（型付きの次元）。** 型付け $s$ と、実現されたラベル $X=(B,\mathbf t)$（$\mathbf t=\widehat s^{(d)}(\mathbf u)$, $\mathbf u\in L_B(G)$）に対して $m_s(X):=\min\{\mathrm{St}(T):T\text{ は } X \text{ の導出}\}$ とおき、$\dim_s(G):=\max_X m_s(X)$ と定める。$\dim_s(G)\le\dim(G)$ である。

**どちらで定理を述べるか。** 主定理は構造的な $\dim(G)$ で述べる。これは文法の形だけで決まり、型付けによらず、判定できる。証明が実際に使うのは $\dim_s(G)\le b$ だけなので、上界はこのより弱い仮定でも成り立つ（定理 C2 の注）。

「最短の導出だけ」で取る版、$\dim_{\min}(G):=\max_B\min\{\mathrm{St}(T):T$ は $B$ の最短の（長さ、次に節点数が最小の）導出$\}$ は**使えない**。例：`prop:typed-thickness-exponential` の文法 $A_i\to A_{i-1}A_{i-1}\mid\mathtt c$ では、型なしの最短導出はすべて $\mathtt c$ なので $\dim_{\min}=0$ である。ところがラベル $(A_n,1)$ の導出は完全二分木しかなく、$m_s=n$、$t_{\rm typ}\ge2^n$ になる。

### 3.2 判定条件と既知の部分クラスとの関係

**命題 M1（判定）〔VALID〕。** $G$ は reduced とし、依存グラフ（$A\to$ 規則の子）の強連結成分（SCC）を考える。

1. $\dim(G)<\infty$ ⟺ どの規則も、左辺と同じ SCC に属する子の出現を二つ以上持たない（**nonexpansive**）。
2. このとき $\dim(G)\le c(G)-1\le|V|-1$ である。$c(G)$ は SCC の縮約 DAG の最長の鎖に含まれる SCC の数とする。
3. 正確な値は、$v_A:=\max_{A\to\rho(B_1..B_k)}g(v_{B_1},\dots,v_{B_k})$ の Kleene 反復（初期値は「木なし」）で多項式時間に求まる。

*証明。* (⇒の対偶)規則 $A\to\rho(\dots B_i\dots B_j\dots)$ で $B_i,B_j$ が $A$ と同じ SCC にあるとする。reduced なので、$B_i$ からも $B_j$ からも、ある節点のラベルが $A$ である導出文脈が作れる。他の子は任意の終端導出で埋める。これで $A$ を根とし、比較不能な二つの $A$ の穴を持つ「フォーク」$F$ ができる。$F$ を深さ $k$ まで入れ子にして穴を終端導出で埋めると、各フォークの節点の二つの子は帰納的に Strahler 数 $\ge k-1$ を持つので、全体は $\ge k$ になる。
(⇐)SCC $Q$ の木の中では、各節点で $Q$ に留まる子は高々一つである。$Q$ の外の子は帰納法により $\le D:=\max_{Q'}d(Q')$（$Q$ の直下の SCC について）を満たす。$Q$ 内の背骨の上の値 $x$ は、$x\le D+1$ と子 $\le D$ から $g\le D+1$ に保たれる。下に SCC がなければ値は 0 である。
(3) $k$ 回目の反復値は「高さ $\le k$ の木の最大の Strahler 数」に等しい（$g$ の単調性と、子の木を独立に選べることによる）。値は上に有界で単調なので、変化しなくなった時点で上限に達している。∎

有限検査 [A]：例に加えて、ランダムな非巡回 CFG 247 個で Kleene 反復と全木の総当たりが一致した。

**命題 M2（既知の部分クラス）〔VALID〕。**

1. reduced なら、$\dim(G)=0$ ⟺ すべての規則の rank が 1 以下。二つ以上の子を持つ節点の値は必ず 1 以上になり、reduced ならどの規則もある木に現れるからである。したがって **rank 1（fan-out 1 では線形 CFG）＝次元 0** である。
2. ultralinear 分解 $\{A_0,\dots,A_k\}$ を持つ CFG なら $\dim\le k$。定義（Ginsburg–Spanier p.438、原頁で確認）では、$\xi\in A_i$ の規則は $\xi\to u\xi'v$（$\xi'\in A_i$, $u,v\in\Sigma^*$）か $\xi\to w$（$w\in(\Sigma\cup A_0\cup\cdots\cup A_{i-1})^*$）である。$A_0$ の木は値 0、$A_i$ の脱出規則の子は $A_{<i}$ の値 $\le i-1$ を持つので、値は $\le i$ になる。逆は成り立たない。例：$S\to\mathtt aST\mid\mathtt a$, $T\to\mathtt bT\mathtt c\mid\mathtt{bc}$ は nonexpansive で $\dim=1$ だが、SCC 内の規則の外側に非終端 $T$ がある（[A] で確認）。
3. **index との関係（自分の証明）。** rank $\le r$ で $\mathrm{St}(T)\le b$ の木には、文形の非終端の数が $(r-1)b+1$ 以下になる導出がある。根の子のうち Strahler 数が最大のものを最後に展開する。こうすると、他の子を展開している間に保留されるのは高々 $r-1$ 個で、その子の Strahler 数は $\le b-1$ である。帰納法で $I(T)\le(r-1)b+1$ が出る。CNF なら $I=\mathrm{St}+1$ がちょうど成り立つ（ELS 2014、WebFetch の要約で確認。Ganardi–Lohrey の抜粋も同じ）。したがって $\dim(G)\le b$ なら $G$ は index $\le(r-1)b+1$（有限指数）の文法である。逆向きは文法の水準では成り立たない。有限指数は語ごとに一つの導出があればよいが、$\dim$ はすべての木を抑えるからである。

**命題 M3（言語の水準での潰し込み。スケッチ）〔CONDITIONAL：細部は検査していない〕。** fan-out $f$、rank $r$、$\dim\le b$ の MCFG の言語は $\mathsf{MCFL}(kf,1)$（$k=(r-1)b+1$）に入る。証明の考え方：木を帰りがけ順（Ershov の順序）にたどり、終わった部分木の組を高々 $k$ 個保留する。保留中の組の連接を一つの非終端の成分とし、終端規則の push と、規則の template による pop・合成を単項規則で書く。`lem:rank-one-edt0l`（証明は読んだ）と合わせると、有界次元の MCFL は index 有限の EDT0L に入る。逆の包含と、非分岐 MCFL＝有限指数 EDT0L という同定は、compendium が引く Gallot (2021) Theorem 29 による（**未読**）。

### 3.3 機械との対応表

| 次元の制限 | 文法の側 | 機械の側 | 典拠の状態 |
|---|---|---|---|
| fan-out 1、$\dim=0$ | rank 1＝線形 CFG（M2-1） | 1 ターン PDA | Ginsburg–Spanier の序（p.429）が §6 で扱うと述べる（原頁で確認）。#1 §8 も同じ文献を引く。§6 本文は未読 |
| fan-out 1、$\dim\le k$ | ultralinear 分解の水準 $k$ ⇒ $\dim\le k$（M2-2） | 有限ターン PDA ⟺ ultralinear（Lemma 3.1 とその逆）。ultralinear ⟺ nonterminal bounded（**Theorem 4.1**） | Lemma 3.1 と Theorem 4.1 は原頁で確認。逆向きの証明（§2）は未読。$(2k-1)$ ターンの PDA から得られる分解は $A_1,\dots,A_{2k}$ なので、$\dim\le2k-1$（p.438 の記述からの自分の推論） |
| fan-out 1、$\dim<\infty$ | nonexpansive（M1） | 有限指数の言語（言語の水準で nonexpansive な文法を持つもの） | **記憶による。未確認**（Salomaa、Gruska、Brainerd）。index と Strahler 数の関係（CNF）は ELS で確認。文法の水準の包含 $\dim\le b$ ⇒ index $\le(r-1)b+1$ は自分の証明（M2-3） |
| fan-out $\ge2$、$\dim=0$ | rank 1（非分岐）MCFG | 有限指数 EDT0L（index $\le f'$） | 一方向は `lem:rank-one-edt0l`（証明を読んだ）。同値は Gallot (2021) による（compendium の引用、**未読**） |
| fan-out $\ge2$、$\dim\le b$ | 有界次元 MCFG ⊆ $\mathsf{MCFL}(kf,1)$（M3、スケッチ） | 対応する機械の制限は**見つからなかった**。$k$-restricted tree-stack automata ⟺ $k$-MCFG（Denkinger 2016、要旨で確認）は fan-out の制限であって次元の制限ではない。thread automata・EPDA（WN な fan-out 2 ＝TAL）は**記憶による。未確認** | 「有限指数の LCFRS」という名の文献は検索で見つからなかった |

### 3.4 部分クラスの問題の定式化

**定義 P（有界次元の一様多項式データ）。** $f,r\ge1$、$b\ge0$ を固定する。型付け $s$ が条件 $\mathrm{UP}_{f,r}(s;b)$ を満たすとは、多項式 $p$ があって、すべての $L\in\mathcal C^{\mathrm{mcf}}_{f,s}$ と、$L\cap\Sigma^+$ の **reduced good・fan-out $\le f$・rank $\le r$・$\dim(G)\le b$ の提示** $G$ について、$\mathcal B^{\le r}_{f,s}$ が $\|F\|_+\le p(\|G\|,\bar\theta_G)$ の特徴標本 $F$ を持つことをいう。学習器は変えない。測る二量は常に同じ $G$ のものとし、`rr:RV1-wn`(i) と同じ形にする。

定理 C2 から、すべての $s$ と $b$ で $\mathrm{UP}_{f,r}(s;b)$ が成り立つ。そこで意味を持つのは**次数**である。
\[
 \delta_s(b):=\inf\{d\ge0:\ \exists C\ \forall L,G\ (\text{上の範囲})\ \ \min_F\|F\|_+\le C(\|G\|\bar\theta_G)^d\}.
\]
擬多様体については $\Delta_{f,r}(\mathbf V):=\sup_{s:\,s(\Sigma^+)\in\mathbf V}\sup_b\delta_s(b)$ とおく。

注：$\|G\|$ だけで測った次数は、LG でも自明な型付けでも $b$ とともに増える。例：一語の言語 $\{\mathtt a^{n^{b+1}}\}$ は、次元 $b$・大きさ $O(bn)$ の入れ子の鎖で書ける。データはその語を含むので $\ge n^{b+1}$ である。したがって $(\|G\|,\bar\theta_G)$ の組で測ることが本質的である。

---

## 4. C2　上界

**定理 C2〔VALID〕。** $f,r\ge1$、有限半群への型付け $s:\Sigma^+\twoheadrightarrow\mathsf S$（LG とは仮定しない）、$b\ge0$ を固定する。$G$ を reduced good・fan-out $\le f$・rank $\le r$ の提示で $\dim_s(G)\le b$（特に $\dim(G)\le b$）とする。$h:=n_{\widehat s}(G)\le|V||\mathsf S|^f$ を実現ラベルの数、$\ell:=$規則が明示的に書く終端の最大数（$\le\theta_G$、`lem:thickness-equivalence`(i)）とし、
\[
 \mathrm{Nd}_r(h,b):=\sum_{i=0}^{h-1}\sum_{j=0}^{\min(i,b)}\binom ij(r-1)^j=\sum_{j=0}^{b}(r-1)^j\binom h{j+1}\ \le\ 2r^bh^{b+1}
\]
とおく（$r=1$ なら $=h$）。このとき次が成り立つ。

1. すべての型付き非終端 $X$ について $\min_{\mathbf u\in L_X}\|\mathbf u\|_1\le\ell\cdot\mathrm{Nd}_r(h,m_s(X))$。したがって $t_{\rm typ}(G,s)\le\theta_G\,\mathrm{Nd}_r(h,b)\le2r^b\bar\theta_G(|V||\mathsf S|^f)^{b+1}$。
2. $L\in\mathcal C^{\mathrm{mcf}}_{f,s}$、$L(G)=L\cap\Sigma^+$ なら、$K=\mathrm{Wit}(\widetilde G_0)\cup(\{\varepsilon\}\cap L)$ は $\mathcal B^{\le r}_{f,s}$ と $\mathcal B_{f,s}$ の共通の特徴標本で、
\[
 \|K\|_+\le N_{\rm typ}\bigl(1+2\bar\theta_G+r\,\theta_G\mathrm{Nd}_r(h,b)\bigr)+1
 \le|\mathsf S^\sharp|^{fr}\|G\|\,\bar\theta_G\bigl(3+2r^{b+1}(|V||\mathsf S|^f)^{b+1}\bigr)+1 .
\]
つまり $\|K\|_+=O_{f,r,|\mathsf S|,b}(\|G\|^{b+2}\bar\theta_G)$ であり、次数は $\|G\|$ について $b+2$、$\bar\theta_G$ について 1 である。$\delta_s(b)\le b+2$。
3. 構造的な $\dim(G)\le b$ のもとでは $\bar\theta_G\le4r^b\|G\|^{b+3}$ である。したがって $\|K\|_+=O(\|G\|^{2b+5})$ となり、厚さを使わずに大きさだけで抑えられる（`thm:rankone-polydata`(ii) の一般化。ただし $b=0$ では元の $\|G\|^3$ より粗い）。

*証明。*
**(a) ラベルの交換。** 節点 $v$（非終端 $C$、収率 $\mathbf u$）のラベルを $(C,\widehat s^{(\mathrm{fan}\,C)}(\mathbf u))$ とする。good な template では、親の各成分は終端と子の成分を template の順に並べた連接である。$\widehat s$ は射なので、親の型ベクトルは規則と子の型ベクトルだけで決まる。したがって部分木 $T_v$ を、同じ非終端・同じ型ベクトルの別の導出に置き換えても、祖先のラベルはすべて変わらない（路に沿った帰納法）。これは導出木の上の操作であり（文脈自由性）、代入可能性も Rect も使わない。

**(b) 縮約。** 実現ラベル $X$ をとる。$m_s(X)\le b$ なので、Strahler 数 $\le b$ の $X$ の導出がある。その中で節点数が最小のもの $T$ を選ぶ。ある路で祖先 $u$ と子孫 $v$ のラベルが等しいとする。**子孫の部分木 $T_v$ を祖先の位置 $u$ に代入する**と、(a) より $X$ の導出が得られ、節点数は真に減る。$\mathrm{St}(T_v)\le\mathrm{St}(T_u)$（節点の値は各子の値以上なので、各子孫の値以上）であり、$g$ は単調なので、祖先の値は増えない。新しい木の Strahler 数も $\le b$ になり、$T$ の最小性に反する。よって各路のラベルは相異なり、各路の節点数は $\le h$ である。

**(c) 数え上げ。** 各節点で、Strahler 数が最大の子を一つ「主」とする。主でない子へ進むと値は真に減る。最大値を取る子が一つだけなら、他の子は最大値より小さく、最大値は親の値に等しい。二つ以上なら、親の値は最大値 $+1$ である。子の値が親を超えることはない。よって根から深さ $i$ の節点までの路で、主でない一歩は $\le b$ 回である。その位置の選び方は $\binom ij$ 通り、各回の子の選び方は $\le r-1$ 通りなので、深さ $i$ の節点は $\le\sum_{j\le\min(i,b)}\binom ij(r-1)^j$ 個である。$i<h$ で和をとり、ホッケースティック恒等式を使う。上界 $2r^bh^{b+1}$ は $\binom h{j+1}\le h^{j+1}/(j+1)!$ と $\sum_j1/(j+1)!<2$ から出る。

**(d) 長さ。** 各節点は終端を $\le\ell$ 個書くので、(1) が出る。`lem:witness-length-template`(i) により、最短の生成組を正準組に取れる。

**(e) データ。** `thm:data-from-typed-thickness` と $N_{\rm typ}\le C_s(G)\le|\mathsf S^\sharp|^{fr}\|G\|$、$1+2\bar\theta_G\le3\bar\theta_G$ から (2) が出る。

**(3)** 自明な型付け（ラベル＝非終端、$h=|V|$）で (b)〜(d) を使うと $t_G\le\ell\,\mathrm{Nd}_r(|V|,b)$。`lem:thickness-equivalence`(iii) の $\theta_G\le2\|G\|\max\{1,t_G\}$ と $\ell\le\|G\|$ から得られる。∎

**注。** (b) は、どのラベルにも Strahler 数 $\le b$ の導出が**一つ**あればよい。$\dim_s$ 版で足りるのはこのためである。

### 4.1 依頼の三点の確認

- **型付き精密化の次元は元と等しいか。〔VALID〕** $\dim(\widetilde G_0)=\dim(G)$ が成り立つ。$\widetilde G$ の導出木は、$G$ の導出木に型を注記したものと一対一に対応し、形が同じなので Strahler 数も同じである。trimming で消えるのは、成功導出に現れない型付き規則だけである。$G$ が reduced なら、到達可能な $B$ からの $G$ の木はどれも成功導出の部分木になり、その注記は $\widetilde G$ の成功導出なので $\widetilde G_0$ に残る。開始の連結規則 $\widehat S\to S_{(m)}$ は単項なので値を変えない。有限検査 [B] で、表の 19 組と、次元が有限なランダム文法 88 個（各 2 型付け）について一致を確かめた。ただし、証明そのものは $G$ の上でラベルを使っており、$\widetilde G_0$ の次元は使わない。
- **代表元か生成組か。到達文脈は。** 上界は生成組の長さ $t_{\rm typ}$ に対するもので、$\tau\le t_{\rm typ}$ も抑える。標本は代表元で足りる（`lem:witness-length-template`(iv)）が、ここでは生成組で済む。文脈は型によらない $E_B$ で、$|E_B|_{\rm fix}\le\theta_G$ である。#1・02-v3 の CFG の枠組み（BUNF、型付きの到達文脈）なら、文脈は $\le(N|\mathsf S^\sharp|-1)\tau^{\rm typ}$ で、次数が 1 増える。どちらの枠組みでも $b$ についての次数の形は変わらない。
- **定数の $|\mathsf S|$ への依存。** $h\le|V||\mathsf S|^f$ から $t_{\rm typ}$ に $|\mathsf S|^{f(b+1)}$、$N_{\rm typ}$ から $|\mathsf S^\sharp|^{fr}$ が入る。合わせて $|\mathsf S^\sharp|^{f(r+b+1)}$ である。$|\mathsf S|$ を固定すれば次数には影響しない。内容型付けの根の型だけなら、RV1 の（非終端、和集合の内容）のラベルで $h=|V|2^{|m|}$ にできる。

### 4.2 fan-out 1 と一般の fan-out

fan-out 1 では、good＝$\varepsilon$-free な CFG（任意の rank）である。定理 C2 は $t_{\rm typ}\le2r^b\bar\theta_G(|V||\mathsf S|)^{b+1}$、すなわち $\|K\|_+=O(\|G\|^{b+2}\bar\theta_G)$ を与える。$b=0$ では #1 §8（線形）と `thm:rankone-polydata` の形に戻る（次数は同じ型）。一般の $f$ では、上の式がそのまま成り立つ。

### 4.3 自己監査（C2）

- **置換の向き。** 子孫を祖先の位置へ代入している。逆向き（祖先を子孫の位置へ）では木が大きくなり、Strahler 数が増えうる。ここではその向きを使っていない。
- **fan-out $\ge2$ で (a) は正しいか。** 成分が離れていても、親の各成分の型は template の中の順序つきの積である。$\widehat s$ は自由モノイドからの射なので、交差や入れ子の配置には依存しない。$\varepsilon$-free でない場合は、型を $\mathsf S^\sharp$ でとれば同じ議論が通る（$h\le|V||\mathsf S^\sharp|^f$）。
- **最小性の取り方。** 「長さ最小」ではなく「Strahler 数 $\le b$ の中で節点数最小」をとった。長さ最小の導出は Strahler 数が大きいことがありうるので、この選び方が要る。RV1 は最短語の中で節点数最小をとった。本定理ではすべてのラベルを扱うため、短さは (d) の帰結として得られる。
- **数え上げの穴。** 主でない一歩で値が「真に」減ることが要る。親の値と最大値が等しい場合（最大値を取る子が一つ）と、親が最大値 $+1$ の場合を分けて確かめた。いずれでも主でない子の値は親より小さい。
- **有限検査との照合（[B]）。** 120 個のランダムな reduced good 文法（fan-out 2 の非終端を含むもの 48、rank 2 のもの 67）と、$G_{n,b}$・02-v3 の $L_n$ について、二つの型付け（$s_{U,3}$、$c_{\{a,b,c\}}$）で、全ラベルの最短の型付き収率が $\ell\,\mathrm{Nd}_r(h,m_s(X))$ 以下であることを確かめた（最大比は 0.5）。これは全称証明ではなく、有限の照合である（CERTIFIED FINITE）。
- **残る弱点。** 次数 $b+2$ が最良かどうかは分からない。§5 の下界は $(b+1)/2$（積で測った場合）または $\|G\|$ について $b+1$ なので、差は $\|G\|$ について 1 次である。

---

## 5. C3　下界

### 5.1 族の定義

$n\ge1$、$b\ge0$、$N:=(b+1)n$ とする。$1\le t\le N$ に対して $\ell(t):=\lceil t/n\rceil-1$（段の番号）、$a(t):=\ell(t)\,n$（一つ下の段の頂上）と定める。アルファベットは $\{\mathtt a,\mathtt b,\mathtt c\}$ に固定し、文法 $G_{n,b}$ を次で定める。
\[
\begin{aligned}
 &E_0\to\mathtt a,\qquad E_t\to\mathtt cE_{t-1}\mathtt c\quad(1\le t\le N),\\
 &E_t\to\mathtt bE_{t-1}\mathtt b\quad(\ell(t)=0),\qquad
 E_t\to\mathtt bE_{a(t)}E_{t-1}\mathtt b\quad(\ell(t)\ge1),
\end{aligned}
\]
開始記号は $E_N$ とする。$L_t:=L_{E_t}$、$L_{n,b}:=L_N$ とおく。段 0 は線形な鎖、段 $k\ge1$ は「同じ下段の頂上 $E_{kn}$ を $n$ 回脇に付ける鎖」である。$b=n$ 段で各段 1 歩にすると 02-v3 の倍増族に近い形になる。ここでは段の数を $b$ に固定し、各段を長さ $n$ の鎖に置き換えている。

$W_0=\mathtt a$、段 0 では $W_t=\mathtt bW_{t-1}\mathtt b$、段 $\ge1$ では $W_t=\mathtt bW_{a(t)}W_{t-1}\mathtt b$ とし、$W:=W_N$ とおく。

### 5.2 基本量〔VALID。式は [C] で $0\le b\le4$、$1\le n\le7$ について照合〕

- **reduced・good・rank。** $\varepsilon$-free で、$E_t\Rightarrow^*\mathtt c^t\mathtt a\mathtt c^t$ である。rank は $b\ge1$ なら 2、$b=0$ なら 1。
- **大きさ。** $\|G_{n,b}\|=(N+1)+2+5N+5n+7bn=(13b+11)n+3$。
- **厚さ。** $E_t$ の最短収率は $2t+1$ である。最短文脈は $2(N-t)$ である。親が $E_{t+1}$ なら $+2$。第一子の位置（親 $E_{t'}$、$a(t')=t$）なら、文脈は $\ge2(N-t')+2+2(t'-1)+1>2(N-t)$ になる。帰納法で $\ge2(N-t)$ となり、$\mathtt c$ の鎖で等号が成り立つ。したがって $\theta(\text{単項規則と } E_0\to\mathtt a)=2N+1$、$\theta(E_t\to\mathtt bE_{a(t)}E_{t-1}\mathtt b)=2N+2a(t)+2$ となり、$\bar\theta_{G_{n,b}}=(4b+2)n+2$（$b\ge1$）、$=2n+1$（$b=0$）である。
- **次元。** 非巡回なので M1 の Kleene 反復で、$\dim(E_t)=\ell(t)$（$t\ge1$）である。段 $k$ の最初の節点 $t=kn+1$ では $g(k-1,k-1)=k$、以降は $g(k-1,k)=k$。したがって $\dim(G_{n,b})=b$。$\mathtt c$ を使わない唯一の木の Strahler 数もちょうど $b$ である。
- **$\mathtt c$ のない語。** 各 $E_t$（$t\ge1$）は $\mathtt c$ を含まない規則をちょうど一つ持ち、$E_0$ は $E_0\to\mathtt a$ だけを持つ。$\mathtt c$ を書く規則を使わない導出は一つしかなく、$\mathtt c$ のない語は $W$ だけである。段 $k$ の頂上の長さ $M_k:=|W_{(k+1)n}|$ は $M_0=2n+1$、$M_k=(n+1)M_{k-1}+2n$ を満たす。よって $M_k+2=(n+1)^k(2n+3)$ で、
\[
 |W|=(n+1)^b(2n+3)-2\ \ge\ (n+1)^{b+1}.
\]
また $W$ は $\mathtt b^{n+b}\mathtt a\mathtt b^n$ で始まる。

### 5.3 代入可能性〔VALID。02-v3 付録 B の決定的パーサの論法を移植。有限検査 [D] で照合〕

**定理 S.** $L_{n,b}$ は Clark–Eyraud 代入可能である。$L_{n,b}$ は有限なので、$\{\mathtt a,\mathtt b,\mathtt c\}$ を含むどのアルファベットのどの型付け $s$ についても $L_{n,b}\in\mathcal C^{\mathrm{mcf}}_{1,s}$ となる。

*証明。* スタック記号は $E_t$（$0\le t\le N$）と閉じの印 $\hat{\mathtt b}_t,\hat{\mathtt c}_t$（$1\le t\le N$）とし、スタックの頂上を左に書く。動きは次のものだけである。
\[
\begin{aligned}
 &E_0\mathcal Z\xrightarrow{\mathtt a}\mathcal Z,\qquad E_t\mathcal Z\xrightarrow{\mathtt c}E_{t-1}\hat{\mathtt c}_t\mathcal Z,\\
 &E_t\mathcal Z\xrightarrow{\mathtt b}E_{t-1}\hat{\mathtt b}_t\mathcal Z\ (\ell(t)=0),\qquad
 E_t\mathcal Z\xrightarrow{\mathtt b}E_{a(t)}E_{t-1}\hat{\mathtt b}_t\mathcal Z\ (\ell(t)\ge1),\\
 &\hat{\mathtt b}_t\mathcal Z\xrightarrow{\mathtt b}\mathcal Z,\qquad\hat{\mathtt c}_t\mathcal Z\xrightarrow{\mathtt c}\mathcal Z .
\end{aligned}
\]
- (D1) **決定性。** 頂上の記号と文字で動きが決まる。
- (D2) **重み。** $\mathrm{wt}(E_t)=4^t$、印の重みを 1 とする。$a(t)\le t-1$ なので $4^t>4^{a(t)}+4^{t-1}+1$ であり、どの動きでも重みが真に減る。
- (D3) **局所性。** 02-v3 と同じく、動きは頂上だけを読み書きし、印は消されるだけである。

**補題 (i)。** $E_t\mathcal Z\xrightarrow w\mathcal Z$ ⟺ $w\in L_t$。
証明は 02-v3 と同じである。段 $\ge1$ で $\mathtt b$ を読んだ後は、$E_{a(t)}E_{t-1}\hat{\mathtt b}_t$ を (D3)(a) で三回分割する。

**補題 (ii)（到達可能なスタック上の単射性）。** 枠を次で定める。印の枠 $\hat{\mathtt b}_t,\hat{\mathtt c}_t$（子の添字 $\kappa=t-1$）と、保留の枠 $P_t:=E_{t-1}\hat{\mathtt b}_t$（$t>n$ のときだけ。$\kappa=a(t)$）である。枠の積 $F_1\cdots F_m$ を、$\mathrm{idx}(F_m)=N$、$\mathrm{idx}(F_i)=\kappa(F_{i+1})$ を満たすものとする。到達可能なスタック（$E_N\xrightarrow u\mathcal X$）は、$\varepsilon$ か、$\mathcal YF_1\cdots F_m$（$\mathcal Y\in\{E_u,\hat{\mathtt b}_u,\hat{\mathtt c}_u\}$、$u=\kappa(F_1)$、$m=0$ なら $u=N$）の形をしている。これは四種類の動きで閉じていることから確かめられる。枠の積の中では $E$ の直後は必ず $\hat{\mathtt b}$ なので、分解は一意である。

各文字の像は次のとおりである。
- $\mathtt a$：$E_0\mathcal Z\mapsto\mathcal Z$。
- $\mathtt c$ の開き：像は $E\,\hat{\mathtt c}$ で始まる。これは枠の積には現れない。
- $\mathtt c$ の閉じ：像は枠の積 $\mathcal Z$ で、元の添字は $\kappa(F_1)$（または $N$）で決まる。
- $\mathtt b$ の開き（段 0）：像は $E_{t-1}\hat{\mathtt b}_t$（$t\le n$）で始まる。
- $\mathtt b$ の開き（段 $\ge1$）：像は $E\,E$ で始まる。
- $\mathtt b$ の閉じ：像は枠の積で、$\varepsilon$、印、または $E_{t'-1}\hat{\mathtt b}_{t'}$（$t'>n$）で始まる。

段 0 の開きと閉じの像は、印の添字が $\le n$ か $>n$ かで分かれる（**02-v3 からの変更点はここである。** 保留の枠は $t>n$ にしかない）。どの行も単射で、行どうしの像は交わらない。よって各文字、したがって各語は、到達可能なスタック上の部分単射である。

**補題 (iii)（交換）。** $\mathcal X$ が到達可能、$w\in L_t$、$\mathcal X\xrightarrow w\mathcal Y$ なら、$\mathcal X=E_t\mathcal Y$。
$t$ についての帰納法で示す。途中のスタックはすべて到達可能である。
- $t=0$：$\mathtt a$ を読めるのは $E_0$ だけ。
- $w=\mathtt cv\mathtt c$：最初の $\mathtt c$ が $E_{t'}$ を開くなら、帰納法の仮定から $t'-1=t-1$。最後の $\mathtt c$ は $\hat{\mathtt c}_t$ を消す。最初の $\mathtt c$ が印を消すなら、残りは枠の積 $\mathcal Z$ で、帰納法の仮定から $\mathcal Z=E_{t-1}\cdots$ となる。$E$ で始まる枠の積の第一枠は保留の枠 $P_t$ なので、$v$ の後の頂上は $\hat{\mathtt b}_t$ であり、$\mathtt c$ は動けない。
- $w=\mathtt bv\mathtt b$（段 0）：$E_{t'}$（段 0）を開くなら $t'=t$。$E_{t'}$（段 $\ge1$）を開くなら $a(t')=t-1\le n-1$ となるが、$a(t')\ge n$ なので矛盾する。印を消すなら、帰納法の仮定から第一枠が $P_t$ となり、$t\le n$ と $P_t$ の $t>n$ が矛盾する。
- $w=\mathtt buv\mathtt b$（段 $\ge1$、$u\in L_{a(t)}$, $v\in L_{t-1}$）：段 0 の $E_{t'}$ を開くなら $t'-1=a(t)\ge n$ で矛盾する。段 $\ge1$ の $E_{t'}$ を開くなら、$u$ から $a(t')=a(t)$、$v$ から $t'=t$。印を消すなら、$u$ の後の頂上が印 $\hat{\mathtt b}$ になり、$v$ について帰納法の仮定（頂上は $E_{t-1}$ のはず）に反する。

帰結：$w,w'\in L_t$ なら $w\equiv w'$。$pwq\in L$ の走行で $\mathcal X=E_t\mathcal Y$ となり、補題 (i) から $E_t\mathcal Y\xrightarrow{w'}\mathcal Y$ が出る。

**補題 (iv)（枝の同期）。** 二つの異なる文字を許す頂上は $E_t$（$t\ge1$）だけである（$\mathtt b$ と $\mathtt c$）。(D3)(b) の場合は、$\mathcal Y_1$ が $\hat{\mathtt c}_t$ で終わり、$\mathcal Y_2$ が $\hat{\mathtt b}_t$ で終わるので起こらない。(a) の場合は、補題 (i) で両方が $L_t$ の語で始まる。02-v3 と同じである。

**結論。** 02-v3 の Proposition（$\mathcal X\xrightarrow x\mathcal Y$ かつ $\mathcal X\xrightarrow y\mathcal Y$ なら $x\equiv y$）は、$|x|+|y|$ についての帰納法で同じように示せる。$uxv,uyv\in L$ なら、$v$ が到達可能なスタック上で単射であることから中間のスタックが一致し、$x\equiv y$ となる。∎

**有限検査 [D]（CERTIFIED FINITE）。**
- 総当たりによる完全な判定（因子と文脈の二部グラフの各連結成分が完全二部であること）で、$(n,b)\in\{(1..5,0),(1,1),(2,1),(3,1),(1,2),(1,3)\}$ のすべてで代入可能性を確かめた。最大は $(3,1)$ の 5,832 語・因子の出現 3,058,776 個。
- 到達可能なスタックを列挙し、8 組の $(n,b)$（最大 6,862 スタック）で、重みが減ることと各文字の単射性を確かめた。
- パーサの受理が言語の所属と一致することも、乱択で確かめた。

### 5.4 fan-out 1 の下界

**定理 C3.1〔VALID〕。** $b\ge0$、$n\ge1$、$s=s_{U,3}$ とする。$L_{n,b}\in\mathcal C^{\mathrm{mcf}}_{1,s}$ で、型 1 の語は $W$ だけである。`prop:rare-type`（fan-out 1）から、$\mathcal B^{\le r}_{1,s}$（$r\ge1$）、$\mathcal B_{1,s}$、および $\mathcal C^{\mathrm{mcf}}_{1,s}$ の全体で特徴標本を持つ任意の set-driven な作用素について、すべての特徴標本は $W$ を含む。
\[
 \|F\|_+\ \ge\ (n+1)^b(2n+3)-1\ \ge\ \Bigl(\frac{\|G_{n,b}\|\,\bar\theta_{G_{n,b}}}{(13b+14)(4b+4)}\Bigr)^{(b+1)/2}.
\]
（$\|G\|\bar\theta\le(13b+14)(4b+4)n^2$ による。[F] で $1\le b\le5$、$n<200$ について照合した。）したがって $\delta_{s_{U,3}}(b)\ge(b+1)/2$ であり、$\|G\|^{d_1}\bar\theta_G^{d_2}$ の形の上界は $d_1+d_2<b+1$ では成り立たない。

**最小に近い提示についても成り立つこと（水増しをしていないこと）。** 下界 $\|F\|_+\ge|W|+1$ は言語の量 $\mu_1(L_{n,b})$ によるので、**どの**提示についても成り立つ。$\|G'\|\bar\theta_{G'}\le\|G_{n,b}\|\bar\theta_{G_{n,b}}$ を満たす提示 $G'$ なら、同じ式がより強い形で成り立つ。さらに次のことが言える。
- (a) どの提示も $\bar\theta_{G'}\ge2N+1$ を満たす（最短の語の長さ）。$\bar\theta_{G_{n,b}}\le2(2N+1)$ なので、厚さは最小の 2 倍以内である。
- (b) 次元 $\le b$・rank $\le r'$ のどの提示 $G'$ についても、C2(1) から $|W|\le2r'^b\bar\theta_{G'}(2|V'|)^{b+1}$。よって $|V'|^{b+1}\bar\theta_{G'}\ge(n+1)^{b+1}/(2^{b+2}r'^b)$ である。我々の提示はこの積が $O_b(n^{b+2})$ なので、範囲内で最小の積の $O_b(n)$ 倍以内に収まる。
- $\|G\|$ と $\bar\theta$ はどちらも $\Theta_b(n)$ であり、水増しで比を作っていない。

**系（型付けの水準）〔VALID〕。** 02-v3 の `cor:typing-level-obstruction` の仮定（相異なる冪等元 $e,z$ で $ez=ze=z$、文字の重ならない $u,v,w$ で $s(u)=s(v)=e$、$s(w)=z$）を満たす型付け $s$ では、$h:\mathtt a,\mathtt b,\mathtt c\mapsto u,v,w$ による像 $h(L_{n,b})$ が Clark–Eyraud 代入可能である（`lem:app-u1-code`。$L_{n,b}$ は有限）。像の文法は同じ形の木を持つので次元は $b$、大きさと厚さは $u,v,w$ の長さの定数倍である。型 $e$ の語は $h(W)$ だけになる。したがって同じ次数の下界 $\delta_s(b)\ge(b+1)/2$ が成り立つ。$U_1$ への型付けで型 1 の文字が二つ以上あるものは、すべてこれに当たる。

### 5.5 LG の外でも一様な次数になる場合

C3-2 の問い「LG の外では次数が必ず $b$ とともに増えるか」への答えは、**型付けの水準では否**である〔VALID、既知の結果による〕。

$s_{U,2}$（$\mathtt a\mapsto1$, $\mathtt b\mapsto\zeta$）、より一般に型 1 の文字がちょうど一つの $U_1$ への型付け、および二文字上の半束型付けでは、compendium の `cor:two-letter-fanout-one` が、どの rank のどの reduced good な fan-out 1 提示についても $\|K\|_+\le C'r(\|G\|+2)^{23}\bar\theta_G^{\,8}$ を与える（主張を読んだ。証明は未読）。この上界は次元によらず、$(\|G\|+2)^{23}\bar\theta^{\,8}\le3^{23}(\|G\|\bar\theta)^{23}$ なので、$\delta_s(b)\le23$ がすべての $b$ で成り立つ。像 $U_1$ は LG ではない。

**擬多様体の水準では正しい。** $\mathbf V\not\subseteq\mathbf{LG}$ なら $U_1\in\mathbf V$ であり、$s_{U,3}$ の像は $U_1$ なので、$\Delta_{1,r}(\mathbf V)=\infty$ となる。

### 5.6 fan-out 1 の二分法

**定理 C3（fan-out 1、$r\ge2$）〔VALID〕。**
1. すべての型付け $s$ について $\delta_s(b)\le b+2$（C2）。
2. $s(\Sigma^+)\in\mathbf{LG}$ なら $\delta_s(b)\le2$ がすべての $b$ で成り立つ（`thm:local-group-polydata` の $O(\|G\|^2\bar\theta_G)$ は次元によらず、$\|G\|^2\bar\theta\le(\|G\|\bar\theta)^2$）。
3. $s_{U,3}$ と §5.4 の系の型付けでは $(b+1)/2\le\delta_s(b)\le b+2$。
4. 擬多様体 $\mathbf V$ について、$\Delta_{1,r}(\mathbf V)<\infty$ ⟺ $\mathbf V\subseteq\mathbf{LG}$ ⟺ $\mathbf V$ は fan-out 1 で一様多項式データを持つ（後半の同値は `thm:fanout-one-data`）。

したがって fan-out 1 では、LG の境界は「**次元が有界なうちはどの型付けでも多項式で、LG の外では次数が次元に比例して増え、次元が有界でなくなる極限で多項式性そのものが壊れる**」という形で現れる。既知の事実とも合う：rank 1 は次元 0（M2-1）、倍増族の次元は $n=\Theta(\|G\|)$（[A]）。

**補足（どの次元から LG の上界を超えるか）。** 我々の族では $|W|\sim2n^{b+1}$、$\|G\|^2\bar\theta\sim\Theta_b(n^3)$ なので、$b\ge3$ で $O(\|G\|^2\bar\theta_G)$ を漸近的に超える。$b\le2$ で $s_{U,3}$ に LG と同じ形の上界が成り立つかどうかは調べていない。

### 5.7 fan-out 2 への持ち上げ

**命題 E（持ち上がらない）〔VALID。[E] で照合〕。** $f\ge2$、$b\ge0$ とし、任意の型付け $s$ で $n\ge2|\mathsf S|+2$ とする。$W$ を含む $L\in\mathcal C^{\mathrm{mcf}}_{f,s}$ は、$W$ と長さ・Parikh ベクトル・型が同じで $\mathtt c$ を含まない別の語を含む。特に $L_{n,b}\notin\mathcal C^{\mathrm{mcf}}_{f,s}$ である。

*証明。* `thm:doubling-no-lift` と同じく `lem:power-transfer` による。$W=\mathtt b^{n+b}\mathtt a\mathtt b^n R'$ は冪 $\mathtt b^{n+b}$ を含み、$\mathtt a$ の後にも $\mathtt b^n$ が続く。

$s_{U,3}$ では $s(\mathtt b)=1$ が単位元なので $i_0=p=1$ となり、$n\ge4$ で次の**具体的な二穴 Rect 違反**がある。

| 項目 | 内容 |
|---|---|
| 比較タプル | $\mathbf x=(\mathtt b,\ \mathtt b^{n-2})$、$\mathbf y=(\mathtt b^2,\ \mathtt b^{n-3})$。成分は非空（$n\ge4$） |
| 成分ごとの型 | どちらも $(1,1)$ |
| 共有文脈 $E_0$ | $\mathtt b^{b}\,\square_1\,\mathtt b\,\square_2\,\mathtt a\mathtt b^nR'$（中央 $\mathtt b$ は非空） |
| 試験文脈 $E_1$ | $\mathtt b\,\square_1\,\mathtt b^{n+b-2}\mathtt a\mathtt b^2\,\square_2\,R'$（中央は非空） |
| 四つの語 | $E_0[\mathbf x]=E_0[\mathbf y]=E_1[\mathbf x]=W\in L_{n,b}$。$E_1[\mathbf y]=\mathtt b^{n+b+1}\mathtt a\mathtt b^{n-1}R'$ は $\mathtt c$ を含まず $W$ と異なるので、$\notin L_{n,b}$ |

穴は二つだけで、三つ目の穴は加えていない。∎（[E]：$0\le b\le3$、$4\le n\le9$ について、パーサで四つの語を判定した。）

**fan-out 2 の下界：OPEN。**

障害の正体ははっきりしている。有界次元で長さが掛け算で増えるのは、背骨の上で**同じ**脇の非終端を繰り返し使うからである。そのため $\mathtt c$ のない語は $(\mathtt bW_{kn})^n$ のような高い冪を含み、冪移送にかかる。

脇の子を二つの非終端 $X_1,X_2$ から cube-free な順序（Thue–Morse 型）で選べば、長い冪は避けられ、大きさは $O(bn)$、長さは $\Theta(n^{b+1})$ のままにできる。しかしそれで全一穴・二穴の条件を満たせるかどうかは、周期的でない宿主の問題（R6 の Thue–Morse 型候補 10 例は $n=3,4$ で Rect 違反。R8 の注記でも「残る設計空間」に挙がっている）そのものである。今回は**試していない**。

R1・R2・R8 で排除された形（倍増型、周期的な背骨に段ごとに一様な逃げ道）は、ここでは提案していない。§5.1 の族は fan-out 1 専用であり、fan-out 2 では上の命題 E で倒れる。

**帰着（fan-out $f\ge2$）〔VALID〕。** `prop:sl-reduction` と同じ論法が次数版にも通る。
- (i) $\Delta_{f,r}$ は部分擬多様体へ単調に下がる。$\mathbf V\not\subseteq\mathbf{LG}$ なら $\mathbf{SL}\subseteq\mathbf V$。
- (ii) $s\preceq c_\Sigma$ なら `lem:typing-monotone` により、同じ提示・同じ標本で $\delta_s(b)\le\delta_{c_\Sigma}(b)$。

よって「fan-out $f$ で LG の外のすべての擬多様体の次数が有界でない」⟺ $\sup_\Sigma\sup_b\delta_{c_\Sigma}(b)=\infty$。$|\Sigma|=2$ では `thm:two-letter-content` が次元によらない上界を与えるので、$|\Sigma|\ge3$ が必要である。R4 系 B の次数版（データ ⟺ 希少型）が成り立つには、R4 の型の積と正規化の各段が次元を保つ必要がある。これは**確かめていない**（CONDITIONAL）。

### 5.8 自己監査（C3）

- **02-v3 の証明からの変更点を洗い出した。** 枠の添字が連続しない（$a(t)$ への跳び）こと、段 0 の開きの像が保留の枠と同じ形 $E\hat{\mathtt b}$ になることの二点である。前者は「子の添字 $\kappa$」で枠の積を定義し直して扱った。後者は印の添字の範囲（$\le n$ か $>n$ か）で分けた。交換補題では、四種類の分解それぞれについて「開く」「印を消す」の二つの場合を尽くした。印を消す場合の矛盾は、02-v3 では「頂上が $\hat{\mathtt b}_i$ になり $\mathtt c$ が動けない」の一種類だったが、ここでは添字の範囲の矛盾も使う。
- **網羅性。** 代入可能性は Rect の場合分けではなく、パーサの合同（全ての $x,y$ について）で示している。有限検査は、証明が正しいことの独立な照合として、最大 5,832 語の言語で完全な判定をした。
- **型の確認。** 下界は `prop:rare-type` だけに依存し、根の型 1 の語が $W$ だけであることは文法の形（$\mathtt c$ のない規則が各非終端に一つ）から出る。持ち上げの Rect では、成分ごとの実際の型（$s_{U,3}(\mathtt b^k)=1$）を書いた。語全体の計数から合法性を導いていない。
- **反証済みの推論との照合。** PAUSE_FALSE_ROUTES の A 表（X1、CA、R15 一般 IH、E1 の型越え決定性）は使っていない。小さい $n$ の検査で大きい $n$ の主張を立てていない（式はすべて一般の $n,b$ で証明し、有限検査は照合だけに使った）。
- **最も弱い点。** §5.3 の補題 (ii) の像の場合分けは表で一回確かめただけである。到達可能なスタックの列挙検査（最大 6,862 個）は正しさを支持するが、全称証明ではない。別系列による監査の最優先の対象とする。

---

## 6. C4　位置づけ

### 6.1 `op:fanout-two` に対する意味

**従うこと。**
1. **構造的な必要条件〔VALID〕。** `op:fanout-two` を肯定する族（ある型付けで、データが $(\|G\|,\bar\theta)$ のどの多項式も超える族）は、$\dim_s(G_n)\to\infty$ を満たさなければならない。定量的には、C2(2) から
\[
 \dim_s(G_n)+2\ \ge\ \frac{\log\|F\|-\log\bar\theta_{G_n}-O(1)}{\log\bigl(O(r|\mathsf S|^f)\|G_n\|\bigr)}
\]
となる。指数的なデータ（$\log\|F\|\ge c(\|G\|+\bar\theta)$）には $\dim=\Omega(\|G\|/\log\|G\|)$ が要る。倍増族の次元は $\Theta(\|G\|)$ で、これと合う。
希少型については、より強く次が言える。$\mu_m>\theta_G\mathrm{Nd}_r(h,b)$ なら、**型 $m$ のすべての語のすべての導出**の Strahler 数が $b$ を超える。
2. **`conj:rare-types` は、すべての有界次元の部分クラスで成り立つ〔VALID〕。** $\mu^\star\le t_{\rm typ}\le2r^b\bar\theta_G(|V||\mathsf S|^f)^{b+1}$。どの fan-out・どの型付けでもよい。反例には次元が有界でないことが要る。
3. fan-out 1 では、二分法が閉じた（定理 C3）。

**従わないこと。**
- C3 で次数が増えることは、一様多項式データの失敗そのものではない（各 $b$ では多項式）。fan-out 1 での失敗には、倍増族（次元 $n$）がやはり必要である。
- 逆に、fan-out 2 で $\sup_b\delta_s(b)<\infty$ が示されても、定数 $C_{s,b}$ が $b$ とともに増えうるので、`op:fanout-two` の否定にはならない。fan-out 2 で次数が増える族が見つかっても、肯定にはならない。二つの問いは論理的に独立である。
- 言語の水準の潰し込み（M3）は、学習の問いには使えない。クラスが fan-out について単調でないからである（§2）。

### 6.2 既存の筋道との関係

| 既存の結果 | 関係 |
|---|---|
| `thm:rankone-polydata` | $b=0$ の場合（M2-1 により rank 1＝次元 0）。$\|G\|$ だけの形では、こちらの指数は粗い（$\|G\|^5$ と $\|G\|^3$） |
| RV1 (ii) | 論法は同じ。型付け一般・全ラベル・データへ拡張した。内容型付けの根の型だけなら、RV1 のラベルの方が鋭い（$|V|2^{|m|}$） |
| R1・R2（倍増型の no-go） | 対象は次元が有界でない倍増型で、本報告の fan-out 1 の族とは重ならない。fan-out 2 への持ち上げでは、倍増型・一様な逃げ道を提案していない |
| R8 定理 H4 | H4 は周期的な背骨の設計に対して $|V|\ge2^{M/(3r)}/\mathrm{poly}$ を与える。C2 からは、**どの**設計でも次元 $\le b$ なら $|V|\ge(\mu/(2\ell r^b))^{1/(b+1)}/|\mathsf S|^f$。指数的な $\mu=2^M$ には $|V|\ge2^{M/(b+1)}/\mathrm{poly}$ が要る。したがって H4 型の大きさの下界は有界次元では自動的に成り立ち、H4 の内容は「次元が有界でない周期的な設計でも失敗する」点にある |
| R13（WN、入れ子の分裂型の塔） | C2 から、WN の希少型の上界を破る族は、WN の提示で $\dim_s\to\infty$ を満たさなければならない。RV1 の「WN だけでは Strahler 数は有界にならない」とは整合する（WN と有界次元は独立な制限）。残る「塔」の配置は、分岐の入れ子の深さが有界でないことと両立しなければならない。塔の形がそれを強制するかどうかは調べていない |
| `thm:doubling-no-lift` | 命題 E は同じ機構を有界次元の族に使ったものである。具体的な二穴 Rect を明示した |
| `conj:rare-types` | 有界次元の部分クラスでは成り立つ（§6.1-2）。一般には OPEN のまま |

### 6.3 論文になるか

**判断：独立した論文としては薄い。博士論文の一章、または 02-v3（fan-out 1 の分類論文）の一節として価値がある。**（確信度：中）

- **新しい点。** (1) 「次元（分岐の入れ子の深さ）」を、線形（#1 §8、次元 0）と一般の CFG の間をつなぐ定量的な階層として導入した。(2) すべての型付けで多項式（次数 $\le b+2$）、LG では次数が一様、LG の外では次数 $\Theta(b)$ という二分法を示した。(3) 境界が「極限の現象」であることを明示した。02-v3 `rem:scope`(b)「線形ならすべての型付けで多項式、倍増族は二分の規則を使う」を、二分の規則の**入れ子の深さ**で定量化したことになる。
- **新しくない点。** 上界は標準的な Strahler の数え上げ（RV1 (ii)）と既存のデータの上界の組み合わせである。下界の族は 02-v3 の倍増族を打ち切ったもので、代入可能性の証明は既存の決定的パーサの論法の移植である。
- **文献との比較。** Yoshinaka (2011) の効率の基準（大きさと厚さで測る）は compendium の引用で知っているだけで、Yoshinaka (2015, MoL) は**未読**である。これらに次元で層別した結果があるかどうかは**確認していない**（記憶による限り、ないと思うが未確認）。
- **独立した論文にする条件。** fan-out 2 での下半分（ある $c_\Sigma$ で次数が増える族）か、一様な次数の証明が得られれば、それ自体で一本になる。

---

## 7. 既存結果との照合表

| 結果 | 本報告での扱い | 判定 |
|---|---|---|
| `thm:rankone-polydata` | 定理 C2 の $b=0$ の場合として再導出。証明全文と照合し、ラベル付きの鎖の論法が同じであることを確かめた | 整合 |
| RV1 (ii) | 論法を一般の型付け・全ラベルに拡張。RV1 の版（根の内容型）はラベルが粗い分だけ鋭い | 整合。拡張は VALID（自己判定） |
| R1 定理 2・R2 定理 B | 本報告の構成は彼らのクラス（倍増型・層状）に入らない。fan-out 2 への持ち上げで再提案していない | 抵触なし（R1・R2 は部分読み） |
| R8 定理 H4 | 有界次元では、同じ型の大きさの下界が C2 から一般に出る（§6.2） | 整合 |
| R13 | WN の反例には次元の非有界性が必要（§6.2） | 整合（R13 の主張自体は検証していない） |
| `thm:doubling-no-lift` | 同じ機構で $L_{n,b}$ も持ち上がらない（命題 E） | 整合 |
| `conj:rare-types` | 有界次元の部分クラスで成り立つ。一般は OPEN | 新しい部分結果（VALID、自己判定） |
| `thm:local-group-polydata` | 次元によらない $O(\|G\|^2\bar\theta)$。二分法の LG 側 | 整合 |
| `cor:two-letter-fanout-one`・`thm:two-letter-content` | LG の外でも次数が一様な型付けの例（§5.5）、二文字では fan-out 2 でも次数が一様（§5.7） | 整合（主張のみ読んだ） |
| 02-v3 `prop:three-letter-family`・付録 B | 打ち切り版 $L_{n,b}$ に移植。$b$ 段・各段 $n$ 歩 | 拡張（VALID、自己判定。監査の最優先） |

---

## 8. 次の最小義務（3 項目）

1. **§5.3（$L_{n,b}$ の代入可能性）の別系列による監査。** 特に補題 (ii) の像の場合分け（段 0 の開きと保留の枠の区別）と、交換補題の「印を消す」場合。下界はこれだけに依存している。
2. **fan-out 2 の下半分の最初の試験。** 有界次元の背骨で、脇の子を cube-free な順序で選ぶ族（冪移送を避ける）を、小さい $n$ で全一穴・二穴の Rect について検査する。または、$|\Sigma|=3$ の内容型付けで $\delta_{c_\Sigma}(b)$ が一様であることを、R10・R11 の筋（$m=\{\mathtt a\}$）の有界次元版として示す。どちらか一方でよい。
3. **次元の保存の確認。** R4 の型の積と正規化の各段（`lem:normalization-stages`、`prop:pattern-thickness-transfer`）、および good 正規化が次元を保つかを確かめる。R4 系 B の次数版と、標準の提示への C2 の移転に必要になる。BUNF の二分化は次元を上げうる（§2 の例）ので、別の正規化が要るかもしれない。
