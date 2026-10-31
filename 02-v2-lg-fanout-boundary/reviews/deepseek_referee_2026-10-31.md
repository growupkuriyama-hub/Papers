# 査読報告 — Local Groups, Fan-Out, and the Length of Characteristic Data in Typed Distributional Learning of Multiple Context-Free Languages

**査読者**：DeepSeek（形式言語理論／MCFG・分布学習・有限半群と擬多様体）
**日付**：2026-10-31
**対象**：`02-v2-lg-fanout-boundary/main.tex`（4,520 行）
**参照した資料**：同フォルダの `README.md`、`INSTRUCTIONS_FOR_AI.md`、`reviews/chatgpt_compare_v1_v2_2026-10-30.md`、姉妹論文 `01_fixed-h-cfg/main.tex`（以下「01」）。

---

## 0. 対象の同定

- 題名は "Local Groups, Fan-Out, and the Length of Characteristic Data in Typed Distributional Learning of Multiple Context-Free Languages"（L60–61）で、指定の接頭辞と一致する。
- `\label{prop:u1-weight-all-fanout}` が L1929 にあり、命題本体（L1928–1933）と証明（L3918–3955、付録 J）が存在する。**査読対象は新しい版**であり、旧版ではない。よって査読を実施した。
- 原稿・付録・README 等のファイルは一切変更していない。出力は本報告のみ。計算はすべて一時ディレクトリで行い、`reviews/` には本ファイル以外を置いていない。

---

## 1. 総合判定

**minor revision**

理由：

1. 前回外部査読が致命的・重大とした 2 点、すなわち `cor:trivial-exact` の「最大の特徴標本」と `thm:A(ii)` のアルファベット条件は、いずれも正しく修正されている。要旨（L78–81）、定理 A(ii)(iii)（L163–171）、`cor:trivial-exact`（L1661–1671）、結論（L2104–2105）が整合し、「最大」という無意味な量は残っていない。v1 §6.1–6.2 も付録 K に復活し、MCFG 固有の実例が戻った。
2. 新規の `prop:u1-weight-all-fanout`（全ファンアウト・全 $U_1$ 型付け・重み一定）と `prop:binary-u1-weight-slice` の証明を 1 行ずつ追い、論理的な破綻は見つけられなかった。特に前者は「重み一定」から $\psi(\boldsymbol\eta_{R,j})=\ell_{u_j}$ を強制する点が巧妙で、場合分け（$\lambda\le1$／$\lambda>1$ と $N<\lambda$／$N\ge\lambda$）も閉じている。主要な数値（$\|G\|$、$\bar\theta_G$）はすべて独立に再計算して一致した（§5.3）。
3. 反例・偽の主張は発見できなかった。残る指摘は、証明の 1 文不足（R1）、定理 B(iii) の量化の不正確さ（R2）、要旨の証明より広い表現（R4）、重複表の 1 セル（R3）、用語の未定義（R5）、AI 利用宣言（R6）で、いずれも本文の修正で足りる。
4. ただし付録 A・F・G・H の組合せ論的証明は長く、本報告は「私が追えた範囲で誤りなし」であって機械検証ではない。投稿前に `lem:app-u1-parikh`（付録 H）と `lem:order-homogenize`（付録 A）に限定した第 2 の独立再読を勧める。

---

## 2. 観点別評価（各 10 点）

| 観点 | 点 | 理由 |
|---|---:|---|
| 正しさ | 8 | 偽の主張・反例は発見できず、新規証明も追えた。`prop:binary-u1-weight-slice`(i) の $\mu^\star$ への帰結に 1 文の欠落（R1）。 |
| 主張と証明の一致 | 8 | A(ii)(iii) は修正済みで整合。B(iii) の最後の文（R2）と要旨（R4）に、証明より広い読みが残る。 |
| 新規性 | 8 | 重み一定での全ファンアウト二次上界、ファンアウト 2 の多項式データ、LG 境界は新しい。v1・姉妹論文からの移植は明示的に帰属済み。 |
| MCFG 固有性 | 7 | 非可換群の owner 単位同時置換と二穴 power transfer は MCFG 固有。ただし看板 B(i) はファンアウト 1（CFG 的）で、MCFG 固有の実例は付録 K に後退している。 |
| 構成と読みやすさ | 8 | 三定理の構成、定理ごとの付録参照、縮約の明示は明快。本文 24 頁に対し付録 28 頁で、付録 H の追跡には時間がかかる。 |
| 先行研究の扱い | 7 | 帰属は丁寧で、Yoshinaka の定性結果と本稿の長さ解析を明確に分けている。重複表の 1 セルが不正確（R3）。外部文献の番号は未照合（§6）。 |

合計 **46/60**。

---

## 3. 指摘一覧

| 番号 | 深刻度 | 場所（label・節・行） | 要旨 |
|---|---|---|---|
| R1 | 軽微 | §7 `prop:binary-u1-weight-slice`(i)（L1896–1913）、証明は付録 J（L3876–3916） | 「hence $\mu^\star\le B(\theta)$」が証明されていない。証明は純な yield を持つ非終端だけを扱い、type $\zeta$ の $\mu_\zeta\le B(\theta)$ に触れていない。 |
| R2 | 軽微 | §1 定理 B(iii)（L186–194） | 「this bound holds at every fan-out and for every typing onto $U_1$」は、重み $\psi_\lambda$ が型付けの $\Sigma_1$ に依存することを無視している。また type 1 の語が存在しない場合に「the shortest word of type 1」が定義されない。 |
| R3 | 軽微 | §1 `tab:companion-overlap` 第 1 行（L284–288） | 01 の "Lemma 2.2" は fresh-identity completion の補題で、typed reconstruction / Gold learner / typed-thickness のいずれでもない。 |
| R4 | 軽微 | 要旨（L86–90） | 「the typing onto $U_1$ with a single letter of type 1」は、証明済みの $s_{U,2}$（$\Sigma=\{\mathtt a,\mathtt b\}$）より広く読める。 |
| R5 | 表現 | 定理 A(ii)（L163–167）、要旨（L79–81） | "asymptotically smallest presentations" が未定義。(iii) が示すのは「最小の定数倍以内」。 |
| R6 | 表現 | 宣言（L4292–4297） | AI 利用の宣言が「organization / expression / editing」に限定されているが、著者側文書によれば 2 つの命題は AI の調査報告に由来する。 |

