# 研究台帳 — 09_typed-fcp-fkp

状態の記号：**PROVED**（完全な証明あり）／**PROVED-CONDITIONAL**／**CHECKED-FINITE**（有限計算のみ）／**CONJECTURED**／**OPEN**／**REFUTED**／**KNOWN**（既存結果かその直接の帰結）。
証明はすべて Claude（2026-11-24）による。**別系列モデル・人間による独立監査はまだない。**

## 確立した結果（`main.tex`）

| ラベル | 内容 | 状態 | 新規性の判定 |
|---|---|---|---|
| `lem:clark` | $X^{\rhd\lhd}Y^{\rhd\lhd}\subseteq(XY)^{\rhd\lhd}$ | PROVED | KNOWN（Clark 2013 の式(1)の片側。自己完結の証明を付けた） |
| `lem:reach` | SPP と到達文脈 | PROVED | KNOWN（KY2017 p.4、KY2023 Lemma 2） |
| `lem:product` | 文法の型付き細分化 | PROVED | KNOWN（#1 Prop 5.1 と同型の標準構成） |
| `lem:typed-galois` | 型ファイバーごとのガロア接続 | PROVED | KNOWN 相当（制限しただけ） |
| `lem:star` | 文脈集合は閉包の取り替えに鈍感 | PROVED | 補題としては易しい。本稿の要 |
| `prop:typed-prop1` | KY2017 Prop 1 の型付き版 | PROVED | KNOWN 相当 |
| `prop:learners` | 型付き dual/primal 学習器 ⇔ 型付き very weak 性質 | PROVED（KY の証明の移植） | **KNOWN**：Yoshinaka 2015 の sorted 枠組みの特殊例 |
| `rem:exreg` | 型付き文脈集合は KY2023 の拡張正則閉包に入る | KNOWN（帰結） | パラメータ対応は未照合 |
| `lem:reduction` | **核の縮約補題**：型付き核の SPP ⇔ 均質な通常核の SPP | PROVED | 新（と判断。文献上の先行は未発見） |
| `thm:duality` | **文脈–核の双対性**：核側は細分化で単調減少、文脈側は単調増加。型付き VW-FKP = W-FKP | PROVED | 新（(a) は KY2017 Prop 10 の移植、(b)(c) の比較が新） |
| `cor:primal-dominated` | 型付き primal 学習器は型なしに支配される | PROVED | 新 |
| `prop:strict-context` | 文脈側の厳密性（KY2017 Prop 2(i) の言語、$c$ の指示型付け） | PROVED | 例は KY2017。$s_0$ 型付きへの拡張と $U_1$ での救済が新 |
| `prop:strict-kernel` | 核側の厳密性：$L_K$ は $s_0$ で VW 2-FKP、$h_{\{y,z\}}$ ではどの $k$ でも不可 | PROVED | 新 |
| `cor:invariant` | KY2017 Prop 2(ii) の核の失敗はどの観測でも直らない | PROVED | 新（双対性の系） |
| `thm:uniform` | **任意の $s$ について $\mathcal C^{\rm cf}_s\subseteq$ 型なし weak 1-FKP（階数 2）**。単一の primal 学習器 $\mathrm{Primal}_{2,1}$ が $\bigcup_s\mathcal C^{\rm cf}_s$ を同定 | PROVED | $s=s_0$ は KNOWN（合同文法 ⇒ 1-FKP）。全観測を一つの学習器で、が新 |
| `lem:nodes` | 括弧倍化族の節点構造 | PROVED | 補助 |
| `prop:deletion-upper` | $L_n$：強 1-FKP・1-FCP（多項式）、$M_n$：$s_U$ 型付き強 1-FCP（多項式） | PROVED + CHECKED-FINITE（n≤4） | 新 |
| `lem:capture` | **核の捕獲補題** | PROVED + CHECKED-FINITE（n≤4、1204 組） | 新 |
| `thm:deletion` | **$M_n$ の核下界**：VW-FKP を持つ任意の文法で $\rho\,\lvert N\rvert\max(\kappa,1)\ge3\cdot2^{n-1}-1$、どの型付けでも | PROVED | 新 |
| `cor:primal-data` | primal 学習器の収束時データ $\ge 2^{\Omega(n/k)}$ | PROVED | 新 |
| `prop:dual-refutation` | dual 学習器（型付き $s_U$・型なし、$r\ge2$）は収束時に $w^*_{n-1}$ を見ている必要 | PROVED | 新（「反駁のコスト」） |

