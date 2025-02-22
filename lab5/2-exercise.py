import re

text_path = r'C:\Users\Acer Aspire Lite\pp2\labs_pp2\lab5\row.txt'

with open(text_path, 'r', encoding='utf-8') as file:
    string = file.read().strip()

pattern = r'\.{2,3}ab'

result = re.findall(pattern, string)

if result:
    print(result)
else:
    print("Not found")
