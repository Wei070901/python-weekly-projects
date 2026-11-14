records = []

while True:
    
    print("1. 新增學習紀錄")
    print("2. 查看所有紀錄")
    print("3. 統計各科時間")
    print("0. 離開")
    
    choice = input()
    if choice not in ["0", "1", "2", "3"]:
        print("請輸入0~3")
        continue
    
    if choice == "1":
        subject = input("請輸入科目:").strip()
        if not subject:
            print("科目不可空白")
            continue
        try:
            minutes = int(input("請輸入分鐘數:"))
        except ValueError:
            print("分鐘數必須是整數")
            continue
        if minutes <= 0:
            print("分鐘數不可小於或等於0")
            continue
        record = {"subject": subject, "minutes": minutes}
        records.append(record)
        print(records)
        
    elif choice == "2":
        if not records:
            print("目前沒有學習紀錄")
        else:
            for record in records:
                print(f"{record['subject']}:{record['minutes']}分鐘")
    
    elif choice == "3":
        totals = {}
        sumtotals = 0
        if not records:
            print("目前沒有學習紀錄")
        for record in records:
            subject = record["subject"]
            minutes = record['minutes']
            totals[subject] = totals.get(subject, 0) + minutes
            sumtotals += minutes
        for subject, minutes in totals.items():
            print(f'{subject}:{minutes}分鐘')
        if records:
            print(f'總時間:{sumtotals}分鐘')
                
    elif choice == "0":
        print("離開")
        break