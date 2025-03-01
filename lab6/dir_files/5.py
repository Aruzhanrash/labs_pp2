import os
dir_path = "C:/Users/Acer Aspire lite/pp2/labs_pp2/lab6/dir_files"
file_path = os.path.join(dir_path, "text.txt")

data_list = ["KBTU", "jhhbjh", "PP2", "Date", "4444"]

with open(file_path, "w", encoding="utf-8") as f:
    for item in data_list:
        f.write(item + "\n")

print(f"Файл успешно записан: {file_path}")
