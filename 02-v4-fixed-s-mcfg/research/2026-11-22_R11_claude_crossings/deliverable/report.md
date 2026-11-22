# R11 報告：交差と「ちょうど埋める」— 単一文字の類では $\mathtt a$ が中心になり、二つの障害はどちらも消える（Claude Opus 5.5, 2026-11-22）

**結論（要約）**

- **T1（交差 (R1)）。単一文字の類では閉じた。依頼の (b)（族の選び直し）の形で閉じ、(a)（成分ごとの剛性）は部分的に答えた。**
  - **補題 RC・NFK［VALID（自己判定）］。** 単一文字の類 $K=\{\mathtt a,\mathtt x\}$ の重い節点の成分に現れる $\mathtt x$ の連の長さを $R$ とする。$n\in R$ なら $\mathtt a\mathtt x^n\equiv\mathtt x^n\mathtt a$（一穴の合同）である。したがって、極大な $\mathtt x$ の連の長さが $\langle R\rangle$（$R$ の生成する加法半群）に入る $\{\mathtt a,\mathtt x\}$ 上の語の一穴の類は、**Parikh ベクトルだけで決まる**。使うのは代入可能性と $\mathtt a$ の連の滑らせ P1′（`lem:power-transfer`）だけで、機構は本稿 `lem:app-two-runs`(ii) と同じである。
  - **補題 SD（単一文字の溶解）［VALID（自己判定）］。** 比較できない重い非境界の $K$ 節点 $v,w$ が**どの配置でも**（離れる・入れ子・交差・ちょうど埋める）、$v$ の $\mathtt x$ を含む成分 $\pi_0=\omega^i_v$ について、全ての $1\le g\le N-\ell_v-p_w-4$ で
    $$\pi_0\,\mathtt a^g\,e_w\,\mathtt a\ \equiv\ \pi_0\,\mathtt a^{g+p_w+1}$$
    が成り立つ。これは R10 の定理 HΞ\* の溶解の仮定 (Ξ2\*) そのものである。族は R9 の一穴の族（連続した逃げ道を並べたもの）のままでよく、**入れ替えで食い違った語は生じない**。
  - **系 2［VALID（自己判定）］。** 単一文字の類では、R15 型の反例（交差した配置はあるのに、連結した対の配置が $L$ にない言語）は作れない。比較できない $K$ 節点の対には、必ず対の配置 $\mathtt a^se_v\mathtt a^ge_w\mathtt a^t\in L$ がある。
  - **命題 3（成分ごとの重み）［VALID（自己判定）］。** 固定した文脈では、$K$ の語の $\mathtt a$ の欠損は $\mathtt x$ の個数だけの関数 $\mathrm{Def}$ になる。成分ごとの重み $\lambda,\rho$ が $\lambda+\rho+1=p$ を満たすのは、$\mathrm{Def}$ が成分の $\mathtt x$ の個数で定義されて加法的なときに限る。一般には示していない（本報告の結論には不要）。
- **T2（ちょうど埋める (R3)）。全ての類で閉じた。**
  - **補題 PNF・命題 5（射影の正規形と射影の基準）［VALID（自己判定）］。** 一般の類でも、$\mathtt a$ は成分の非 $\mathtt a$ の塊と可換である。よって $K$ の語の一穴の類は、非 $\mathtt a$ の射影 $\pi(\cdot)$ と $\mathtt a$ の個数で決まる（十分条件）。ちょうど埋める配置では、溶解の目標の語の射影が生まれつきの語の射影と**一致する**ので、(R3) は内容の条件のもとで常に使える。
- **T3。** $m=\{\mathtt a\}$ の多項式上界は次の場合に得られた［VALID（自己判定。R9 の HΞ・R10 の HΞ\*・Φ2・定理 A に依存）］。
  - **得られた範囲。** 非 $\mathtt a$ の文字を二つ以上持つ類 $K$ についてだけ、R10 の仮定 (U) を課せばよい（定理 4）。とくに、強制部分木の重い節点のうち、そのような類の節点がすべて実質 fan-out 1 なら成り立つ。$|\Sigma|=2$ はすでに本稿の `thm:two-letter-content` で無条件に解けている。
  - **残る障害（一般の fan-out 2）。** 二文字以上の類の対だけが残る。正確には、交差で成分の射影が可換にならない対と、内容が成分に分かれる対（R15 の $L_{N,d}$ はこちら）である。
  - **判断。** 否定（多項式）に傾き、確信度は R10 よりやや上がった。予想である。

ラベル（VALID / CONDITIONAL / REFUTED / OPEN / CERTIFIED FINITE）はすべて報告者の**自己判定**であり、独立監査は受けていない。報告者は R4〜R10 の報告者と同じモデル系列である。

---

## 1. 読了表

参照先は `growupkuriyama-hub/Papers`（`main`、2026-11-22 に `git clone --depth 1`）の `02-v4-fixed-s-mcfg/` 以下である。

| 資料 | 読んだ範囲 | 未読 |
|---|---|---|
| `research/README.md` | 全文（最初に読んだ） | — |
| `v2/reviews/PAUSE_FALSE_ROUTES_2026-11-16.md` | 全文（最初の段階で読んだ） | リンク先の R13・R14 完全ソース |
| `research/2026-11-22_R10_.../deliverable/report.md` | **全文**（§0〜付録） | — |
| 同 `code/run_all.py`、`run_all.log` | 冒頭の説明と関数一覧（全セクションの構成）、`check_step` の周辺、ログ全文 | 各セクションの関数本体。再実行はしていない |
| 同 `claude_check_R10_2026-11-22.md` | 全文 | — |
| `research/2026-11-22_R9_.../deliverable/report.md` | §0〜§3.4（§2.1〜§2.5 の V0・P1〜P7・NF・Φγ、§3.1 の HΞ、§3.3 の (F1)〜(F6)・Hγ1・Hγ2、§3.4）、§4 の冒頭 | §3.2（Hα）、§4 の後半〜付録 |
| `research/2026-11-21_R5_.../deliverable/report.md` | §2.1〜§2.5（定理 0.1・0.2、補題 0.3、系 0.4） | §3 以降 |
| `main.tex` 第 IV 部 | `sec:p4-ptree`（表と `rf:ptree`）、`sec:p4-resume-R8`〜`R10` 全文、`sec:p4-open` | `sec:p4-resume-R1`〜`R7`、その他の節 |
| `main.tex` 第 I〜III 部 | `def:tuple-substitutable`（注記 (a)〜(c)）、`prop:abelian-coset-filter`（主張）、`prop:rare-type`（主張）、`conj:rare-types` と直後の注記、**`thm:two-letter-content`・`cor:two-letter-semilattice`**（主張と直後の説明）、付録 `app:two-letter-content` の冒頭・証明の地図・`lem:app-two-runs`（証明つき） | その他（`lem:power-transfer` と `lem:thickness-equivalence` は R9・R10 の引用で把握。今回は本文を開いていない） |
| `v2/reviews/STATUS_ASTRA_FANOUT2_ROUND15_2026-11-16.md` | 全文 | — |
| `v2/reviews/astra_fanout2_round15_report_2026-11-16.md` | 冒頭結論、§1〜§2、§4（ST と $L_{N,d}$）、§5（$G^{\rm cross}_{d,q},G^{\rm nest}_{d,q}$、厚さ、最小木、具体例、室条件）、§6〜§10（課題 3 を含む） | §3（BT・NF）、付録のコード |
| R6・R7・R8・R4 の報告本体、`main.pdf` | **未読**（台帳と `main.tex` の要約で把握） | 全体 |

