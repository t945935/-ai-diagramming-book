# 需求與工具間對照

虛構案例，箭頭表示呼叫，回應省略，不表示時間順序。

| 需求 | D2 路徑／連線 |
| --- | --- |
| 使用者端在平台外 | client |
| 前端、訂單 API、資料庫屬平台管理範圍 | platform.web、platform.orders、platform.db |
| 支付屬外部服務 | external.payment |
| 使用者開啟前端頁面 | client → platform.web |
| 前端要求建立訂單 | platform.web → platform.orders |
| API 請求支付 | platform.orders → external.payment |
| API 讀寫訂單 | platform.orders → platform.db |

與 draw.io 範例使用相同業務元件及邊。本圖增加管理範圍容器，第一條邊標籤從 HTTPS 改為「開啟頁面」，統一描述動作；不改變協定要求，也不新增元件。

容器不是部署、網路或安全隔離保證。建單、寫入與付款的精確順序，退款、回呼、庫存、客服、失敗補償與冪等均未在本圖定義。
