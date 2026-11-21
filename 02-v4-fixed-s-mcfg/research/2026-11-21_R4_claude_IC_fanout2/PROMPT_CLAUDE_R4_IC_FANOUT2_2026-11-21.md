# Claude 依頼 R4：fan-out 2 で IC は破れるか（Astra から引き継ぎ）— 2026-11-21

あなたは有限半群型付け付き MCFG の分布学習を研究する数学者です。研究者（論文の著者）の開問題 `op:fanout-two` を、別のモデル（ChatGPT「Astra」）が R1〜R3 の三ラウンド攻めてきました。今回からあなたが引き継ぎます。前任者の判定を鵜呑みにせず、自分で確かめながら進めてください。

**成果物は 1 つの .zip ファイルだけ**です（§6）。チャットの本文には、zip を渡すときの 5 行以内の要約だけを書いてください。

## 0. 資料（実際に開いて読むこと）

公開リポジトリ：https://github.com/growupkuriyama-hub/Papers （ブランチ `main`）。以下のパスはすべて `02-v4-fixed-s-mcfg/` 以下。生ファイルは `https://raw.githubusercontent.com/growupkuriyama-hub/Papers/main/02-v4-fixed-s-mcfg/<パス>` で取得できる。

1. `research/README.md`：再開後の研究台帳。最初に読む。
2. `research/2026-11-21_R3_astra_internal_class/`：R3 の報告 `astra_R3_internal_class_report_2026-11-21.md` と確認メモ `claude_check_R3_2026-11-21.md`
3. `research/2026-11-21_R1_astra_routeBprime/` と `research/2026-11-21_R2_astra_marker_slices/`：各ラウンドの報告と確認メモ
4. `main.tex`（PDF は `main.pdf`、139 ページ）
   - 定義：`def:grammar-properties`, `def:tuple-substitutable`, `def:characteristic-sample`, `def:reconstruction`, `def:witness-set`, `def:uniform-polydata`
   - 結果：`lem:typed-homogeneity`, `thm:data-from-typed-thickness`, `cor:distribution-representatives`, `prop:sl-reduction`, `prop:rare-type`, `prop:typed-thickness-exponential`, `thm:two-letter-content`, `prop:three-letter-family`, `thm:doubling-no-lift`, `prop:full-content-types`, `prop:u1-weight-all-fanout`
   - 問題と予想：`op:fanout-two`, `conj:rare-types`
   - 第 IV 部：`sec:p4-ptree` と `sec:p4-resume-R1`〜`sec:p4-resume-R3`
5. `v2/reviews/PAUSE_FALSE_ROUTES_2026-11-16.md`：反証済みの推論。最初の段階で読むこと。

ネットワークから取得できない資料があれば、作業を始める前に研究者に添付を頼むこと。読めなかった資料は、報告の読了表に「未読」と明記すること。読んだふりは絶対にしない。

## 1. 問題と枠組み

**問題** `op:fanout-two`：f≥2, r_max≥2 を固定する。LG に含まれない擬多様体は、fan-out f・rank r_max で一様多項式特性データ長（`def:uniform-polydata`）を必ず持たないか。
- 十分性（LG に含まれる場合）は既に証明されている。
- `prop:sl-reduction` により、問題は内容型付け c_Σ の場合に帰着される。
- |Σ|=2 では一様多項式データがある。最小の未解決ケースは Σ={a,b,c}, f=2。

**枠組み（R3 で整理。まずあなた自身が原稿で確かめること）**
- 型付き非終端 X=A_m の意味クラスを C_X とし、τ_{C_X} をクラス内の最小総長とする。thickness 補題の文脈 E_A を使うと C_X={z : s(z)=m, E_A[z]∈L} と書ける。
- `cor:distribution-representatives` の τ(G,s) は max_X τ_{C_X} に等しい。
- **予想 IC**：固定の Σ, s, r_max に対して多項式 p があり、fan-out 2 のすべての標的とすべての提示 G について τ(G,s) ≤ p(‖G‖, θ̄_G)。ここで θ̄_G は**元**文法の厚さ。
- 帰結：
  - 全 Σ の c_Σ について IC が成り立てば、答えは**否定**。
  - 答えが**肯定**であるためには、fan-out 2 で IC が破れる族が**必要**。ただし十分ではなく、下界にはさらに標本でそのクラスを回避できないことが要る（R1 結果 `rr:R1-observation`）。
- 既知の事実：
  - IC は fan-out 1 では偽（R3 定理 1：P_n=T_n∖{W_n}）。ただし P_n は二穴 Rect に違反する。
  - 成分ごとの正の保存則があれば、IC はその X について成り立つ（R3 定理 2）。保存則がないことは条件 (5) と同値。
  - 倍増型の構成は R1 定理 2 と R2 定理 B で大きなクラスが排除されている。
  - マーカー切片の系（MS 系）：二つのコピーの間にマーカーがあると、切片に多数の語が要求される。

