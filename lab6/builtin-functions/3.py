def is_palindrome(s):
    cleaned_s = ''.join(s.lower().split()) 
    return cleaned_s == cleaned_s[::-1] 

text = input("Введите строку  ")

if is_palindrome(text):
    print("это палиндром")
else:
    print("это не палиндром")
