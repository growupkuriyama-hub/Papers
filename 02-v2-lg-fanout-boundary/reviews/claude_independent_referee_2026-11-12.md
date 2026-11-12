# 論文 #2 独立査読報告（TCS 投稿前・数学的厳密性優先）

*Distributional Learning of Multiple Context-Free Languages under Fixed Finite-Semigroup Typing: Local Groups and the Length of Characteristic Data*（T. Kuriyama）

査読者：Claude（Opus 5.5）　実施日：2026-11-12 JST
対象：`growupkuriyama-hub/Papers`、`02-v2-lg-fanout-boundary/`

---

## I. Executive verdict

### 査読対象の同定

| 項目 | 値 |
|---|---|
| `main` 最新コミット | `28b6abde95ea3b922e7a5516721ebfa82948ca78`（2026-11-12 16:40 JST, "Merge paper #2 canonical 42/49pp metadata, AI handoff and archive index"） |
| `main.tex` の最終変更コミット | `0ca006248ded69ad7994a13d898298e235fa762e`（2026-11-11 21:09 JST） |
| `main.tex` git blob SHA | `04316baee47182c8b9669186d9f0c7a14c7a4376`（**依頼書の値と一致。11月12日以降の更新なし**） |
| `main.tex` SHA-256 | `ccdeef14f6173aa8a12372ee5dd2869c44d91e5122b2a62bec1eb3879cb5e8c9`（3,719 行） |
| `main.pdf` | 42 頁。手元で `main.tex` から再コンパイルしても 42 頁、未定義参照・未定義引用 0 |
| `japanese/main_JP.tex` git blob SHA | `612428586c1108f7f7c9150534618e92ec7d1cde`（3,811 行） |
| `japanese/main_JP.pdf` | 49 頁 |

### 実際に読んだもの

- `HANDOFF_CURRENT.md`、`PAPER.yaml`（冒頭の status 部分）
- `main.tex` **全 3,719 行**：本文 §1–§8、付録 A–H、参考文献
- `japanese/main_JP.tex`：主定理 A/B/C、`thm:fanout-one-data`、`thm:local-group-polydata`、`thm:doubling-no-lift`、`lem:power-transfer`、`op:fanout-two`、`def:uniform-polydata`、定数 \(c_{\mathbb G,f}\)、日本語版にしかない 3 ラベル。ラベル集合は機械照合した。
- 引用文献の原文：Yoshinaka (2011, TCS 412) の §2.3、§3.1 Example 5、§4.1（Type I–III）、§4.3（thickness \(\tau_G\)、Definition 1、Lemma 6–7、Theorem 1、Corollary 2）。出典はプロジェクトの Core E PDF。Eyraud–Heinz–Yoshinaka (2016) の Definition 2.11–2.12（Core D PDF）。

### 読んでいないもの・使っていないもの

- `plan1/`、`plan2/` の報告書は読んでいない。数学の判定には不要と判断した。
- `reviews/` 内の他 AI による報告・スクリプトは参照していない（依頼書の方針どおり）。
- `parked/` は査読対象外として扱った。

### 独立検証できた範囲

本文と付録のすべての定理・補題・命題について、量化子と仮定を確認したうえで証明を手で再構成した。主要部分は独立に書いた Python で計算検査した（§III・付録 Z）。特に、付録 A の非可換群ブロック置換（順序分類、Ramsey 型抽出、境界状態 \(\eta_p=P_pQ_p^{-1}\) による区間選択）と、付録 B の局所群座標・buffer 補題は一行ずつ再導出した。

### 未検証の範囲

- Yoshinaka (2015, MoL) の Lemma 2–3・Theorem 1。原文を入手できなかったため照合していない。ただし本論文は該当結果を付録 D で直接証明しており、引用は帰属のためだけに使われている。
- Almeida–Margolis–Steinberg–Volkov (2009) Prop. 2.3 の項目番号 (1)(3)(4)。原文未照合。ただし該当する同値性は下記 m6 のとおり数行で自己完結に証明できることを確認した。
- 次の文献は原文未照合。いずれも主定理の証明の鎖には入っていない。
  - Costa (2002)、Straubing (1985)、Tilson (1987)
  - Geroldinger–Halter-Koch の定理番号（Remark `rem:davenport-size` のみで使用）
  - Rambow–Satta の \(\mathsf{MCFL}(2,2)=\mathsf{MCFL}(2,3)\)（前置きの注意のみ）
  - Duncan et al. (2026)
- Seki et al. の正規化構成 (f3) は、原文と照合せずに付録 F の主張を直接検討した。
- 日本語版の証明の逐行照合（主張と定数のみ照合した）。
- PDF の目視校正。

### 全体判定

**Minor Revision**

重大（Critical/Major）な数学的誤り・反例・証明の欠落は**見つからなかった**。定理 A・B・C、`thm:doubling-no-lift`、非 CFL 分離命題はいずれも、現行原稿の証明で成立すると判断する。

ただし 1 件、補題の**言明**に修正が必要な箇所がある（m1）。`lem:group-interval` の仮定「二つのブロック位置 \(t,u\)」が \(t=u\) を含むと明記されていない。\(t\neq u\) のみと読むと**言明自体が偽**になる（\(S_3\) で反例を構成した）。定理 A への適用では \(t=u\) の場合が均質化で供給されるので、主定理には影響しない。

---

## II. 数学的誤り・疑義

**重大（M 番号）に該当する項目：なし。**

以下はすべて Minor である。確信度は各項目に記した。

### m1　`lem:group-interval` の仮定に \(t=u\) が明示されていない

