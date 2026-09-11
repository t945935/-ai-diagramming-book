# 部分退款綜合案例

虛構需求變更，沒有真實退款 API 或資料庫實作。

- [第 13 章](../../docs/chapters/13-refund-project.md)
- [需求單](requirements.md)／[跨工具影響與來源指紋](change-impact.md)
- [Mermaid 原始檔](refund-flow.mmd)／[SVG](refund-flow.svg)／[PNG](refund-flow.png)
- [PlantUML 原始檔](refund-state.puml)／[SVG](refund-state.svg)／[PNG](refund-state.png)
- [AI 提示詞](../../prompts/partial-refund.md)
- [六個額度與四個狀態快照](scenarios.json)
- [規格故障注入證據](test-evidence.json)／[實際渲染結果](render-results.json)
- [測試集合結果](suite-output.txt)／[驗證限制](verification.md)／[產物指紋](checksums.json)

## 重跑

在 Repo 根目錄，以 Python 3 執行：

```sh
python3 -m unittest discover -s tests -p 'test_refund_change.py' -v
make check-core
```

目前核心為六個測試方法；完整集合十個另用 make check-full，需準備第 10 章的渲染器。不要設定 REFUND_SCENARIOS 或 BOOK_SOURCE_ROOT，除非刻意測試隔離副本。

Mermaid 使用既有專案 CLI，按本機 Chromium 情況添加 `-p`：

```sh
./node_modules/.bin/mmdc -i examples/refund-change/refund-flow.mmd -o examples/refund-change/refund-flow.svg
./node_modules/.bin/mmdc -i examples/refund-change/refund-flow.mmd -o examples/refund-change/refund-flow.png
```

PlantUML 依第 6 章安裝 Java 與 JAR。下面 `$PLANTUML_JAR` 要先設定為自己的 JAR 路徑：

```sh
java -Djava.awt.headless=true -DPLANTUML_SECURITY_PROFILE=SANDBOX -jar "$PLANTUML_JAR" -charset UTF-8 -checkonly -failfast2 examples/refund-change/refund-state.puml
java -Djava.awt.headless=true -DPLANTUML_SECURITY_PROFILE=SANDBOX -jar "$PLANTUML_JAR" -charset UTF-8 -tsvg -failfast2 examples/refund-change/refund-state.puml
java -Djava.awt.headless=true -DPLANTUML_SECURITY_PROFILE=SANDBOX -jar "$PLANTUML_JAR" -charset UTF-8 -tpng -failfast2 examples/refund-change/refund-state.puml
```

以上是 POSIX 指令示例；跨平台安裝未驗證。匯出會覆寫本案例預覽，先保存自己的修改。既有付款範例不受影響。
