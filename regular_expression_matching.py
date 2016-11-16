# T: O(n)
# S: O(1)
def regular_expression_matching(string, pattern):
    # Only supports '.' and '*'
    # '.' matches any single character
    # '*' matches zero or more of preceding character
    s_index = 0
    p_index = 0
    while s_index < len(string):
        if p_index >= len(pattern):
            return False

        if pattern[p_index] == ".":
            p_index += 1
        # elif pattern[p_index] == "*":
        #     char = pattern[p_index - 1]
        elif string[s_index] != pattern[p_index]:
            return False
        elif string[s_index] == pattern[p_index]:
            p_index += 1

        s_index += 1

    return True

print(regular_expression_matching("aa", "a"))
print(regular_expression_matching("aa", "aa"))
print(regular_expression_matching("ab", "a."))
print(regular_expression_matching("aaa", "aa"))
print(regular_expression_matching("aa", "a*"))
print(regular_expression_matching("aa", ".*"))
print(regular_expression_matching("ab", ".*"))
print(regular_expression_matching("aab", "c*a*b"))
