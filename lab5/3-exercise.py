import re

text = '/Users/Acer Aspire lite/pp2/labs_pp2/lab5/row.txt'

with open(text, 'r', encoding='utf-8') as file:
    string = file.read()

pattern = r'\b[a-z]+_[a-z]+\b'
result = re.findall(pattern, string)

if result:
    print(result)
else:
    print("Not found")