## 有限計算（`tools/`）

| スクリプト | 内容 | 結果 |
|---|---|---|
| `check_deletion_family.py 4` | `prop:deletion-upper`、`lem:capture`、反駁補題のファイバー等式を n=2,3,4 で全数 | すべて通過（n=4 で 1204 組、2.7 秒） |
| `check_reduction_identity.py 4000` | `lem:star` と `lem:reduction` の規則ごとの同値を、$\{a,b,c\}$ 上の乱数有限言語 4000 個 × 5 種の型付けで | 反例なし（規則同値 2159 件） |

## 予想・未解決

| 番号 | 内容 | 状態 | メモ |
|---|---|---|---|
| `op:weak-fcp` | weak FCP は細分化で単調か | OPEN（反例候補あり＝CONJECTURED: 単調でない） | KY Thm 14 の言語の $\$$ を新文字に替えた語を足す構成。KY Lemma 12 の全非終端記号の再検査が必要 |
| `op:robust` | 任意の $s$ で $\mathrm{FCP_{vw}}[s]\ne\mathrm{FCP_w}[s]$ か | OPEN | KY Thm 14 の証拠は $\$$ の指示型付けで壊れる（Lemma 13 の証明が通らない）。冪等冪による頑健化が方針 |
| `op:Mn-context` | 型なし VW-FCP 文法での $M_n$ の文脈長・大きさの指数下界 | OPEN（部分結果 PROVED：ζ 節点を丸ごと含む構成素は巨大） | |
| 濾過核 | 混合核＋型の濾過の primal 変種は $\mathrm{FKP_{vw}}$ を真に拡張するか | OPEN | $\mathrm{FKP_{vw}}$ と $L_K$ は含む |
| その他 | $\bigcup_s\mathcal C^{\rm cf}_s\subseteq\mathrm{FCP_{vw}}$ か／型付き strong FKP の反単調性／MCFG への拡張 | OPEN | |

## 途中で否定された案（再探索しないための記録）

1. **REFUTED**：$L=\{a^izb^i\}\cup\{a^mb^n:m\ne n\}$ が型なし強 1-FKP を持つ、という最初の案。$a^+$ を生む非終端記号は、$z$ の文脈が $a$ の個数を固定するため有限核で特徴づけられない（$\{a,aa\}$ の閉包にも $a^3$ が入らない）。→ $z$ と $y$ を左右に置いた $L_K$ に修正して成立。
2. **REFUTED**：「型付き dual 学習器なら $M_n$ を多項式データで学べる」。型 1 のファイバー $\{c\}^{\lhd}\cap F_1=\{w^*_{n-1}\}$ を含む不正な規則の反駁に $w^*_{n-1}$ が要る（`prop:dual-refutation`）。初期記号を観測済みの型に限っても、この規則は残る。
3. **REFUTED（懸念の解消）**：「型付き primal の妥当性は $J$ と MQ では有限に検査できない」。`lem:star` により型付き妥当性は型なしの妥当性と同値。
4. **部分的**：「型付けで KY Thm 9/14 の分離が崩れる」。証拠の言語では、決め手の語（$\$$ を含む語と $c^id^ie^i$ を含む語）が別ファイバーに入り Lemma 7/13 の論法が通らない。ただし型付き strong／weak FCP が実際に成り立つかは全非終端記号の確認が要り、未確認。
5. **KNOWN と判定**：型付き FCP/FKP と学習器の対応（Yoshinaka 2015 の sorted 枠組み）、型付き文脈側の多くの部分（KY2023 の拡張正則閉包）。

## 次の作業

1. 別系列モデルによる独立監査：`lem:reduction`、`thm:duality`、`prop:strict-kernel`、`thm:uniform`、`lem:capture`、`thm:deletion`、`prop:dual-refutation`。
2. KY2023 の EXREG パラメータと型付き文脈集合の対応の照合（`rem:exreg`）。
3. KY2017 の LATA 最終版（Springer）で定理番号と $L_2$ の不等式の向きを照合（本稿は著者版 PDF の抽出テキストによる）。
4. `op:weak-fcp` の候補例の検証。
5. 量的な上界：$\mathrm{Primal}_{2,1}$ の特徴データを型付き厚さで抑えられるか。
