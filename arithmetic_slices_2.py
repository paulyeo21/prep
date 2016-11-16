"""
    A sequence of numbers is called arithmetic if it consists of 
    at least three elements and if the difference between any
    two consecutive elements is the same.

    arithmetic examples:
    1, 3, 5, 7, 9
    7, 7, 7, 7
    3, -1, -5, -9

    non-arithmetic example:
    1, 1, 2, 5, 7

    Return the number of arithmetic subsequence slices
"""
def isArithmetic(sequence):
    if len(sequence) < 3:
        return False

    difference = sequence[1] - sequence[0]
    previous = sequence[1]
    for current in sequence[2:]:
        if difference != current - previous:
            return False
        previous = current

    return True

def numberOfSubsequencesHelper(sequence, count):
    if sequence:
        for i in range(1, len(sequence) + 1):
            if isArithmetic(sequence[:i]):
                count += 1
        return numberOfSubsequencesHelper(sequence[1:], count)

    else:
        return count

def numberOfSubsequences(sequence):
    # 1. Generate all subsequences
    # 2. Count those that are arithmetic

    count = 0
    return numberOfSubsequencesHelper(sequence, count)

print(numberOfSubsequences([2, 4, 6, 8, 10]))

