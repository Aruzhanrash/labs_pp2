def unique_elements(nums):
    unique_list = []
    for i in range(len(nums)):
        for j in range(i):
            if nums[i] == nums[j]:
                break
        else: 
            unique_list.append(nums[i])
    return unique_list

