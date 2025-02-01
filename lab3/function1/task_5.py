def permute(s, answer=""):
    if len(s) == 0:
        print(answer)
        return

    for i in range(len(s)):
        remaining = s[:i] + s[i+1:]  
        permute(remaining, answer + s[i]) 
string = input()
permute(string)
