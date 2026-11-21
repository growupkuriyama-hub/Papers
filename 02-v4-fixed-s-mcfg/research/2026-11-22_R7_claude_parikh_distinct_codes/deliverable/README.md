# R7：Parikh 差の異なる符号の決着（Claude Opus 5.5, 2026-11-22）

## 結論（3 行）

1. R6 の D3 の例 $\mathtt{ca^scb^{s^2}c}$ は、周期的な背骨でも Thue–Morse 宿主でも、$n=6$ で 3 段の証明書（C2 を 2 回、C1 を 1 回）で近道を強制する。二つの端の連の符号は、指数が単調なら $|W|\le4\ell\theta^2$ である（定理 E：端の walk のポテンシャルと鳩の巣）。Parikh 差が異なるかどうかは関係しない。
2. 中の連も段で変わる符号は、冪の移送または吸収（Parikh を保つ段）で錠が外れて倒れる（$n=6,7,8$ で証明書）。$\mathtt{ca^scb^{2^s}c}$ は、背骨では吸収で倒れ、Thue–Morse 宿主では端の walk の上で加法的で倒れない。この符号の厚さは指数的である。
3. 残るのは「錠のかかった剛い符号」で、移送の計算は閉じる（命題 F）。単一の逃げ道からの閉包は厳密に代入可能（rig, $n=5$, 104 語）。二つの逃げ道の段階と (D3) は OPEN。判断は否定に傾く（予想）。

ラベルはすべて報告者の自己判定。独立監査は受けていない。

## 中身

| ファイル | 内容 |
|---|---|
| `report.md` | 報告本体（読了表、T1・T2・T3、照合表、自己監査、次の義務） |
| `code/run_all.py` | 全ての有限検査（[A]〜[H]）。標準ライブラリのみ、ネットワーク不使用 |
| `code/run_all.log` | `run_all.py` の実際の出力（標準出力） |
| `code/long/run_long.sh`, `gen_one.py`, `r7lib.py`, `codes.py` | 上限 $|W|$ の一般の SUB 閉包（$n=6$、10 通り、予算 2 万語、各 600 秒）。`run_all.py` には入れていない |
| `code/long/gen_long.log` | その実際のログ |
| `SHA256SUMS.txt` | 上記全ファイルの sha256 |

## 再実行

```
cd code
python3 -I run_all.py > run_all.log      # 約 3 分（2 コア機で 167 秒）。終了コード 0
cd long
sh run_long.sh > gen_long.log            # 約 6 分。メモリを最大 4 GB 程度使う
```

`run_all.py` の出力は `PYTHONHASHSEED` によらない（`PYTHONHASHSEED=0` と `98765` でバイト単位で一致することを確かめた）。経過時間だけは標準エラーに出す。
