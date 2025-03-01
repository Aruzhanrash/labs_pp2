def count_letters(s):
    upper_count = sum(1 for char in s if char.isupper())  # Количество заглавных букв
    lower_count = sum(1 for char in s if char.islower())  # Количество строчных букв
    return upper_count, lower_count

text = input("Введите строку: ")
upper, lower = count_letters(text)
print(f"Заглавных букв: {upper}")
print(f"Строчных букв: {lower}")
