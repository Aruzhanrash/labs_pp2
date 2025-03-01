def all_true(t):
    return all(t)  

tuple1 = (1, True, "Hello", 5.5)  
tuple2 = (1, 0, True, "Hi")  

print(all_true(tuple1))  
print(all_true(tuple2))  