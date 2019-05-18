# Given a string find the length of the longest substring without 
# repeating characters.

def longestSubstringWithoutRepeatingChar(s):
    # Consider the case when the longest substring starts in the middle
    # of another substring. For instance, for the string 'dvdf', if we try
    # 'dv' and start checking substrings after 'dv' such as 'df', we wont
    # consider the substring 'vdf' which is actually the longest substring.
    # What we need to do is still use two pointers, i and j, with i as the
    # beginning of a substring and j as the end of a substring, but when
    # j encounters a character that has already been encountered, increment
    # i by 1 and remove the previous character at i.
    # T: O(n)
    # S: O(n)

    if len(s) == 0:
        return 0

    i, j = 0, 1
    longest_length = 0
    encountered_chars = set()
    encountered_chars.add(s[i])

    while j < len(s):
        if s[j] in encountered_chars:
            longest_length = max(longest_length, j - i)
            encountered_chars.remove(s[i])
            i += 1
        else:
            encountered_chars.add(s[j])
            j += 1

    longest_length = max(longest_length, j - i)
    return longest_length

print longestSubstringWithoutRepeatingChar('abcabcd') # 4
print longestSubstringWithoutRepeatingChar('dvdf') # 3
print longestSubstringWithoutRepeatingChar('bbbbbb') # 1
print longestSubstringWithoutRepeatingChar('ddvf') # 3
print longestSubstringWithoutRepeatingChar('pwwkew') # 3
print longestSubstringWithoutRepeatingChar('dvdf') # 3
print longestSubstringWithoutRepeatingChar('tmmzuxt') # 5
