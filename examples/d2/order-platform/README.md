# D2 訂單平台架構

[第 5 章](../../../docs/chapters/05-d2.md) · [需求規格](requirements.md) · [提示詞](../../../prompts/d2-order-platform.md) · [驗證](verification.md)

![D2 平台架構](order-platform.svg)

[原始 D2](order-platform.d2)／[PNG](order-platform.png)

## 重現

本次版本是 D2 v0.9.0，佈局為 dagre。從 https://github.com/d2lang/d2/releases/tag/v0.9.0 取得符合自己系統的版本，執行 `d2 version` 確認。

本例字型來自 https://github.com/notofonts/noto-cjk ，路徑為 Sans/Variable/TTF/Subset/NotoSansTC-VF.ttf；字型未隨庫發布。使用自己的本機字型路徑，並核對 verification.md 的 SHA-256 可確認是否與本次相同。

在 Repo 根目錄執行（下例為類 Unix shell）：

```sh
d2 validate examples/d2/order-platform/order-platform.d2
d2 fmt --check examples/d2/order-platform/order-platform.d2
FONT=/absolute/path/to/NotoSansTC-VF.ttf
d2 --layout=dagre --font-regular="$FONT" --font-bold="$FONT" examples/d2/order-platform/order-platform.d2 examples/d2/order-platform/order-platform.svg
d2 --layout=dagre --font-regular="$FONT" --font-bold="$FONT" examples/d2/order-platform/order-platform.d2 examples/d2/order-platform/order-platform.png
```

Windows 使用對應執行檔及自己的字型路徑；未測試 Windows。PNG 匯出可能需要瀏覽器相依，依工具錯誤訊息及官方安裝文件處理，不以停用安全機制當作預設修復。

本例不需要根目錄 Mermaid 的 npm 套件。`.d2` 是維護來源，修改後重新產生兩種預覽。

## 已知限制

付款標籤較靠近容器底邊，連線文字偏細；正式紙本仍需排版檢查。只驗證 dagre、當前 Linux／WSL 環境，未執行跨平台或 CI。
