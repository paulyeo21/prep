def delete_distance(str1, str2):
    occurrences = {}
    for char in str1:
        if char in occurrences:
            occurrences[char] += 1
        else:
            occurrences[char] = 1

    matched = 0
    for char in str2:
        if char in occurrences:
            if occurrences[char] > 0:
                occurrences[char] -= 1
                matched += 1

    return len(str1) + len(str2) - 2 * matched

print(delete_distance("at", "cat"))
print(delete_distance("bat", "cat"))