---

## 4. 指摘の詳細

### R1（軽微）`prop:binary-u1-weight-slice`(i)：$\mu^\star$ への帰結が未証明

**原文**（L1902–1903）

> \item Every nonterminal with a pure yield has exactly one pure yield, of length at most $B(\theta)$; hence $\mu^\star(L(G),s_{U,2})\le B(\theta)$.

**何が問題か。** 付録 J の証明（L3876–3899）が示すのは「純な yield を持つ非終端 $A$ について、その唯一の純な yield $\mathtt a^{\ell_A}$ の長さが $B(\theta)=\lfloor(\theta+1)^2/4\rfloor$ 以下」という**非終端についての**主張である。一方 $\mu^\star(L,s)=\max_{m\in M_L}\mu_m(L)$ は**実現される型**上の最大で、この文法では $m\in\{1,\zeta\}$ の両方が入りうる。$\mu_1$ は始非終端の純な yield から直ちに従うが、$\mu_\zeta$（$\mathtt b$ を含む最短語）は (i) の証明からは従わない。

**根拠。** 証明には $\mu_\zeta$ の議論がない。ただし命題自体は正しく、`prop:u1-weight-all-fanout` の証明の冒頭 2 文（L3921–3922）がそのまま埋める：$\mathtt b$ を含む語が存在すれば $\mathtt b$ を書く規則 $R$ があり、$R$ を使う文はすべて type $\zeta$ なので $\mu_\zeta\le\theta_G(R)\le\bar\theta_G\le B(\theta)$。つまり**証明の 1 文不足**であって、命題の偽ではない。

**修正案。** (i) の証明末尾（L3899 の直前）に次を追加する：

> If some word of $L(G)$ contains $\mathtt b$, then some rule writes $\mathtt b$; every sentence using it has type $\zeta$, so $\mu_\zeta\le\theta\le B(\theta)$.

あるいは (i) の後半（$\mu^\star$ の部分）を `prop:u1-weight-all-fanout` に委ね、そこでは証明済みであることを明記する。

**確信度：確認済み**（欠落は本文の記述から確認できる。命題の真偽については、上記の 1 文で閉じることを確認した）。

---

### R2（軽微）定理 B(iii) の最後の文：重みの型付け依存と存在前提

**原文**（L191–193）

> For targets whose words all have the same positive weight $|w|_{\mathtt a}+\lambda|w|_{\mathtt b}$, the shortest word of type $1$ has length at most $(\bar\theta_G+1)^2/4$, with equality for the targets of the first sentence (Proposition~\ref{prop:binary-u1-weight-slice}); this bound holds at every fan-out and for every typing onto $U_1$ (Proposition~\ref{prop:u1-weight-all-fanout}).

**何が問題か。** 2 点ある。

1. `prop:u1-weight-all-fanout`（L1928–1933）の仮定は「$\psi_\lambda$ が $L(G)$ 上定数」だが、その $\psi_\lambda$ は L1922–1926 で $\Sigma_1=\{x\in\Sigma:s(x)=1\}$ に対して定義される。定理の文は重みを $|w|_{\mathtt a}+\lambda|w|_{\mathtt b}$ に**固定したまま**「すべての $U_1$ への型付け」に量化しており、型付けを変えれば $\Sigma_1$ も変わるので、仮定が同一ではない。したがってこの文は、引用した命題からは直接従わない。
2. 「the shortest word of type 1」は、type 1 の語が存在しない場合に定義されない。たとえば $L=\{\mathtt a^4,\mathtt a^2\mathtt b^2\}$ は $|w|_{\mathtt a}+|w|_{\mathtt b}$ 一定だが、$\mathtt b\mapsto1,\mathtt a\mapsto\zeta$ の型付けでは type 1 の語が存在しない。

