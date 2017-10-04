# You are climbing a stair case. It takes n steps to reach to the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways 
# can you climb to the top?

# Note: Given n will be a positive integer.

# Recursive
# T: O(2^n)
# S: O(n) 
def climbStairs(n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return climbStairs(n - 1) + climbStairs(n - 2)

# Dynamic Programming
# T: O(n)
# S: O(n)
def climbStairs1(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        dp = [0 for i in range(n)]
        dp[0] = 1
        dp[1] = 2
        for i in range(2, n):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n - 1]

# DP w/o array
# T: O(n)
# S: O(1)
def climbStairs2(n):
    if n < 3:
        return n
    a = 1
    b = 2
    for i in range(2, n):
        tmp = b
        b += a
        a = tmp
    return b


assert climbStairs(1) == 1
assert climbStairs(2) == 2 # [1, 1] [2]
assert climbStairs(3) == 3 # [1, 1, 1] [1, 2] [2, 1]
assert climbStairs(4) == 5 # [1, 1, 1, 1] [1, 1, 2] [1, 2, 1] [2, 1, 1] [2, 2]

assert climbStairs1(1) == 1 # dp = [1]
assert climbStairs1(2) == 2 # dp = [1, 2]
assert climbStairs1(3) == 3 # dp = [1, 2, 3]
assert climbStairs1(4) == 5 # dp = [1, 2, 3, 5]

assert climbStairs2(1) == 1 # dp = [1]
assert climbStairs2(2) == 2 # dp = [1, 2]
assert climbStairs2(3) == 3 # dp = [1, 2, 3]
assert climbStairs2(4) == 5 # dp = [1, 2, 3, 5]
