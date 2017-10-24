"""
Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

For example,
Given n = 3, there are a total of 5 unique BST's.

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
"""

# T: O(n)
# S: O(n)
def unique_binary_search_trees(n):
    if n == 0:
        return 1
    if n == 1:
        return 1
    if n == 2:
        return 2

    dp = [0 for _ in xrange(n + 1)] # Stores number of unique binary search trees for index = nodes
    dp[0] = 1
    dp[1] = 1
    dp[2] = 2
    for i in range(3, n + 1):
        for j in range(1, i + 1):
            dp[i] += dp[j - 1] * dp[i - j]
            # Sum over roots from i to j
            # dp[j - 1] corresponds to number of unique bsts for left branch
            # dp[i - j] corresponds to number of unique bsts for right branch
    return dp[n]


assert unique_binary_search_trees(1) == 1
assert unique_binary_search_trees(2) == 2
assert unique_binary_search_trees(3) == 5
