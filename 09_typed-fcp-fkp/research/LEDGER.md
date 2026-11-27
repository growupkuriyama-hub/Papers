# 研究台帳 — 09_typed-fcp-fkp

状態の記号：**PROVED**（完全な証明あり）／**PROVED-CONDITIONAL**／**CHECKED-FINITE**（有限計算のみ）／**CONJECTURED**／**OPEN**／**REFUTED**／**KNOWN**（既存結果かその直接の帰結）。
証明はすべて Claude（2026-11-24）による。**2026-11-24 に ChatGPT による外部査読を受けた**（29 判定：CORRECT 11、CORRECT-WITH-FIX 8、GAP 0、FALSE 0、KNOWN 10。対応は [`REVIEW_RESPONSE_2026-11-24.md`](REVIEW_RESPONSE_2026-11-24.md)）。**2026-11-25 に ChatGPT（Astra、記憶をリセットした別会話）による 2 回目の外部査読を受けた**（Major revision 相当。主定理の撤回は不要。重大な指摘 2 件はどちらも正しく、対応は [`REVIEW_RESPONSE_2026-11-25.md`](REVIEW_RESPONSE_2026-11-25.md)）。人間による監査はまだない。

## 確立した結果（`main.tex`）

| ラベル | 内容 | 状態 | 新規性の判定 |
|---|---|---|---|
| `lem:clark` | $X^{\rhd\lhd}Y^{\rhd\lhd}\subseteq(XY)^{\rhd\lhd}$ | PROVED | KNOWN（Clark 2013 の式(1)の片側。自己完結の証明を付けた） |
| `lem:reach` | SPP と到達文脈 | PROVED | KNOWN（KY2017 p.4、KY2023 Lemma 2） |
| `lem:product` | 文法の型付き細分化 | PROVED（rev2 で型の積の式を修正：中間の $\widehat h(w_i)$ が抜けていた） | KNOWN（#1 Prop 5.1 と同型の標準構成） |
| `lem:typed-galois` | 型ファイバーごとのガロア接続 | PROVED | KNOWN 相当（制限しただけ） |
| `lem:star` | 文脈集合は閉包の取り替えに鈍感 | PROVED | **KNOWN**（KY2017 式(1)・Clark Props 3.26, 3.28 の直接の帰結。外部査読の判定） |
| `prop:typed-prop1` | KY2017 Prop 1 の型付き版 | PROVED | KNOWN 相当 |
| `prop:learners` | 型付き dual/primal 学習器 ⇔ 型付き very weak 性質 | PROVED（KY の証明の移植） | **KNOWN**：Yoshinaka 2015 の sorted 枠組みの特殊例 |
| `rem:exreg` | 型付き文脈集合は KY2023 の拡張正則閉包に入る | KNOWN（帰結） | パラメータ対応は未照合（2026-11-27 に注意を本文から削除、序論の一文のみ） |
| `lem:reduction` | **核の縮約補題**：型付き核の SPP ⇔ 均質な通常核の SPP | PROVED | 直接の帰結（KY2017 §4 p.6 の規則妥当性の同値＋制限したガロア接続）。外部査読は KNOWN と判定。明示化としては残す |
| `thm:duality` | **文脈–核の双対性**：核側は細分化で単調減少、文脈側は単調増加。型付き VW-FKP = W-FKP | PROVED（外部査読 CORRECT） | 包含自体は短い帰結。Yoshinaka 2015 §8 も signature の比較を扱う。逆向きの振る舞いの明示と厳密性の証人が追加分 |
| `cor:primal-dominated` | 型付き primal 学習器は型なしに支配される | PROVED | 新（2026-11-27 に系から命題 6.1 の後の一文へ） |
| `prop:strict-context` | 文脈側の厳密性（KY2017 Prop 2(i) の言語、$c$ の指示型付け） | PROVED | 例は KY2017。$s_0$ 型付きへの拡張と $U_1$ での救済が新 |
| `prop:strict-kernel` | 核側の厳密性：$L_K$ は $s_0$ で **strong 1-FKP**（rev2 で強化、初期記号 $S_+,S_-$）、$h_{\{y,z\}}$ ではどの $k$ でも VW-FKP 不可 | PROVED（外部査読 CORRECT＋強化案） | 新（照合範囲で同じ構成なし） |
| `cor:invariant` | KY2017 Prop 2(ii) の核の失敗はどの観測でも直らない | PROVED | 新（双対性の系） |
| `thm:uniform`（rev2 で Corollary に格下げ） | 任意の $s$ について $\mathcal C^{\rm cf}_s\subseteq$ 型なし weak 1-FKP（階数 2）。単一の primal 学習器が $\bigcup_s\mathcal C^{\rm cf}_s$ を同定 | PROVED | **KNOWN**：#1 Prop 9.7（$\bigcup_s\mathcal C^{\rm cf}_s\subseteq\mathsf{CONG}$）＋合同文法 ⇒ 1-FKP（Yoshinaka 2015 §6.3）＋KY2017 Thm 6 の直接の帰結 |
| `lem:nodes` | 括弧倍化族の節点構造 | PROVED | 補助 |
| `prop:deletion-upper` | $L_n$：強 1-FKP・1-FCP（多項式）、$M_n$：$s_U$ 型付き強 1-FCP（多項式） | PROVED + CHECKED-FINITE（n≤4） | 新 |
| `lem:capture` | **核の捕獲補題** | PROVED + CHECKED-FINITE（n≤4、1204 組） | 新 |
| `thm:gap`（rev3 で追加、主定理） | 核と文脈の隔たりのまとめ：$M_n$ は $U_1$ 型付きで大きさ $O(n)$（$2n$ 非終端記号、$6n-4$ 規則）の強 1-FCP、核の表示はどの型付けでも指数的、$L_n$ は両側 $O(n)$ | PROVED（既存の命題・定理のまとめ） | 新 （2026-11-27 に本文から削除：定理 A の再掲。内容は命題 4.2・4.3、定理 4.7 にある） |
| `ex:toy`（rev3 で追加） | 序論の例（数の一致を持つ英語断片）の文脈・例の閉包 | CHECKED-FINITE（`tools/check_toy_example.py`、有限言語なので全数で厳密） | 説明用 |
| `thm:deletion` | **$M_n$ の核下界**：VW-FKP を持つ任意の文法で $\rho\,\lvert N\rvert\max(\kappa,1)\ge3\cdot2^{n-1}-1$、どの型付けでも | PROVED（外部査読 CORRECT） | 新（外部査読も「照合範囲で同じ主張なし、最も独立性が高い」）。**本稿の主結果** |
| `cor:primal-data` | primal 学習器の収束時データ $\ge 2^{\Omega(n/k)}$ | PROVED | 新 |
| `prop:dual-refutation` | dual 学習器（型付き $s_U$・型なし、$r\ge2$）は収束時に $w^*_{n-1}$ を見ている必要 | PROVED（外部査読 CORRECT） | 新（「反駁のコスト」）。KY2017 Algorithm 1 そのもの（候補を刈り込まない実装）についての下界 |
| `lem:rec-kernel`（2026-11-25 追加） | #1 の $\mathsf{Rec}_s(K)$ が正しく再構成するとき、開始記号を外した文法は核の大きさ 1 の SPP（$\{x\}^{\rhd\lhd}$）を持つ | PROVED + CHECKED-FINITE（$K=M_n$、n=2,3） | 新（#1 と KY2017 をつなぐ補題） |
| `cor:rec-data`（2026-11-25 追加） | **正例のみの下界**：$M_n\in\mathcal C^{\rm cf}_s$ となるどの型付け $s$ でも、$\mathsf{Rec}_s$ が $M_n$ を返す標本は $\|K\|^3\ge3\cdot2^{n-1}-1$ | PROVED | 新。#1 Prop 6.4 は $L_n$ の下界で、$M_n$ 自身の下界は #1 に無い（main.tex・日本語版・R1 原稿・revision メモを全文検索して確認） |
| `prop:weak-not-preserved`（rev2 で追加、2026-11-25 に強化） | $L^+=L'\cup L_1^@$ は型なし weak 2-FCP と **$s_0$ 型付き weak 2-FCP** を持つが、$@$ の指示型付け $h$（$s_0\preceq h$）では型付き weak FCP を持たない。よって **型付き weak FCP は細分化で単調でない**（$k\ge2$） | **PROVED**。$s_0$ 版は 2 回目の外部査読（Astra）の構成を本文に入れたもの。鍵は「$L_2,L_3$ の非空語を全部受ける文脈は $u\in\{a,b,\#\}^*$、$v\in\{a,b\}^*$ で空語も受ける」という主張で、Claude が証明を確認し、独立のコード（`tools/check_weak_fcp_s0.py`）でも確認。同時に、$S_2,S_3$ の閉包を KY2017 Lemma 12 の証明なしの主張（「同じ文脈で特徴づけられたまま」）に頼らず直接示すようにした。KY2017 から使うのは、Lemma 8・12 の証明に書かれた等式（$L$ または $L'$ 相対）と Lemma 13 の証明だけ | 新。外部査読（ChatGPT、2 回）が発見 |
| `prop:Ln-sU`（2026-11-25 追加） | **観測が核を長くする**：$s_U$ 型付きで型付き very weak FKP を持つ $L_n$ の文法は、どの $k$ でも初期記号の核が $\{w^*_n\}$（$\kappa\ge3\cdot2^n-2$）。文脈側は $s_U$ 型付き強 1-FCP で $O(n)$ | PROVED | **#1 系 6.6 の論法を核に移したもの**（#1 系 6.6 は同じ孤立ファイバー $L_n\cap F_1=\{w^*_n\}$ から、$s_U$ での型付き厚さ $\ge3\cdot2^n-2$ を示す。2026-11-25 に本文で明記）。主張自体は 2 回目の外部査読が指摘（旧比較表の「核側：どの型付けでも $L_n$ は $O(n)$」は誤りだった） |
| `prop:Mn-constituent`（rev2 で追加） | ζ 節点を一つだけ持つ語で、その ζ 節点を丸ごと含む構成素の長さ $\ge|w^*_n|-\ell-|w^*_{j-1}|$ | PROVED | 新（`op:Mn-context` の部分結果。外部査読が定式化を補完） |

