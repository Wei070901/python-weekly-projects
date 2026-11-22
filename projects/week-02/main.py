file_path = input("請輸入檔案路徑：")
try:
    with open(file_path, "r", encoding="UTF-8") as file:
        text = file.read().splitlines()
except FileNotFoundError:
    print("找不到檔案")
    raise SystemExit(1)
except OSError:
    print("無法讀取檔案")
    raise SystemExit(1)
except UnicodeDecodeError:
    print("編碼錯誤")
    raise SystemExit(1)

search = input("請輸入想搜尋的字").strip()

def search_lines(lines, keyword):
    total_number = 0
    
    if keyword == "":
        print("關鍵字不可空白")

    else:
        for line_number, line in enumerate(lines, start=1):
            if keyword in line:
                print(f"第{line_number}行：{line}")
                total_number += 1
        if total_number == 0:
            print("找不到符合的內容")
        else:
            print(f"共找到{total_number}行")
search_lines(text, search)