**根拠。** 定義（L1922–1926）と命題（L1928–1933）。なお $\Sigma=\{\mathtt a,\mathtt b\}$ では $U_1$ への全射型付けは $s_{U,2}$ かその swap しかなく、swap については $\lambda'=1/\lambda$ と取れば $\psi^{(s')}_{\lambda'}$ も定数になる（$|w|_{\mathtt a}+\lambda|w|_{\mathtt b}=W$ のとき $|w|_{\mathtt b}+\lambda'|w|_{\mathtt a}=W/\lambda+(\lambda'-1/\lambda)|w|_{\mathtt a}$）。よって**主張は（type 1 が実現されるとき）救える**が、その 1 文が本文にない。

**修正案。** 次のように書き換える：

> For every typing $s$ onto $U_1$, if the weight $\psi^{(s)}_{\lambda'}$ determined by $\Sigma_1=\{x:s(x)=1\}$ is constant on the target for some $\lambda'>0$ and type $1$ is realized, then the shortest word of type $1$ has length at most $(\bar\theta_G+1)^2/4$ (Proposition~\ref{prop:u1-weight-all-fanout}); for $s_{U,2}$ this is Proposition~\ref{prop:binary-u1-weight-slice}, and for its swap one takes $\lambda'=1/\lambda$.

**確信度：確認済み**（文言が引用命題の仮定と一致しないこと）。主張自体の反例は構成できなかったため、「偽」ではなく「本文だけでは従わない・ill-posed な場合がある」という指摘である。

---

### R3（軽微）`tab:companion-overlap` 第 1 行の "Lemma 2.2"

**原文**（L284–288）

> Typed reconstruction, Gold learner, typed-thickness witness bound
>  & Lemma~2.2; Sections~4--5; Lemma~6.2, Corollary~6.3
>  & Tuple versions (Section~\ref{sec:learner}, Theorem~\ref{thm:data-from-typed-thickness}); qualitative results credited to Yoshinaka; not new\\

**何が問題か。** 01 は `\newtheorem{theorem}{Theorem}[section]` の下で theorem/lemma/proposition/corollary/definition/remark が同一カウンタを共有する。この数え方で 01 を列挙すると、**Lemma 2.2 は "canonical fresh-identity completion"**（型付けの予備、v2 の `lem:semigroup-transfer` の類似物）であり、typed reconstruction でも Gold learner でも typed-thickness でもない。対応するのは Theorem 4.2（soundness）、Theorem 5.2（completeness）、Theorem 5.3（exact reconstruction）、Corollary 5.4（Gold）、Lemma 6.2、Corollary 6.3 である。

**根拠（計算）。** 01 の `main.tex` を節ごとに数えるスクリプトの出力（抜粋）：

```
=== SECTION 2: Preliminaries
  2.1  definition  fixed-$s$ substitutability          label=def:hsubst
  2.2  lemma       canonical fresh-identity completion  label=lem:fresh-identity
=== SECTION 4: Reconstruction Operator and Sequential Learner
  4.1  lemma       sample consistency                   label=lem:sample-consistency
  4.2  theorem     soundness                            label=thm:soundness
=== SECTION 5: Finite Witnesses, Exact Reconstruction, and Complexity
  5.2  theorem     completeness from the finite witnesses   label=thm:complete
  5.3  theorem     exact finite-sample reconstruction       label=thm:reconstruction-fixed-s
  5.4  corollary   Gold identification                      label=cor:ilt
=== SECTION 6: Typed Thickness for General Fixed Typings
  6.2  lemma       typed-thickness witness bound        label=lem:typed-thickness-bound
  6.3  corollary   characteristic data via BUNF normalization  label=cor:typed-thickness-data
```

他のセルは 01 の現行番号・内容と一致した：Proposition 3.5 = `prop:li-window`、Lemma 7.1 = `lem:window-typed-yield`、Theorem 7.2 = `thm:window-thick`、Lemma 7.4 = `lem:li-group-factor`、Corollary 7.5 = `cor:li-thickness`、Lemma 7.6 = `lem:U1-outside`、Remark 7.7 = 「LI∨Grp の十分性のみ、必要性は未証明」、Proposition 6.4 = `prop:typed-thickness-gap`（括弧付き倍増族 $L_n$）、Corollary 6.6 = `cor:typed-gap-intrinsic`、Theorem 8.3 = `thm:linear-poly`、Appendix C = 01 の第 3 付録「Substitutability of the bracketed doubling family」。**誤りは第 1 行の Lemma 2.2 のみ**。

**修正案。** "Theorem 4.2; Theorems 5.2--5.3, Corollary 5.4; Lemma 6.2, Corollary 6.3" に置き換える。Lemma 2.2 を残したい場合は、型付けの枠組み（fresh-identity completion）の行を別に立てる。

**確信度：確認済み**（01 の現物と突き合わせた）。

---

### R4（軽微）要旨の「the typing onto $U_1$ with a single letter of type 1」

**原文**（L86–90）

> Second, the fan-out-one obstruction does not carry over to fan-out two: there the typing onto $U_1$ with a single letter of type $1$ admits polynomial data although $U_1$ is not a local group, and the exponential fan-out-one family is not tuple-substitutable under any fixed typing.

**何が問題か。** `thm:binary-u1-polydata`（L2039–2054）が扱うのは $\Sigma=\{\mathtt a,\mathtt b\}$ 上の $s_{U,2}$（$\mathtt a\mapsto1$, $\mathtt b\mapsto\zeta$）**だけ**である。証明（付録 H）は $\mathtt a$ の run、Parikh ベクトル、$\mathtt a^6$ 深い挿入など、2 文字アルファベットに強く依存している。にもかかわらず要旨は定冠詞付きの「the typing」と書き、あたかも「type 1 の文字が 1 個」という条件だけで一意に定まるかのように読める。$\{\mathtt a,\mathtt c\}\mapsto1,\ \mathtt b\mapsto\zeta$ のような型付けへの拡張は証明されていない。

**修正案。** "the binary typing $s_{U,2}$ ($\mathtt a\mapsto1$, $\mathtt b\mapsto\zeta$)" と明記する。定理 C(i) の文面（$s_{U,2}$ を明示）と揃う。

**確信度：確認済み**（定理の量化と要旨の表現の比較）。

---

### R5（表現）"asymptotically smallest presentations" が未定義

**原文**（L163–167）

> \item If $\Sigma$ has at least $4f+1$ letters \textup($3$ letters if $f=1$\textup), then for every typing $s$ there are finite targets in $\Cmcf{f}{s}$, with presentations of asymptotically smallest size, whose characteristic samples all have length $\Omega(\|G\|\bar\theta_G)$

および要旨（L79–81）"some targets with asymptotically smallest presentations"。

**何が問題か。** 用語が定義されていない。実際に `prop:linear-factor-all-fanout`(iii)（L1638–1643）が示すのは「任意の reduced good な提示で $\bar\theta_G=W$ かつ $\|G\|\ge q+1$、提示した $G^{(f)}_{q,k}$ は $\|G^{(f)}_{q,k}\|\le(7f+17)(q+1)$」、すなわち「最小サイズの定数倍以内」である。

**修正案。** "within a constant factor of the minimum size among reduced good presentations" などに置き換える。あるいは (ii) の直後に「asymptotically smallest とは、最小サイズの定数倍以内の提示をいう」と定義する。

**確信度：確認済み**（用語の未定義。主張自体は (iii) で支持される）。

---

### R6（表現・編集）AI 利用宣言の範囲

**原文**（L4292–4297）

> During preparation of this work, the author used ChatGPT (OpenAI) and Claude (Anthropic) to assist with organization of the manuscript, expression and translation of text, cross-checks of references and notation, and editing of \LaTeX{} source.

**何が問題か。** 宣言は AI の用途を「構成・表現・翻訳・参照と記法の突き合わせ・LaTeX 編集」に限定している。しかし著者側文書（`README.md` の変更履歴、`INSTRUCTIONS_FOR_AI.md` §0）によれば、`prop:binary-u1-weight-slice` と `prop:u1-weight-all-fanout` は外部 AI の調査報告を著者が検証・書き直して得たものであり、AI が**結果の候補の導出**に関与している。Information and Computation（Elsevier）の AI 方針との整合を確認し、必要なら「AI システムが補題・命題の候補の導出に用いられ、著者が独立に検証した」旨を追記すべきである。

**修正案。** 事実に即した宣言に直すか、方針上「研究内容への AI 関与の記載は不要」であることを確認して現状維持とする。いずれにせよ投稿前に編集部の方針を確認されたい。

**確信度：疑い**（原稿外の著者側文書に基づく。原稿だけからは判断できない）。

---

## 5. 確認して問題なしと判断した証明

以下は 1 行ずつ追い、主張と証明の対応・定数・場合分けを確認したもの。**「問題なし」は「私が追えた範囲で誤りが見つからない」の意味**であり、機械検証ではない。

### 5.1 定性再構成（§3・付録 C・D）

- `lem:filling-identity`（付録 C, L2704–2714）— 内側の区切りが非空になること（同一成分内は非併合、成分をまたぐ場合は $v_i\in\Sigma^+$）。
- `lem:witnessed-composition` — `lem:filling-identity` の適用と、型の一致（$\out_\rho$ の準同型性）。
- `prop:reconstruction-soundness` — Const/Link/Comp/Start の 4 場合。Link が substitutability を使う点。
- `prop:completeness` — $\iota(X)\in L_X$ を仮定しない議論、$q=0$ の場合分け、rank の上限 $\le\|K\|_+$。
- `thm:exact-reconstruction` — soundness と completeness の合成、$\eps$ の扱い、$r_{\max}\ge\max\{1,r_G\}$。
- `thm:poly` — 構成の概略（計算量の定数は未追跡、§6）。
- `cor:gold-explanatory` — 保守的学習・TxtEx の議論。
- `prop:output-invariants` — 帰納と一意持ち上げ、$L(\widetilde G_0)=L(G)$。
- `lem:semigroup-transfer` — $h_0$ と $\widehat{s_0}$ の同値、trimmed refinement の一致。
- `lem:identity-canonical-contexts` — 経路に沿った `lem:filling-identity` の反復。
- `lem:typed-homogeneity` — $\chi(X)$ を共有する同型の分布一致。
- `lem:thickness-equivalence` — (i)(ii)(iii)(iv)。(iii) の $\theta_G\le2\|G\|\max\{1,t_G\}$ は依存パスの規則の相異性から。
- `lem:witness-length-template` — (i) 型保存交換、(ii) 長さ $2\bar\theta_G+r_{\max}b$、(iii) 細分化厚さ、(iv) 特性標本。
- `lem:typed-thickness-equivalence` — $t_{\mathrm{typ}}\le\theta_{\mathrm{typ}}\le2\bar\theta_G+r_{\max}t_{\mathrm{typ}}$。
- `thm:data-from-typed-thickness` — $N_{\mathrm{typ}}$ による数え上げと長さの評価。
- `lem:type-deletion` — 正規言語 $\widehat s^{-1}(\mathsf S^\sharp\setminus\{m\})$ との共通部分。
- `prop:rare-type` — 型ごとの語の強制。$F\subseteq L^{\setminus m}$ と soundness の矛盾、クラス全体では $F\cup F'$。
- `cor:typed-sandwich` — 上下界の合成。
- `prop:typed-thickness-exponential` — $\theta_{G_n}=2$、$t_{\mathrm{typ}}\ge2^n$、$\|G_n\|=O(n)$。
- `cor:distribution-representatives` — $\tau$ による上界と $\tau_X\ge\mu_m(L)$（始非終端の $\chi=\blank_1$）。

### 5.2 上界（§5・付録 A・B）

- `prop:block-replacement-interface` — 付録 A の (a) 零和、(b) パターン分け＋`lem:order-homogenize`＋`lem:group-interval`。
- `lem:block-replacement`(a) — 零和定数 $\mathsf d(\mathbb G^f)$ による選択。
- `lem:block-replacement`(b) — パターン数 $\mathcal P_f=f^{f+1}f!$、$N_{\mathbb G,f}^{2^{f^2}}$ の数え方、破棄した所有者の定数への吸収。
- `rem:davenport-size` — 引用のみ（§6）。
- `lem:group-block-order` — 「両方増加」「$X\wedge\neg Y$ で分離」「$\neg X\wedge\neg Y$ で矛盾」の各場合、類の推移性、領域の分離、$n\ge3$。
- `lem:group-interval` — $\kappa_p=P_pQ_p^{-1}$ による同値、増加／減少領域の chunk 対応（$p=n-b$, $p'=n-a$）、状態数 $n+1>|\mathbb G|^c$。
- `ex:nonabelian-reverse-owner` — 両行の値が $1$ になることを手計算（$\alpha\beta\alpha\alpha\beta\alpha\beta\beta=1$、$\alpha\beta\beta\alpha\beta\beta=1$）。
- `lem:two-sequence` — 行非減少の 2 場合（列非増加・列非減少）と $(m-1)^2+1\ge2m-1$。
- `lem:order-homogenize` — $k\le f^2$、$m_k\le N^{2^k}$、$(t,t)$ を先に処理、$t\ne u$ で `lem:two-sequence` を適用する際の単調方向（$i$ については $p_t$ と逆向き）。
- `lem:marked-heavy-window-group` — マーク数 $h=f(k+\ell+1)$、マークを含む反鎖 $\le h$、置換後の $\widehat s_{k,\ell}$ 型の保存。
- `lem:boundary-short-canonical` — 自明な $\mathbb G$ の場合。
- `thm:window-group-polydata` — $K_{k,\ell,\mathbb G}$ の導出（$1+2\bar\theta\le3\|G\|\bar\theta$、$|V|\le\|G\|$）。
- `lem:mcfg-li-group-window` — $\mathsf S_0^k\subseteq\mathsf S_0E\mathsf S_0$ と $euf=ef$、$|w|\ge2k$ の分解。
- `lem:local-group-morphism` — 積の公式 $\gamma(u)J_\nu\gamma(v)$ と短い語の場合分け。
- `lem:local-group-blocks` — 因子をブロック内／ブロック間に分ける $z_j$ 分解。
- `lem:lg-rees-window-coordinate` — Rees 座標の (1)(2)(3)（積が $\mathsf K$ に入ること、左乗算の $\Lambda$ 座標、群座標の積）。
- `thm:lg-characterization` — (i)–(iv) の同値。$\mathsf K$ の外の冪等元から $\{e,f\}\cong U_1$、逆向きは $\mathsf K$ 内の 2 冪等元の一致。
- `prop:li-g-strict` — (i) $\nu(F)=g(\text{last letter})$、(ii) $u=\mathtt b^m\mathtt a^{N_0}\mathtt b^m$, $v=\mathtt b^{2m}$。
- `lem:lg-buffered-owners` — 隣接グラフの次数 $\le4kf$、貪欲独立集合、拡大ブロックの (a)(b)(c)。
- `lem:local-group-shortest` — $|Q_0|>(4kf+1)c_{\mathbb G,f}$ から $|I|>c_{\mathbb G,f}$、$\lambda$ 型の保存、長さの減少。
- `thm:local-group-polydata` — 上記の合成で $t_{\mathrm{typ}}=O(\|G\|\bar\theta)$、$\|\Wit\|_+=O(\|G\|^2\bar\theta)$。

### 5.3 下界（§6・§7・付録 F・G・I・J）

- `prop:linear-factor-sharp` — (i) マーカー位置 $h(i+1)$ と距離 $(h'-h)(i+1)$、(ii) 特性標本は $L$ 自身、(iii) サイズと $\bar\theta$。**計算照合**：$\|G_{q,k}\|=17q+6k+13$、$\bar\theta_G=W=2^k+2q+2$ が $(q,k)=(1,1),(2,1),(2,2),(3,2)$ で一致。
- `prop:linear-factor-all-fanout` — (i) 固定部分のマーカー $\le d-1$、$x$ が $\ge d+1$ 個、2 個持つ成分が $i$ を決める、(ii) 同上、(iii) サイズ。**計算照合**：$\|G^{(f)}_{q,k}\|=(7f+11)q+6k+3f+10$、$\bar\theta=W=2fq+2^k+2f$ が $(f,q,k)=(1,1,1),(1,2,1),(2,1,1),(2,2,1)$ で一致。**代入可能性も全分解列挙で確認**（5.4(a)）。
- `cor:trivial-exact` — $t_{\mathrm{typ}}=t_G\le\bar\theta_G$ と (ii) の達成。前回指摘の「最大」が消え「最短の特性標本」になっていること。
- `prop:bracketed-family` — (i) $\theta\le4n$、(ii) Clark–Eyraud 代入可能性（付録 F）、(iii) ceiling-free 語の一意性と長さ、(iv) rare type。**計算照合**：$\theta=4n$（$n\le4$）、ceiling-free 語は一意で長さ $3\cdot2^n-2$、$L_n$ は $n\le4$ で代入可能。
- `thm:fanout-one-data` — (ii) は `thm:local-group-polydata`、(iii) は `thm:lg-characterization`(ii) と `prop:bracketed-family`(iv) から。$3\cdot2^n-1$ が多項式で抑えられないこと。
- `prop:three-letter-family` — サイズ $13n+7$、$\theta=4n$、$V_n$ の一意性。**計算照合**：$(n=1,2,3)$ で一致、$K_n$ は代入可能、$c$ を含まない語は $V_n$ のみで長さ $3\cdot2^n-2$。
- `cor:typing-level-obstruction` — $\{e,z\}\cong U_1$ の下で $c$ を含まない語が $V_n$ だけであること、$U_1$ への全射型付けで $\zeta$ の文字が取れること。
- `prop:binary-u1-quadratic` — (i) ブロック分解と $\alpha,\beta$ の $\bmod k$ 一致、(ii) $\theta_G(R)=o_B+c_R+\sum d_{B_j}$ から $\bar\theta=M+k-1$、(iii) 純語 $\mathtt a^{kM}$ と rare type。**計算照合**：$\|G_{m,n}\|=6m+6n+9$、$\bar\theta=2^m+2^n-1$、$(1,s_{U,2})$-代入可能（$m,n$ 小）。
- `prop:binary-u1-weight-slice` — (i) 臨界節点の存在、$h\ge\lambda$、$\theta\ge h+(W-h)/\lambda$、(ii) 依存グラフのパスと各ノード $\le\theta-d_C\le\theta-1$、(iii) 定数 $3^r(r+3)\|G\|^2\theta^2$。**R1 の 1 点を除き**確認。
- `prop:u1-weight-all-fanout` — **1 行ずつ確認**。$\psi(\boldsymbol\eta_{R,j})=\ell_{u_j}$ が定数重みから強制されること、$\lambda\le1$ で $N\le\theta$、$\lambda>1,N<\lambda$ で $\boldsymbol\eta_R$ が純語、$\lambda>1,N\ge\lambda$ で $h+\frac{N-h}{\lambda}\le\theta$ と平方完成、$\mu_\zeta\le\theta$。**論理的な穴は見つからなかった。**
- `lem:power-transfer` — 共通文脈 $p'u\blank_1u\blank_2q'$（内側の区切り $u\ne\eps$）、eventual periodicity による成分ごとの型の一致、$w_{\mathrm M}\ne\eps$ の必要性。
- `thm:doubling-no-lift` — $i_0+q\le|\mathsf S|+1$ から $2i_0+q+2\le2|\mathsf S|+3$、$b=n-a-d-2\ge i_0$、分解 $W_n=w_{\mathrm L}\lfloor^a w_{\mathrm M}\lfloor^{d+b}w_{\mathrm R}$、得られる語が $\lfloor^{n+d}\mathtt a$ で始まること。
- `thm:binary-u1-polydata` — 6-deep insertion の有無による場合分け、定数 $C_{r_{\max}}$ と $3^{2r}(3+rC)$ の導出。
- `lem:app-u1-fillers` — $E_A$ を共有する同型の分布一致による $\operatorname{Cl}$ の特徴づけ。
- `lem:app-u1-identity` — Parikh 相等から経路上の規則が恒等であること。
- `lem:app-u1-shallow` — マーク、$|H|\le2cf\cdot2^fv$、$c$-deep insertion の矛盾、型の保存。
- `lem:app-u1-runs` — $\zeta$-run の数と重い節点の反鎖、$|Q|\le2f+(2f+1)k$。
- `lem:app-u1-transfer` — (i) 二穴移送、(ii) Parikh 飽和。
- `lem:app-u1-deep` — $e=1$ と $e\ge2$ の場合分けと $w_k$ の構成。
- `lem:app-u1-parikh` — (P1) 行剛性、(P2) 高さ、(P3) 重い純節点、(P4) 頻出非終端、(P5) 比 $\alpha\le\alpha_\ast$、(P6) 数え上げ。**特に念入りに追い、飛躍は見つからなかった。**
- `lem:app-lf-path` — パス言語の特徴づけ（穴の両端の頂点が $E$ で決まる）。
- `lem:app-lf-descent` — $o_B+d_B\ge\mu$、$\theta_G(R)=o_B+c_R+\sum d_{B_j}$、最短でない節点の短縮。
- `prop:app-br-congruence` — 付録 F のパーサー議論（(P1)–(P3)、認識、交換、分岐同期）。結論は $n\le4$ で計算確認。
- `prop:app-tl-congruence` — 付録 G のパーサー議論（到達可能スタック上の単射性）。結論は $n\le3$ で計算確認。
- `prop:good-normalization` / `lem:normalization-stages` — 付録 E の 4 段階（非削除・非置換・空成分・非併合）とサイズ。
- `prop:feature-cross-typed` — 付録 K の $L_R$ の文法と 3 つの言語の共通部分。
- `prop:lg-needed-target` / `prop:nonabelian-needed-target` — 付録 K の分離（$u,v$ の $\#_{\mathtt{ab}}$ と $g_{\mathrm B}$ の値、`lem:flag-separation` の適用）。
- `thm:rankone-polydata` — 付録 L の $\bar\theta_G\le2\|G\|$ と $t_{\mathrm{typ}}\le|V||\mathsf S^\sharp|^f\bar\theta_G$。

### 5.4 計算による確認（反例探索と数値照合）

**これは全称の主張の証明ではない**。有限個の例での確認にすぎない。

**(a) 代入可能性の全分解列挙。** 有限言語 $L$ に対し、$d$ 穴の全分解（成分は非空、内側の区切りは非空）を列挙し、$D_L(\boldsymbol x)$ を「$L$ の語における $\boldsymbol x$ の出現の文脈集合」として計算した。有限 $L$ では $D_L(\boldsymbol x)$ は出現文脈の集合に一致するので、これは完全な検査である。判定は「同じ型で文脈を共有する 2 つの組は同じ分布を持つか」を、$(\text{型},\text{文脈})$ ごとに分布が一意かどうかで行った。

```python
def observations(L, d):
    obs = defaultdict(set)
    for w in L:
        n = len(w)
        for cuts in itertools.combinations(range(n + 1), 2 * d):
            if not all(cuts[2*h+1] > cuts[2*h] for h in range(d)): continue
            if not all(cuts[2*h+1] < cuts[2*h+2] for h in range(d-1)): continue
            tup = tuple(w[cuts[2*h]:cuts[2*h+1]] for h in range(d))
            ctx = (w[:cuts[0]],) + tuple(w[cuts[2*h+1]:cuts[2*h+2]]
                                         for h in range(d-1)) + (w[cuts[2*d-1]:],)
            obs[tup].add(ctx)
    return {t: frozenset(c) for t, c in obs.items()}

def check(L, d_max, typ=lambda t: None):
    for d in range(1, d_max + 1):
        obs, seen, bad = observations(L, d), {}, 0
        for tup, ctxs in obs.items():
            for c in ctxs:
                key = (typ(tup), c)
                if key in seen and seen[key] != ctxs: bad += 1
                else: seen.setdefault(key, ctxs)
        print(d, len(obs), "tuples", "OK" if bad == 0 else f"{bad} VIOLATIONS")
```

出力（抜粋）：

```
== prop:linear-factor-sharp (f=1), trivial typing ==
  [LF-sharp q=1 k=1] 2 words, lengths [6]
  [LF-sharp q=1 k=1] d=1: 30 distinct tuples, OK
      all lengths = W = 6
  [LF-sharp q=2 k=2] 3 words, lengths [10]
  [LF-sharp q=2 k=2] d=1: 102 distinct tuples, OK
  [LF-sharp q=3 k=2] 4 words, lengths [12]
  [LF-sharp q=3 k=2] d=1: 180 distinct tuples, OK
== prop:linear-factor-all-fanout (f=2), trivial typing ==
  [LF-all f=2 q=1 k=1] 2 words, lengths [10]
  [LF-all f=2 q=1 k=1] d=1: 86 distinct tuples, OK
  [LF-all f=2 q=1 k=1] d=2: 423 distinct tuples, OK
  [LF-all f=2 q=2 k=1] 3 words, lengths [14]
  [LF-all f=2 q=2 k=1] d=2: 1998 distinct tuples, OK
== prop:linear-factor-sharp: all nonempty subsets, q=k=1,2 ==
  q=1,k=1: subsets with violations: 0
  q=2,k=1: subsets with violations: 0
== prop:binary-u1-quadratic L_{m,n}, (1,s_U2) ==
  [L_1,1] d=1: 10 distinct tuples, OK
  [L_1,2] d=1: 60 distinct tuples, OK
  [L_2,1] d=1: 18 distinct tuples, OK
== prop:bracketed-family L_n (独立 2 コピー), trivial typing ==
  L_1: 2 words, lengths [3, 4]
  [L_1] d=1: 14 tuples, OK
      ceiling-free: ['[aa]']  (unique? True); length [4], 3*2^n-2 = 4
  L_2: 6 words, lengths [5, 6, 8, 9, 10]
  [L_2] d=1: 125 tuples, OK
      ceiling-free: ['[[aa][aa]]']; length [10], 3*2^n-2 = 10
  L_3: 42 words ... [L_3] d=1: 2027 tuples, OK ... length [22]
  L_4: 1806 words ... [L_4] d=1: 143213 tuples, OK ... length [46]
== prop:three-letter-family K_n, trivial typing ==
  [K_1] d=1: 12 tuples, OK
  [K_2] d=1: 93 tuples, OK
  [K_3] d=1: 1845 tuples, OK
      words without c: length 4 / 10 / 22  (3*2^n-2)
```

注：$L_{m,n}$ の $d=2$ では（$m=1,n=2$ でも）違反が出るが、これは論文が $L_{m,n}$ について主張するのはファンアウト 1 のみ（`prop:binary-u1-quadratic`(i)）であり、$m\ge3, n\ge2$ で $(2,s_{U,2})$-代入可能でないという §7 の注意（L1884–1886）と矛盾しない（むしろ閾値 $m\ge3$ は十分条件にすぎないことが分かる）。論文の主張の反例ではない。

**(b) 文法の数値の照合。** `def:standard-mcfg` の $\|G\|=|V|+\sum_R(1+r+\sum_i|\alpha_i|)$ を実装し、$\theta_G(R)$ を「$R$ を使う成功導出の語の最小長」の固定点計算で求めた。

```python
def size(self):
    s = len(self.V)
    for (lhs, templ, children) in self.rules:
        s += 1 + len(children) + sum(len(comp) for comp in templ)
    return s
# theta_of_rule: U[(i,A)] = A から規則 i を使って導けるタプル集合、の固定点
```

出力：

```
--- prop:linear-factor-sharp: ||G_{q,k}||=17q+6k+13, theta=W ---
  G_1,1: ||G||=36 (paper 36: OK)  theta=6 (paper 6: OK)
  G_2,1: ||G||=53 (paper 53: OK)  theta=8 (paper 8: OK)
  G_2,2: ||G||=59 (paper 59: OK)  theta=10 (paper 10: OK)
  G_3,2: ||G||=76 (paper 76: OK)  theta=12 (paper 12: OK)
--- prop:linear-factor-all-fanout: ||G||=(7f+11)q+6k+3f+10, theta=W ---
  G^(1)_1,1: ||G||=37 (paper 37: OK)  theta=6 (paper 6: OK)
  G^(1)_2,1: ||G||=55 (paper 55: OK)  theta=8 (paper 8: OK)
  G^(2)_1,1: ||G||=47 (paper 47: OK)  theta=10 (paper 10: OK)
  G^(2)_2,1: ||G||=72 (paper 72: OK)  theta=14 (paper 14: OK)
--- prop:binary-u1-quadratic: ||G_{m,n}||=6m+6n+9, theta=2^m+2^n-1 ---
  G_1,1: ||G||=21 (OK) theta=3 (OK)   G_1,2: ||G||=27 (OK) theta=5 (OK)
  G_2,1: ||G||=27 (OK) theta=5 (OK)   G_2,2: ||G||=33 (OK) theta=7 (OK)
--- prop:bracketed-family: theta <= 4n ---
  G_1: theta=4 (<=4)   G_2: theta=8 (<=8)   G_3: theta=12   G_4: theta=16
--- prop:three-letter-family: ||G'_n||=13n+7, theta=4n ---
  G'_1: ||G||=20 (OK) theta=4 (OK)   G'_2: 33 OK, 8 OK   G'_3: 46 OK, 12 OK
```

いずれも論文の値と一致した。$\theta$ の計算は「規則 $i$ を使う語」の固定点によるので、単なる上界ではなく厳密値である。

**(c) 重み一定の上界の反例探索。** $\{\mathtt a,\mathtt b\}$ 上の小さな fan-out 1・reduced good 文法をランダムに生成し、言語が有限・重み一定（$\lambda\in\{1,1/2,2,1/3,3,3/2,2/3\}$ のいずれか）になるものについて $\mu^\star$ と $(\bar\theta+1)^2/4$ を比較した。**219 個の文法で反例なし**（最大の $\mu^\star-(\bar\theta+1)^2/4$ は $0$、すなわち等号例のみ）。ただし生成器が粗く、得られたのは主に自明な例なので、これは弱い証拠である。

**(d) 等号例の確認。** $G_{n,n}$（$n=1,2$）で $\mu_1=kM=4^n$、$\bar\theta=2^{n+1}-1$、$(\bar\theta+1)^2/4=4^n$ を確認（$n=1$: $\mu^\star=4$, $B(3)=4$；$n=2$: $\mu^\star=16$, $B(7)=16$）。これらは定数重み $\lambda=2^m$ をもつ。

**(e) 参照整合性。** `\ref` 418 個、`\label` 150 個（重複 0、未定義参照 0）をスクリプトで確認。未参照の label が 28 個あるが（`lem:boundary-short-canonical`, `prop:app-tl-congruence`, `rem:binary-u1-scope` など）、誤りではない。

---

## 6. 読み切れなかった箇所

1. **外部文献の番号・内容。** Yoshinaka 2011 の Lemma 7 / Theorem 1、Yoshinaka 2015 の Lemma 2–3 / Theorem 1、Almeida et al. 2009 の Proposition 2.3、Costa 2002 の 2 論文、Geroldinger–Halter-Koch の定理番号、Rambow–Satta 1999 / Gómez-Rodríguez et al. 2009 の「$\mathsf{MCFL}(2,2)=\mathsf{MCFL}(2,3)$」は原典を入手していない。したがって §3 の対応表（「Yoshinaka の Lemma 2/3 に対応」）と §2 の文献依存の主張は**未検証**である。
2. **`rem:davenport-size` の不等式**（van Emde Boas–Kruyswijk の上界、$p$-群での等号）は引用に依存し、証明は読んでいない。
3. **`thm:poly` の計算量**（$(1+\|K\|_+)^{O(fr_{\max})}$）は証明の概略のみ確認し、定数の導出は追っていない。
4. **付録 F・G のパーサー議論**は、(P1)–(P3)、`lem:app-br-recognition`、`lem:app-br-exchange`、`lem:app-br-branch`、`prop:app-br-congruence` の筋を読み、結論を $n\le4$（F）・$n\le3$（G）で計算機確認したが、すべてのステップを独立に検証したわけではない（特に `lem:app-tl-reachable` の到達可能スタックの形）。
5. **付録 K の分離命題**（`prop:lg-needed-target`, `prop:nonabelian-needed-target`）は主張と証明の対応、$u,v$ の $\#_{\mathtt{ab}}$ と $g_{\mathrm B}$ の値、`lem:flag-separation` の適用を確認したが、$L_{\mathrm A},L_{\mathrm B}$ の $\mathsf{MCFL}(2,2)$ 性（文法の goodness の細部）は軽く見ただけである。
6. **組版。** LaTeX を回していないので、ページ数・overfull・未定義参照（`\ref` 以外）は未確認。ただし `\ref`/`\label` の整合はスクリプトで確認した。
7. **前回査読との関係。** 前回の指摘（`cor:trivial-exact` の「最大」、`thm:A(ii)` のアルファベット条件、C(ii) の閾値、付録 K の復活、`prop:binary-u1-weight-slice` の臨界節点の明示）はすべて v2 で修正済みであることを確認したうえで、本報告では**再指摘していない**。今回の R1–R6 は前回とは別の論点である。

---

## 7. 補足（判定の理由と、著者への依頼）

- 本報告で「問題なし」とした証明は、私が 1 行ずつ追って整合を確認したものである。特に `prop:u1-weight-all-fanout`（新規）と `lem:app-u1-parikh`（最重要）については、飛ばし読みをしていない。それでも組合せ論的証明の独立検証には限界があるため、**投稿前に `lem:order-homogenize` と `lem:app-u1-parikh` だけを対象にした第 2 の再読**を勧める。
- R1・R2 は「主張が偽」ではなく「証明・文言が主張に追いついていない」類である。R1 は 1 文、R2 は 2 文の追加で閉じる。R3 は表の 1 セル、R4 は要旨の 1 句、R5 は用語の定義で足りる。
- 以上の修正と、`lem:app-u1-parikh`・`lem:order-homogenize` の再読を条件に、本稿は **minor revision** と判定する。
