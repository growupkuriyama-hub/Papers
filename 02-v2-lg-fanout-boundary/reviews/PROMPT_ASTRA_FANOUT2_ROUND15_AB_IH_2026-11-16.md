# Astra 第十五段・独立数学探索依頼
## MCFG fan-out 2：非可換 Parikh 還元の残余 AB / IH と LG 境界問題

**目的は純粋な数学研究です。** 博士論文#2の既存原稿を編集せず、論文の新規執筆・提案、GitHubへの書き込みも行わないでください。第十四段までのClaude・Fableの結果を単に要約するのではなく、**未解決部分を独立に証明・反証すること**を目標にしてください。失敗した場合も、破綻する最小の仮定と再現可能な反例を成果とします。日本語で報告してください。

## 1. 必ず実物を読む一次資料（閲覧専用）

GitHub: https://github.com/growupkuriyama-hub/Papers

1. 最新研究索引：https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/STATUS_FANOUT2_ROUNDS12_TO14_FABLE_2026-11-16.md
2. 現行ハンドオフ：https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/HANDOFF_CURRENT.md
3. **定義・既存定理・正式開問題の正本**：https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/main.tex
4. 第十四段の**最新独立監査（原報告より優先）**：https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/audit_claude_round14_noncomm_Parikh_independent_2026-11-16.md
5. 第十三段独立監査：https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/audit_claude_round13_noncomm_U_independent_2026-11-15.md
6. Fable-C独立手証明監査：https://github.com/growupkuriyama-hub/Papers/blob/main/02-v2-lg-fanout-boundary/reviews/Fable_C_complete_independent_mathematical_audit_2026-11-15.md
7. 第十四段原報告と残存義務：同じ `reviews/` 内の `claude_round14_noncomm_Parikh_report_2026-11-15.md`、`claude_round14_noncomm_Parikh_next_obligations_2026-11-15.md`。

完全な原報告・ソースコード・ログ・独立監査は以下の4束に原バイト／SHA-256付きで保存済みです。必要な証明箇所と反例を直接検査してください。
- 第十二段：`reviews/ROUND12_COMPLETE_SOURCE_AUDIT_2026-11-16.md`
- Fable：`reviews/FABLE_20261115_COMPLETE_SOURCE_AUDIT_2026-11-16.md`
- 第十三段：`reviews/ROUND13_COMPLETE_SOURCE_AUDIT_2026-11-16.md`
- 第十四段：`reviews/ROUND14_COMPLETE_SOURCE_AUDIT_2026-11-16.md`

GitHub PR #130は2026-11-16にマージ済み：https://github.com/growupkuriyama-hub/Papers/pull/130 。リンクが読めない場合はその旨を記し、読めない証明を既読・検証済みと偽らないでください。

## 2. 現在の数学的状況：混同禁止

**正式開問題 `op:fanout-two`：OPEN。** 固定fan-out `f≥2`、rank `r_max≥2` で、有限半群擬多様体の一様多項式characteristic-data長の正確な境界はLGか。`V⊆LG` の十分性は現行Theorem Aで既に `O(‖G‖² θ̄_G)` と証明済み。fan-out 1の必要十分性は現行Theorem Cで証明済み。**fan-out≥2のLG必要性が未解決。** 一般非LGを攻める最小障害は `U₁={1,ζ}`（`ζ²=ζ`）、例えば固定 `Σ={a,b,c}`、`s_U(a)=s_U(b)=1, s_U(c)=ζ`。過去の特殊な二射影クラス「U₂」と、この半群 U₁を混同しないこと。

既存の研究上の到達点：
- 第十二段：3,093候補の下界探索はすべて1穴または2穴代入可能性の違反が判明し、合法な超多項式下界は未発見。
- **Fable-A/B**：倍増言語族全体の包含からの短語強制／アーベル剰余類フィルタ障壁。Fable-Aは**長い `W_n` 1語だけ**から `baab` を強制しない。
- **Fable-C**：**可換言語に限定**した最短 `a^N` の上界 `N=O_{D,r}(v θ̄_G^{1+D+D²2^D})`。独立手証明監査で有効（補足あり）；非可換への拡張は未証明。
- 第十三段 **T1**：`N < θ̄_G [2(r+1)]^{2M+1}` は独立手証明監査済み。`M` は最重子経路で現れる大節点の**核骨格の種類数**。Mの一般的な小ささは未証明。
- 第十四段 **TR**：異なる非a文字 `d,e` のRot核 `de/ed` は、**加法的な連結二核宿主**と十分な室 `N≥4 max(δ_de,δ_ed)+1` の下で欠損が一致。独立した手証明と有限証明書replayあり。TRは原文CAを使わない。

