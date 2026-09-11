# Graphviz 依賴總覽與付款影響子圖

[第 7 章](../../../docs/chapters/07-graphviz.md) · [資料](dependencies.json) · [提示詞](../../../prompts/graphviz-dependencies.md) · [驗證](verification.md)

此為虛構模組清單，不是對真實程式庫的掃描。A → B 代表 A 依賴 B，影響分析反向追蹤；結果只是潛在檢查範圍。

| 視圖 | DOT | SVG | PNG |
| --- | --- | --- | --- |
| 總覽 | [DOT](generated/overview.dot) | [SVG](generated/overview.svg) | [PNG](generated/overview.png) |
| 付款影響 | [DOT](generated/impact.dot) | [SVG](generated/impact.svg) | [PNG](generated/impact.png) |

## 執行

需要 Python 3 與 Graphviz，中文需 Noto Sans CJK TC。本次 Python 3.12.3，dot 回報 2.43.0；不需要 npm 套件。

在根目錄執行：

```sh
python3 -m unittest discover -s tests -p 'test_graphviz_generator.py' -v
python3 scripts/graphviz_dependencies.py examples/graphviz/dependencies/dependencies.json examples/graphviz/dependencies/generated --changed payment
dot -Tsvg examples/graphviz/dependencies/generated/overview.dot -o examples/graphviz/dependencies/generated/overview.svg
dot -Tpng examples/graphviz/dependencies/generated/overview.dot -o examples/graphviz/dependencies/generated/overview.png
dot -Tsvg examples/graphviz/dependencies/generated/impact.dot -o examples/graphviz/dependencies/generated/impact.svg
dot -Tpng examples/graphviz/dependencies/generated/impact.dot -o examples/graphviz/dependencies/generated/impact.png
```

來源是 dependencies.json 與產圖程式；不要手改生成 DOT 再期待 JSON 重跑保留修改。程式覆寫 overview.dot、impact.dot、impact.json，請使用專用輸出目錄。

## 資料與驗收

總覽 16 節點、17 邊；付款子圖 9 節點、10 邊。結果清單見 [impact.json](generated/impact.json)。訂單／發票循環是刻意設計的資料；程式會避免重複走訪，沒有計算或列出全部循環群組。

總覽中央有交叉線，局部子圖較清楚。已確認中文、圖例可讀且未裁切。尚未測試大型效能、跨平台或 CI。
