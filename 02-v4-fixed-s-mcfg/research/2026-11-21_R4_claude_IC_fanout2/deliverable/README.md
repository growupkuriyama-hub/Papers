# R4_claude_IC_fanout2_2026-11-21

Claude Opus 5.5 による R4（`op:fanout-two`、IC 路線）の報告一式。

## 中身
- `report.md` … 報告本体（日本語、§1 読了表〜§7 次の義務）
- `code/run_all.py` … 全有限検査（Python 3、標準ライブラリのみ、ネットワーク不使用）
- `code/run_all.log` … 実際の実行ログ
- `SHA256SUMS.txt` … 上記ファイルの sha256

## 結論（3 行）
1. T1（fan-out 2 で IC を破る族）は OPEN。T2(b) は文字どおりの形では REFUTED（Σ⁺ が反例）。
2. 定理 A（自己判定 VALID、`prop:pattern-thickness-transfer` に依存）：c_Σ の IC は、拡大アルファベット Γ_f(Σ)（f=2, |Σ|=3 で 9 文字）での希少型予想から従う。文脈長の制限はない。
3. 系 B：各 (f, r) で、SL の一様多項式データ ⇔ 全 c_Σ の希少型 ⇔ 全 c_Σ の IC。`op:fanout-two` は内容型付けの希少型問題に集約される。

## 再実行
```
cd code && python3 -I run_all.py > run_all.log; echo $?   # 0 になる。所要時間は約 6 秒
sha256sum -c SHA256SUMS.txt                               # 展開したディレクトリの最上位で実行
```
有限検査はすべて CERTIFIED FINITE であり、全称の主張は report.md の証明による。
