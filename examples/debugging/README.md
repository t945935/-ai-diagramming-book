# 可重現的繪圖除錯室

四組刻意製造的教學反例。不是六套工具的完整測試，也不是歷史事故原檔。

## 案例清單

| 問題 | 反例 | 修正版 | 預期 |
| --- | --- | --- | --- |
| Mermaid 缺括號 | [broken.mmd](mermaid/broken.mmd) | [fixed.mmd](mermaid/fixed.mmd) | Parse error → 成功 |
| DOT 缺目的端 | [broken.dot](dot/broken.dot) | [fixed.dot](dot/fixed.dot) | syntax error → 成功 |
| 依賴方向與需求相反 | [broken.json](direction/broken.json) | [fixed.json](direction/fixed.json) | 兩者 exit 0，但只有 fixed 符合影響集合 |
| 邊端點拼錯 | [broken.json](endpoint/broken.json) | [fixed.json](endpoint/fixed.json) | 拒絕且不建輸出 → 成功 |

- [第 10 章](../../docs/chapters/10-debugging.md)／[提示詞](../../prompts/diagram-debugging.md)
- [完整實測輸出](results.json)／[測試輸出](test-output.txt)／[驗證與限制](verification.md)
- [除錯紀錄模板](debug-report-template.md)
- Mermaid 修正版：[SVG](generated/mermaid-fixed.svg)／[PNG](generated/mermaid-fixed.png)
- DOT 修正版：[SVG](generated/dot-fixed.svg)／[PNG](generated/dot-fixed.png)

## 準備環境

需要 Python 3、Node.js、專案 lockfile 的 Mermaid CLI、可用 Chromium 以及 Graphviz `dot`。本次版本見 results.json。先依 [Mermaid 範例](../mermaid/order-flow/README.md) 設定瀏覽器，依 [Graphviz 範例](../graphviz/dependencies/README.md) 安裝 dot。

以下在儲存庫根目錄執行，不需安裝新的 Python 套件。非系統安裝的 dot 可用環境變數 `DOT` 指定完整執行檔路徑；仍須自行設定該安裝需要的動態函式庫和外掛環境。`MMDC` 可覆寫 Mermaid CLI 路徑。`PUPPETEER_CONFIG` 可指定自己的 JSON 設定檔；預設不添加 `-p`。

```sh
python3 -m unittest discover -s tests -p 'test_debugging_lab.py' -v
python3 -m unittest discover -s tests -v
```

缺少工具會報錯，不會略過後聲稱全部通過。測試會真實啟動渲染器，產物放在隔離暫存目錄並於完成後清除，不覆寫既有章節成品。

## 單獨重現

Mermaid：依自身環境在以下命令加上 `-p <你的設定檔>`。broken 預期失敗，不要用 `&&` 將它和修正版串成「失敗就停止」的批次。

```sh
./node_modules/.bin/mmdc -i examples/debugging/mermaid/broken.mmd -o /tmp/debug-broken.svg
./node_modules/.bin/mmdc -i examples/debugging/mermaid/fixed.mmd -o /tmp/debug-fixed.svg

dot -Tsvg examples/debugging/dot/broken.dot -o /tmp/dot-broken.svg
dot -Tsvg examples/debugging/dot/fixed.dot -o /tmp/dot-fixed.svg

python3 scripts/graphviz_dependencies.py examples/debugging/direction/broken.json /tmp/direction-broken --changed payment
python3 scripts/graphviz_dependencies.py examples/debugging/direction/fixed.json /tmp/direction-fixed --changed payment

python3 scripts/graphviz_dependencies.py examples/debugging/endpoint/broken.json /tmp/endpoint-broken --changed payment
python3 scripts/graphviz_dependencies.py examples/debugging/endpoint/fixed.json /tmp/endpoint-fixed --changed payment
```

以上為 POSIX 示範，Windows 請替換暫存路徑與 CLI 啟動方式，尚未驗證 Windows。單獨重現請使用自己新建的輸出目錄／檔名，不覆寫有用資料。results.json 的絕對路徑是維護者當時執行紀錄，不是可原樣複製的跨機器設定。

方向案例的需求：web 依賴 order，order 依賴 payment。修改 payment 時，期望潛在檢查清單為 order、payment、web；不是沿箭頭前進。查看兩個輸出目錄的 impact.json 即可比較。
