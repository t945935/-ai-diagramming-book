# 跨工具協作：對照與契約

- [第 11 章](../../docs/chapters/11-cross-tool.md)
- [概念對照與八份來源指紋](concept-map.json)
- [十個引用比對結果](mapping-verification.json)
- [權威來源表](authority.md)／[變更演練單](change-drill.md)
- [跨工具提示詞](../../prompts/cross-tool-handoff.md)
- [故障注入與正常來源測試輸出](contract-test-output.json)
- [驗證限制](verification.md)

這不是通用轉換器。對照表分開處理付款模組與外部支付服務，不以同名推定同一個物件。

## 重跑四邊契約

在儲存庫根目錄執行，需要 Python 3，無額外 Python 套件或渲染器：

```sh
python3 -m unittest discover -s tests -p 'test_cross_tool_contract.py' -v
```

它讀取既有 D2 與 draw.io 原始檔，比對呼叫端點，不驗證標籤、樣式或所有 D2 語法。只支援本例單行連線表示，不可當作正式 D2 解析器使用。

預期四條為 browser→web、web→order_api、order_api→external_payment、order_api→order_store。對照表與測試內的映射須經需求確認後維護。

測試預設以其所在儲存庫為來源。需要在隔離副本重現缺邊時，可用環境變數 `BOOK_SOURCE_ROOT` 指向保留相同相對路徑的副本，只刪副本中的 D2 資料庫邊；預期失敗。此變數不可用來讓正式來源的問題被另一份正常來源掩蓋。完成後取消設定。

正常案例一個測試方法通過；刻意刪邊副本同一方法失敗。結果見 contract-test-output.json。既有圖未修改；沒有在本章新做 GUI 編輯或格式轉換。
