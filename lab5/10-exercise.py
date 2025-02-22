import re

def camel_to_snake(camel_str):
    snake_str = re.sub(r'([A-Z])', r'_\1', camel_str).lower()
    return snake_str.lstrip('_')

camel_string = input("Введите строку в CamelCase: ")
snake_string = camel_to_snake(camel_string)
print("Snake case:", snake_string)
