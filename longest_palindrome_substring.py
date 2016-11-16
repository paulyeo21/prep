# O(n^2)
def longest_palindrome_substring(string):
    longest_start = 0
    longest_end = 0
    for i, char in enumerate(string):
        # Odd
        start, end = i, i
        while start >= 0 and end < len(string):
            if string[start] == string[end]:
                if end - start > longest_end - longest_start:
                    longest_start = start
                    longest_end = end
                start -= 1
                end += 1
            else:
                break

        # Even
        start, end = i, i+1
        while start >= 0 and end < len(string):
            if string[start] == string[end]:
                if end - start > longest_end - longest_start:
                    longest_start = start
                    longest_end = end
                start -= 1
                end += 1
            else:
                break

    return string[longest_start:longest_end+1]

print(longest_palindrome_substring("12321"))
print(longest_palindrome_substring("123321"))
print(longest_palindrome_substring("512343218"))
