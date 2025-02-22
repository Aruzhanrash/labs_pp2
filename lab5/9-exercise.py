import re

def insert_spaces(s):
    return re.sub(r'(?<!^)([A-Z])', r' \1', s)

text = input("Введите строку: ")
result = insert_spaces(text)
print("Результат:", result)
