"""
Find the contiguous subarray within an array (containing at least one number) which has the largest product.

For example, given the array [2,3,-2,4],
the contiguous subarray [2,3] has the largest product = 6.
"""

# Brute force T: O(n^2)
def maxProduct(nums):
    global_max = nums[0]
    for i in range(len(nums) - 1):
        previous_product = nums[i]
        local_max = nums[i]
        for j in range(i + 1, len(nums)):
            local_max = max(local_max, previous_product * nums[j])
            previous_product = previous_product * nums[j]
        global_max = max(global_max, local_max)
    return global_max

assert maxProduct([2, 3, -2, 4]) == 6

# DP
def maxProduct1(nums):
    local_max = nums[0]
    local_min = nums[0]
    global_max = nums[0]
    max_prev = nums[0]
    min_prev = nums[0]
    for num in nums[1:]:
        local_max = max(num, max(max_prev * num, min_prev * num))
        local_min = min(num, min(max_prev * num, min_prev * num))
        global_max = max(global_max, local_max)
        max_prev = local_max
        min_prev = local_min
    return global_max

print maxProduct1([2, 3, -2, 4])
print maxProduct1([2, 3, -2, -1])

