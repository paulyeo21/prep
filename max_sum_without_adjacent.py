# Given a list of integers find the max sum without using adjacent
# integers. Integers can only be positive.

def maxSumWithoutAdj(ints):
    # Using dynamic programming while iterating over the list of
    # integers, find the max sum up to each index by comparing
    # ints[i] + sums[i-2] > sums[i-1]. If True, max sum at i is 
    # ints[i] + sums[i-2], if False, max sum at i is sums[i-1]
    # T: O(n)
    # S: O(n)

    if len(ints) == 0:
        return 0

    if len(ints) == 1:
        return ints[0]

    sums = [0] * len(ints)

    sums[0] = ints[0]
    sums[1] = max(ints[0], ints[1])

    for i in range(2, len(ints)):
        if ints[i] + sums[i-2] > sums[i-1]:
            sums[i] = ints[i] + sums[i-2]
        else:
            sums[i] = sums[i-1]

    return sums[len(sums)-1]

print maxSumWithoutAdj([1,67,1]) # 67
print maxSumWithoutAdj([10,1,1,10]) # 20
print maxSumWithoutAdj([10,1,5,1,10]) # 25
print maxSumWithoutAdj([10,5,1,1,10]) # 21