**使ってはならない偽補題：**
1. 第十三段の**原文 X1：REFUTED**。内容型付き2-tuple-substitutableの40語有限言語で、`κ=bc, κ'=acb, λ=λ'=3, N=8` は `s(aκ)=s(aκ')` だが `bc∈L, acb∉L`。実際に交換する断片の型一致が欠落。**X1⁺は正のaパディング `i,i'≥1` 等を付した別の限定主張**。
2. 第十四段の**原文 CA：REFUTED**。67語の厳密な組代入可能言語で `N=10`、`κ_B=bc, κ_C=cb`、`δ_B=δ_C=2`、`bccb a³∈L` だが `bccb a⁶∉L`。正の初期a室があっても、**初期連結種のa-budgetが加法的でなければ**結論は偽。**CA\*** は出発種のa-budgetの加法的一致と、初期・目標の室（典型的には各≥3）を明示する必要がある。
3. 第十四段原報告／古い `next_obligations` に「CA PROVED」とあるのは**後の独立監査で否定済み**。`P_tree ⇐ CA + IH + AB` を無条件の成果として引用せず、最低限 `CA*` の前提を再検証すること。

## 3. 絶対に守る定義

現行 `main.tex` の `def:grammar-properties`、`def:tuple-substitutable`、`lem:thickness-equivalence`、`op:fanout-two` が優先です。

- `good`：`ε`-free、nondeleting、nonpermuting、nonmerging。`reduced`：全非終端が到達可能・生産的。fan-outとrankを区別する。
- 適法なd穴文脈は `v₀□₁v₁ ... v_{d−1}□_d v_d`、**各穴の語と各内側区切りが非空**。特に2穴中央セパレータは必ず非空。
- 比較する各tuple成分の**実際の型**が等しく、**共通の受理文脈**があれば全受理文脈が一致する、という条件を `d=1,2` の両方で課す。内容型 `c_Σ(w)=alph(w)` と `s_U` を同一視しない。
- 計算量は**元の reduced good 文法**の `‖G‖` と `θ̄_G` で測り、後付けの型精密化文法の厚さで置き換えない。
- 有界探索のPASS、閉包のcap/truncated、全称の数学的証明を区別する。有限言語の反例の適法性は、全ての受理1穴・2穴文脈について厳密に確認できる。

## 4. 最優先課題A：AB_pair の証明または反証

まず `Σ={a,b,c}`、内容型 `c_Σ`、`L∈C^{mcf}_{2,c_Σ}`、`N=min{n≥1:a^n∈L}` を固定。**Rot核** `κ` は両端が非aで、単独受理語 `a^p κ a^q∈L`（`p,q≥1`、`λ(κ)=p+q∈[3,N−1]`）を持つとする。

`δ(κ):=N−λ(κ)−|κ|_a`、`h(κ):=δ(κ)+|κ|_a=N−λ(κ)`。ここでは**非a文字のParikhベクトル** `V_Δ(κ)` と、κ内部のa個数とを分けて扱う。`V_Δ(κ)=V_Δ(κ')` は、核の**完全なParikhベクトルが等しいことより弱い**。両者を混同すると、最終的な `P_tree` には届かないおそれがある。

以下の候補命題の**正しい最小仮定と真偽**を調べてください：

> `V_Δ(κ)=V_Δ(κ')≠0`、単独Rot証人があり、**実在する受理済み連結宿主** `a^x κ a^y κ' a^z∈L` がある。さらに `x+y+z=N−h(κ)−h(κ')≥3`（**加法的な初期a-budget**）かつ適切な室条件 `N≥c₁ max(δ(κ),δ(κ'))+c₂` などを課す。このとき `δ(κ)=δ(κ')` と結論できるか。

ここに記した命題は**未証明の探索対象**であり、真と仮定して進めてはいけません。`c₁,c₂` が存在するならその依存先（`θ̄_G, D, |κ|` などに依存してよいか）を厳密化してください。室が不足するなら、十分条件を強める／反例を示す、のどちらでも構いません。

推奨する切片：
- **A1：枠内隣接転置** `κ=pdeq`, `κ'=pedq`。枠補題Fは内部語が両方非空のときだけ使える。TRの7手を再構成できるか。
- **A2：一般隣接転置列**。非a Parikhが等しい語を隣接交換で結ぶ際、各中間核がRot証人と加法的宿主を持つかを先に証明する。単純な「同Parikhだから順序交換可能」は禁止。
- **A3：境界横断・複合核** `bcc/cbc`, `bcc/ccb`, `bbcc/bcbc`、および `bc/bbcc`（最後は**同Parikh対ではなく**比例・多単位関係のテスト）。有限の矛盾証明書を一般の文脈恒等式に昇格できるか。
- もしAB_pairが偽なら、**CA*の前提・十分な室を満たす**反例を狙う。単に連結宿主がない82語例やCA原文の67語例を再提出してもAB_pairの反証にはならない。

