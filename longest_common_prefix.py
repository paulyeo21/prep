def longest_common_prefix(strings):
    if strings:
        # Get shortest length
        shortest_length = len(strings[0])
        for string in strings[1:]:
            shortest_length = min(len(string), shortest_length)

        # Find longest commmon prefix iterate over shortest length
        longest_common_prefix = ""
        for i in range(shortest_length):

            current = strings[0]
            for string in strings[1:]:
                if string[i] != current[i]:
                    return longest_common_prefix

            longest_common_prefix += current[i]
        
        return longest_common_prefix
    else:
        return ""

print(longest_common_prefix([]))
print(longest_common_prefix(["ab", "a"]))
print(longest_common_prefix(["ab", "aba"]))