- **重大度**：Minor（言明の不備。主定理への影響なし）
- **場所**：付録 A.1、`lem:group-interval`（main.tex 2318–2327 行、仮定は 2322–2325 行）
- **原稿の主張**：同じ行に置かれた「二つのブロック位置 \(t,u\)」について、「添字 \(i\) のブロック \(t\) が添字 \(j\) のブロック \(u\) の左にある」の真偽が \(i<j\) によらず一定なら、置換して全行の値を保つ非空の添字区間 \(J\) が存在する。
- **問題の理由**：証明は `lem:group-block-order` を適用する。その仮定 (ii) は「\(t=u\) を含む」と明記されており、各型の点が \(i\) について単調であることを要求する。"two block positions" を相異なる 2 つと読むと、`lem:group-interval` の言明はこの単調性を仮定しないことになり、**偽になる**。
- **反例**（`verify_scripts/v6_interval_hyp.py`）：
  - \(\mathbb G=S_3\)、\(f=1\)、ブロック型 1 種、添字数 \(n=6=|\mathbb G|^f\)。
  - 行上の添字の並びを \(1,4,2,5,0,3\) とし、定数と元の値・置換後の値を適当に選ぶ。
  - このとき、行の値を保つ非空の添字区間は一つも存在しない。
  - \(t\neq u\) の仮定は型が 1 種なので空虚に成り立つ。
- **他の箇所で解決されているか**：`lem:block-replacement`(b) の証明は、`lem:order-homogenize` で \((t,t)\) を含むすべての順序対を先に均質化し、`lem:group-block-order` の (i)(ii) を明示的に確認してから `lem:group-interval` を呼ぶ。したがって**定理 A の証明は正しい**。欠けているのは独立に読んだときの言明だけである。
- **修正可能性・最小修正案**：仮定を次のように直す。
  > "... for every two block positions \(t,u\) on a common line, **\(t=u\) allowed**, the truth value of ..."
- **主定理への影響**：なし。
- **確信度**：Confirmed（反例は計算で確認済み）

### m2　\(f=1\) の場合の先行研究（Olson–White の順序付き積 1 問題）が引用されていない

- **重大度**：Minor（credit と位置づけ）
- **場所**：
  - `lem:block-replacement`(c)（2425–2432 行）
  - 定数 \(c_{\mathbb G,f}\)（1344–1351 行）
  - 結論の "Tightness" 段落（2171–2175 行）
