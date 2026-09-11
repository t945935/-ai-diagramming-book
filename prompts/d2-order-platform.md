# D2 架構圖提示詞

根據 examples/d2/order-platform/requirements.md 生成 D2 架構圖，固定使用 direction: right。

使用 client、platform.web、platform.orders、platform.db、external.payment 這些業務節點 ID。platform 是平台管理範圍，external 是外部服務分組，不代表容器化部署。

只畫規格的四條呼叫，回應省略。所有標籤用繁體中文，邊標籤以動作描述，不擅自補出快取、佇列或微服務。資料庫使用 cylinder 形狀。

先宣告全部元件，再畫連線，避免拼字錯誤產生隱含節點。不重複宣告同一條邊；D2 重複連線可能變成多條連線，不是覆寫。

交付 .d2 原始碼、元件／邊對照及驗證清單。檢查 validate、fmt、SVG／PNG 渲染、容器歸屬與中文字型。未實際執行的步驟標示未驗證。

需要修改時保留既有 ID，只更動指定標籤或關係。不能將重新排版視為改變管理範圍的理由。