## 2. 課題

### T0. 枠組みの検証（短く）
§1 の帰結が原稿の定義と量化で本当に成り立つかを確認すること。特に `def:uniform-polydata` の量化の順序と、`prop:sl-reduction` の f, r_max の扱いに注意する。誤りがあれば最初に報告すること。

### T1. fan-out 2 で IC を破る族の構成（主課題）
Σ={a,b,c}（必要なら |Σ|≥4 でもよい）、s=c_Σ または s_U、f=2、r_max=2 で、次をすべて満たす族 (L_n, G_n) を作ること。

1. L_n∈C^{mcf}_{2,s}（全一穴・二穴 Rect）。
2. G_n は reduced good、fan-out ≤2、rank ≤2。‖G_n‖ と元厚さ θ̄_{G_n} は n の多項式。
3. ある X について τ_{C_X} が超多項式。C_X の全体を特定すること（t_X だけを評価してはいけない）。

設計上の制約：
- 全実現支持で (5) を満たす。
- MS 系と R2 定理 B を避ける。
- `thm:doubling-no-lift` を避ける。
- 族を作る前に、P_n がどこで二穴 Rect に違反したか（R3 §2）を分析し、その違反を避ける仕組みを言葉で説明すること。

### T2. 構成できない場合：IC の部分クラスでの証明
次のいずれか（または両方）を証明すること。
- (a) 明示した部分クラス（例：X が arity 2 で両成分が `c` なし）で、(5) と二穴 Rect が両立しない、またはそのとき τ_{C_X} が多項式で抑えられる。
- (b) R3 では仮定だった成分ごとの正の保存則を、二穴 Rect の帰結として導く。どの条件下で導けるかを明示すること。

### T3. 判断（一段落）
答えが肯定・否定のどちらに傾いていると考えるかを、根拠とともに述べること。予想であることは明記する。

**時間配分の目安**：T0 は短く。T1 と T2 に大半を使う。T1 で行き詰まったら、障害を記録して T2 に移ってよい。

## 3. 必須検査（違反した論証は無効）

- 型は穴ごとの**実際の文字内容**で決まる。意味クラスは型と分布で決まる。語全体の Parikh ベクトルの一致から、代入の合法性を導かない。
- 穴の語は非空、二穴の中央も非空。外側文脈は空でよい。3 つ目の穴を密かに追加しない。
- 各 Rect で、比較タプル x, y・成分ごとの型・共有文脈 E₀・試験文脈 E₁・四語をすべて書き出す。全 Rect の主張では、場合分けが網羅的であることを論証する。
- 文法についての主張では ‖G‖・**元**厚さ θ̄_G・reduced/good・fan-out/rank を明示する。
- 反証済みの R13 原文 X1、R14 原文 CA、R15 一般 IH、R2 の退化した短縮補題を前提にしない。小さい n の反例で大きい n の一般定理を反証しない。有限検査を全称証明と呼ばない。

## 4. 検証の作法

- 主張には VALID / CONDITIONAL（条件を明記）/ REFUTED / OPEN / CERTIFIED FINITE のいずれかを付ける。自己判定であることを明記する。
- 計算できるものはコードで確かめる。Python 3、標準ライブラリのみ、ネットワーク不使用、`python3 -I run_all.py` 一本で全検査が走り、終了コード 0 で終わる形にする。実行ログを保存する。
- 主要な定理には、自分で書いた証明を別の観点から一度読み直す「自己監査」節を付け、弱い箇所を正直に書く。

## 5. 報告の構成（`report.md`、日本語、数式は LaTeX）

1. 読了表（資料・読んだ範囲・未読）
2. T0 の結論
3. T1（または T2）の定理文・仮定・完全な証明または反例
4. T3 の判断
5. 既存結果（X1, CA, 一般 IH, doubling-no-lift, R1 定理 2, R2 定理 B・C, R3 定理 1・2）との照合表
6. 自己監査
7. 次の最小義務（3 項目以内）

## 6. 成果物：1 つの .zip のみ

ファイル名：`R4_claude_IC_fanout2_<YYYY-MM-DD>.zip`。中身は次の構成にすること。

```
R4_claude_IC_fanout2_<日付>/
  README.md        … 中身の一覧、結論 3 行、再実行コマンド
  report.md        … §5 の報告本体
  code/run_all.py  … 全有限検査（コードを使わなかった場合も、使わなかった旨を README に書く）
  code/run_all.log … 実際の実行ログ
  SHA256SUMS.txt   … 上記全ファイルの sha256
```

- zip 以外のファイルは渡さないこと。
- zip を渡す前に、自分で展開して `run_all.py` を実行し、`SHA256SUMS.txt` が一致することを確認すること。
- GitHub への反映は研究者側が行う。あなたは行わないこと。

途中で誤りに気づいたら、取り繕わずにその時点の結論を報告すること。「OPEN のまま、障害はここ」も正当な成果です。