---

## 2. T1：交差 (R1)

### 2.0 設定と記号（R10 §2.0 に従う）

- $\Sigma$ は族の中で固定した有限アルファベット、$c=c_\Sigma$ は内容型付けとする。$L\in\Cmcf{2}{c_\Sigma}$ で、$\mathtt a$ だけからなる語を含むとする。比べる成分は空でなく、二穴の中央も空でない。外側文脈は空でよい。
- 一穴の合同 $x\equiv y$ とは、$c(x)=c(y)$ かつ一穴の分布が等しいことである。代入可能性から、同じ型の二語が一つでも共有文脈を持てば $x\equiv y$ となる。$\equiv$ は $\Sigma^+$ 上の合同である（R8 補題 0）。すなわち $x\equiv y$ なら、任意の $P,Q$ で $PxQ\equiv PyQ$ であり、$PxQ\in L\iff PyQ\in L$ である（文脈 $(\varepsilon,\varepsilon)$ を含む）。
- $G=(V,\Sigma,P,S,\mathrm{fan})$ は $L$ の reduced good な文法で、fan-out $\le2$、rank $\le r$ とする。$v:=|V|\le\|G\|$、$\theta:=\bar\theta_G$（**元**文法の規則厚さ）と置く。`lem:thickness-equivalence` の (T1)（各規則が直接書く終端は $\theta$ 個以下）と (T2)（各 $B$ に総長 $\theta$ 以下の生成 $\omega_B$）を使う。
- $N:=\mu_{\{\mathtt a\}}(L)$、$W:=\mathtt a^N$ は $L$ の**実際の**最短の $\mathtt a$ の冪である。$T$ は長さ $N$ の内容 $\{\mathtt a\}$ の語の全導出の中で節点数が最小のものとする。
- R9 (F1)(F2) により、重い非境界の節点 $y$ は強制節点で、次を持つ。
  - 逃げ道 $e_y$：$d_y=1$ なら $\omega_y$、$d_y=2$ なら $\omega^1_y\mathtt a\,\omega^2_y$
  - 孤立した配置 $I_y:=\mathtt a\,e_y\,\mathtt a^{N-p_y-1}\in L$（P1′ で外側の連は自由に配り直せる）
  - 重み $p_y=\ell_y+d_y-1$
- **P1′（滑らせ。R9 P1 の帰結、`lem:power-transfer` で $u=\mathtt a$）。** $U\mathtt a^{p_1}M\mathtt a^{q_1}V\in L$、$M\ne\varepsilon$、$p_1+q_1=p_2+q_2\le N-1$、全て $\ge1$ なら、$U\mathtt a^{p_2}M\mathtt a^{q_2}V\in L$ である。Rect は次のとおりである。
  - 比較組 $(\mathtt a^{p_1},\mathtt a^{q_1})$、$(\mathtt a^{p_2},\mathtt a^{q_2})$。型は $(\{\mathtt a\},\{\mathtt a\})$。
  - 共有文脈 $E_0=(\varepsilon,\mathtt a^{N-p_1-q_1},\varepsilon)$（中央は空でない）。$E_0[\cdot]=W$（二通りとも）。
  - 試験文脈 $E_1=(U,M,V)$。
- 本報告で扱う語の $\mathtt a$ の個数は、すべて $N$ 未満である（重い節点の逃げ道を含むので）。したがって P1′ の条件 $p_1+q_1\le N-1$ は自動的に満たされる。
- **類。** $\mathrm{cl}(y):=c(e_y)\cup\{\mathtt a\}$。**単一文字の類**とは $K=\{\mathtt a,\mathtt x\}$（$\mathtt x\ne\mathtt a$）のことである。$K$ 節点とは $\mathrm{cl}(y)=K$ の重い非境界の節点である。その逃げ道は $\mathtt x$ を含み、成分は $\{\mathtt a,\mathtt x\}^+$ の語である。
- **連。** 語 $u$ の**極大な $\mathtt x$ の連**とは、両隣が $\mathtt x$ でない因子 $\mathtt x^n$ のことである。
  - $R_K$ を、$N-p_y\ge3$ を満たす全ての $K$ 節点 $y$ と成分 $\omega^j_y$ について、$\omega^j_y$ の中の極大な $\mathtt x$ の連の長さを集めた集合とする。定理 1 で使う節点は全て $\ell\le N/16$ なので、この条件を満たす。
  - $\langle R_K\rangle$ はその生成する加法半群である。
  - 孤立した配置 $I_y$ の中で、成分の連は両隣が $\mathtt a$ である。成分の端の連も、外側の連（$\ge1$）か隙間（$\ge1$）に接するからである。

### 2.1 補題 RC（連の交換）［VALID（自己判定）］

> **補題 RC.** $n\in R_K$ なら $\mathtt a\,\mathtt x^n\equiv\mathtt x^n\mathtt a$ である。