- **内容**：ブロックごとに \(h_b:=A_b\,x'_b\,x_b^{-1}A_b^{-1}\) とおく。\(A_b\) は行の、ブロック \(b\) より左の元の値の積である。このとき任意の \(J\) について次が成り立つ（行内の位置順の積）。
  \[
  \operatorname{val}_\varrho(J)=\Bigl(\prod_{b\in\varrho,\ o(b)\in J}h_b\Bigr)\operatorname{val}_\varrho(\varnothing)
  \]
  この恒等式は手で示せ、\(S_4\) で 20,000 例の数値検査でも誤りはなかった（`v5_conjugation.py`）。
  - \(f=1\) の問題は、定数を消すと**順序付き部分列の積が 1 になる問題**、すなわち Olson–White (1977) の ordered Davenport constant の問題そのものになる。本論文の \(|\mathbb G|\) は、そのうち区間に限った自明な鳩の巣評価である。
  - \(f\ge2\) は「行ごとに異なる順序で、同時に積 1 を作る」問題として述べ直せる。
- **影響**：数学的誤りではない。ただし、結論の未解決問題「\(f\ge2\) で \(\mathrm{poly}(|\mathbb G|^f)\) 個の所有者で足りるか」は、この文献系列に置くべきである。
- **修正案**：
  - 付録 A に上の共役による言い換えを 1 段落加える。
  - Olson–White (1977) と、非可換群の small / ordered Davenport constant に関する近年の文献を引用する。
- **確信度**：Confirmed（恒等式）／文献の適用範囲は Probable

### m3　定理 A の隠れた定数を明示すべき

- **重大度**：Minor（主張の正確さ）
- **場所**：定理 A（152–161 行）、`thm:local-group-polydata`（1535–1566 行）、`lem:local-group-shortest`
- **内容**：証明から次の上界が読み取れる。
  \[
  \|\Wit\|_+\le|\mathsf S^\sharp|^{fr_{\max}}\bigl(3+r_{\max}(r_{\max}+1)\,C^{\mathrm{buf}}_{k,\mathbb H,f}\,|M_{k,\nu}|^f\bigr)\|G\|^2\bar\theta_G
  \]
  - ここで \(k=|\mathsf S|\)、\(|M_{k,\nu}|\le|\Sigma|^{<2k}+|\Sigma|^{2k}|\mathbb H|\) である。
  - したがって定数は少なくとも \(|\Sigma|^{2|\mathsf S|f}\) の大きさをもつ。非可換かつ \(f\ge2\) なら、さらに \(N^{2^{f^2}}\) が掛かる。
  - 窓–群の場合（`thm:window-group-polydata`）は \(K_{k,\ell,\mathbb G}\) が明示されているのに、局所群の場合は \(O(\cdot)\) のみで非対称である。
- **修正案**：`thm:local-group-polydata` に上式を書き、表 `tab:scope` に「定数は \(|\mathsf S|\)、\(|\Sigma|\)、\(f\) について指数的」と注記する。
- **確信度**：Confirmed

### m4　`prop:typed-separation` 直後の文で rank の条件が抜けている

- **重大度**：Minor
- **場所**：991–995 行
- **内容**：「定理 A は \(L_{\mathrm{sep}}\) の各既約良い表示に \(O(\|G\|^2\bar\theta_G)\) を与える」とある。しかし定理 A は rank \(\le r_{\max}\) の表示に限られ、定数も \(r_{\max}\) に依存する。
- **修正案**："for each of its reduced good presentations **of rank \(\le r_{\max}\)** (with the constant depending on \(r_{\max}\))"
- **確信度**：Confirmed

### m5　`cor:iptd`(ii) の証明の論理の書き方

- **重大度**：Minor（論理は正しいが、文が無条件の主張に読める）
- **場所**：1960–1963 行
- **内容**："Such an algorithm has a characteristic sample for every member of the class" は、背理法の仮定として「データ条件を満たすアルゴリズムは」と読むべきところである。EHY Def. 2.12 の条件 2 は \(\mathcal R\) の各表示について特徴標本の存在を要求するので、論理自体は正しい（原文で照合済み）。
- **修正案**："If an algorithm satisfied the data condition, it would have a characteristic sample for every member of the class, since ..."
- **確信度**：Confirmed

### m6　`thm:lg-characterization` の (i)⇔(ii)⇔(iii) が外部文献の項目番号に依存している

- **重大度**：Minor（自己完結性）
- **場所**：2587–2592 行
- **内容**：(i)⇔(ii) と「\(\mathsf S^m=\mathsf K\)」との同値を Almeida et al. Prop. 2.3 の項目 (1)(3)(4) に帰着させている。私はこの番号を原文で照合できていない。ただし直接の証明は短い。
  - **(i)⇒(ii)**：\(\{e,f\}\cong U_1\) なら \(f\in e\mathsf Se\) は群 \(e\mathsf Se\) の冪等元なので \(f=e\)。矛盾。
  - **(ii)⇒(i)**：\(e\mathsf Se\) が群でないなら、非単元 \(x\) について \(x^\omega\ne e\)。このとき \(\{e,x^\omega\}\cong U_1\)。
  - **(i)⇒(iii)**：\(\mathsf K\) の冪等元 \(f\) をとると \(efe\in\mathsf K\cap e\mathsf Se\)。よって \(e=(efe)(efe)^{-1}\in\mathsf K\)。
  - **(iii)⇒(i)**：\(e\in\mathsf K\) なら \(e\mathsf Se\) は \(e\) の \(\mathcal H\)-類で、群である。
- **修正案**：上の 4 行を証明に加え、引用は帰属のためだけにする。
- **確信度**：同値性そのものは Confirmed／引用番号は Unresolved（未照合）

### m7　英日版の不一致

§VI を参照。Minor、Confirmed。

### m8　表記の衝突と誤植

- **重大度**：Minor（任意修正）
- **内容**：
  - \(m_0\) が二重に定義されている：窓の閾値（402 行）と `lem:order-homogenize` の \(m_0:=n_0\)（2405 行）。
  - `lem:group-interval` の証明でクラス数に \(c\) を使っており、反鎖の上界 \(c\) と衝突する。
  - 2409 行に "... on a common line, If \(n\ge\) ..."（カンマの後が大文字）の誤植がある。
- **確信度**：Confirmed

### m9　要旨の「必要」の表現

- **重大度**：Minor
- **場所**：要旨 86–88 行
- **内容**："Length linear in grammar size times rule thickness is necessary under every typing over large enough alphabets." は、個々の標的についての主張と誤読されうる。実際の主張は、ある有限標的族について最悪の場合に必要、というものである（定理 B(i)）。
- **修正案**："... is necessary in the worst case (for explicit finite targets with rank-two presentations) under every typing ..."
- **確信度**：Confirmed

### m10　Yoshinaka の \(\tau_G\le\|G\|t_G\) への言及

- **重大度**：Minor（任意）
- **内容**：`lem:thickness-equivalence`(iii) の \(\theta_G\le2\|G\|\max\{1,t_G\}\) は本論文内で正しく証明されている。ただし Yoshinaka (2011, §4.3) は \(\tau_G\le\|G\|t_G\) を述べている（原文で確認）。一言触れると読者に親切である。

---

## III. 定理別検証表

| 対象 | 検証結果 | 最大の懸念 | 判定根拠 |
|---|---|---|---|
| **定理 A**（`thm:local-group-polydata`） | **正しい** | 定数の巨大さ（m3）。数学的欠陥なし | 証明の鎖をすべて手で再構成した：`lem:heavy-node-count` → `lem:lg-buffered-owners` → `lem:local-group-blocks` → `prop:block-replacement-interface` → `lem:witness-length-template` → `thm:data-from-typed-thickness`。計算検査と矛盾なし |
| **非可換群の同時短縮**（`lem:block-replacement`(b)、`lem:group-block-order`、`lem:two-sequence`、`lem:order-homogenize`、`lem:group-interval`） | **正しい**（m1 の言明修正を除く） | `lem:group-interval` の \(t=u\) が明示されていない（m1） | 下記「定理 A の詳細」と付録 Z を参照 |
| **局所群への拡張**（付録 B） | **正しい** | なし | Rees 座標、右作用の恒等式、\(\Lambda\) 座標が窓で決まること、`lem:local-group-morphism`、(iv)⇒(i) の群構造を手で確認。ブロック分解の数値検査 67,322 例で失敗 0 |
| **定理 B**（`prop:linear-factor-all-fanout`、`cor:trivial-exact`） | **正しい** | 「必要」の表現（m9） | 部分集合の代入可能性、文法サイズ \((7f+11)q+6n+3f+10\)、\(\|G\|\ge q+1\)、下界の算術を確認。小さい場合を全数検査 |
| **定理 C**（`thm:fanout-one-data`） | **正しい** | なし | 「if」は定理 A の \(f=1\)。「only if」は \(U_1\) の埋め込みと `prop:three-letter-family`。\(3\cdot2^n-1\ge2^{(17n+7)/17}\) も確認 |
| **倍増族と parser**（付録 G） | **正しい** | なし | (D1)–(D3)、到達可能スタックの形、各文字の部分単射性、`lem:app-br-exchange`、分岐同期、合同性を手で確認。\(n\le4\)（\(|L_4|=1806\)）で Clark–Eyraud 代入可能性を全因子について計算確認 |
| **fan-out 2 非持ち上げ**（`thm:doubling-no-lift`、`lem:power-transfer`） | **正しい** | なし | 添字の不等式を確認：\(i_0+p\le|\mathsf S|+1\)、\(n\ge2|\mathsf S|+2\Rightarrow j\ge i_0\)、\(\delta+j\le n-1\)、\(w_{\mathrm M}\ne\eps\)。\(n=6\) で \(w'\ne W_n\)、Parikh 一致、\(w'\notin L_6\) を計算確認 |
| **非 CFL 分離例**（`prop:typed-separation`、`prop:lg-needed-target`、`prop:nonabelian-needed-target`） | **正しい** | 分離は「クラスの被覆」についてのもの（論文自身が明記） | 文法、非 CFL 性、strictly 2-local 補題、型の分離語（\(\#_{\mathtt{ab}}\)、\(g_{\mathrm B}\)）を確認。分離語は計算でも確認 |
| **再構成の質的保証**（付録 D） | **正しい** | Yoshinaka 2015 の原文は未照合 | 健全性・完全性・正確な再構成・Gold 同定を、Yoshinaka 2011 の Type I–III、Lemma 6–7、Theorem 1 と照合 |
| **正規化・厚さ**（付録 F、`lem:thickness-equivalence`） | **正しい** | (a)–(d) の各段のサイズ係数は概略的 | 言語の恒等式とサイズ係数 \(2^f, f!, 2^{fr_{\max}}\) の妥当性を確認。厚さ (i)–(iv) は独立に再導出 |

### 定理 A の詳細（依頼 §3 A-1〜A-4 への回答）

**A-1　最短代表と厚さ**

- reduced good であることは十分である。ε-free から各成分が非空になり、`lem:witness-length-template`(i) の型の伝達と `lem:local-group-blocks` の窓が働く。nondeleting・linear から、各ノードの成分が根の成分の連続区間として一度ずつ現れる。
- λ-minimal 導出（まず総長、次にノード数を最小化）では、同じラベルの祖先と子孫は存在しない。したがって根から葉への経路は高々 \(n_\lambda(G)\) ノード。
- 重いノード（総長 \(>\bar\theta_G\)）は祖先について閉じた部分木をなし、その葉は反鎖である。したがって重いノード数 \(\le c\,n_\lambda(G)\)。
- 終端記号は、重いノードが書くもの（各 \(\le\bar\theta_G\)）か、軽い子の中にあるもの（各 \(\le b\)）である。
- 循環はない。λ 値は元の文法 \(G\) 上で扱われ、型細分 \(\widetilde G_0\) の厚さは使っていない。指数的悪化（`prop:typed-thickness-exponential`）は回避されている。
- 空語は開始記号でのみ扱われる。\(L\cap\Sigma^+=\emptyset\) の場合は既約表示が存在しないので、定理 A は空虚に成立する。境界事例の見落としはない。

**A-2　非可換群の同時置換（最重点）**

- **`lem:group-block-order`**：すべての場合分けを独立に追跡した。
  - 同方向で \(X\wedge Y\) なら交互配置。片側だけなら分離。\(\neg X\wedge\neg Y\) は循環による矛盾。
  - 逆方向では \(X\wedge Y\) と \(\neg X\wedge\neg Y\) が \(n\ge3\) で矛盾する。
  - 交互配置の推移性、クラス領域に他の点が入らないこと、chunk 構造も確認した。
  - 計算：全順列を検査した。\((|T|,n)=(1,3),(2,3),(3,3),(2,4),(2,5)\) の均質配置はそれぞれ 2, 12, 108, 12, 12 個あり、すべて結論を満たした。
- **`lem:two-sequence`**：
  - nx 連鎖の議論（列が非増加のとき）と \(i^\ast\) による 2 分割（非減少のとき）を確認した。\((m-1)^2+1\ge2m-1\iff(m-1)(m-3)\ge0\) である。
  - \(m=3\)、\(m'=5\) を全数検査した：単調な関数 98 個すべてで成立。\(m'=4\) では 4 個の反例があり、閾値 \((m-1)^2+1\) は \(m=3\) で必要である。
- **`lem:order-homogenize`**：
  - \(m_{q+1}=(m_q-1)^2+1\le m_q^2\) と、\(|\mathcal O|\le f^2\) を確認した。
  - 証明どおりの構成的実装を、型 2 個・同じ行・\(|\mathcal O|=4\)・\(n=m_4=65537\) で 20 回実行した。抽出された 3 点はすべて均質だった。
- **`lem:group-interval`**：
  - 区間 \((p,p']\) を置換した値は \(P_p(Q_p^{-1}Q_{p'})(P_{p'}^{-1}P_n)\) である。これが \(P_n\) に等しいことと \(\eta_p=\eta_{p'}\) は同値であり、積の順序の入れ替えは一切使っていない。
  - 減少する領域では添字 \((a,b]\) が chunk \((n-b,n-a]\) に対応し、状態は \(\eta_{n-j}\) をとる。
  - 状態は \(n+1>|\mathbb G|^f\ge|\mathbb G|^c\) 個あるので鳩の巣が働く。
  - 計算：\(\eta\) による判定は、ランダムな chunk 列 2,000 組で総当たりの結果と完全に一致した。逆順の \(Q_p^{-1}P_p\) で判定すると 5,000 例中 804 例で誤る。論文の「順序は強制される」という注意は正しい。\(S_3\)、\(f=2\)、\(n=36\) のランダムな均質族 300 個すべてで区間が見つかった。
- **所有者の扱い**：
  - 除外した所有者のブロックは元の値のまま定数になる。\(J\) は残した所有者からしか選ばれないので、元の族での \(\operatorname{val}(J)\) と一致する。
  - パターン数 \(\le f\cdot f^f\cdot f!\) は過大評価だが正しい。
- 例 `ex:nonabelian-reverse-owner` の 2 行の値がともに 1 になることを確認した。この計算は積の規約によらない。

**A-3　局所群への拡張**

- **Rees 座標**：
  - \(r_j=(i_0,p_{ji_0}^{-1},j)\) は右単位元、\(e'=(i,p_{j''i}^{-1},j'')\) は左から固定する冪等元であることを確認した。
  - 右作用の恒等式 \((i,\gamma,j)y=(i,\gamma\,\mathrm{act}(j,y),j')\) を確認した。
  - \(\mathsf S^k\subseteq\mathsf K\) から、\(j_t\) は直前 \(k\) 文字で決まる。したがって \(\nu(F)\) は長さ \(k+1\) の因子で定まる。
- **(iv)⇒(i)**：\(\{\langle p,q\rangle\}\times\mathbb G\) に演算 \(\gamma\Delta\gamma'\) を入れたものは \(\gamma\mapsto\gamma\Delta\) で \(\mathbb G\) と同型な群になり、\(e\mathsf Te\) はその有限部分半群なので部分群である。
- **kernel refinement**：\(|w|\ge2k\) では \((\star)\) により \(s(w)\) が \(\lambda_{k,\nu}(w)\) で決まり、短い語は窓 \(\widehat s_{k,k}\) が正確に記録する。
- **`lem:lg-buffered-owners`**：
  - 近傍の数 \(\le4kf\) と、貪欲法による独立集合の大きさ \(\ge m/(4kf+1)\) を確認した。
  - 距離が \(2k\) 以上なので、拡大ブロックの内部は互いに素である。
  - 拡大ブロックの先頭 \(k\) 文字に \(Q_1\) の区間が入らない（\(l_0\) の最小性と距離による）。
  - 同じ所有者の拡大ブロックを併合しても、他の \(Q_1\) 所有者は入り込まない。入り込めば距離 \(<2k\) となり、独立性に反する。
- **`lem:local-group-blocks`**：長さ \(k+1\) の因子は、あるブロックの内部にあるか、ブロックと高々 \(k\) 文字で接するかのどちらかである（ブロック長 \(\ge2k\) による）。後者の列は \(J\) によらない。
- **暗黙の制限の有無**：可換群や窓–群への暗黙の制限はない。群 \(\mathbb H\) は Rees 構造群で任意であり、`prop:block-replacement-interface` は任意の有限群について使われている。定数は \(s,\Sigma,f,r_{\max}\) にのみ依存し、対象文法には依存しない。

**A-4　特徴データへの変換**

- 語の数：\(|\Wit|\le C_s(G)\le|\mathsf S^\sharp|^{fr_{\max}}\|G\|\)
- 各語の長さ：\(\le2\bar\theta_G+r_{\max}\beta_\lambda\)。文脈は \(\bar\theta_G\)、テンプレートは \(\bar\theta_G\)、子は \(r_{\max}\) 個。
- \(\beta_\lambda=(r_{\max}+1)\bar\theta_G\,C^{\mathrm{buf}}\,|V||M_{k,\nu}|^f=O(\|G\|\bar\theta_G)\)
- 積をとると \(O(\|G\|^2\bar\theta_G)\) になり、指数は主張どおりである。隠れた定数は m3 に記した。

### 定理 B・C の要点

**B**

- \(i\ne j\) のとき、文脈の固定部分に置ける標識は高々 \(d-1\) 個である。よって \(\vec x\) は \(\ge d+1\) 個の標識を含み、ある成分が 2 個を含む。この成分は \(w_i\) を一意に決める。
- \(f=1\) の 2 文字版では、因子 \(\mathtt d\mathtt a^i\mathtt d\) が一意である。
- 一部の作用素についての下界を一般化しすぎているか：していない。作用素は「\(L\) と \(L\setminus\{w_i\}\) の両方に特徴標本をもつ集合駆動型」に限られ、`lem:distinguishing` の仮定と一致している。
- rank の整合性：\(G^{(f)}_{q,n}\) は rank 2 なので、達成性の主張には \(r_{\max}\ge2\) が必要である。`cor:trivial-exact` に正しく明記されている。

**C**

- 個別の型付けについての主張と擬多様体についての主張は混同されていない。Remark `rem:fanout-one-data`(b) も正しい。
- rank 1 の主張を rank 2 以上の結果から導いている箇所はない。定理は \(r_{\max}\ge2\) に限られている。

### その他の補題・命題の検証台帳（表に含めなかったもの）

| ラベル | 判定 | メモ |
|---|---|---|
| `prop:abelian-coset-filter` | ✓ | 無限 \(\mathsf A\) の場合の但し書きも正しい |
| `lem:app-lf-path` | ✓ | |
| `lem:filling-identity`、`lem:witnessed-composition` | ✓ | nonmerging により内部区切りが非空になる |
| `prop:output-invariants`、`lem:identity-canonical-contexts`、`lem:typed-homogeneity` | ✓ | |
| `prop:reconstruction-soundness`、`prop:completeness`、`thm:exact-reconstruction`、`thm:poly`、`cor:gold-explanatory` | ✓ | Yoshinaka 2011 と照合 |
| `prop:good-normalization`、`lem:normalization-stages` | ✓（概略） | (c) の「支持パターン」の飽和計算は標準的 |
| `lem:thickness-equivalence` (i)–(iv) | ✓ | (iv) の「derivational」は lift の一意性による |
| `lem:witness-length-template` (i)–(iv) | ✓ | |
| `thm:data-from-typed-thickness`、`cor:distribution-representatives` | ✓ | |
| `lem:type-deletion`、`lem:distinguishing`、`prop:rare-type` | ✓ | |
| `prop:typed-thickness-exponential` | ✓ | \(\theta\le2\)、\(t_{\mathrm{typ}}\ge2^n\) |
| `lem:heavy-node-count`、`lem:marked-heavy-window-group`、`thm:window-group-polydata`、`rem:window-abelian` | ✓ | 印の数 \(\le f(k+\ell+1)\)、\(K_{k,\ell,\mathbb G}\) の算術 |
| `lem:block-replacement`(a)(c) | ✓ | (c) は m2 を参照 |
| `rem:davenport-size` | 引用定理は未照合 | 主定理の鎖の外 |
| `lem:local-group-morphism`、`lem:lg-rees-window-coordinate`、`thm:lg-characterization` | ✓（m6） | |
| `lem:mcfg-li-group-window` | ✓ | \(eye'=ee'\)（LI 恒等式） |
| `prop:li-g-strict` | ✓ | \(u=\mathtt b^m\mathtt a^n\mathtt b^m\)、\(v=\mathtt b^{2m}\) |
| `lem:flag-separation`、`lem:sl2-boundary-control` | ✓ | |
| `lem:reduced-good-hypothesis`、`cor:iptd` | ✓（m5） | EHY Def. 2.12 と照合 |
| 結論 "Tightness" の例（\(\|G_n\|=10n+16\)、\(t_{\mathrm{typ}}\ge n+1\)） | ✓ | 手計算 |

---

## IV. 付録の完全監査

| 付録 | 何を証明するか | 主要な補題 | 自己完結性 | 本文への依存 | 不安な箇所 |
|---|---|---|---|---|---|
| A　有限群の同時ブロック置換 | `prop:block-replacement-interface` | `lem:group-block-order`、`lem:group-interval`、`lem:two-sequence`、`lem:order-homogenize` | ほぼ自己完結。Davenport 定数の上界のみ外部（Remark、主定理外） | なし | **m1**（言明）。m2（先行研究） |
| B　局所群座標と MCFG ブロック短縮 | `thm:lg-characterization`、`lem:local-group-shortest` | `lem:local-group-blocks`、`lem:lg-buffered-owners`、Rees 座標 | (i)–(iii) の同値性を Almeida et al. に依存（m6 で自己完結化可能） | `lem:heavy-node-count`、`lem:thickness-equivalence` | なし |
| C　分離標的 | `prop:lg-needed-target`、`prop:nonabelian-needed-target` | `lem:sl2-boundary-control`、`lem:flag-separation` | 自己完結 | `prop:abelian-coset-filter`、項目 (c) | なし |
| D　質的再構成 | 健全性、完全性、正確な再構成、`thm:poly`、Gold 同定 | `lem:filling-identity`、`lem:witnessed-composition` | 自己完結（Yoshinaka の Prop. 4 による所属判定時間のみ外部） | — | なし |
| E　型付き witness | `prop:output-invariants`、`lem:thickness-equivalence`、`lem:witness-length-template` ほか | `lem:semigroup-transfer` | 自己完結 | — | なし |
| F　良い正規化 | `prop:good-normalization` | `lem:normalization-stages` (a)–(d) | 構成は標準文献を参照し、恒等式とサイズは自前 | — | (c)(d) は記述が簡潔。査読者によっては詳細を求めうる（任意） |
| G　三文字倍増族 | `prop:three-letter-family` | parser (D1)–(D3)、`lem:app-br-recognition`、`lem:app-br-exchange`、`lem:app-br-branch`、`prop:app-br-congruence` | 自己完結（companion の議論を翻案と明記） | `prop:rare-type` | なし（\(n\le4\) で計算確認） |
| H　全 fan-out の線形因子 | `prop:linear-factor-all-fanout` | `lem:app-lf-path` | 自己完結 | `thm:exact-reconstruction`、`lem:distinguishing` | なし |

---

## V. 新規性と引用の監査

### 分類

1. **既知の結果をそのまま使っている**
   - 質的再構成とその保証：Yoshinaka 2011 と 2015 の型付き版。原稿自身が "not new results" と明記しており、帰属は適切。
   - \(\mathbf{LG}\) の特徴づけ、Rees 座標、\(\mathbf{LG}=\mathbf{Grp}*\mathbf D\)：古典的。
   - Davenport 定数、Erdős–Szekeres、正規化構成。
2. **既知の結果を非自明に一般化している**
   - 窓型付けの多項式データ（Yoshinaka 2008、\(f=1\)）を、窓–群および局所群の型付きで fan-out \(f\) に拡張したこと。
   - 稀型下界と倍増族による \(f=1\) の \(U_1\) 下界（companion の 5 文字版の 3 文字版）。
   - 線形因子下界：Yoshinaka の \(\|K_G\|\le|P|\tau_G\) が全 fan-out で定数倍まで達成されることを示した。
3. **本論文独自の結果**
   - **定理 A の核心**：非可換有限群で、交互配置された \(f\) 成分のブロックを、順序付き積を保ったまま同時に置換する論法。これに局所群座標と buffer 補題を組み合わせたもの。既知理論の単純な系ではない。
     - 窓–群の場合は群準同型なので、各成分の値はブロック値の順序付き積になり、可換群なら零和で済む。非可換の場合は、ブロックの交互配置と行ごとに異なる所有者の順序（増加・減少）を同時に扱う必要があり、Ramsey 型の均質化と \(\eta\) 状態による区間選択が新しい。
     - ただし、\(f=1\) の場合は m2 のとおり古典的な順序付き積 1 問題そのものである。
   - 定理 C の \(f=1\) における擬多様体境界の厳密性（companion の \(\mathbf{LI}\vee\mathbf{Grp}\) から \(\mathbf{LG}\) への拡張と、only-if 方向の組み合わせ）。
   - `thm:doubling-no-lift`（冪移送による fan-out 2 の非持ち上げ）。
   - 非 CFL の分離例。

### 引用の不足・確認事項

- Olson–White (1977)、ordered / small Davenport constant（m2）：**追加を推奨**。
- Yoshinaka 2011 の引用：§2.3（λ-free、Lemma 1）、§3.1 Example 5（\(\{w\#w^R\}\)）、§4.1 Type I–III、§4.3 thickness・Definition 1・Lemma 6–7・Theorem 1・Corollary 2・Proposition 4 を原文で確認した。**すべて正確**。
- EHY 2016 Def. 2.11（厚さ＝規則左辺の最短語長の最大、すなわち \(t_G\)）と Def. 2.12（IPTtD）を原文で確認した。本論文の使い方は正確。
- Yoshinaka 2015 の Lemma 2–3・Theorem 1、Almeida et al. Prop. 2.3 の項目番号、Costa 2002、Duncan et al. 2026：**原文未照合**。照合済みとは書けない。
- **companion 論文（TCS-D-26-00494）との重複**：
  - 表 `tab:companion-overlap` と「we use no companion theorem」の明記は適切である。parser 論法の翻案も付録 G 冒頭で明示されている。
  - ただし、companion が審査中のまま本論文を投稿すると、編集者が \(f=1\) 部分の重複を問題にする可能性はある。`PAPER.yaml` の「companion の判定後に投稿」という方針は妥当である。

---

## VI. 英日版の不一致

| 箇所 | 英語版 | 日本語版 | 修正案 |
|---|---|---|---|
| 定理 C(ii) と `thm:fanout-one-data`(iii) | \(\|G_n\|=13n+7\)、\(\bar\theta_{G_n}=4n\)、\(3\cdot2^n-1\ge2^{(\|G_n\|+\bar\theta_{G_n})/17}\) と、「no intermediate growth occurs」の一文 | \(O(n)\) のみ。\(2^{(\cdot)/17}\) の下界と「中間的成長なし」の文がない | 日本語版に英語版の正確な数値と結論文を移植する（意味は矛盾しないが、日本語版の方が弱い） |
| 日本語版のみのラベル | — | `cor:typed-sandwich`（系）、`lem:boundary-short-canonical`（Remark）、`lem:typed-thickness-equivalence`（Remark） | 内容は確認し、正しい（\(\theta_G\le\theta_{\mathrm{typ}}\)、\(t_{\mathrm{typ}}\le\theta_{\mathrm{typ}}\le2\bar\theta_G+r_{\max}t_{\mathrm{typ}}\)、はさみうち）。Remark に `lem:` 接頭辞は紛らわしいので `rem:` に改める。英語版に入れるか、日本語版の付録扱いにするかを明示する |
| 定理 A、定理 B、\(c_{\mathbb G,f}\)、\(C^{\mathrm{buf}}\)、\((7f+11)q+6n+3f+10\)、\(13n+7\)、`thm:doubling-no-lift`、`lem:power-transfer`、`op:fanout-two`、`def:uniform-polydata` | — | — | 主張・仮定・量化子・定数は一致（照合済み） |

日本語版の定理 A の直後の段落には、IPTtD についての文が英語版より詳しく書かれている（引用 Yoshinaka2008、EHY2016）。内容は英語版の `cor:iptd` と整合している。

---

## VII. 投稿前に必要な修正

### 必須修正（主張の正確さ）

1. **m1**：`lem:group-interval` の仮定に「\(t=u\) allowed」を明記する。現状の文言には、言明が偽になる読み方がある。
2. **m4**：`prop:typed-separation` 直後の文に rank \(\le r_{\max}\) を補う。
3. **m9**：要旨の「necessary」を最悪の場合の主張として明確にする。
4. **m7**：日本語版の定理 C を英語版の数値と結論に揃える（日本語版も公開・提出するなら）。

### 推奨修正（論理の説明・引用・構成）

1. **m2**：付録 A に共役による言い換え（\(h_b\)）を書き、Olson–White の ordered Davenport constant を引用する。結論の未解決問題をこの文脈に置く。
2. **m3**：定理 A の定数を明示し、\(|\Sigma|^{2|\mathsf S|f}\) 程度の依存を表に注記する。
3. **m6**：`thm:lg-characterization` の同値性を数行で自己完結させる。
4. **m5**：`cor:iptd`(ii) の背理法の書き方を直す。
5. 付録 F の (c)(d) について、支持パターンの飽和と合成分解の一意性を 1–2 文ずつ補うと、査読者からの質問を減らせる。

### 任意修正（表現・組版）

- **m8**：\(m_0\) と \(c\) の記号衝突、2409 行の誤植。
- **m10**：Yoshinaka の \(\tau_G\le\|G\|t_G\) に言及する。
- 「uniform polynomial characteristic-data length」の "uniform" は標的について一様という意味である。型付けについての一様性と誤解されないよう、定義直後の注意（既存）を定理 C の本文にも短く置く。

---

## VIII. 最終判断

1. **定理 A は正しいか。**
   正しいと判断する。証明の鎖をすべて独立に再構成し、穴は見つからなかった。非可換群の順序分類・均質化・区間選択、局所群座標、buffer 補題も含む。唯一の欠陥は `lem:group-interval` の言明の文言（m1）で、適用箇所では正しく満たされている。
2. **定理 B は正しいか。**
   正しい。部分集合で閉じた族の代入可能性、サイズ、下界の算術、作用素の範囲を確認した。
3. **定理 C は正しいか。**
   正しい（\(f=1\)、\(r_{\max}\ge2\)）。倍増族の parser による代入可能性は手で検証し、\(n\le4\) で計算でも確認した。
4. **最も危険な補題はどれか。**
   `lem:group-interval` と `lem:group-block-order` の組。論法は正しいが、言明を単独で読むと仮定が不足している（m1）。次点は `lem:lg-buffered-owners`。正しいが、拡大ブロックの併合と他所有者の文字の扱いが簡潔な記述に依存している。
5. **現状のまま TCS に投稿してよいか。**
   数学的には投稿を止める誤りはない。ただし m1・m4・m9 は数時間で直せるので、修正してからの投稿を勧める。新規性の位置づけのため m2 と m3 も入れるのが望ましい。
6. **投稿を止めるべき問題はあるか。**
   数学的にはない。編集上の判断として、companion 論文（TCS-D-26-00494）の結果を待つという `PAPER.yaml` の方針は妥当である。
7. **次に著者が一つだけ修正するとしたら何か。**
   **m1**：`lem:group-interval` の仮定に「\(t=u\) を含む」を明記すること。定理 A の核心にある補題で、現状の文言のままでは単独で読んだときに偽になる唯一の箇所である。

### TCS 査読者としての総合評価（依頼 §10）

- **新規性**：中心は定理 A の非可換同時短縮で、明確である。定理 A を主役にした構成は適切である。定理 B・C は境界を与える補完として妥当である。
- **fan-out 2 の扱い**：定理 1 つと未解決問題 1 つという分量は適切である。要旨・序論・結論のいずれにも、fan-out 2 の境界を解決したかのような過大表現はない（確認済み）。
- **非 CFL 分離例**：「正規な旗付き接頭部＋固定の非 CFL 部分」という単純な構成である。クラス被覆の分離としては正しく有益だが、MCFG 特有の深さは乏しい。論文も 1670 行付近でそう認めている。本文を 1/2 程度に短縮しても価値は落ちない。
- **長さ（42 頁）**：内容に見合う。付録 F・G は短縮の余地がある。
- **掲載価値の懸念**：
  - 上界と下界の間に \(\|G\|\) 一因子の差が残る。
  - 定数が \(|\Sigma|,|\mathsf S|\) について指数的、\(f\) について二重指数的である。
  - 結果が出力表示と witness 法に相対的である。
  
  TCS の査読者はこれらを「限定的」と評する可能性がある。ただし、いずれも論文自身が正直に述べており（"Tightness of the exponents"、Remark `rem:fanout-one-data`）、主張は過大ではない。

---

## 付録 Z　計算による独立検証の記録

すべて本査読のために新規に実装した（`verify_scripts/`）。既存のリポジトリ内スクリプトは使っていない。**数値実験は証明の代わりではない**。各項目の数学的根拠は §III の手による再構成にある。

| スクリプト | 内容 | 結果 |
|---|---|---|
| `v1_groups.py` | `lem:group-block-order` の全順列検査（5 設定）、`lem:two-sequence` の全数検査（\(m=3\), \(m'=4,5\)）、\(S_3\)・\(f=2\)・\(n=36\) のランダム均質族 300 個での区間存在、\(\eta\) 判定の総当たり照合、逆順 \(Q^{-1}P\) の不正確さ、例 `ex:nonabelian-reverse-owner` | 全成功。\(m'=4\) では反例 4 個（閾値が必要であることを確認） |
| `v2_homog.py` | `lem:order-homogenize` と `lem:two-sequence` の証明どおりの構成的実装（\(n=65537\)、\(|\mathcal O|=4\)） | 抽出集合はすべて均質 |
| `v3_families.py` | 倍増族 \(n=1..4\) の CE 代入可能性・\(W_n\) の一意性・\(|W_n|\)・\(\theta=4n\)。`thm:doubling-no-lift` の \(w'\)（\(n=6\)）。線形因子族 4 設定の全部分集合の \((f,\mathrm{triv})\)-代入可能性。サイズ式 | 全成功 |
| `v4_sliding.py` | `lem:local-group-blocks`（\(k=1,2,3\)、67,322 例）、`lem:local-group-morphism` の公式、分離語 | 全成功 |
| `v5_conjugation.py` | m2 の共役恒等式（\(S_4\)、20,000 例） | 失敗 0 |
| `v6_interval_hyp.py` | m1：\(t\ne u\) のみと読んだ `lem:group-interval` の反例探索 | 反例を発見（\(S_3\)、\(n=6\)） |

**計算で確認できなかった範囲**：

- 閾値 \(M_{\mathbb G,f}\) 付近の非均質族の全数探索（規模的に不可能）。この部分は証明でのみ確認した。
- 局所群一般（Rees 構造が非自明で \(\mathsf S\ne\mathsf K\) の半群）での \((\star)\) の数値検査は行っていない。手による証明のみ。

---

*本報告はリポジトリへのコミット・push を行っていない。`reviews/` に置く場合は著者の判断で追加されたい。*