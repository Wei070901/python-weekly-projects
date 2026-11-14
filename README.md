# Python Weekly Projects 🐍

Weekly Python projects and learning notes.

每週完成一個實用的 Python 小專案，累積 GitHub 作品，並逐步建立未來就讀資工所需的程式設計能力。

## 目前進度

**已完成 1 個專案。** 點選專案名稱，可查看詳細功能、執行方式、驗收結果與程式碼。

| 週次 | 專案 | 核心技能 | 狀態 |
| --- | --- | --- | --- |
| 01 | [學習時間紀錄器](projects/week-01/) | 輸入、條件判斷、迴圈、串列、字典、例外處理 | 已完成 |

## 學習方向

依實際學習狀況調整進度，難度從簡單逐步提升至中等：

1. **Python 基礎**：變數、條件判斷、迴圈、函式、串列與字典。
2. **實用工具**：文字處理、檔案讀寫、CSV／JSON、輸入檢查與例外處理。
3. **程式組織**：模組拆分、命令列介面、測試與除錯。
4. **資工基礎應用**：資料結構、搜尋與排序、時間複雜度、SQLite 與 API。

初期每個專案預計投入約 2～4 小時。以當週題目的基本要求驗收，延伸功能列為選做。

## 資料夾安排

```text
python-weekly-projects/
├── README.md                    # 作品集介紹與專案目錄
├── .gitignore                   # Python 暫存檔與本機環境的忽略規則
├── projects/
│   ├── README.md                # 專案整理方式
│   └── week-01/
│       ├── README.md            # 專案介紹、執行方式與驗收結果
│       └── main.py              # 第 1 週學習時間紀錄器
└── templates/
    └── project-readme.md        # 有需要時可使用的專案說明範本
```

每週專案放在獨立資料夾，例如 `projects/week-01/`。首頁維護專案目錄；各週 README 記錄作品介紹、功能與執行方式，並連結程式碼。題目、提示與解答透過聊天討論。

## 每週實作流程

1. 確認題目、學習目標與基本驗收要求。
2. 先自行實作，遇到問題時透過提示與討論釐清觀念。
3. 測試正常輸入與邊界情況，修正程式。
4. 基本任務驗收通過後，提交並推送至 GitHub。
5. 更新首頁的作品連結與完成狀態，將詳細功能與驗收結果記錄於該週 README。

需要額外說明時，可使用 [專案說明範本](templates/project-readme.md)，記錄執行方式、學習心得與參考來源。

## 取得儲存庫

先安裝 Python 3 與 Git，再執行：

```powershell
git clone https://github.com/Wei070901/python-weekly-projects.git
cd python-weekly-projects
```

各專案獨立執行；需要的環境與套件會隨專案說明。

公開範例使用虛構資料；密碼、API 金鑰與個人資料不放入儲存庫。
