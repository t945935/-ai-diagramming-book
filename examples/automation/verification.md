# 第 12 章實際驗證

日期：2026-09-11。本機 Linux／WSL，沿用既有工具環境。

- make check-core：兩個測試集合，共四個方法通過，exit 0。
- make check-full：八個方法通過，無略過，exit 0；只是現有 Python 套件測試，不是六工具完整 GUI 或渲染矩陣。
- make audit-npm：exit 0，當下 found 0 vulnerabilities；不代表整體安全稽核通過。
- 真正 GitHub Actions push 執行：[34585128709](https://github.com/t945935/-ai-diagramming-book/actions/runs/34585128709)，head SHA `c61557405d3edfbb9d991911459b4edfbe2e036e`，core job 及各步驟回報 success；已經 API 讀回驗證。
- 工作流程與 Makefile 先提交並讀回比對，確定不是只有本機 YAML 草稿。

完整 stdout／stderr 見 local-results.json；GitHub run 與 job API 摘錄見 ci-evidence.json。CI 只跑四個核心測試，本機八個與 npm audit 是另外的證據。

尚未設定或驗證：required status checks、正式 Release／tag、Pages、秘密掃描、完整渲染 CI、Windows／macOS、六工具乾淨安裝、字型和紙本品質統一驗收。ubuntu-24.04 runner 映像會更新，未固定整個環境 digest。
