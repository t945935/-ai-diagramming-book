# 版本、自動化與安全操作入口

- [第 12 章](../../docs/chapters/12-automation-security.md)
- [Makefile](../../Makefile)／[GitHub workflow](../../.github/workflows/core-contracts.yml)
- [本機實測](local-results.json)／[GitHub API 證據](ci-evidence.json)
- [驗證範圍](verification.md)／[發布前檢查表](release-checklist.md)
- [AI 交付檢查提示詞](../../prompts/release-verification.md)

## 本機執行

從儲存庫根目錄執行：

```sh
make check-core
make check-full
make audit-npm
```

第 13 章新增退款規格測試後，check-core 只需 Python 3 與 make，共六個測試。沒有 make 時：

```sh
python3 -m unittest discover -s tests -p 'test_graphviz_generator.py' -v
python3 -m unittest discover -s tests -p 'test_cross_tool_contract.py' -v
python3 -m unittest discover -s tests -p 'test_refund_change.py' -v
```

check-full 為目前十個 Python 測試，需要 [除錯實驗室](../debugging/README.md) 說明的 Mermaid CLI、Chromium 與 Graphviz 環境。可用 DOT、MMDC、PUPPETEER_CONFIG 指定自身工具；不可照抄維護者的絕對路徑。正常檢查不要設定 BOOK_SOURCE_ROOT 或 REFUND_SCENARIOS。

audit-npm 需要專案 npm 套件資訊與網路，只查 npm 公告，不掃描秘密或圖檔中的個資。沒有工具時應回報失敗，不要略過後說通過。

## GitHub 實際範圍

[已成功的核心執行](https://github.com/t945935/-ai-diagramming-book/actions/runs/34585128709) 對應引入工作流程的提交 `c61557405d3edfbb9d991911459b4edfbe2e036e`。僅執行 check-core，沒有安裝渲染器、沒有發布權限或 Secrets 引用。此證據固定在該次執行，之後版本請查看對應 head SHA 的 Actions。

CI 使用 ubuntu-24.04 託管 runner；本機驗證在 Linux／WSL。這不是六套工具跨平台驗證。尚未設定 required status checks、Pages 或正式 Release。
