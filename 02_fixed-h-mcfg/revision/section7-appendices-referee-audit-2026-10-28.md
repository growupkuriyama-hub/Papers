# §7・Appendices 数学的再査読 — 2026-10-28

## 対象
`02_fixed-h-mcfg/main.tex` / `japanese/main_JP.tex`、特にConclusion (§7) と Appendix（有限群同時置換・局所群・pattern thickness・質的再構成・型付き証拠・good正規化）。2026-10-27 PR #92 での大幅短縮・明示化を基準に、本文§4–§6での使用箇所まで遡った。これは機械形式化による全証明検証ではない。

## 確定した修正と重要度

1. **§7 Open Problem — Major editorial / mathematical quantification.** 後半の「U1 が超多項式の特徴データを強制するか」は、(a) 対象作用素、(b) 固定ファンアウトとランク、(c) 文法サイズと厚さに対する下界、(d) 全特徴標本に対する量化を省略していた。正語像U1の固定型付け `s`、固定 `f,r_max≥2`、`||G_n|| bar(theta_Gn) = n^{O(1)}` の族、`B^{≤r_max}_{f,s}` の**全て**の特徴標本に `n^{ω(1)}` の下界、という正確な問いに改訂。作用素固有の下界と全学習器に共通の下界を区別。前半の存在上界との量化の対照を明確化。
2. **Appendix A: group interval — Minor proof exposition.** 非可換群の区間選択では同じ固定定数を原値と置換値の両方に同順で含める必要がある。領域の前後・チャンク間の定数をどのチャンクに吸収するかを明記し、`P_p Q_p^{-1}` の境界状態と `P_p (Q_p^{-1}Q_p') (P_p'^{-1}P_n)` の等式の読みを正確化。証明の代数的式や定数 `M_{A,f}` は変更していない。

## 独立の証明点検

- **Appendix A (Simultaneous replacement):** 非可換の群積を交換せず、順序の同質化・領域分解・増減方向に沿う境界状態の同時衝突を用いる構成を点検。限界幅 `q ≤ f`、境界状態数 `|A|^q` と `n+1>|A|^q`、所有者パターン `U_f` と多段抽出 `N^{2^{f^2}}` の伝播を確認。三置換例の `S_3` で元・置換後の二列の積がともに単位元であることを独立に計算した（`(12),(23)` を置換として合成）。
- **Appendix B (§`app:window-group`):** order-homogenization の単調二次元真偽行列の分岐 `X(i,j)` と領域分解を追跡。引数の全ケースを別形式証明として検証したわけではない。
- **Appendix C (Local-group coordinates):** 短語を正確に区別する `s_{k,k}`、長語のordered sliding-factor product、Rees matrix座標の右作用、ブロック分解を照合。有限半群の `S^{|S|}=SE(S)S` はAlmeida–Margolis–Steinberg–Volkov, Lemma 2.2に対応し、Pin の有限半群の補題とも整合。正語像に対するLGと、空語を分離する新単位元添加の区別は維持。
- **Appendix D (Pattern transfer):** `π_J,σ,μ` は総長非増加、supportは元supportから決まり、stage(c)の各非空support fibreごとに短い代表を転送する論証を照合。`θ_H` や通常の `t_H` だけでは足りない点を維持。
- **Appendix E (Qualitative reconstruction):** Const/Link/Comp 健全性・完全性、開始規則の `ε` と非空語の分岐、Gold-style conservative updatingを本文§3と照合。個々のcanonical tupleが元のtyped非終端から導出可能でない場合の使用条件も確認。
- **Appendix F (Typed witness):** 型ラベルの一意の持ち上げ、有限モノイド実装の比較が**good MCFG**に限定される点（空成分を許す一般MCFGでは一致しない）を再確認。
- **Appendix G (Normalization):** 非消去→非置換→support別非空化→非融合の順序、それぞれのタプル言語の像恒等式、rank/fan-outを増やさないことと固定 `f,r` のサイズ増加を照合。例 `E_n` が `t_{pat}` と元 `θ` の指数分離を与えることを確認。

## 編集上の優先順位

- 上述の§7の量化精密化が、今回の投稿前修正として最も実質的。数学的主定理を変更しない。
- 非可換群の全ての順序分類ケース、標準MCFGからgood MCFGへの任意テンプレートの変換、外部文献の全補題を形式的に検証したという主張はしない。ビルド・ラベル整合性は証明の正しさを保証しない。
- 精密化厚さのLG必要十分条件は**特徴データ下界**ではない。明示したopen problemの作用素と量化を混同しない。
- 先行TCSコンパニオンの下界を本論文の独創的下界として復活させない。

## 外部参考
- J. Almeida, S. Margolis, B. Steinberg, M. Volkov, *Representation Theory of Finite Semigroups, Semigroup Radicals and Formal Language Theory*, Proposition 2.3, Lemma 2.2: https://cmup.fc.up.pt/cmup/jalmeida/preprints/Last_Radical.pdf
- J.-É. Pin, *Mathematical Foundations of Automata Theory*, finite-semigroup pumping lemma and Corollary 5.5: https://citeseerx.ist.psu.edu/document?doi=2ace0c8422f2a25debf94e5c7219ffb8b7849c26&repid=rep1&type=pdf
