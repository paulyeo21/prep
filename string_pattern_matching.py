# Given a string text and a pattern pat print all occurences where
# pattern exists in text.

def patternOccurrencesInText(text, pattern):
    # Naive solution is to have two pointers, i and j, where i is the
    # index of text and j is the index of pattern. When text[i] ==
    # pattern[j] increment both i and j. If they do not match, reset
    # j. Do this until end of text.
    # T: O(n * m) where n is the length of text and m is length of pattern.
    # S: O(1)

    n = len(text)
    m = len(pattern)

    for i in range(n - m + 1):

        j = 0
        while j < m: # iterate over pattern and check if matches
            if text[i + j] != pattern[j]:
                break
            j += 1

        if j == m:
            print i,
    print

def preprocessPrefixes(pattern):
    prefixes = [0] * len(pattern)
    previous = pattern[0]
    count = 0

    for i in range(1, len(pattern)):
        if pattern[i] == previous:
            count += 1
        else:
            count = 0

        previous = pattern[i]
        prefixes[i] = count

    return prefixes

def patternOccurrencesInText(text, pattern):
    # Knuth Morris Pratt pattern searching algorithm uses a preprocessed
    # longest prefix list. When at index j in pattern does not match,
    # use longest prefix up to index j - 1 so not to start over like
    # naive solution. For instance, if text is 'AAABAAAB' and pattern
    # is 'AAA' when checking the pattern portion 'AAB' and 'AAA' instead
    # of naively incrementing i and failing at the same portion, we know
    # that the prefix 'AA' for this portion of text and pattern match,
    # so instead use the preprocessed prefix and check the last char
    # up to preprocessed prefix index with current text char. Do this
    # until j == 0, then increment i. 
    # T: O(n)
    # T: O(m)

    prefixes = preprocessPrefixes(pattern)
    i, j = 0, 0

    while i < len(text):
        print i, j

        if j == len(pattern):
            # print i - j,
            j = prefixes[j - 1]

        elif text[i] == pattern[j]:
            i += 1
            j += 1

        else:
            if j == 0:
                i += 1
            j = prefixes[j - 1]

    if j == len(pattern):
        print i - j,
    print

# patternOccurrencesInText('TTEST', 'TEST') # 1
# patternOccurrencesInText('TESTT', 'TEST') # 0
# patternOccurrencesInText('THIS IS A TEST TEXT', 'TEST') # 10
patternOccurrencesInText('AABAACAADAABAABA', 'AABA') # 0, 9, 12
# patternOccurrencesInText('AAAAABAAABA', 'AAAA') # 0, 9, 12
