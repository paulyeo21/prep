# Given an array find the max down sequences.

def maxDownSequences(sequence):
    # get all subsequences.
    # For all subsequences find down sequences
    sequence = str(sequence)
    subsequences = [sequence[0]]
    for num in sequence[1:]:
        temp = []
        for s in subsequences:
            for i in xrange(len(s) + 1):
                temp.append(s[:i] + num + s[i:])
        subsequences = temp
    return permutations

print maxDownSequences([4,1,3,2,5]) # 1
