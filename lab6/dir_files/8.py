import os

file_path = "C:/Users/Acer Aspire lite/pp2/labs_pp2/lab6/dir_files/delete_me.txt"

if os.path.exists(file_path):

    if os.access(file_path, os.W_OK):
        os.remove(file_path)
        print(f"Файл {file_path} успешно удалён")
    else:
        print(f"Нет доступа к удалению файла {file_path}")
else:
    print(f"Файл {file_path} не найден")
