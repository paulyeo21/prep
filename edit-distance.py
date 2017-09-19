# Given two words word1 and word2, find the minimum number of steps 
# required to convert word1 to word2. (each operation is counted as 1 step.)
#
# You have the following 3 operations permitted on a word:
#
#    a) Insert a character
#    b) Delete a character
#    c) Replace a character
#
# T: O(m * n)
# S: O(m)

def min_edit_distance(word1, word2):
    m = len(word1)
    n = len(word2)
    dp = [0 for i in range(m + 1)]

    for i in range(m + 1):
        dp[i] = i

    for j in range(1, n + 1):
        previous = dp[0]
        dp[0] = j
        for i in range(1, m + 1):
            temp = dp[i]
            if word1[i - 1] == word2[j - 1]:
                dp[i] = previous
            else:
                dp[i] = min(previous + 1, \
                        min(dp[i - 1] + 1, dp[i] + 1))
            previous = temp

    return dp[m]

assert min_edit_distance("a", "") == 1 # delete
assert min_edit_distance("a", "b") == 1 # replace
assert min_edit_distance("a", "aa") == 1 # insert
assert min_edit_distance("abbb", "bbb") == 1 # delete
assert min_edit_distance("bbba", "bbb") == 1 # delete
