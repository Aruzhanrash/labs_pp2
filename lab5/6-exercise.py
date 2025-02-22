import re

text = '/Users/Acer Aspire lite/pp2/labs_pp2/lab5/row.txt'

with open(text, 'r', encoding='utf-8') as file:
    string = file.read().strip()

pattern = r'[ ,.]'
replacement = ':'
result = re.sub(pattern, replacement, string)

print(result)
