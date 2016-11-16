""" pattern: "abba"
    input: "redbluebluered"

    Write a function that takes a pattern and an input, and determines whether you have a match.
    Return 1 if it is a match, 0 if it is not a match.
"""

def word_pattern(pattern, string):
    instances = {}
    if word_pattern_helper(pattern, 0, string, 0, instances):
        return 1
    else:
        return 0

def distinct(substring, instances):
    for key, value in instances.iteritems():
        if substring == value:
            return False
    return True

def word_pattern_helper(pattern, p_index, string, s_index, instances):
    if p_index == len(pattern) and s_index == len(string):
        return True

    if p_index == len(pattern) or s_index == len(string):
        return False

    char = pattern[p_index]
    for i in range(s_index + 1, len(string) + 1):
        substring = string[s_index:i]
        # print("P index " + str(p_index))
        # print("S index " + str(s_index))
        # print("I index " + str(i))
        # print("Char: " + char)
        # print("Substring: " + substring)
        # print(instances)

        if char in instances:
            # print("Char exists")
            if instances[char] == substring:
                return word_pattern_helper(pattern, p_index + 1, string, i, instances)
        else:
            # print("Char does not exist")
            if distinct(substring, instances):
                instances[char] = substring
                found = word_pattern_helper(pattern, p_index + 1, string, i, instances)
                if found:
                    return True
                else:
                    # print("Popping: " + char)
                    instances.pop(char)
    return False

# print(word_pattern("aba", "rbrb"))
# print(word_pattern("aba", "rbr"))
# print(word_pattern("abba", "redbluebluered"))
# print(word_pattern("aaaa", "asdasdasdasd"))
# print(word_pattern("aabb", "xyzabcxyzabc"))
print(word_pattern("abba", "redredredred"))