## 有限計算（`tools/`）

| スクリプト | 内容 | 結果 |
|---|---|---|
| `check_deletion_family.py 4` | `prop:deletion-upper`、`lem:capture`、反駁補題のファイバー等式を n=2,3,4 で全数。`lem:rec-kernel` の前提（$\mathsf{Rec}_{s_U}(M_n)=M_n$、(U) の組の分布一致）を n=2,3 で | すべて通過（n=4 で捕獲 1204 組、n=3 で (U) 1967 組）。2026-11-25 に型の判定のバグ（閉じ括弧 ⌉ だけを含む因子を標識なしとしていた）を修正。修正前の (U) の数は 15／1732 |
| `check_reduction_identity.py 4000` | `lem:star` と `lem:reduction` の規則ごとの同値を、$\{a,b,c\}$ 上の乱数有限言語 4000 個（試行ごとに 5 種の型付けから一つ） | 反例なし（規則同値 2230 件、rev2 で再現性を修正） |
| `check_weak_fcp_s0.py`（2026-11-25 追加） | 命題 6.5（旧 6.6）の主張：長さ 2 以下の全文脈（24,642 個）で、$L_2,L_3$ の非空語の標本を全部受けるものは $u\in\{a,b,\#\}^*$、$v\in\{a,b\}^*$ で空語も受ける。長さ 5 以下の全語（111,111 個）で $S_2,S_3$ の文脈集合の閉包が $L_2\cup J_0$、$L_3\cup J_0$ に一致。証明中の表の 12 行を長さ 5 以下の全語（133 万件）で照合 | 反例なし |
| 外部査読のスクリプト（`external_review_2026-11-24/scripts/`） | 有限還元の全数検査、$L_K$ の閉包、空の収量を含む捕獲補題、$L^+$ の文脈述語 | こちらでも再実行して全通過 |

## 予想・未解決

| 番号 | 内容 | 状態 | メモ |
|---|---|---|---|
| `op:weak-fcp` | weak 1-FCP は細分化で単調か | $k\ge2$ は **否定的に解決**（`prop:weak-not-preserved`、$s_0\preceq h_{\{@\}}$）。$k=1$ だけ OPEN | |
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

1. ~~別系列モデルによる独立監査~~（2026-11-24 実施、反例なし）。次は人間（金澤先生・吉仲先生）に見せる前の整理。
2. ~~KY2023 の EXREG パラメータとの照合~~（rev2 で `rem:exreg` を具体化）。
3. ~~KY2017 の定理・補題番号、$L_2$ の不等号、命題 6.5 の引用関係を原典照合~~（2026-11-25、情報源04の著者稿により確認済み。Springer 最終刊行版本文との差分のみ未確認。下記追記参照）。
4. ~~`op:weak-fcp` の残り：$L^+$ に $s_0$ 型付きの weak FCP 文法を作る~~（2026-11-25、Astra の査読で解決）。残りは $k=1$。
6. ~~題名の変更~~（2026-11-24 実施）。
5. 量的な上界：$\mathrm{Primal}_{2,1}$ の特徴データを型付き厚さで抑えられるか。


## 2026-11-25 の番号の変更（TCS 査読者の観点での自己査読）

- 新しい定義 3.4（提示とその大きさ）。§2 に学習器の記法の段落。
- 旧 命題 3.3（KY Prop 1 の型付き版）は命題 6.1(a) の証明に組み込み、削除。
- 命題 3.5 は健全性だけを完全に証明（完全性の側は使わない）。
- 旧 系 5.7 と注意 5.8 は注意 5.7 にまとめた（証明なし、既知）。
- 旧 定理 6.1 は命題 6.1。旧 系 6.5 は本文の一文に。
- weak FCP の非単調性 `prop:weak-not-preserved` は命題 6.6 から **命題 6.5** に。

---

## 2026-11-25 追記：KY2017 の原典照合（ChatGPT）

対象原稿：`main.tex`（照合時 Git blob `bff1123e4a79ddde9b2485297f3d751711207ba7`）。資料：博士論文統合プロジェクト情報源04 `04_Residual_Structure_Canonical_CFGs_and_Strong_Learning_v3.pdf` 合本 pp.117–128（Kanazawa–Yoshinaka, *The Strong, Weak, and Very Weak Finite Context and Kernel Properties*, LATA 2017 の著者稿、原稿 pp.1–12）。刊行書誌：LNCS 10168, pp.77–88, DOI [10.1007/978-3-319-53733-7_5](https://doi.org/10.1007/978-3-319-53733-7_5)。

| 照合対象 | 合本ページ | 判定 |
|---|---|---|
| Proposition 1、Proposition 2 | 120–121 | 著者稿と一致 |
| Algorithms 1–2、Theorems 3–6 | 122–124 | 著者稿と一致 |
| $L_2,L_3$ の定義 | 124 | $L_2$ は $|w|_a\ge |w|_b$、$L_3$ は $|w|_a\le |w|_b$。現行原稿と一致 |
| Lemma 8 | 125–126 | 文法と使用する閉包等式を照合 |
| Proposition 10 | 126 | weak FKP と very weak FKP の言語クラスの同値 |
| Lemma 12 | 126–127 | very weak 2-FCP の構成と使用する等式を照合。weak 2-FCP の主張ではない |
| Lemma 13、Theorem 14 | 127 | weak FCP の不可能性と分離結果を照合 |

命題 6.5（`prop:weak-not-preserved`）について、Lemma 8・12 に由来する表の文法・文脈集合・閉包等式、および Lemma 13 の証明で得られる非終端記号 $D$ の性質を確認した。特に真の閉包から十分大きい $c^id^ie^i$ が排除される一方、任意の有限な共通文脈集合では十分大きい $c^id^ie^i$ を排除できないこと、これらの語と $a^m\$a^l$ が新標識 @ を含まない同じ非空ファイバーに属することを確認した。照合範囲で引用番号、定義、不等号、引用の用途に問題は見つからなかった。命題 6.5 全体の人間による独立証明監査とは区別する。

**状態：著者稿による数学的な原典照合は確認済み。** Springer 最終刊行版の書誌情報は確認済みだが、情報源04のPDFは冒頭に刊行予定と記された著者稿であり、最終刊行版本文との版間差分は未確認。刊行版を入手した際に追加照合することは望ましいが、今回の照合結果を踏まえ、それだけを理由に投稿を延期する必要はないと判断する。今回の作業は研究記録の更新であり、定理・証明・新規性判定の変更ではない。
