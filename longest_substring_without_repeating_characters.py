def longest_substring_without_repeating_characters(string):
    repeated = {}
    max_length = 0
    current_length = 0
    index_of_last_repeated_char = 0

    for i, char in enumerate(string):
        index_of_previous_current_char = repeated.get(char, -1)
        if index_of_previous_current_char < 0:
            current_length += 1
        else:
            max_length = max(max_length, current_length)
            current_length = i - max(index_of_previous_current_char, index_of_last_repeated_char)
            index_of_last_repeated_char = max(index_of_previous_current_char, index_of_last_repeated_char)

        repeated[char] = i

    max_length = max(max_length, current_length)
    return max_length

print(longest_substring_without_repeating_characters("bbbbbb"))
print(longest_substring_without_repeating_characters("abcabcd"))
print(longest_substring_without_repeating_characters("pwwkew"))
print(longest_substring_without_repeating_characters("dvdf"))
print(longest_substring_without_repeating_characters("tmmzuxt"))
print(longest_substring_without_repeating_characters("zwnigfunjwz"))
print(longest_substring_without_repeating_characters("gzdrgocdtidpxmucbqojrghfel"))
