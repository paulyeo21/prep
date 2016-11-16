def containsDuplicate(nums, k):
    uniqueNums = {}
    for i, num in enumerate(nums):
        if num in uniqueNums:
            if i - uniqueNums[num] <= k:
                return True
            else:
                uniqueNums[num] = i
        else:
            uniqueNums[num] = i
    return False

print(containsDuplicate([], 1))
print(containsDuplicate([99, 99], 2))
print(containsDuplicate([1, 0, 1, 1], 1))
