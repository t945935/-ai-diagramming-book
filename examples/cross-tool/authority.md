# 權威來源與產物

需求的已確認狀態優先於圖，教學假設不得偽裝成真實需求。以下是本庫案例的來源規則，不是每套工具唯一的使用方式。

| 視圖 | 可維護來源（相對 Repo 根目錄） | 衍生產物 | 保留的特殊資訊 |
| --- | --- | --- | --- |
| 訂單流程 | examples/mermaid/order-flow/order-flow.mmd | 同目錄 SVG／PNG | 分支與例外 |
| 服務架構 | examples/d2/order-platform/order-platform.d2 | 同目錄 SVG／PNG | 容器與佈局來源 |
| 付款模型 | examples/plantuml/payment/*.puml | 各圖 SVG／PNG | 時序、狀態、概念類別與假設 |
| 模組依賴 | examples/graphviz/dependencies/dependencies.json + scripts/graphviz_dependencies.py | generated/ 的 DOT／JSON／SVG／PNG | consumer→dependency，反向影響算法 |
| 人工交接圖 | examples/drawio/order-platform/order-platform.drawio | 同目錄 SVG／PNG | 位置、模型端點綁定 |
| 需求白板 | examples/excalidraw/requirements-board/requirements-board.excalidraw + decisions.md | 同目錄 SVG／PNG | 便條群組、分類、決策依據 |

八份來源指紋是本章對照快照，不包含表內每一份相關文件；不是全庫完整性清單。標準工具版本、字型與渲染設定另見各章驗證文件。

變更流程：確認規則及影響範圍 → 修改該視圖權威來源 → 重產受影響預覽 → 契約及視覺檢查 → 必要時真實編輯／保存／重開 → 更新對照和驗證紀錄。

原始檔與衍生產物若衝突，先查生成鏈與版本，不憑檔案修改時間自行指定新權威。不要只修 PNG 後宣稱源碼已同步。
