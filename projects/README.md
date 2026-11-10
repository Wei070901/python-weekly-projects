# 每週專案

這裡存放實際完成或正在開發的 Python 小專案。目前尚未新增第一個專案。

## 命名方式

使用 `week-週次-英文名稱`，例如 `week-01-project-name`；英文名稱使用小寫與連字號。

每個專案獨立存放，建議從最少的必要檔案開始：

```text
week-01-project-name/
├── README.md
└── main.py
```

有實際需要時，再加入 `tests/`、`examples/` 或 `requirements.txt`。若僅使用 Python 標準函式庫，直接在 README 說明即可。

## 新增一個專案

1. 在本資料夾建立該週專案資料夾。
2. 將 [說明範本](../templates/project-readme.md) 複製成專案內的 `README.md`。
3. 完成程式、必要的範例資料與驗收。
4. 在 [作品集首頁](../README.md) 加入連結、核心技能與實際狀態。

首頁目錄新增一列的格式如下；請換成實際資料後再使用：

```markdown
| 01 | [專案名稱](projects/week-01-project-name/) | 函式、檔案讀寫 | 進行中 |
```

只有完成基本功能與驗收後，才將狀態標示為「已完成」。
