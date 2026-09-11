# Graphviz 本機驗證紀錄

## 環境與方法

Linux／WSL x86_64；Python 3.12.3；Graphviz Ubuntu 套件 2.42.2-9ubuntu0.1，執行 `dot -V` 回報 2.43.0 (0)。字型為 Noto Sans CJK TC。

系統缺少 Graphviz 且無免密碼 sudo。使用 apt-get download 取得 graphviz、libgvc6、libcgraph6、libcdt5、libpathplan4、libgvpr2、liblab-gamut1，並補上 libltdl7，解到使用者目錄，不變更系統套件。

本機執行檔：/home/j5/.local/share/diagram-tools/graphviz/usr/bin/dot

函式庫路徑：/home/j5/.local/share/diagram-tools/graphviz/usr/lib/x86_64-linux-gnu

外掛路徑：上述目錄下的 graphviz 子目錄，以 GVBINDIR 指定。

`dot -c` 設定時有 neato 外掛缺相依的警告；本章使用 dot，實際四次 SVG／PNG 匯出均無錯誤並 exit 0，沒有宣稱 neato 可用。

## 測試紀錄

先建立反向傳遞與循環測試，看到 CLI 不存在造成失敗；完成最小實作後通過。接著非法輸入測試先失敗，再補上輸出前驗證。最後圖例測試先因缺說明失敗，再加入圖例並重跑。

最終 `python3 -m unittest discover -s tests -p 'test_graphviz_generator.py' -v`：Ran 3 tests，OK。非法輸入測試包含四個 subtest，沒有將它們另加成七個獨立測試。

程式以真實子程序執行；循環會終止，影響集合不包含起點自己的下游 SDK，非法端點、起點、邊形狀、標籤拒絕且不建立輸出。

## 生成與視覺

依 README 命令產生 DOT 與 impact.json，四次 dot 匯出均成功。SVG 已解析確認，PNG 檔頭有效且兩張均經視覺檢查。初版缺箭頭圖例，補上後再次渲染及檢查，圖例完整、未裁切。

總覽中央有交叉與箭頭集中；局部圖的訂單／發票循環更清楚。未以刪除真實資料邊改善外觀。

計數由程式讀取資料及結果：總覽 16 節點／17 邊，影響 9 節點／10 邊。成品雜湊見 artifacts.json。

## 未驗證

未掃描真實程式碼、未進行大型效能／跨平台／CI 測試，未實作完整循環群組分析。資料可信且規模小；未提供公開上傳服務所需的資源限制與完整 schema 防護。
