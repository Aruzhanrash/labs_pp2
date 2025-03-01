import math
import time

number = int(input("Введите число "))  
delay = int(input("Введите задержку в миллисекундах "))

time.sleep(delay / 1000)

sqrt_result = math.sqrt(number)

print(f"Square root of {number} after {delay} milliseconds is {sqrt_result}")
