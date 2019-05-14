# Given an amount and a list of denominations,
# return the number of unique ways to make the
# amount with the denominations.

def denomination_permutations(amount, denoms):
    # Base case when amount == 0, we found a way.
    # Can be duplicates like [1,1,2] == [1,2,1] == [2,1,1]
    # From the highest denomination to the lowest decrease
    # amount. If amount == 0, add to number of ways, if
    # amount < 0, don't add to number of ways. Either way
    # move on to next denomination. Continue until no more denominations
    # T: O(n * m)
    # S: 

    if amount == 0:
        return 1

    if amount < 0:
        return 0

    print 'checking ways to make %i with %s' % (amount, denoms)

    denoms.sort(reverse=True)
    number_of_permutations = 0

    for i in xrange(len(denoms)):
        number_of_permutations += denomination_permutations(amount - denoms[i], denoms[i:])

    return number_of_permutations

print denomination_permutations(4, [1,2,3]) # [4]... [1,1,1,1], [1,1,2], [1,3], [2,2]
print denomination_permutations(4, [])
print denomination_permutations(4, [10])