## 5. 最優先課題B：IH（交錯・入れ子の宿主）の証明または反証

`a^N` の**節点数最小導出木**にある、同じ非a内容類の比較不能な内部大節点 `B,C` を、短い生産的tupleに**同時置換**する。逐次配置なら連結種を得やすいが、fan-out 2には **交錯 `B₁C₁B₂C₂`、入れ子 `B₁C₁C₂B₂`** がある。

目標：元の実在する木由来の二重置換語から、**同じ内容類のRot核 `κ_J,κ_{J'}` を連結配置する実際の受理語** `a^xκ_Ja^yκ_{J'}a^z∈L` を導き、必要なら `x+y+z=N−h(κ_J)−h(κ_{J'})≥3` を保持する、という**加法的なIH**を証明するか、偽であることを正確な仮定の下で示す。

注意：`B,C` の各tuple**成分の内容型**は一般に異なる。2穴全体を任意の連結語に一括変形してはならない。非空セパレータ、元のgood導出の配置、実際に使える宿主、a-budgetを一手ずつ追跡すること。有限言語の反例だけでは**木由来IH**の反例にならないため、失敗を主張するなら条件を満たす**明示的reduced good MCFGと導出木**を提示すること。

推奨：最小交錯 `B=C=(b,c)` 型の構成から始め、1穴Rot、型安全なX1⁺／S／F、2穴OS／CSによる**連結化アルゴリズム**を作る。無理なら実際に保存される弱い不変量を発見し、IHを成立する部分クラスに分割する。

## 6. 自由な別経路（歓迎）

AB・IHの前提がそもそも誤っていると思えば、そこを最優先で攻撃してよい。さらに次の独立経路を追求してよい：

- **非可換予想U**（最短 `a^N` の多項式上界）の新証明／反例。成功しても一般characteristic-data長、正式LG境界の解決とは区別。
- 正式な `op:fanout-two` の**必要性**に直接迫る、固定 `U₁` 型付けのreduced good、fan-out 2/rank 2 の超多項式希少型族、あるいは組代入可能な真部分言語間の**超多項式の最短区別語**。倍増族の単純移植は既存 `thm:doubling-no-lift` で失敗。
- 逆に `U₁` 型一般での多項式上界を見出す試み。ただし単一型の最短語上界だけでは正式問題への否定回答にならない。
- 有限証明書から**全称的な局所恒等式**を抽出する、木の成分順を保持する新たな不変量を設計する等、既存Claudeの路線に依存しない発想。

## 7. 成功基準・検証方法・成果物

**証明を出す場合：** 全称量化・適法な型・共通受理文脈・適用文脈・正の穴とセパレータを表示し、`E₀[x],E₀[y],E₁[x]∈L ⇒ E₁[y]∈L` を各非自明ステップで具体化。CA*を使う場合は**どの木由来語が初期加法的種か**を示す。補題の依存関係をDAGまたは明示リストにする。

**反例を出す場合：** 明示的な言語・文法、破綻する式、受理／非受理の具体語、1穴・2穴組代入可能性、good/reduced、必要に応じて木由来性を区別して証明。有限探索なら、元コードと独立実装、完全な閉包判定、seed・cap・打切り・終了コードを公開可能にする。

**出力：**
1. `astra_fanout2_round15_report_2026-11-16.md` 相当の**完成した数学報告**。冒頭に「新しく確立したこと／反証したこと／未解決」を各1〜数行で記す。
2. 命題ごとに `PROVED`、`PROVED WITH CLARIFICATIONS`、`CONDITIONAL`、`CERTIFIED FINITE`、`REFUTED`、`OPEN` の判定表。**提案・有望・実験PASSはPROVEDではない**。
3. 必要に応じてPython 3標準ライブラリだけの再現コード、完全な実行ログ、具体証明書、短いcheckpoint。実行していない検証を実行済みと書かない。
4. **次の一手**：未解決で残る最小補題を1〜3個、各々の正確な仮定・想定反例・突破方法付きで挙げる。

早い段階で**既知の40語X1反例・67語CA反例と整合するか**を確認すること。計算が大きくなる場合、まず意味のある中間定理・反例・小さい証明書を優先する。研究が完結しなくても、得られた確かな部分成果をすべて報告する。

**最重要：論文原稿 `main.tex`・日本語原稿・PDF・`PAPER.yaml` を編集せず、GitHubへのPR/commit/pushもせず、独立論文を起案しないこと。**
