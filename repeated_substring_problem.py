"""
Given a non-empty string check if it can be constructed by taking a substring of it and appending multiple copies of the substring together. You may assume the given string consists of lowercase English letters only and its length will not exceed 10000.
"""
def repeatedSubstringPattern(string):
    length = len(string)
    for i in range(1, length/2 + 1):
        substring = string[:i]
        multiples = length / len(substring) 
        if multiples % 1 == 0:
            if substring * multiples == string:
                return True
    return False

print(repeatedSubstringPattern("abab"))
print(repeatedSubstringPattern("aba"))
print(repeatedSubstringPattern("abcabcabcabc"))
