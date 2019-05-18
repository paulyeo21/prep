# Given a list of integers, find the maximum sum of a contiguous subarray.

def maxSubarraySum(ints):
    # Since we dont have to look at all subarrays and only contiguous
    # subarrays, the Naive solution is to use two pointers and store
    # the max sum as we iterate over contiguous subarrays.
    # T: O(n**2)
    # S: O(n**2)

    max_sum = ints[0]

    for i in range(len(ints)-1):

        current_sum = 0
        for j in range(i, len(ints)):
            current_sum += ints[j]
            max_sum = max(max_sum, current_sum)

    return max_sum

def maxSubarraySum(ints):
    # get contiguous subarrays using recursion
    # T: O(n**2)
    # S: O(n**2)

    if len(ints) == 1:
        return ints[0]

    current_sum = sum(ints)
    return max(current_sum, maxSubarraySum(ints[1:]), maxSubarraySum(ints[:1]))

def maxSubarraySum(ints):
    # Use dynamic programming. We want to populate the dp index with the
    # max sum for any subarray up to each index. For instance, given
    # [1,-2,12,-3, 1], our dp should be [1,-1,12,9,10] which is the max
    # of any contiguous subarray up to each index. After we get this we can
    # iterate last time over the dp list and get the max.
    # T: O(n)
    # S: O(n)

    dp = [0] * len(ints)
    dp[0] = ints[0]
    previous = ints[0]

    for i in range(1, len(ints)):
        current = ints[i]
        dp[i] = max(dp[i-1] + current, current)

    return max(dp)

print maxSubarraySum([1,2,3]) # [1,2,3] = 6
print maxSubarraySum([1,-2,12,-3]) # [12] = 12
print maxSubarraySum([1,-2,12,-3,1]) # [12] = 12
print maxSubarraySum([-1,-2,-12,-3]) # [-1] = -1
