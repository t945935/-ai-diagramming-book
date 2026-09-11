# PlantUML 付款範例

[第 6 章](../../../docs/chapters/06-plantuml.md) · [需求](requirements.md) · [提示詞](../../../prompts/plantuml-payment.md) · [驗證](verification.md)

| 圖 | 原始碼 | SVG | PNG |
| --- | --- | --- | --- |
| 初次付款時序 | [puml](payment-sequence.puml) | [SVG](payment-sequence.svg) | [PNG](payment-sequence.png) |
| 訂單付款狀態 | [puml](order-state.puml) | [SVG](order-state.svg) | [PNG](order-state.png) |
| 付款紀錄概念類別 | [puml](payment-model.puml) | [SVG](payment-model.svg) | [PNG](payment-model.png) |

## 重現

使用 Java 及 PlantUML 1.2026.8。本次 Java 是 Temurin 21.0.12.1+1，中文使用 Noto Sans CJK TC。Java、JAR 與字型均未隨庫分發。

官方下載：https://github.com/plantuml/plantuml/releases/tag/v1.2026.8

在 Repo 根目錄執行，下方 JAR 路徑須換成自己的實際路徑：

```sh
java -Djava.awt.headless=true -DPLANTUML_SECURITY_PROFILE=SANDBOX -jar /path/to/plantuml-1.2026.8.jar -charset UTF-8 -checkonly "examples/plantuml/payment/*.puml"
java -Djava.awt.headless=true -DPLANTUML_SECURITY_PROFILE=SANDBOX -jar /path/to/plantuml-1.2026.8.jar -charset UTF-8 -tsvg -failfast2 "examples/plantuml/payment/*.puml"
java -Djava.awt.headless=true -DPLANTUML_SECURITY_PROFILE=SANDBOX -jar /path/to/plantuml-1.2026.8.jar -charset UTF-8 -tpng -failfast2 "examples/plantuml/payment/*.puml"
```

本次沒有 Graphviz，狀態及類別圖以來源中的 Smetana 設定渲染。若使用其他版本或引擎，輸出佈局可能不同。

`.puml` 是維護來源，修改後重建 SVG 與 PNG。執行成功後也要檢查圖片，不能把錯誤訊息圖當成成功結果。

## 邊界

沒有執行扣款程式。本例只重試查詢，不重試扣款。自動查詢最多三次是教學假設，不代表建議的實際支付策略。跨平台、乾淨環境及 CI 未驗證。
