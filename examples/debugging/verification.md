# 第 10 章實測紀錄

日期：2026-09-11。Linux／WSL；Python 3.12.3、Node.js v24.21.0、Mermaid CLI 11.17.0、Graphviz dot 2.43.0。沿用既有 Chromium 設定與套件 lockfile，未做乾淨安裝。

## 本次實際執行

四組教學案例，各執行反例與修正版：

| 案例 | broken 退出碼 | fixed 退出碼 | 核心觀察 |
| --- | --- | --- | --- |
| Mermaid 括號 | 1 | 0 | 反例 Parse error on line 2 |
| DOT 目的端 | 1 | 0 | 反例 syntax error in line 2 near ';' |
| 依賴方向 | 0 | 0 | 反例只得到 payment；修正版 order、payment、web |
| 未知端點 | 2 | 0 | 反例拒絕未知節點；修正版 order、payment |

完整命令、stdout、stderr、影響清單與工具版本讀回見 results.json。其暫存路徑已隨測試清除，不能當作下載位置。

執行 `python3 -m unittest discover -s tests -v`，七個測試方法通過，沒有略過項目。其中本章新增四個，既有 Graphviz 三個。測試輸出保存於 test-output.txt。測試針對現有渲染器與產圖 CLI 加反例，沒有修改產圖器的實作，也不宣稱新增了通用圖意驗證器。

Mermaid 與 DOT 修正版的 SVG／PNG 均由各自真實 CLI 匯出。SVG 可解析，PNG 檔頭有效；視覺檢查兩張 PNG，未見明顯文字重疊或裁切，Mermaid 繁中可讀。DOT 圖採最小英文 ID，不能拿它證明 DOT 中文字型通過。成品 SHA-256 見 checksums.json。

## 本次未重新執行

D2、PlantUML、draw.io、Excalidraw 的歷史問題在章內連結各自驗證紀錄。本章沒有重新操作這四個工具，不將它們計入七個自動測試。

## 限制

- 沒有 Windows／macOS、CI、乾淨安裝或印刷尺寸驗證。
- 所有需求與資料為教學案例，不是真實金流測試。
- 錯誤訊息隨工具版本可能變動；測試採關鍵片語，沒有鎖定整段堆疊。
- 圖像完整不表示所有讀者都能正確理解；DOT 依賴語意須看章內說明。
- 沒有執行字型缺失、截斷匯出及未綁定便條的自動故障注入；這些仍是人工檢查項。
