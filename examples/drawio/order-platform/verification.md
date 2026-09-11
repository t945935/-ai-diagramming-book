# draw.io 實際驗證紀錄

## 方法與結果

- XML 解析、ID 唯一及連線端點檢查通過。
- 使用 app.diagrams.net 載入的 EditorUi 31.4.5 建立測試編輯器，透過 setGraphXml 載入原始模型。
- 透過瀏覽器滑鼠事件拖曳 orders 節點，座標由 (560,160) 變成 (560,210)。
- e2、e3、e4 的 source／target 維持 web → orders、orders → payment、orders → db。
- 透過編輯器 cellLabelChanged 修改標籤，再序列化 XML 並重新載入，確認座標、文字與邊均保留。
- 測試後恢復原始模型，以編輯器 getSvg 匯出 SVG。
- Chrome for Testing 151.0.7922.34 載入 SVG 並產生 PNG；沒有使用 draw.io PNG 匯出對話框。
- 圖像檢查：中文可讀、未見裁切或節點文字重疊；箭頭方向符合規格。連線標籤較擁擠、協定與動作標籤混用，正式版可再改善。

機器可讀拖曳與重新載入結果見 edit-verification.json。原始圖恢復初始狀態後才匯出，因此成品座標與測試移動後座標不同，這是刻意安排。

## 未驗證

GUI 檔案選擇器、另存新檔對話框、桌面版、其他瀏覽器、雲端儲存及乾淨環境重跑。無自動化 CI，不宣稱全平台通過。

## SHA-256

- order-platform.drawio：dc774bc35a3b7696c5b3f21864770110bec582fc0c3212364742b6ac714d5e6c
- order-platform.svg：125e72a1188201dd7dcfa7237dc3bf8e1de16011b2a3c1d22a237d93c6ee4644
- order-platform.png：a4c82992ef9d96662df66270ef99cdd05b411947ac6600b8fa948bcd831bd956
