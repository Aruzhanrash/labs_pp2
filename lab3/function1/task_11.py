def palindrome(word):
    str1 = ""
    for i in word.lower():
        if i.isalnum():  
            str1 += i
    
    reversed_str =str1[::-1]  
    return str1 == reversed_str
word=input()
if palindrome(word):
    print(True)
else:
    print(False)