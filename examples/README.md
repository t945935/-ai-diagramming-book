# 範例交付標準

目前可試用 [Mermaid 訂單流程](mermaid/order-flow/README.md)：已完成本機渲染、需求與視覺走查，限制詳見範例驗證紀錄。另有 [draw.io 可編輯架構試作](drawio/order-platform/README.md)，已驗證拖曳與模型重新載入；另有 [D2 架構範例](d2/order-platform/README.md)，已驗證 dagre 佈局及 SVG／PNG 匯出；另有 [PlantUML 三圖範例](plantuml/payment/README.md)，已完成語法與 SVG／PNG 渲染檢查；另有 [Graphviz 依賴分析](graphviz/dependencies/README.md)，含已測試的 JSON 產圖程式及影響子圖；另有 [Excalidraw 需求白板](excalidraw/requirements-board/README.md)，已驗證場景匯入、拖曳、瀏覽器重載及影像匯出，尚無正式隨書 Release。

另有 [第 10 章除錯實驗室](debugging/README.md)：四組刻意製造的反例與修正版，含真實 CLI 輸出及回歸測試。

每個範例需要：

- 對應章節、工作情境、需求來源及明確假設。
- AI 提示詞與可編輯原始檔。
- 工具／渲染器版本、字型、作業系統與操作方式。
- 匯出圖及需求對照檢查。
- 實際執行結果、已知限制與驗證狀態。
- 練習與參考修正（如適用）。

Mermaid 使用 .mmd，D2 使用 .d2，PlantUML 使用 .puml，Graphviz 使用 .dot，draw.io 使用 .drawio，Excalidraw 使用 .excalidraw。

## 驗證狀態

- 草稿：尚未實際驗證。
- 可渲染／可開啟：語法或檔案格式檢查通過，不代表語意與視覺通過。
- 已驗證：完成需求對照與視覺檢查，並記錄環境與結果。

圖形編輯器的 JSON／XML 能解析，不代表已確認可編輯；必須實際匯入或開啟。
