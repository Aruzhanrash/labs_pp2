import shutil
source_file = "C:/Users/Acer Aspire lite/pp2/labs_pp2/lab6/dir_files/source.txt"

destination_file = "C:/Users/Acer Aspire lite/pp2/labs_pp2/lab6/dir_files/copy.txt"

shutil.copy(source_file, destination_file)

print(f"Файл успешно скопирован из {source_file} в {destination_file}")
