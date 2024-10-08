import csv
import json

# 定義檔案路徑
csv_file_path = r'C:\Users\at930\OneDrive\桌面\筆記夾\二上程式設計\workspace\aa.csv'
json_file_path = r'C:\Users\at930\OneDrive\桌面\筆記夾\二上程式設計\workspace\aa.json'

# 讀取CSV檔案並轉換為JSON格式
data = []
with open(csv_file_path, newline='', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
        data.append(row)

# 將資料寫入JSON檔案
with open(json_file_path, 'w', encoding='utf-8') as jsonfile:
    json.dump(data, jsonfile, ensure_ascii=False, indent=4)

print(f"CSV檔案已成功轉換為JSON檔案，儲存於: {json_file_path}")