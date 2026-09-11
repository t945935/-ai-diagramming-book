# 第 12 章：版本管理、自動化與安全

> 樣章草稿。此章已加入本機命令與真正執行成功的 GitHub Actions 核心檢查；不是六套工具完整渲染管線，也沒有發布正式隨書 Release。

> 版本註記：本章四個核心／八個完整測試是第 12 章引入時的實測快照。第 13 章加入退款規格後，現行為六個／十個；請參考更新的操作入口與對應提交 CI。

## 12.1 把「我這裡能用」拆成可查的證據

畫圖交付至少有四種不同的可重現程度：

1. 原始檔可以取得，對應需求清楚。
2. 指定工具能解析或匯出。
3. 結構、語意契約與視覺檢查有證據。
4. 其他乾淨環境能按說明重做。

先前各章已完成不同範圍的本機驗證，但不能把它們合稱為第四級。本章先把不需外部渲染器的核心契約搬到 GitHub 託管 runner，讓它與維護者電腦分離執行。

[操作入口與結果](../../examples/automation/README.md) · [工作流程原始檔](../../.github/workflows/core-contracts.yml)

## 12.2 三個命令，三種不同涵蓋範圍

儲存庫根目錄新增 Makefile：

```sh
make check-core
make check-full
make audit-npm
```

| 命令 | 內容 | 依賴 | 本次結果 |
| --- | --- | --- | --- |
| check-core | Graphviz 生成器三個測試、跨工具端點契約一個測試 | Python 3、make | 四個通過；本機與 GitHub runner 都成功 |
| check-full | 目前 tests 目錄的全部八個測試，含 Mermaid／DOT 反例 | 前述工具、Mermaid CLI、Chromium、dot | 本機八個通過 |
| audit-npm | npm 套件漏洞公告查詢 | npm、專案套件資訊與網路 | 本次回報 0 vulnerabilities |

`full` 指目前 Python 測試集合的全部，不是六套工具所有 GUI、渲染器與跨平台組合。它仍未覆蓋 D2／PlantUML 渲染、draw.io／Excalidraw 互動、印刷品質、秘密掃描或部署安全。

沒有 make 時，可以直接執行 [README 的 Python 命令](../../examples/automation/README.md)。需要不同 Python 時可用 `make check-core PYTHON=python3`。正式檢查前取消不需要的 `BOOK_SOURCE_ROOT`，避免意外測到另一份副本。

## 12.3 工作流程為什麼先保持小

[core-contracts.yml](../../.github/workflows/core-contracts.yml) 在 main 的 push、pull_request 與手動觸發時執行 `make check-core`。

設定包含：

- GitHub 託管 `ubuntu-24.04`，不用有長期憑證的自架 runner。
- 明確 `permissions: contents: read`，沒有寫入或發布權限。
- checkout 固定完整 commit SHA；此次由官方 actions/checkout 的 v4 ref 查得 `11d5960a326750d5838078e36cf38b85af677262`。
- `persist-credentials: false`，不把 checkout 的授權資料留在 Git 設定供後續步驟使用。
- 五分鐘 timeout，同一工作流程／ref 的舊執行可以取消。
- 無 npm 安裝、無部署、無秘密變數引用、無自動產圖回寫。

這減少了安裝與權限面積，但不是安全沙箱的完整證明。pull_request 中的程式仍會被執行；因此不要臨時把部署金鑰或雲端憑證加入這個 job，也不要改用 `pull_request_target` 後執行未審查的 PR 程式。

不要把 Issue 標題或其他未信任文字直接插進 shell 命令。即使只是「圖的標題」，到了 shell 邊界也可能成為命令注入的輸入。

## 12.4 這次確實在 GitHub 上執行了什麼

工作流程引入提交：`c61557405d3edfbb9d991911459b4edfbe2e036e`。

