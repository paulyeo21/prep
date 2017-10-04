# Given an unsorted array of integers, find the length of longest increasing subsequence.

# For example,
# Given [10, 9, 2, 5, 3, 7, 101, 18],
# The longest increasing subsequence is [2, 3, 7, 101], therefore the length is 4.
# Note that there may be more than one LIS combination, it is only necessary for
# you to return the length.

# Dynamic Programming
# T: O(n^2)
# S: O(1)
def longestIncreasingSubsequence(nums):
    if nums:
        dp = [1 for i in range(len(nums))]
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[j] + 1, dp[i])
        return max(dp)
    return 0


assert longestIncreasingSubsequence([]) == 0
assert longestIncreasingSubsequence([0]) == 1
assert longestIncreasingSubsequence([10, 101, 11, 9]) == 2 # [10, 101] or ...
assert longestIncreasingSubsequence([10, 101, 11, 102]) == 3 # [10, 101, 102] or ...
assert longestIncreasingSubsequence([10, 101, 11, 12]) == 3 # [10, 11, 12]
assert longestIncreasingSubsequence([4, 10, 4, 3, 8, 9]) == 3 # [4, 8, 9]
assert longestIncreasingSubsequence([10, 9, 2, 5, 3, 7, 101, 18]) == 4 # [2, 3, 7, 101]
assert longestIncreasingSubsequence([1,3,6,7,9,4,10,5,6]) == 6
