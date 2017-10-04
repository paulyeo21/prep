# Find the contiguous subarray within an array (containing at least one number) 
# which has the largest sum.

# For example, given the array [-2,1,-3,4,-1,2,1,-5,4],
# the contiguous subarray [4,-1,2,1] has the largest sum = 6.

# Brute Force
# T: O(n^2)
# S: O(1)
def maxSubarray(numbers):
    global_max = numbers[0]
    for i in range(len(numbers)):
        local_max = numbers[i]
        for j in range(i + 1, len(numbers)):
            subarray = numbers[i:j + 1]
            local_max = max(local_max, sum(subarray))
        global_max = max(global_max, local_max)
    return global_max

# Dynamic Programming
# T: O(n)
# S: O(n)
def maxSubarray1(numbers):
    # 1. number by itself is max
    # 2. number plus any contiguous block is max
    dp = [0 for i in range(len(numbers))]
    dp[0] = numbers[0]
    maximum = numbers[0]
    for i in range(1, len(numbers)):
        dp[i] = max(numbers[i], dp[i - 1] + numbers[i])
        maximum = max(dp[i], maximum)
    return maximum

# Dynamic Programming w/o space
# T: O(n)
# S: O(1)
def maxSubarray2(numbers):
    total = numbers[0]
    best = numbers[0]
    for n in numbers[1:]:
        total = max(n, total + n)
        best = max(best, total)
    return best

assert maxSubarray2([1]) == 1
assert maxSubarray2([1, 1]) == 2
assert maxSubarray2([-1, 1]) == 1
assert maxSubarray2([2, -1, 2]) == 3
assert maxSubarray2([1, -1, 3]) == 3
assert maxSubarray2([-2, 1, -3, 4, -1, 2, 1, -5, 4]) == 6