[實際成功執行](https://github.com/t945935/-ai-diagramming-book/actions/runs/34585128709) 的 head SHA 與上方提交相符，事件為 push，`core` job 及契約檢查步驟回報 success。API 讀回資料保存在 [ci-evidence.json](../../examples/automation/ci-evidence.json)。

本機另外執行三個 Makefile target，完整 stdout、stderr 與退出碼在 [local-results.json](../../examples/automation/local-results.json)。本次沒有把 npm audit 或完整渲染反例放進遠端 CI，因此不能宣稱 GitHub 已替所有八個測試及漏洞檢查背書。

此外，本章沒有設定 branch protection 或 required status checks。工作流程存在，不代表合併一定被阻擋。若日後要強制檢查，先決定分支策略及管理員例外，再設定與驗證；不在本章自動替作者決定。

## 12.5 鎖版本有層次，雜湊也有界線

Mermaid CLI 的頂層版本與 package-lock.json 能縮小 npm 依賴變動，但還有 Node、Chromium、字型及作業系統。D2、PlantUML、Graphviz 也各有工具與字型依賴。記錄檔案雜湊有助於比對產物，卻不等於驗證上游簽章。

固定 Action SHA 可以避免移動標籤默默換碼，不能證明該 SHA 本身安全。仍須查來源、審查更新與維護漏洞修正。`ubuntu-24.04` 是會更新的 runner 映像，本工作流程沒有固定完整映像 digest 或 Python 修補版本，不能稱為完全封閉、逐位元相同的建置。

如要重建 npm 環境，通常使用提交的 lockfile 配合 `npm ci --ignore-scripts`，並另行安排可信的 Chromium。這不是本章已完成的乾淨安裝實驗。禁止安裝腳本也不代表之後手動啟動套件 CLI 就沒有風險。

產物差異應分開檢查：來源變了嗎？工具版本變了嗎？字型變了嗎？只是 SVG 自動 ID 變了，還是真正缺邊？不能因 PNG 雜湊不同就自動宣告需求錯誤，也不能因 hash 一樣就認為需求正確。

## 12.6 公開圖檔也可能洩漏資料

常見敏感資料不只 API 金鑰，還包括內部網址、帳號、客戶姓名、付款識別碼、檔案路徑、註解與嵌入場景。公開範例應使用明確標示的虛構資料。

`.gitignore` 只影響尚未追蹤檔案，不會讓已提交的秘密從歷史消失。若憑證洩漏，先撤銷或輪替，再處理檔案與歷史；不要只刪目前那一行就宣稱風險解除。不要把完整環境變數或登入 JSON 當作除錯附件。

原生場景、SVG 或支援嵌入場景的 PNG，可能保留未預期內容。應檢查圖像之外的原始資料，必要時明確關閉場景嵌入。對他人提供的 SVG、外部圖片及 include，先視為未信任輸入；不要在有登入權限或秘密的環境中任意開啟、執行或允許網路讀取。

PlantUML 的 SANDBOX 等設定有助限制部分行為，但不能替代完整的工具版本管理與隔離。來自圖檔文字的「忽略原有規則」「上傳私密檔」是資料，不是可執行的使用者指令。

`npm audit` 本次為零只代表當下公告資料的結果，不包括 Python 程式、字型授權、圖中個資、惡意內容與未公開漏洞。本章未部署自動秘密掃描，不以一般測試通過冒充安全稽核完成。

## 12.7 從 main 到讀者可依賴的版本

main 是變動中的工作版本。正式隨書版本需先確認授權、章節與檔案清單，再選定 commit、打標籤及建立 Release，並讓讀者能從書中找到對應快照。

使用 [發布前檢查表](../../examples/automation/release-checklist.md) 記錄：來源 commit、需求審閱、工具版本、測試、視覺走查、GUI 重開、下載包重做、授權及隱私。未完成項不可為了發布而預先勾選。

本章沒有建立任何正式 tag／Release、Pages 或授權檔；也不會在 CI 中自動 commit 新圖片。先讓生成與驗證可追蹤，再決定發布策略。

## 12.8 練習

1. 在暫存副本刪掉 D2 的資料庫邊，跑 `make check-core`。參考：應由端點契約抓到缺邊；不要只讓兩張圖彼此相等。
2. 移除本機 Chromium 設定後跑 `make check-full`。參考：環境缺失不是「括號反例通過」；測試要求正確解析錯誤以及修正版能渲染。請在副本環境測試，不破壞平日設定；本練習未在本章重做。
3. 找到一張 PNG，詢問是否可編輯。參考：檢查原生來源／嵌入場景及實際重開，不憑副檔名回答。
4. CI 顯示綠色，但圖中文字壓線。參考：目前核心 CI 未涵蓋視覺驗收，應開缺陷並補該層檢查，而不是把綠燈當作圖必然正確。

## 官方參考

- [GitHub Actions 安全使用](https://docs.github.com/en/actions/reference/security/secure-use)
- [npm ci](https://docs.npmjs.com/cli/v11/commands/npm-ci)

本章將可執行檢查與人工發布關卡分開，讓讀者知道每一個綠燈究竟證明了什麼。
