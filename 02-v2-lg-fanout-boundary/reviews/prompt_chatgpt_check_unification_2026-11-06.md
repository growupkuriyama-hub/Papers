# 検算依頼：一本化・一般化・圧縮の改訂（README (161)(162)）

あなたは有限半群と MCFG の分布学習に詳しい査読者です。下の GitHub 上の原稿について、**今回の改訂で書き換えた証明だけ**を独立に検算してください。新しい研究の提案や文体の改善は不要です。

## 対象

- リポジトリ：`growupkuriyama-hub/Papers`
- ファイル：`02-v2-lg-fanout-boundary/main.tex`
- コミット：**`2234ded`**（README (162)）。直前の版は `9b49d07`（README (161)）と `7150f5e`（README (159)）。
- 差分の確認：`git diff 7150f5e 2234ded -- 02-v2-lg-fanout-boundary/main.tex`
- 改訂の記録：同フォルダの `README.md` の Change log、(161) と (162)。

**最初に**、取得した `main.tex` のコミット SHA（またはblob SHA）と行数を報告してください。`2234ded` と一致しない場合は、その旨を書いたうえで手元の版で作業してください。

## 検算してほしい項目（優先順）

各項目について、**正しい／修正が必要（どこを、どう）／誤り（反例）**のどれかで判定し、根拠を書いてください。

### C1. 短縮の原理 `lem:heavy-node-count`
- (i) 実現ラベル数 n_λ(G)（C∈V と u∈L_C(G) からなる組 (C, λ(u)) の数）で経路の長さを抑えてよいか。
- (ii) 「重い反鎖 Q に対し |Q∖Q_0|≤h なる Q_0 があり、|Q_0|>c なら空でない J⊆Q_0 を長さ ≤ θ̄_G の組へ一斉に置換して根の λ ベクトルを保てる」という仮定から、反鎖の大きさ ≤ c+h、そして β=(r_max+1)θ̄_G max{1,(c+h)n_λ(G)} の (R_β^λ) が出るか。
  - 特に、置換後の根の長さが**真に**短くなる議論（線形性・非削除性により置換された各 yield が根にちょうど一度現れる）の正しさ。
- 二つの適用が仮定を正しく満たしているか：
  - `lem:marked-heavy-window-group`（c=c_{G,f}, h=f(k+ℓ+1)）
  - `lem:local-group-shortest`（c=(4kf+1)c_{G,f}, h=2kf, J⊆I⊆Q_0）
- 定理の上界（`thm:window-group-polydata`, `thm:local-group-polydata`）の数値が改訂前と変わっていないこと。

### C2. Pumping（付録 B 冒頭）とその三つの使用箇所
- 「有限半群 T で、|T| 個以上の元の積は T¹E(T)T¹ に入る」とその二行の証明。
- `lem:lg-rees-window-coordinate`：
  - 仮定が「S^k⊆K を満たす任意の k≥1」になったこと。
  - 旧ステップ (1) を消して pumping に置き換えたこと。
  - 番号を付け替えた (1)(2) の参照が正しいこと。
- `thm:lg-characterization`：
  - 直接の (ii)⇒(iii) 証明を消しても、(i)–(iii) の同値が Almeida–Margolis–Steinberg–Volkov 2009 Prop. 2.3 と pumping から完結すること。
  - (iv) の「S^k=K となる任意の k」。
- `lem:mcfg-li-group-window`（付録 B に移動）：
  - a,b,c,d∈S_0^1 にした分解 τ(p)=aeb, τ(z)=cfd が正しいこと。
  - τ(w)=aefd が p と z だけで決まること。

### C3. ファンアウト1の群定数 `lem:block-replacement`(c)
- f=1, m≥|G| で、空でない区間 J が唯一の行の値を保つこと（各 owner はブロック一つ、位置で番号を付け直し、状態 κ_p=P_pQ_p^{-1} の鳩の巣）。
- c_{G,f} の定義（可換：d(G^f)、非可換かつ f=1：|G|−1、それ以外：M_{G,f}−1）と、`prop:block-replacement-interface` の「m>c_{G,f}」との整合。

### C4. 特性標本の統合 `lem:witness-length-template`(ii),(iv)
- ι(X)∈Cl_{L,s}(X) ならば、Wit_ι⊆L であり、Wit_ι∪({ε}∩L) が B^{≤r_max}_{f,s} と B_{f,s} の両方について特性標本になること。
  - `prop:completeness` の仮定（型の一致、χ(S_t)=□、r_G≤r_max）が満たされることを含む。
- `thm:data-from-typed-thickness`（ι=ω）と `cor:distribution-representatives`（ι は類の中で最短）の短くなった証明が、旧証明と同じ結論を与えること。μ* ≤ τ の部分を含みます。

### C5. 挿入の事実 `prop:output-invariants`(iv)
- 「型付き非終端 X からの G^ŝ 導出は刈り込んだ G̃_0 の規則しか使わない」とその証明。
- `lem:witness-length-template`(i) での使い方。

### C6. 小さな変更（一言ずつでよい）
- `prop:li-g-strict`(i)：LI∨Grp⊆LG を「LG は LI と Grp を含む擬多様体」で示すこと。
- 付録 B 冒頭の擬恒等式 (x^ω y x^ω)^ω = x^ω による LG の記述とその理由。
- typing の定義後の一文「S^♯ は {1_♯, f}≅U₁ を含むので局所群でない」。

## ルール
- 主張は原稿の番号・ラベルで特定し、根拠を数学的に書いてください。
- 計算で確かめられるもの（例：C3 を小さな群 S₃・D₄ で全探索、C2 を小さな半群で確認）は、スクリプトと出力を報告に含めてもかまいません。
- 「たぶん正しい」は避け、確かめられなかった点は「未確認」と明記してください。
- 原稿の他の部分の問題に気づいた場合は、最後に「範囲外の指摘」として短く挙げてください。

## 出力形式
**報告は一つの Markdown ファイル**にまとめてください。ファイル名は `chatgpt_check_unification_2026-11-06.md` です。構成は次のとおりです。

1. 取得した版（SHA・行数）
2. 総合判定（一行）
3. C1–C6 の項目ごとの判定と根拠
4. 必要な修正の一覧（LaTeX の差し替え案があれば付ける）
5. 範囲外の指摘（あれば）
6. 実行したスクリプトと出力（あれば）
