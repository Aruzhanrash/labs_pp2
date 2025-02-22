import re

def split_by_uppercase(s):
    return re.findall(r'[A-Z][a-z]*', s)

text = input("Введите строку: ")
result = split_by_uppercase(text)
print("Разделенные слова:", result)
