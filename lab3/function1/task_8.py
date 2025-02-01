def spy_game(nums):
    sequence = []
    for num in nums:
        if num == 0 or num == 7:
            sequence.append(num)
        if sequence == [0, 0, 7]:
            return True
    return False

print(spy_game([1, 2, 4, 0, 0, 7, 5])) 
print(spy_game([1, 0, 2, 4, 0, 5, 7]))      
print(spy_game([1, 7, 2, 0, 4, 5, 0])) 
