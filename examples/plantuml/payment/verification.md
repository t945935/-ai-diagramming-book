# PlantUML 本機驗證紀錄

## 工具

PlantUML 1.2026.8（149874a）、Temurin JRE 21.0.12.1+1、Linux／WSL x86_64、Noto Sans CJK TC。使用 headless=true 及 PLANTUML_SECURITY_PROFILE=SANDBOX，沒有載入外部 include。

JAR SHA-256：5e1ecfa8ecd32c90b03bbf3b1eb6f020943f98ab0fcf4032be31a0002ee2c462

JRE 下載壓縮包 SHA-256：2413149700df0f7d440500a84a8f764c535f21e5a5e87d38328b64eec2c5b500

兩者與 GitHub 官方 release asset API 的 digest 一致；不等同額外驗證簽章。

## 實際執行

依 README 的 -checkonly、-tsvg -failfast2、-tpng -failfast2 命令執行三份 puml，三階段退出碼均為 0。維護者使用的 Java 及 JAR 絕對路徑在 /home/j5/.local/share/diagram-tools/ 下；未隨庫分發。

狀態圖調整後再次執行 SVG／PNG 匯出，均 exit 0。已確認三份 SVG 為可解析 SVG XML、三份 PNG 具有 PNG 檔頭，並檢查全部 PNG 圖像。成品指紋見 artifacts.json。

本機沒有 Graphviz；版本資訊顯示 Dot 缺失的一般警告，但狀態與類別來源明確指定 Smetana，實際成功產生圖。

## 語意及視覺走查

- 時序：三個 alt 分支可辨識，逾時為 API 自身觀察，沒有支付服務假回覆；中文完整、未見裁切。長分支條件略靠近生命線。
- 狀態：初版自迴圈文字與註解引線擁擠。縮短條件、將 n 與計數規則移至圖例後重新渲染，第二次檢查無明顯字線重疊；右側長標籤仍較貼邊。
- 類別：中文及 0..1、0..3 基數清楚，沒有明顯裁切或重疊。
- 跨圖：成功／失敗／未知分流、一次付款請求、三次自動查詢與需求一致。第三次已確認結果仍走成功或失敗，不走人工。

## 未測

Java／JAR 的跨平台安裝、CI、其他佈局、真實付款、資料庫鎖與補償。沒有聲稱支付功能或程式單元測試通過。圖檔是教學文件，不能單憑通過渲染作為生產上線依據。
