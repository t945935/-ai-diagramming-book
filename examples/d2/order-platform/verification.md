# D2 本機驗證紀錄

## 環境與實際命令

- Linux／WSL，x86_64。
- 官方 release 的 d2-v0.9.0-linux-amd64.tar.gz；執行 `d2 version` 回傳 v0.9.0。
- 佈局明確指定 dagre，未測其他引擎。
- 字型 NotoSansTC-VF.ttf 同時用於 --font-regular 及 --font-bold；未隨庫分發。

```sh
d2 validate examples/d2/order-platform/order-platform.d2
d2 fmt --check examples/d2/order-platform/order-platform.d2
d2 --layout=dagre --font-regular=/home/j5/.local/share/fonts/NotoSansTC-VF.ttf --font-bold=/home/j5/.local/share/fonts/NotoSansTC-VF.ttf examples/d2/order-platform/order-platform.d2 examples/d2/order-platform/order-platform.svg
d2 --layout=dagre --font-regular=/home/j5/.local/share/fonts/NotoSansTC-VF.ttf --font-bold=/home/j5/.local/share/fonts/NotoSansTC-VF.ttf examples/d2/order-platform/order-platform.d2 examples/d2/order-platform/order-platform.png
```

validate 回傳 Success；fmt --check 退出碼 0；兩次匯出均回傳 successfully compiled，退出碼 0。這些是實際 CLI 執行結果，不是示意輸出。讀者須替換上方維護者本機字型路徑。

## 視覺與需求走查

PNG 中五個業務元件、兩個分組及四條呼叫可辨識，容器歸屬與需求一致；未見中文缺字、節點或容器裁切。

已知排版問題：付款標籤貼近平台底邊；連線標籤偏細且較低對比，縮圖需放大。箭頭與邊界穿越仍可追蹤，不宣稱已達紙本最終品質。

## 未測試

乾淨環境安裝、Windows／macOS、替代佈局引擎、CI、真實平台 API。此圖是文件，不是可執行系統模型。

## 指紋

官方下載網址：https://github.com/d2lang/d2/releases/download/v0.9.0/d2-v0.9.0-linux-amd64.tar.gz

下載壓縮包 SHA-256：5669ddc46b99e942cc96078f4a4e36d5e62103348f4c05179ede27802fdd87a9

字型 SHA-256：ac091cc8cd19e848202afc8fe6d3809b4526c8fdbdb4be82da20c4f785949591

上述為本機計算的重現指紋，沒有宣稱已驗證上游簽章。

- order-platform.d2 SHA-256：b799cba8082ef822de5634f379449f9ac6009d511b789847ad351bd8fb9b33be
- order-platform.svg SHA-256：914884eeda9846938a14d9ba1c027d3e2dc4dc52df20b48555dd3000f557082b
- order-platform.png SHA-256：a4bec77ddfc36727fed9433e28bc90f78932fa91627bdf8022b67ef949ef0d34
