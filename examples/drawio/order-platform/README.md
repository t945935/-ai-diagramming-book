# draw.io 平台架構：可編輯性試作

[第 8 章擴寫樣章](../../../docs/chapters/08-drawio.md) · [提示詞](../../../prompts/drawio-order-platform.md) · [驗證紀錄](verification.md)

![預覽](order-platform.svg)

- 原始檔：[order-platform.drawio](order-platform.drawio)
- 預覽：[SVG](order-platform.svg)／[PNG](order-platform.png)
- 機器可讀編輯測試：[edit-verification.json](edit-verification.json)

## 開啟與練習

下載原始 `.drawio`，到 https://app.diagrams.net/ 選 File → Open From → Device。拖動「訂單 API」，確認三條連線跟隨；修改標籤，另存副本後重新開啟。

本例已驗證真實編輯器內的滑鼠拖曳、API 標籤修改、XML 序列化重新載入與 SVG 匯出。GUI 檔案選擇／儲存、桌面版與跨平台尚未逐一測試。未提供自動化 CLI，使用本例不需安裝根目錄的 Mermaid npm 工具。

## 元件與連線規格

| ID | 元件 | 角色 |
| --- | --- | --- |
| client | 使用者瀏覽器 | 存取前端 |
| web | Web 前端 | 呼叫建立訂單 API |
| orders | 訂單 API | 呼叫支付服務及讀寫訂單資料 |
| payment | 外部支付服務 | 外部依賴 |
| db | 訂單資料庫 | 保存訂單 |

連線：client → web、web → orders、orders → payment、orders → db。箭頭表示呼叫，不表示時間順序，回應省略。其他模組與失敗處理不在本圖範圍。

`.drawio` 是維護來源，預覽不包含可編輯原生資料的保證。正式交接請同時提供原始檔。使用 Noto Sans CJK TC 顯示本次中文，字型未隨庫提供。
