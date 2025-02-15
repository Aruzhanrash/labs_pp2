def squares(a, b):
   
    for number in range(a, b + 1):
        yield number ** 2


a = int(input("Enter the start of the range (a): "))
b = int(input("Enter the end of the range (b): "))


for square in squares(a, b):
    print(square)
