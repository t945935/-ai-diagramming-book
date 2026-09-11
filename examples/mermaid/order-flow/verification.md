# 本機驗證紀錄

狀態：已完成本機 SVG／PNG 渲染與需求、視覺走查；尚未做乾淨環境安裝、跨平台或 GitHub Actions 驗證。樣章保留排版改善項目。

## 環境

- Linux／WSL；Node.js v24.21.0，npm 11.19.0。
- Mermaid CLI 11.17.0、Mermaid 11.17.2、Puppeteer 25.10.0（以根目錄 lockfile 固定）。
- Google Chrome for Testing 151.0.7922.34。
- Noto Sans CJK TC Regular；來源：https://github.com/notofonts/noto-cjk 。字型未隨 Repo 分發。
- 字型檔 SHA-256：dce08bd4fd91aa8aa76ed8fea4b694c2dfb8550f67871e326843212ddbeb88b4。

## 實際執行

在本庫根目錄執行 `npm install --ignore-scripts`，成功安裝；使用本機 Puppeteer 設定指向既有 Chrome，再執行：

```sh
npm run render:mermaid -- -p /home/j5/.hermes/mermaid-puppeteer.json
npm run render:mermaid:png -- -p /home/j5/.hermes/mermaid-puppeteer.json
npm audit
```

兩次渲染均 exit 0，輸出「Generating single mermaid chart」。npm audit 回報 0 已知漏洞；此結果僅代表執行當下的套件資料庫，不是安全保證。

上方設定檔是維護者本機路徑，沒有隨庫發布。讀者依 README 建立自己的設定，不應直接使用該路徑。

## 需求與視覺檢查

依 requirements.md 逐條對照 R1–R8，資料拒絕、預留失敗、付款前取消、成功、明確失敗及未知結果各自有出口。付款未知不流向失敗，也不直接釋放庫存。

PNG 經視覺檢查，繁體中文可辨識，未見缺字、裁切、文字重疊或混淆路徑。已知問題：整圖縮小時字體偏小；底部長標籤的自動換行較生硬。正式印刷前應拆圖或重新安排版面。

這是文件語意走查，沒有執行訂單或支付程式，沒有宣稱真實金流測試通過。

## 成品 SHA-256

- order-flow.mmd：70a4486ebaf4dff42a64fcbef30201f2c114438f91738b0df28611e4439f3fb9
- order-flow.svg：bda4e002c31a5a20f02f44602584710567eb955cce61c912dad30aff7994ad7f
- order-flow.png：f4383e3dc63a547d5248c249b1999524d56b5ac25ef90774fb5cc392457adf82

渲染器可能產生不同 SVG 識別碼；上述雜湊用於確認本次成品，不要求所有重跑逐位元相同。
