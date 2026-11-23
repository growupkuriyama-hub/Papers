# 02-v5-mcfg-regular-skeletons — #2骨格MCFG（方向A）

*Which Regular Skeletons Give Polynomial Characteristic Data for Multiple Context-Free Languages?*

- 英語正本：[`main.tex`](main.tex)（[PDF](main.pdf)、草稿 17 頁、2026-11-23）
- 日本語版：[`japanese/main_JP.tex`](japanese/main_JP.tex)（LuaLaTeX。ラベルは英語版と同一）
- 研究台帳：[`research/README.md`](research/README.md)
- 英日の整合チェック：`python3 tools/check_labels.py`

## 何の論文か

固定した有限半群型付けのもとでの MCFL の分布学習で、特性データの総長を決める代表長 $\tau(G,s)$ を、**標的の側から**多項式で抑える。

- **主定理（Theorem A）**：正則な骨格 $R$ の統語半群が $\mathbf{L}\,\mathbf{ECom}$（すべての局所モノイドで冪等元が可換）に入り、所属が $R$ の統語値と固定長の因子の個数で決まる標的は、内容・窓・$R$ の統語値を見る型付け（一般に $\mathbf{LG}$ の外）のもとで、全 fan-out で $\tau$ が多項式。
- **方法**：局所計数の標的の定理（定理L）→ 状態の装飾による移送（Theorem B）→ 骨格の代数（Theorem C：$\mathbf{SL}*\mathbf{LG}=\mathbf L\,\mathbf{ECom}$）。
- **限界（Theorem D）**：$\mathbf L\,\mathbf{ECom}$ の外の骨格では、局所群の装飾のあとどんな局所計数条件でも所属が決まらない。最小例 3 つ。
- 型付けの側の境界 $\mathbf{LG}$（#1・02-v3）と、骨格の側の境界 $\mathbf L\,\mathbf{ECom}$（本稿）が、どちらも局所モノイドの条件として並ぶ。
- `op:fanout-two` は解決しない（本文 §7 で関係を述べる）。

## 出典

| 本文 | 由来 | 状態 |
|---|---|---|
| 定理 3.2（`thm:L`）と補題 3.3–3.8 | 第四段（Claude, 2026-11-14）→ GPT-6 監査（FIXABLE）→ R14 T1 修正版 | 修正版は自己判定 VALID。2026-11-23 に六つの補題へ分割、定数は付録 A |
| 補題 3.9（`lem:occurring`、現れる窓だけを数える） | Claude（2026-11-23） | 証明を本文に付けた（$K$ が入る四か所 (a)–(d) を確認）。独立監査は未 |
| 定理 B・定理 4.6（`thm:transfer`）と補題 4.3–4.5 | R16 U1 | 自己判定 VALID、Claude が五段を確認。2026-11-23 に三つの補題へ分割 |
| 定理 5.2（`thm:recovery`、復元 ⟺ SL∗LG） | R16 U3 | 自己判定 VALID、Claude が §5.2 を確認（補う論拠 3 点を本文に反映） |
| 定理 5.3（`thm:SLLG-LECom`、SL∗LG = L ECom） | Claude 確認メモ（2026-11-23） | 文献の組み合わせ。ECom の局所性の既出文献は未確認 |
| 定理 7.1（`thm:limits`）、例 7.2（`ex:minimal`） | R16 U4 | 自己判定 VALID |
| 例 2.4・4.2・5.6・6.4（通しの例：偶数 run） | R14 T3、R16 U2 | Claude が $I_2$、幅 1 の復元、LG 型での反例を手で確認 |

## 次の作業

1. 別系列（DeepSeek など）による独立監査：`thm:L`（補題 3.3–3.9）、`thm:transfer`（補題 4.3–4.5）、`thm:recovery`、`thm:SLLG-LECom`。補題ごとに分けたので、補題単位で依頼できる。
2. ECom の局所性（$\mathbf{ECom}*\mathbf D=\mathbf L\,\mathbf{ECom}$）の既出文献の照合。
3. 群の場合の直接証明（指数 $fk^\ell$、注意 6.3）を付録に入れるかの判断。
4. 謝辞と AI 利用の申告（投稿先の方針に合わせる）。
5. 投稿先の検討（#1・02-v3 との関係、サラミスライスに見えないか）。

## 2026-11-23 の改稿（13 → 17 頁）

査読の負担を下げるための構成変更。数学的な主張は変えていない。

- 序論に先行研究の段落（Clark–Eyraud 2007、Yoshinaka 2011・2015、Clark–Yoshinaka、de la Higuera、Eyraud–Heinz–Yoshinaka）と、証明の三層の図（図 1）を追加。
- §2 に学習器の説明と通しの例（偶数 run、$I_2$）を追加。例は §4（装飾と幅 1 の復元）、§5（代数）、§6（結論）で再登場する。
- §3 の定理L を六つの補題（文脈の不変量、頻度の隙間、骨格、切り口と色、Euler 再配線、一回の削除）に分割し、明示的な定数は付録 A へ。注意だった「現れる窓だけを数える」を補題 3.9 として証明付きに。
- §4 の移送定理を三つの補題（足跡の言語、装飾した代入可能性、装飾した文法）に分割。
- §5 の冒頭に「既知のことと新しいこと」を明記（等式は文献の組み合わせ、新しいのは復元の構成）。
- 日本語版も同じ構成に更新し、`tools/check_labels.py` で一致を確認。
