import os
import string

dir_path = "C:/Users/Acer Aspire lite/pp2/labs_pp2/lab6/dir_files/6_task_generate"

if not os.path.exists(dir_path):
    os.makedirs(dir_path)

for letter in string.ascii_uppercase: 
    file_path = os.path.join(dir_path, f"{letter}.txt")
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.write(f"This is file {letter}.txt\n") 

print(f"26 файлов успешно созданы в папке: {dir_path}")
