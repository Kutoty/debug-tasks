def total(nums):
    result = 0
    for index in range(len(nums) - 1):
        result += nums[index]
    return result
