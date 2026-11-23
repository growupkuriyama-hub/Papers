# 02-v5-mcfg-regular-skeletons — #2骨格MCFG（方向A）

*Polynomial Characteristic Data for Multiple Context-Free Languages with Regular Skeletons beyond Local Groups*

- 英語正本：[`main.tex`](main.tex)（[PDF](main.pdf)、草稿 13 頁、2026-11-23）
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
| 定理 3.2（定理L） | 第四段（Claude, 2026-11-14）→ GPT-6 監査（FIXABLE）→ R14 T1 修正版 | 修正版は自己判定 VALID。補題 L′（注意 3.4）は未確認 |
| 定理 4.2（装飾の移送） | R16 U1 | 自己判定 VALID、Claude が五段を確認 |
| 定理 5.2（復元 ⟺ SL∗LG） | R16 U3 | 自己判定 VALID、Claude が §5.2 を確認（補う論拠 3 点を本文に反映） |
| 定理 5.3（SL∗LG = L ECom） | Claude 確認メモ（2026-11-23） | 文献の組み合わせ。ECom の局所性の既出文献は未確認 |
| 定理 7.1、例 7.2 | R16 U4 | 自己判定 VALID |
| 例 6.4（偶数 run） | R14 T3、R16 U2 | Claude が $I_2$ と LG 型での反例を手で確認 |

## 次の作業

1. 別系列（DeepSeek など）による独立監査：定理 3.2・4.2・5.2・5.3。
2. 注意 3.4（現れる窓だけを数える）の確認。確認できなければ Theorem B の指数を $f(|Q|k)^m$ に戻す。
3. ECom の局所性の文献照合。
4. 序論の先行研究（Yoshinaka 2011, 2015; Clark–Yoshinaka; #1）と関連研究の拡充、群の場合の直接証明（指数 $fk^\ell$）を付録に入れるかの判断。
5. 投稿先の検討（#1・02-v3 との関係、サラミスライスに見えないか）。
