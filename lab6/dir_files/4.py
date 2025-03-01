file_path = "C:/Users/Acer Aspire lite/pp2/labs_pp2/lab6/dir_files/text.txt" 

try:
    with open(file_path, "r", encoding="utf-8") as f:
        data = f.read()
    print("Файл найден.Количество строк:", len(data.splitlines()))
except FileNotFoundError:
    print(" Файл не найден")