*証明（Rect）。* $\mathtt x^n$ を $K$ 節点 $y$ の成分の極大な連とする。
- **語 $J$ の用意。** $I_y$ に P1′ を使い、$\mathtt x^n$ の直前の $\mathtt a$ の連を長さ $\ge2$ にする。外側の連 $\mathtt a^{N-p_y-1}$（$\ge2$）から一文字を移せばよい。中央は二つの連の間の語で、空でない。得られた語を $J=P\,\mathtt a^m\,\mathtt x^n\,\mathtt a^{m'}Q\in L$（$m\ge2$, $m'\ge1$、$\mathtt x^n$ は極大）と書く。
- 比較組：$x=(\mathtt a\mathtt x^n)$、$y=(\mathtt x^n\mathtt a)$。型は $\{\mathtt a,\mathtt x\}=\{\mathtt a,\mathtt x\}$。
- 共有文脈：$E_0=(P\mathtt a^{m-1},\ \mathtt a^{m'}Q)$。
- 二語：
  - $E_0[x]=J$
  - $E_0[y]=P\mathtt a^{m-1}\mathtt x^n\mathtt a^{m'+1}Q$。$J$ から P1′（$(\mathtt a^m,\mathtt a^{m'})\to(\mathtt a^{m-1},\mathtt a^{m'+1})$、中央 $\mathtt x^n$）で得られる。
- 試験文脈 $E_1$ は任意である。代入可能性により、$E_1[x]\in L\iff E_1[y]\in L$ となる。∎

**系（$\langle R_K\rangle$ への拡張）.** $n=n_1+\cdots+n_k$（$n_i\in R_K$）なら、$\mathtt a\mathtt x^n=\mathtt a\mathtt x^{n_1}\mathtt x^{n_2}\cdots\equiv\mathtt x^{n_1}\mathtt a\mathtt x^{n_2}\cdots\equiv\cdots\equiv\mathtt x^n\mathtt a$ である。各段は補題 RC を因子に使う（合同性）。

### 2.2 補題 NFK（単一文字の正規形）と系 PK［VALID（自己判定）］

> **補題 NFK.** $u\in\{\mathtt a,\mathtt x\}^+$ が $|u|_{\mathtt a}\ge1$、$|u|_{\mathtt x}\ge1$ を満たし、その極大な $\mathtt x$ の連の長さがすべて $\langle R_K\rangle$ に入るとする。このとき
> $$u\equiv\mathtt x^{|u|_{\mathtt x}}\mathtt a^{|u|_{\mathtt a}}$$
> である。
>
> **系 PK.** そのような二語 $u,u'$ の Parikh ベクトルが等しければ、任意の $P,Q$ について $PuQ\in L\iff Pu'Q\in L$ である。

*証明。* $\mathrm{inv}(u)$ を「$\mathtt a$ の位置 $<$ $\mathtt x$ の位置」となる組の数として、これについての帰納法による。
- $\mathrm{inv}(u)>0$ なら、ある $\mathtt a$ の直後に極大な連 $\mathtt x^n$（$n\in\langle R_K\rangle$）が来る。
- 系（$\langle R_K\rangle$ への拡張）でその因子 $\mathtt a\mathtt x^n$ を $\mathtt x^n\mathtt a$ に替えた語を $u'$ とする。$u\equiv u'$ で、内容は $\{\mathtt a,\mathtt x\}$ のままである。
- $u'$ では、$\mathtt x^n$ が直前の $\mathtt x$ の連と合流することがある（替えた $\mathtt a$ が長さ 1 の連だった場合）。合流した長さも $\langle R_K\rangle$ に入る。ほかの連は変わらない。
- $\mathrm{inv}(u')=\mathrm{inv}(u)-n$ である。
- $\mathrm{inv}=0$ の語は $\mathtt x^{|u|_{\mathtt x}}\mathtt a^{|u|_{\mathtt a}}$ である。
- 系 PK は、$\equiv$ が合同であることと推移性による。∎

**注意。**
- 使ったのは $W=\mathtt a^N\in L$、P1′、一穴の内容型付きの代入可能性だけである。文法・fan-out・最短性は使っていない。
- 本稿の `lem:app-two-runs`(ii)（$xxyx$ が現れれば Parikh 飽和）は同じ機構の二文字版で、$\mathtt x$ の連長が 1 の場合にあたる。本補題は、ほかの文字があるアルファベットで、一つの類の語に限って同じことを言う。新しいのは補題そのものより、§2.3 の使い方である。
- `run_all.py` [E] の連の型の候補言語（「$\mathtt x$ の連長の列が $1^*2^*$」で R15 の $\mathtt b^*\mathtt c^*$ をまねたもの）は、まさにこの機構で代入可能性が破れる。反例の組は $(\mathtt a^6\mathtt x)$ と $(\mathtt a^5\mathtt x\mathtt a)$ で、共有文脈は $(\varepsilon,\mathtt{axxa})$、区別する文脈は $(\varepsilon,\mathtt{xxaa})$ である［CERTIFIED FINITE］。

### 2.3 補題 SD（単一文字の溶解）［VALID（自己判定）］

> **補題 SD.** $v,w$ を比較できない $K$ 節点とする（$K$ は単一文字の類。配置は問わない）。$v$ の成分 $i$ を、$\omega^i_v$ が $\mathtt x$ を含むように取る（$d_v=1$ なら $i=1$）。$\pi_0:=\omega^i_v$、$G^*:=N-\ell_v-p_w-4$ と置く。このとき、$1\le g\le G^*$ の全ての $g$ について
> $$\pi_0\,\mathtt a^g\,e_w\,\mathtt a\ \equiv\ \pi_0\,\mathtt a^{g+p_w+1}$$
> が成り立つ。鏡像 $\mathtt a\,e_w\,\mathtt a^g\pi_0\equiv\mathtt a^{g+p_w+1}\pi_0$ も成り立つ。

**場合分けの網羅性。**
- $i$ は必ず取れる。$e_v$ は $\mathtt a$ 以外の文字を含み（強制節点、R9 (F2)）、それは $\mathtt x$ だけだからである。
- 証明は $v,w$ の配置（D 離れる・N 入れ子・C 交差・F ちょうど埋める）によらない。使うのは「$v,w$ が比較できない」ことだけである。
- 以下では $d_v=2$、$i=1$ の場合を書く。$i=2$ と $d_v=1$ は文脈を替えるだけで同じ形になる（末尾に記す）。

*証明（Rect）。* $\rho:=N-\ell_v-p_w-g-3\ (\ge1)$ と置く。
- **比較組。**
  - $x=(\omega^1_v\mathtt a^g\,e_w\,\mathtt a)$
  - $y=(\omega^1_v\mathtt a^{g+p_w+1})$
- **型。** $c(x)=c(\omega^1_v)\cup\{\mathtt a\}\cup c(e_w)=\{\mathtt a,\mathtt x\}$、$c(y)=\{\mathtt a,\mathtt x\}$。$\omega^1_v$ が $\mathtt x$ を含み、$c(e_w)\subseteq\{\mathtt a,\mathtt x\}$ だからである。
- **共有文脈。** $E_0=(\mathtt a,\ \mathtt a^{\rho}\,\omega^2_v\,\mathtt a)$。
- **$E_0[y]=\mathtt a\,\omega^1_v\mathtt a^{g+p_w+1+\rho}\omega^2_v\mathtt a\in L$。**
  - $\mathtt a$ の総数は $1+(N-\ell_v-2)+1+|\omega_v|_{\mathtt a}$ で、$v$ の生まれつきの語と同じである。
  - $v$ の生まれつきの語から P1′ で得られる（連は 3 本で、どれも $\ge1$）。
- **$E_0[x]=\mathtt a\,\omega^1_v\mathtt a^g\,e_w\,\mathtt a^{1+\rho}\omega^2_v\mathtt a\in L$。** 次の三段で示す。
  1. **生まれつきの語。** $N_{vw}:=W[\{v,w\}\leftarrow\omega]\in L$ である（比較できないので互いに素な位置、代入可能性は不要）。これを $N_{vw}=\mathtt a^{\alpha}F_N\mathtt a^{\varepsilon}$ と書く。$F_N$ は最初から最後の非 $\mathtt a$ の文字までの因子で、$\alpha,\varepsilon\ge1$（非境界）である。
     - $F_N$ の極大な $\mathtt x$ の連は、成分の連か、隣り合う成分の端の連が合流したものである。後者は間に $\mathtt a$ がない場合で、交差・入れ子・ちょうど埋めるで起こりうる。どちらも長さは $\langle R_K\rangle$ に入る。
     - $|F_N|_{\mathtt x}=|\omega_v|_{\mathtt x}+|\omega_w|_{\mathtt x}=:X$。
  2. **正規形。** $|F_N|_{\mathtt a}\ge1$ なら、補題 NFK で $F_N\equiv\mathtt x^X\mathtt a^{|F_N|_{\mathtt a}}$ である。0 なら $F_N=\mathtt x^X$ である。いずれにせよ $\mathtt a^\alpha\mathtt x^X\mathtt a^{B}\in L$（$B=|F_N|_{\mathtt a}+\varepsilon$）で、P1′ で $\mathtt a\,\mathtt x^X\mathtt a^{\alpha+B-1}\in L$ となる。
  3. **目標の語。** $F_x:=\omega^1_v\mathtt a^ge_w\mathtt a^{1+\rho}\omega^2_v$ の連は成分の連そのもので（間に $\mathtt a$ がある）、$R_K$ に入る。$|F_x|_{\mathtt x}=X$ である。$\mathtt a$ の個数を比べると、
     $$|E_0[x]|_{\mathtt a}=g+\rho+3+|\omega_v|_{\mathtt a}+|\omega_w|_{\mathtt a}+(d_w-1)=N-\ell_v-\ell_w+|\omega_v|_{\mathtt a}+|\omega_w|_{\mathtt a}=|N_{vw}|_{\mathtt a}$$
     である（$p_w=\ell_w+d_w-1$ を使った）。よって $\mathtt aF_x\mathtt a$ と $\mathtt a\,\mathtt x^X\mathtt a^{\alpha+B-1}$ は系 PK の条件を満たし、$E_0[x]\in L$ である。
- **試験文脈** $E_1$ は任意である。$x\equiv y$ となる。∎

**残りの場合の文脈。**
- $i=2$：$E_0=(\mathtt a\,\omega^1_v\mathtt a^{\rho},\ \mathtt a)$、$x=(\omega^2_v\mathtt a^ge_w\mathtt a)$、$y=(\omega^2_v\mathtt a^{g+p_w+1})$。
- $d_v=1$：$E_0=(\mathtt a,\mathtt a^{\rho+1})$、$x=(\omega_v\mathtt a^ge_w\mathtt a)$、$y=(\omega_v\mathtt a^{g+p_w+1})$。
- 鏡像は左右を入れ替える。

**`run_all.py` [B]［CERTIFIED FINITE］。**
- 対象は無作為な配置 380 個である。D（$v$ が fan-out 1 と 2）・N・F（ちょうど埋める、$w$ が fan-out 1 と 2）・C（交差）を含む。
- 各配置で、公理は $\{W,N_v,N_w,N_{vw}\}$（生まれつきの語）だけである。$g\in\{1,\lfloor G^*/2\rfloor,G^*\}$ と $i=1,2$ について、$E_0[x]$ と $E_0[y]$ を導く Rect の列を作り、検査器で全段を再生した。
  - 検査の内容：成分ごとの内容の一致、成分と中央が空でないこと、三つの前提の既知性
  - 段数：合計 188,685 段
  - 結果：2,100 個の場合が全て通った
- 正規化の途中で合流した連の分解は 1,356 回起き、全て $\langle R_K\rangle$ で処理できた。
- 導いた全ての語が、Parikh 線形の模型言語 $\{u:|u|_{\mathtt a}+3|u|_{\mathtt x}=N\}$ に入ることも確かめた（健全性の検査）。この模型言語の代入可能性は [E] で全数確認した。

### 2.4 定理 1（単一文字の類の対は全て使える）［VALID（自己判定。R10 の HΞ\* と Φ2 に依存）］

> **定理 1.** 設定 (Γ) で、$K$ を単一文字の類とする。重い非境界の強制節点 $u$ の部分木に比較できない $K$ 節点 $v,w$ があれば、$(v^*,w^*)=(v,w)$ は R10 の意味で**使える**。すなわち、定理 HΞ\* の (Ξ2\*) と (Ξ3\*) が、$\pi_0=\omega^i_v$ について成り立つ。とくに、R10 の仮定 (U) は単一文字の類について常に成り立ち、系 C の (R1)・(R3) は単一文字の類では起きない。

*証明。*
- (Ξ2\*) は補題 SD による。範囲 $G^*=N-\ell_v-p_w-4$ は、R10 の補題 D2 と同じである。
- (Ξ3\*) は R10 の補題 Φ2 による。$\beta$ を $I^i_v$ の直後の位置に取る。$i=1$ なら $\beta$ は $v$ の隙間の最初の位置で、$i=2$ なら非境界性から殻の右にある。どちらも $\beta\notin\mathrm{frame}(v)$ である。
- 族は R10 定理 A の場合 A と同じく、$u$ の鎖の上の $K$ 節点である（入れ子でよい）。
- 余白 (Ξ4)：全ての重みは $\ell_u\le N/16$ 以下なので、$G^*\ge q_0+\sum_jp_j+p_w+(M+1)g$ が成り立つ。数え方は R10 定理 A の (Ξ4) と同じである。∎

**族は一穴のままでよい。**
- HΞ\* の族の語 $x_\pi=\Phi_L\,\pi_0\,Z\,e_w\,Z\,e_{\pi_1}\cdots Z\,e_{\pi_M}\,Z_\ell\,\Phi_R$ では、スロットの中身は**連続した逃げ道**である。
- 入れ替え補題 W の部分木の交換で得られる語でも、各スロットは一つの族の元の逃げ道である（R9 §3.1 段 5）。
- R10 §3.5 の二側の族は不要になり、**食い違った語の評価という問題そのものが生じない**。これが依頼の (b)「食い違いが起きないように族を選び直す」に当たる。

**`run_all.py` [D]［CERTIFIED FINITE］。** 構成は次のとおりである。
- 交差した単一文字の対：$v=(\mathtt{xax},\mathtt{xx})$、$w=(\mathtt{xx},\mathtt x)$、$N=92$
- 族の逃げ道：$\mathtt x,\mathtt{xx},\mathtt{xxxx}$（重み 2, 4, 8。部分和は相異なる）
- 原型：$v$ の孤立した配置

結果は次のとおりである。
- **強制。** 全ての並べ方（$3!=6$ 通り）の族の語を、原型から NF\* の逆向きの列で導いた。使った手は、補題 SD の溶解、R9 の EX・COM、P1′ である。
- **剛性。** 植えた語（スロットの一つを重み 6 の逃げ道 $\mathtt{xxx}$ に替えたもの）を仮定として加え、NF\* で正規化した。結果は $\mathtt a\,\mathtt{xax}\,\mathtt a^{83}\mathtt{xx}\,\mathtt a$ で、原型の $\mathtt a^{81}$ と食い違う。P7 の Rect から $\mathtt a^{90}$（$W=\mathtt a^{92}$ より短い）が出た。
- 全部で 1,369 段である。

### 2.5 系 2（単一文字の類では R15 型の反例は作れない）［VALID（自己判定）］

> **系 2.** 単一文字の類 $K$ の比較できない $K$ 節点 $v,w$ について、$s+g+t=N-p_v-p_w$（全て $\ge1$）の全ての $(s,g,t)$ で、対の配置 $\mathtt a^se_v\mathtt a^ge_w\mathtt a^t$ と $\mathtt a^se_w\mathtt a^ge_v\mathtt a^t$ が $L$ に入る。より強く、$v,w$ の成分を任意の順に並べ、間を $\mathtt a$ で埋めた語（各連 $\ge1$ で、$\mathtt a$ の総数が $N_{vw}$ と等しいもの）は、すべて $L$ に入る。

*証明。* そのような語の、最初から最後の非 $\mathtt a$ の文字までの因子は、連が $R_K$ に入り、Parikh ベクトルが $F_N$ と等しい。系 PK と P1′ による（補題 SD の証明の段 2・3 と同じ）。∎

**判定。**
- R15 の $L_{N,d}$ で起きたこと（交差した二重置換の語はあるのに、連結した二核の宿主がない）は、単一文字の類では起こりえない［VALID（自己判定）］。
- R10 §3.4 の「単一文字の類の交差で同じことが起きるかは OPEN」は、**否定的に解決した**。

**`run_all.py` [F]［CERTIFIED FINITE］。** 独立の閉包エンジンで確かめた。これは補題 SD の証明書の生成器とは別の実装で、全ての一穴・二穴の出現で「共有文脈 ⇒ 分布の一致」を不動点まで繰り返す。
- 小さい単一文字の交差二例とちょうど埋める一例で、生まれつきの 4 語の最小の代入可能な上位集合は、それぞれ 987、493、305 語になった。そこには全ての対の配置が入っている。
- 対照として、R15 の交差した $B_0$ 対（類は二文字 $\{\mathtt a,\mathtt b,\mathtt c\}$）の 4 語の閉包は $L_{11,4}$ の 72 語全体で、連結した対の配置（射影 $\mathtt{bcbc}$）は一つもない。

### 2.6 命題 3（成分ごとの重み：依頼の (a) への答え）［VALID（自己判定）］

依頼の (a) は、成分ごとの重み $\lambda+\rho=p$ が言語の中で合同として書き込まれるかを最初に調べることだった。単一文字の類での答えは次の命題である。

> **命題 3.**
> - (i) **剛性。** 任意の語 $\Phi_L,\Phi_R$ と、連が $\langle R_K\rangle$ に入る $K$ の語 $U,U'$ について考える。$|U|_{\mathtt x}=|U'|_{\mathtt x}\ge1$、$|U|_{\mathtt a}<|U'|_{\mathtt a}$ で、$\Phi_LU\Phi_R,\ \Phi_LU'\Phi_R\in L$ なら、$L$ は $\mathtt a^{N-(|U'|_{\mathtt a}-|U|_{\mathtt a})}$ を含む。
> - (ii) **欠損の関数。** したがって $X\ge1$ について、$\mathtt aU\mathtt a^t\in L$（$U$ は上の $K$ の語で $|U|_{\mathtt x}=X$）となる語の $\mathtt a$ の総数は一つに決まる。それを $N-\mathrm{Def}(X)$ と書く。$K$ 節点 $y$ では $\mathrm{Def}(|\omega_y|_{\mathtt x})=p_y-|e_y|_{\mathtt a}$ である。
> - (iii) **加法性。** 比較できない $K$ 節点 $v,w$ について、$\mathrm{Def}(X_v+X_w)=\mathrm{Def}(X_v)+\mathrm{Def}(X_w)$ である（$X_y:=|\omega_y|_{\mathtt x}$）。

*証明。*
- **(i)** 補題 NFK で $U\equiv\mathtt x^X\mathtt a^{A}$、$U'\equiv\mathtt x^X\mathtt a^{A'}$（$A<A'$）である。よって $\Phi_L\mathtt x^X\mathtt a^{A}\Phi_R$ と $\Phi_L\mathtt x^X\mathtt a^{A'}\Phi_R$ が $L$ に入る（$A\ge1$ の場合。$A=0$ なら $U=\mathtt x^X$ のまま同じ Rect を取る）。Rect は R9 の P7 で、次のとおりである。
  - 比較組：$x=(\mathtt a^{A'})$、$y=(\mathtt a^{A})$。型 $\{\mathtt a\}$。
  - 共有文脈：$E_0=(\Phi_L\mathtt x^X,\ \Phi_R)$。
  - 試験文脈：$E_1=(\varepsilon,\ \mathtt a^{N-A'})$。
  - 四語：
    - $E_0[x]$, $E_0[y]$：上の二語
    - $E_1[x]=\mathtt a^N=W$
    - $E_1[y]=\mathtt a^{N-(A'-A)}$（結論）
- **(ii)** (i) を $\Phi_L=\mathtt a$、$\Phi_R=\mathtt a^t$ に使い、P1′ で末尾をそろえる。$I_y$ の $\mathtt a$ の総数は $N-p_y+|e_y|_{\mathtt a}$ である。
- **(iii)** $N_{vw}$ の欠損は $(\ell_v-|\omega_v|_{\mathtt a})+(\ell_w-|\omega_w|_{\mathtt a})$ で、$\ell_y-|\omega_y|_{\mathtt a}=p_y-|e_y|_{\mathtt a}$ である。∎

**(a) への答え。**
- $K$ の語 $u$ に**重み** $p(u):=|u|_{\mathtt a}+\mathrm{Def}(|u|_{\mathtt x})$ を定める（$\mathrm{Def}$ が定義される $\mathtt x$ の個数で）。逃げ道では $p(e_y)=p_y$ である。
- 成分の重みを $\lambda_y:=p(\omega^1_y)$、$\rho_y:=p(\omega^2_y)$ と置くと、
  $$\lambda_y+\rho_y+1=p_y\iff\mathrm{Def}(X^1_y)+\mathrm{Def}(X^2_y)=\mathrm{Def}(X^1_y+X^2_y)$$
  である（$X^j_y:=|\omega^j_y|_{\mathtt x}$）。
- (iii) の加法性は**比較できない節点の和**についてしか示していない。成分への分割について示す道具はない。したがって (a) の文字どおりの形（食い違った二側の語がどれも剛性で倒れる）は、一般には示していない［OPEN］。
- ただし定理 1 により一穴の族で足りるので、(a) は本報告の結論に不要である。

---

## 3. T2：ちょうど埋める (R3)

### 3.1 補題 PNF（射影の正規形。一般の類）［VALID（自己判定）］

一般の類 $K$ で、補題 RC・NFK の $\mathtt x^n$ を**極大な非 $\mathtt a$ の塊**に替える。

- **記号。**
  - $\pi$ は $\mathtt a$ を消す射影である。
  - $\mathcal B$ は、重い非境界の節点の成分に現れる極大な非 $\mathtt a$ の塊 $\beta\in(\Sigma\setminus\{\mathtt a\})^+$ の集合である（孤立した配置の中で両隣は $\mathtt a$）。
  - $\mathcal B^+$ はその連結の全体である。

> **補題 PNF.**
> - (i) $\beta\in\mathcal B$ なら $\mathtt a\beta\equiv\beta\mathtt a$。
> - (ii) $|u|_{\mathtt a}\ge1$ で、極大な非 $\mathtt a$ の塊がすべて $\mathcal B^+$ に入る語 $u$ は、$u\equiv\pi(u)\,\mathtt a^{|u|_{\mathtt a}}$ を満たす。
> - (iii) そのような二語は、$\pi$ と $\mathtt a$ の個数が等しければ合同である。

*証明。*
- (i) 補題 RC と同じ Rect である。$x=(\mathtt a\beta)$、$y=(\beta\mathtt a)$ で、型はともに $\{\mathtt a\}\cup c(\beta)$ である。
- (ii)(iii) 補題 NFK と同じ帰納法による。$\beta_1\beta_2$ の塊は $\mathtt a\beta_1\beta_2\equiv\beta_1\mathtt a\beta_2\equiv\beta_1\beta_2\mathtt a$ と動く。∎

**注意。**
- 非 $\mathtt a$ の文字どうしの順序は、この補題では動かない。これが R15 の不変量 $\pi(w)\in\mathtt b^*\mathtt c^*$ と両立する理由である。
- (iii) は合同の**十分条件**である。EX（R9 P4）は射影の異なる逃げ道を合同にするので、$\pi$ は $\equiv$ の不変量ではない。

### 3.2 命題 5（射影の基準）［VALID（自己判定）］

> **命題 5.** $v,w$ を比較できない重い非境界の節点、$K=\mathrm{cl}(v)=\mathrm{cl}(w)$ とする。$v$ の成分 $i$ が $c(e_w)\subseteq\mathrm{cl}_i(v)$ を満たすとする。$e_w$ を $\omega^i_v$ の直後に置いた目標の語の射影を次のように置く。
> - $i=1$：$\Pi_1=\pi(\omega^1_v)\pi(e_w)\pi(\omega^2_v)$
> - $i=2$：$\Pi_2=\pi(\omega^1_v)\pi(\omega^2_v)\pi(e_w)$
>
> 鏡像（直前に置く）では、$\Pi'_1=\pi(e_w)\pi(\omega^1_v)\pi(\omega^2_v)$、$\Pi'_2=\pi(\omega^1_v)\pi(e_w)\pi(\omega^2_v)$ である。$\Pi_i$（または $\Pi'_i$）が生まれつきの語の射影 $\pi(N_{vw})$ と等しければ、$\pi_0=\omega^i_v$ で (Ξ2\*) が成り立つ。

*証明。* 補題 SD の証明で、補題 NFK を補題 PNF に替える。
- Rect（比較組 $x,y$、型、共有文脈 $E_0$）は同じである。
- 型の一致は、$c(e_w)\subseteq\mathrm{cl}_i(v)$ から出る。
- $E_0[y]$ は $v$ の生まれつきの語から P1′ で得られる。
- $E_0[x]$ は $N_{vw}$ から、PNF (ii) と P1′ と PNF (ii) の逆向きで得られる。射影が等しく、$\mathtt a$ の総数が等しいからである。
- 目標の語の塊は成分の塊で、$\mathcal B$ に入る。$N_{vw}$ の塊は、隣り合う成分の塊の連結で、$\mathcal B^+$ に入る。∎

**系 5a（(R3) は全ての類で閉じる）.** R10 系 C の (R3)（入れ子で、内側が fan-out 1 で、外側の隙間をちょうど埋める。内容の条件 $K\subseteq\mathrm{cl}_i(v)$ は満たす）では、次が成り立つ。
- $\pi(N_{vw})=\pi(\omega^1_v)\pi(\omega_w)\pi(\omega^2_v)=\Pi_1$（$i=1$）、$=\Pi'_2$（$i=2$）である。
- よって使える［VALID（自己判定）］。R10 が「$\mathtt a$ を挟む手段がない」とした問題は、$\mathtt a$ を挟まずに、射影の正規形で生まれつきの語から直接目標の語へ移ることで消える。
- 内側が fan-out 2 でちょうど埋める場合（$\omega^1_v\omega^1_w\cdots\omega^2_w\omega^2_v$）も、同じく $\Pi_1$ と一致する。

**系 5b（一般の類の交差の基準）.** 交差 $I^1_v<I^1_w<I^2_v<I^2_w$ では $\pi(N_{vw})=P_1Q_1P_2Q_2$ である（$P_j=\pi(\omega^j_v)$、$Q_j=\pi(\omega^j_w)$）。次のどれかなら使える。
- (a) $P_2Q_2=Q_2P_2$ で、$K\subseteq\mathrm{cl}_1(v)$ または $K\subseteq\mathrm{cl}_2(v)$（$\Pi_1$ または $\Pi'_2$）
- (b) $Q_1P_2=P_2Q_1$ で、$K\subseteq\mathrm{cl}_2(v)$ または $K\subseteq\mathrm{cl}_1(w)$（$\Pi_2$、または $v,w$ を入れ替えた $\Pi'_1$）
- (c) $P_1Q_1=Q_1P_1$ で、$K\subseteq\mathrm{cl}_1(w)$ または $K\subseteq\mathrm{cl}_2(w)$（$v,w$ を入れ替えた $\Pi_1,\Pi'_2$）

単一文字の類では、射影が $\mathtt x$ の冪なので (a)〜(c) は全て成り立つ。これは定理 1 の別証にもなる。

**`run_all.py` [C]［CERTIFIED FINITE］。** 非 $\mathtt a$ の文字が二つの類（$\{\mathtt a,\mathtt b,\mathtt c\}$）で、無作為な配置 310 個を調べた。内容の条件を満たす成分の選び方は 299 通りである。
- 「射影が等しい ⇔ 正規形の手順で目標の語が導ける」が、全ての場合（N 46・F 80・C 173）で一致した。
- 入れ子とちょうど埋めるの隙間への配置（$i=1$）では、射影は常に等しかった。
- 交差では 173 中 147 で等しくなく、正規形の手順では導けない。
- R15 の $L_{11,4}$ の交差した $B_0$ 対では、障害は**内容**であって射影ではない。D2（隙間）の比較組 $(\mathtt{babaca})$ と $(\mathtt{baaaaaa})$ の型は $\{\mathtt a,\mathtt b,\mathtt c\}\ne\{\mathtt a,\mathtt b\}$ である。

### 3.3 残る障害の正確な形（一般の類）

R10 系 C を本報告の結果で置き換える。

> **系 6.** $\Lambda_{\{\mathtt a\}}$ が R10 定理 A の上界を超えるなら、次の性質を持つ重い非境界の強制節点 $u$（$\ell_u\ge\Lambda/\mathrm{poly}$）と類 $K$ がある。
> - **$|K\setminus\{\mathtt a\}|\ge2$** である。
> - $K$ は $u$ の鎖の最初の $T_0$ 節点に $M_0$ 回以上現れる。
> - $u$ の部分木の比較できない $K$ 節点の対は、**すべて**次のどちらかである。
>   - **(R1\*)** 交差で、系 5b の (a)〜(c) がどれも成り立たない（成分の射影が可換でないか、内容が合わない）。
>   - **(R2\*)** 離れているか入れ子で、関係する成分の内容が $K$ を含まない（R10 の (R2)）。
>
> (R3) は現れない。

*証明。* R10 系 C の証明で、使える対の判定に定理 1（単一文字の類）と命題 5 を加える。∎

---

## 4. T3：判断

### 4.1 定理 4（類の消去の拡張）［VALID（自己判定。R9 の HΞ、R10 の HΞ\*・Φ2・補題 2 に依存）］

> **定理 4.** 設定 (Γ) で、仮定 (U) を**非 $\mathtt a$ の文字を二つ以上持つ類**だけに課せば、R10 定理 A の結論が成り立つ。すなわち、
> $$\Lambda_{\{\mathtt a\}}\le(v\theta)^{O(q\,r\log r)},\qquad\mu_{\mathtt a}(L)\le2v(\theta+r\Lambda_{\{\mathtt a\}})$$
> である（定数は $r,|\Sigma|$ による。$v\le\|G\|$、$\theta=\bar\theta_G$）。とくに次の場合に成り立つ。
> - (i) $|\Sigma|=2$。ただしこれは本稿の `thm:two-letter-content` で、無条件にもっと良い上界ですでに知られている。
> - (ii) 強制部分木の重い節点のうち、類が二文字以上の非 $\mathtt a$ 文字を含むものが、すべて実質 fan-out 1 である（R10 補題 D1）。
> - (iii) より一般に、そのような類の比較できない対が、命題 5 の基準か R10 の D1・D2 を満たす。

*証明。* R10 定理 A の証明（補題 2 の類の数についての帰納）で、場合 A の「使える $K$ 対」の存在を、単一文字の類では定理 1 から得る。それ以外は R10 と同じである。∎

R10 の (ii) は「重い節点が**すべて**実質 fan-out 1」だった。定理 4 (ii) はその条件を二文字以上の類に限ったもので、真に広い。

### 4.2 判断（一段落。予想）

**$m=\{\mathtt a\}$ の多項式上界は、一般の fan-out 2 文法では得られていない［OPEN］。**
- 得られたのは定理 4 の範囲である（R9 の HΞ に依存）。
- 残る障害は系 6 の (R1\*)・(R2\*) で、**非 $\mathtt a$ の文字を二つ以上持つ類**に限られる。

**否定（多項式。fan-out 2 でも LG が境界）に傾く。確信度は R10 よりやや上がった。これは予想である。** 根拠は三つある。
1. **$\mathtt a$ は中心である。** 内容型付けと $\mathtt a^N\in L$ だけから、$\mathtt a$ は成分の全ての塊と可換になる（補題 PNF）。残る非可換性は、非 $\mathtt a$ の文字どうしの順序だけである。単一文字の類ではそれもなく、類の語は Parikh ベクトルで決まり、交差もちょうど埋めるも消えた。
2. **残る障害は「順序の不変量」に絞られた。** 肯定の答えには、超多項式の長さの強制節点の部分木で、二文字以上の類の比較できない対が**どの尺度でも**次のどちらかでなければならない。
   - 射影が非可換に交差する
   - 内容が成分に分かれる

   既知の唯一の例は R15 の $L_{N,d}$（分裂。$\pi\in\mathtt b^*\mathtt c^*$）で、$N=O(\bar\theta_G^2)$ である。順序の不変量で重みを運ぶには、長い非 $\mathtt a$ の語を各段に要しそうで、それは元厚さに跳ね返る。ただしこれは証明ではない。
3. **(R1\*) は言語の段階では障害になりうる。** EX は射影の異なる逃げ道を合同にするので、PNF の十分条件の外でも溶解が得られる可能性はある。しかし調べていない。

### 4.3 $|m|\ge2$（周期的でない宿主）へ持ち上げるのに要るもの

1. **補題 RC・PNF の宿主版。** 本報告の機構は P1′（$\mathtt a$ の連の自由な配り直し）だけである。周期的でない宿主では、R6 の P2・P4（文字の 4 乗の強制と骨格を保つ配り直し、本稿 `lem:app-two-runs`(i)）で、4 乗を持つ文字 $z$ の連が動く。そこから「$z$ は $z$ に挟まれた塊と可換」が同じ Rect で出る見込みである（未証明）。宿主に $m$ の他の文字があるので、塊の定義と類の定義（$\mathrm{cl}(y)=c(e_y)\cup m$）を替える必要がある。
2. **「新しい文字が一つの類」（$|K\setminus m|=1$）の扱い。** 単一文字の類の類比である。PNF の射影を $m$ の外の文字に制限したときに可換になるかが鍵になる。
3. **HΞ の材料（R10 §4 の列挙のとおり）。** 原型の構成（Φ2）、NF\* の手（COM・EX は宿主の骨格つき）、剛性 P7（R9 命題 V4 でそのまま持ち上がる）。
4. **R4 補題 4（系 B）の独立監査。** 「全ての $m$ で多項式 ⇒ 否定の答え」に要る。
5. **二文字以上の類（$m=\{\mathtt a\}$ でも未解決）。** 系 6 の (R1\*)・(R2\*)。

---

## 5. 既存結果との照合

| 結果 | 本報告との関係 |
|---|---|
| R13 原文 X1（反証済み） | 使っていない。全ての Rect で、比べる成分の内容を実際にそろえた（補題 RC・SD・PNF の型の行）。$\mathtt a$ の連は全て $\ge1$（P1′ の条件）。 |
| R14 原文 CA（反証済み） | 使っていない。全ての語は生まれつきの語から P1′ と合同で導いた。初期の予算からの合成はしていない。 |
| R15 一般 IH（反証済み） | 使っていない。系 2 は IH の**単一文字の類への限定版が真**であることを示す。IH の反例 $L_{N,d}$ は二文字の分裂の類で、系 2 の外にある（[F] の対照）。 |
| R2 の退化した短縮補題 | 使っていない。近道は P7 の具体的な Rect（命題 3、[D]）からだけ出る。 |
| `thm:doubling-no-lift`、`lem:power-transfer` | P1′ は `lem:power-transfer`（$u=\mathtt a$）である。倍増族には触れていない。 |
| **`thm:two-letter-content`、`lem:app-two-runs`** | **$|\Sigma|=2$ は本稿ですでに無条件に解けている**。定理 4 (i) は新しくない。補題 RC は `lem:app-two-runs`(ii) と同じ機構で、本報告はそれを大きいアルファベットの中の一つの類に使った。 |
| P_tree 計画の AB$_{\rm pair}$ | 単一文字の類では、異なる順序の核の欠損の問いそのものが消える。核は Parikh ベクトルで決まる（補題 NFK）。欠損は $\mathtt x$ の個数の関数である（命題 3）。 |
| R15 の $L_{N,d}$・課題 3「連結化を経由しない P_tree」 | 単一文字の類では、連結化は**導ける**（系 2）。二文字の類では、連結化が導けないことは $L_{N,d}$ のとおりである。そこでも P_tree は命題 5 の内容の条件のもとで、配置を保ったまま溶解を得る形で部分的に答えた。$L_{N,d}$ は内容で阻まれる。 |
| R8 H1〜H4 | H1 の κ3（交換 $\mathtt ae\equiv e\mathtt a$）は補題 RC の逃げ道版である。H4 は R9 HΞ を経て使う。 |
| R9 V0 | 殻の一穴版は使っていない。補題 SD は成分 $\omega^i_v$ で比べる。 |
| R9 P1〜P7、NF | P1′・P3・P4・P7 をそのまま使う。NF\* は R10 の形で使う。 |
| R9 HΞ | 定理 1・4 は HΞ（とくに補題 W）に依存する。新しい仮定は足していない。 |
| R10 定理 A・補題 2 | 定理 4 は仮定 (U) を二文字以上の類に弱めた版である。帰納の構造は変えていない。 |
| R10 HΞ\* | (Ξ2\*) を補題 SD で満たす。HΞ\* の証明には触れていない。 |
| R10 補題 D1・D2 | D2 の (gap)(right) は、命題 5 で射影が自動的に等しい場合である。D2 が除外した「ちょうど埋める」と「交差」は、単一文字の類では補題 SD で入る。 |
| R10 補題 Φ2 | 定理 1 の (Ξ3\*) にそのまま使う。 |
| R10 系 C | 系 6 で置き換えた。(R3) は消え、(R1)・(R2) は二文字以上の類に限られる。 |
| R10 NF2（二側の族） | 不要になった（定理 1 の「族は一穴のままでよい」）。食い違った語の評価（R10 §3.5 の OPEN）は、単一文字の類では問題として生じない。命題 3 は (a) の部分的な答えである。 |
| R10 §2.4 の (D1)(D2) | (D1) はトークンの段階で、文字の段階の合同（補題 RC）を写さない。(D2) の類はどれも二文字（$\{\mathtt a,\mathtt c,\mathtt d\}$、$\{\mathtt a,\mathtt b,\mathtt c\}$）で、本報告と矛盾しない。 |
| R4 系 B、R5 定理 0.1・0.2 | 定理 4 の $\mu_{\mathtt a}$ の評価は R5 定理 0.2 による。系 B には依存しない。 |

---

## 6. 自己監査

主要な主張を、反例を探す立場で読み直した。

1. **補題 RC の前提（重点項目）。**
   - 要るのは、$\mathtt x^n$ が極大な連として現れ、直前の $\mathtt a$ の連が $\ge2$ にできる $L$ の語である。
   - 孤立した配置の外側の連は $N-p_y-1\ge2$ である（$R_K$ の定義の条件 $N-p_y\ge3$）。定理 1 で使う節点では $N-p_y-1\ge N-N/16-2$ で、十分長い。成分の内側の連（長さ 1 でもよい）へも P1′ で一文字移せる。P1′ の中央は二つの連の間の語で、空でない。
   - 補題 SD の $v,w$ は $G^*\ge1$ から $N-p_v\ge3$、$N-p_w\ge3$ を満たすので、その成分の連は $R_K$ に入る。
   - 連の長さの集合 $R_K$ を「成分の中で極大な連」で定義した。成分の端の連が孤立した配置で極大であることは、両隣が外側の連か隙間（$\ge1$、nonmerging）であることから従う。$d_y=2$ のとき隙間が 1 でも、$\mathtt a$ は一文字あるので極大性は保たれる。
2. **補題 NFK の帰納（重点項目）。**
   - 置き換えで連が合流しても、長さは $\langle R_K\rangle$ に留まる。合流は「直前の連」とだけ起き、合流した連の分解は $R_K$ の元の和として DP で取れる。
   - これは [B] で 1,356 回実行され、全て成功した。$\langle R_K\rangle$ の外の長さは一度も現れなかった。
3. **補題 SD の型と語（重点項目）。**
   - 型の一致には「$\omega^i_v$ が $\mathtt x$ を含む」ことだけを使った。二穴の型（成分ごとの内容）は一度も使っていない。**全て一穴の比較**である。
   - $E_0[x]$ の導出は $N_{vw}$ の Parikh ベクトルと連の性質だけによる。配置（交差かどうか）は使っていない。これが交差を閉じる理由である。
   - 「語全体の Parikh ベクトルの一致から代入の合法性を導かない」（必須検査）との関係を確かめた。本報告で Parikh の一致から結論するのは**補題 NFK を経た合同**だけである。その合同は、補題 RC の Rect（型の一致した一穴の比較）を有限回合成したものである。代入の合法性は各段の Rect で別に確かめている。
4. **R10 の部品への依存。**
   - 定理 1・4 は R9 の HΞ（補題 W の組み直しを含む）、R10 の HΞ\*（$\pi_0$ への一般化）、Φ2、補題 2 に全面的に依存する。いずれも同じモデル系列による自己判定で、独立監査はない。
   - 本報告はそれらを読み通したが、再証明はしていない。
   - とくに Φ2 の $\beta$ の位置が $v$ の隙間の中（$i=1$）にあるとき、原型の $\Phi_R$ は隙間の残り（逃がした片を含む）と $\omega^2_v$ を含む。HΞ\* の入れ替えの語でも、K-ブロックは $\pi_0=\omega^1_v$ に先導される。ここは R10 の D2 (gap) と同じ状況で、新しい問題はない。
5. **「入れ替えで食い違いは生じない」の点検。**
   - HΞ\* の族の語の各スロットは、連続した逃げ道 $e_{\pi_i}$ を一つ持つトークンである。分離節点 $u_\pi$ の切れ目の記述子は、トークン番号・スロットの中身・トークン内の位置である。
   - 同じ類の二つの並べ方で部分木を交換すると、切られたスロットは両者で同じ逃げ道で、組み直される。完全に中に入るスロットは一方の並べ方の中身を持つ。
   - 一つのスロットの中で「左右の成分が別の元」になることはない（一穴の族では成分がスロットをまたがない）。
6. **命題 3 の範囲。**
   - (i) は任意の文脈で成り立つ。
   - (iii) の加法性は比較できない節点の対について示しただけである。$\mathrm{Def}$ が線形であることは示していない。
   - したがって依頼の (a)（食い違った二側の語の剛性）は、一般の形では示していない。
7. **命題 5 は十分条件である。**
   - 射影が等しくない交差（[C] で 147 例）が使えないことは示していない。EX などの別の合同で使える可能性は残る。
   - 系 6 の (R1\*) は「本報告の道具で使えない」という意味であり、言語の段階で障害になることを一般には示していない。R15 の例は (R2\*) 型である。
8. **有限検査の性格。**
   - [B][C][D] は合成の配置（生まれつきの語を公理として与える）で、実際の文法の木ではない。証明の各段の**手が合法であること**と、その手で目標の語に届くことを確かめただけで、漸近については何も示さない。
   - [E][F] の言語は小さい（$N\le15$）。
   - [E] の連の型の候補が代入可能でないのは、補題 RC の機構の例示である。全ての単一文字の候補を排除したのではない（排除は系 2 の証明による）。
9. **新規性。**
   - 補題 RC の機構は本稿の `lem:app-two-runs`(ii) にあり、R10 の自己監査 4 も「成分の COM」として見込んでいた。
   - 新しいのは、それを大きいアルファベットの中の単一文字の類に使い、R10 の系 C の (R1)・(R3) を閉じたことである。
   - $|\Sigma|=2$ の帰結は既知である。文献検索はしていない。
10. **独立性。** 報告者は R4〜R10 と同じモデル系列である。

---

## 7. 次の最小義務（3 項目）

1. **独立監査（別系列のモデル）。** 次の連鎖を監査する。通れば、$m=\{\mathtt a\}$ は二文字以上の類の (R1\*)・(R2\*) を除いて閉じたと記録できる。
   - R9 の定理 HΞ（とくに補題 W）
   - R10 の HΞ\*・Φ2・補題 2（類の消去）
   - 本報告の補題 RC・NFK・SD・定理 1・定理 4

   補題 RC・NFK・SD は初等的なので、短時間で手で検査できる見込みである。
2. **二文字以上の類の交差 (R1\*)。** 次のどちらかを行う。
   - EX（射影の異なる逃げ道の合同）を使って、射影が可換でない交差でも溶解を得る。
   - 内容が成分に分かれない（$\mathrm{cl}_1=\mathrm{cl}_2=K$）のに射影が非可換で、連結の対の配置を持たない代入可能な言語を作る。

   最初の試験台は $\{\mathtt a,\mathtt b,\mathtt c\}$ の類で、成分の射影が $\mathtt{bc}$ と $\mathtt{cb}$ の交差である。
3. **$|m|\ge2$ への補題 RC・PNF の持ち上げ。** 4 乗を持つ宿主の文字 $z$ について「$z$ は $z$ に挟まれた塊と可換」を示し、単一の新しい文字の類で補題 SD の類比を得る。

---

## 付録：再実行

```
cd code
python3 -I run_all.py > run_all.log     # 約 6 秒（1 コア）。終了コード 0。経過時間は標準エラー
```

- `run_all.py` の標準出力は `PYTHONHASHSEED` によらない（0, 1, 777, 12345 でログの sha256 が一致することを確かめた）。
- 長時間の探索は同梱していない。
