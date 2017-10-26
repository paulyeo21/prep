"""
Given a string, return whether it is made of a perfectly repeated string pattern.
"""

# T: O(n)
# S: O(1)
def hasStringPattern(string):
    for i in range(len(string)):
        pattern = string[:i + 1]
        substring = string[i + 1:]
        # print pattern, substring
        if matches(pattern, substring):
            return True
    return False

def matches(pattern, string):
    if not string:
        return False
    if len(string) % len(pattern) != 0:
        return False
    while string:
        length = len(pattern)
        if pattern == string[:length]:
            string = string[length:]
        else:
            return False
    return True


assert matches("monkey", "monkeymonkey") == True
assert matches("ab", "abab") == True
assert matches("a", "ab") == False

assert hasStringPattern("a") == False
assert hasStringPattern("aa") == True
assert hasStringPattern("ab") == False
assert hasStringPattern("aaa") == True
assert hasStringPattern("abb") == False
assert hasStringPattern("abc") == False
assert hasStringPattern("monkeymonkeymonkey") == True
