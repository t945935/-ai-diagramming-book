# 跨工具變更影響與既有來源快照

本章只新增 Mermaid 受理圖與 PlantUML 退款狀態圖，不修改原付款案例。所有「不改」都基於本章不新增服務／模組邊界的假設。

| 工具 | 判定 | 理由 |
| --- | --- | --- |
| Mermaid | 新增獨立來源 | 部分退款不是初次付款分支 |
| PlantUML | 新增獨立退款狀態 | 舊付款紀錄與退款紀錄不能混為同一狀態機 |
| D2 | 暫不改 | 本例未新增服務角色；不代表已繪出退款呼叫細節 |
| Graphviz | 暫不改 | 既有 refund→payment；未提供新的依賴 |
| draw.io | 暫不改 | 原同步總覽已明示退款另圖處理 |
| Excalidraw | 保留舊白板 | 不把新章範圍回填成舊工作坊已批准 |

以下 SHA-256 記錄本次交付的既有來源版本；其中先前跨工具對照保存的八份來源已再次比對未變。這不是全庫或全部原圖清單，也不涵蓋所有預覽。

| 來源（Repo 相對路徑） | SHA-256 |
| --- | --- |
| examples/mermaid/order-flow/order-flow.mmd | 70a4486ebaf4dff42a64fcbef30201f2c114438f91738b0df28611e4439f3fb9 |
| examples/d2/order-platform/order-platform.d2 | b799cba8082ef822de5634f379449f9ac6009d511b789847ad351bd8fb9b33be |
| examples/plantuml/payment/payment-sequence.puml | 0a8a270806298a2af3a44dae5b5561632f7034152a94e7a6d71b741b24fa13da |
| examples/plantuml/payment/order-state.puml | eb49b88b4b81a49d4e213946802772ee18700051c2ce44b5a8053ae48b9f77f7 |
| examples/drawio/order-platform/order-platform.drawio | dc774bc35a3b7696c5b3f21864770110bec582fc0c3212364742b6ac714d5e6c |
| examples/graphviz/dependencies/dependencies.json | 9d223ae26eafd205aa125efd1916c05032f522bb77494e4b893d99d29620b93f |
| scripts/graphviz_dependencies.py | 349711ca90dce089676a04265d9ee8250cc9adcb72b26cdadee9d558cb67c279 |
| examples/excalidraw/requirements-board/requirements-board.excalidraw | ac17c0ae0a08ead017b8a8fec08940b482df76afbab215152a8c471f9642bf62 |
| examples/plantuml/payment/payment-model.puml | c355580d32a45dca490a8d896c922afe29abb57ee1d06ed6c18788134a76d560 |
