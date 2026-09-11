# 範例交付標準

目前可試用 [Mermaid 訂單流程](mermaid/order-flow/README.md)：已完成本機渲染、需求與視覺走查，限制詳見範例驗證紀錄。另有 [draw.io 可編輯架構試作](drawio/order-platform/README.md)，已驗證拖曳與模型重新載入；另有 [D2 架構範例](d2/order-platform/README.md)，已驗證 dagre 佈局及 SVG／PNG 匯出；其餘工具仍為規劃中，尚無正式隨書 Release。

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
