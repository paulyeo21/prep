# Given a set of non-negative integers and a value sum, determine if
# there is a subset of the given set with sum equal to given sum.

def subsetSumExists(ints, target_sum):
    # Naive: Generate all subsets of given set and check sum.
    # If sum equals target sum, return True. If end return False
    # T: O(2**n)
    # S: O(2**n)

    subsets = subsetSumExistsHelper(ints)
    for subset in subsets:
        if sum(subset) == target_sum:
            return True

    return False

def subsetSumExistsHelper(ints):

    if len(ints) == 0:
        return [[]]

    current_int = ints[-1]
    subsets = subsetSumExistsHelper(ints[:-1])

    new_subsets = []
    for subset in subsets:
        new_subsets.append(subset + [current_int])

    return subsets + new_subsets

def isSubsetSum(ints, n, target_sum):
    # We can get all subsets if we continually shrink our set by subtracting
    # the last element from the sum. We also need to consider cases when
    # one element can be the whole sum so recurse for sets with same sum
    # but excluding the last element. For instance, if we have the set
    # [1,2,3,4,10] and sum 10, we should try [2,3,4,10] sum 10 and 
    # [2,3,4,10] sum 9 and continue this. We will hit the case [10] sum 0
    # and [] sum 0, which both represent the subset [1,2,3,4] and [10] as
    # valid subsets that sum to 10.
    # T: O(2**n)
    # S: O(1)

    if target_sum == 0:
        return True
    if len(ints) == 0 and target_sum != 0:
        return False

    if ints[-1] > target_sum:
        return isSubsetSum(ints[:-1], n-1, target_sum)

    return isSubsetSum(ints[:-1], n-1, target_sum) or \
            isSubsetSum(ints[:-1], n-1, target_sum - ints[-1])

def isSubsetSum(ints, n, target_sum):
    # Solve this using dynamic programming. The crux of the algorithm
    # still stays the same, if we can get the sum to equal 0, we know that
    # a subset exists that equals the sum. As we iterate over the elements
    # we want to consider 1) if the current number we're at is greater
    # than the sum, don't include that number in our attempts to find
    # a subset that equals the sum. 2) if the current number is less than
    # or equal to the sum, then include that numbe by subtracting the sum
    # by the number and trying the subsets without the current number,
    # otherwise try the same sum without including the current number
    # in the subsets we're trying. For this case two examples can explain
    # why it is the case. If we are given the set [3,34,4,7] and the sum
    # is 7, we know that the subsets [3,4] and [7] can yield True. As
    # we iterate over the elements and arrive at 3, we want the algorithm
    # to continue to try other subsets with the sum - 3 so that we try
    # 4 with the sum at 4 which would yield a sum = 0. In other cases, we
    # also want to try just 7 when sum is 7. So what this example
    # illustrates is that when at element 3, we want to try sum - 3 with
    # other subsets without 3 (this would find us the scenario when [4]
    # and sum is 4) as well as sum without being touched with other 
    # subsets (this would yield us to get [7]).
    # The dynamic programming setup is create a matrix that is n x m
    # where n is the sum and m is the number of elements in the set. 
    # For an element matrix[i][j], i represents the current element
# while j represents the sum we're checking for.
    # T: O(n * m) where n is the sum and m is the # of elements in the set.
    # S: O(n * m)

    matrix = [[False for i in range(target_sum+1)] for i in range(n+1)]
    matrix[0][0] = True

    # j represents the sum
    for j in range(1, target_sum+1):
        matrix[0][j] = False # i = 0 means when no empty subset and 
                             # j != 0 means when sum is not 0, which is
                             # always False

        for i in range(1, n+1):
            matrix[i][0] = True # if j = 0, meaning sum is 0 then we have
                                 # found a solution.

            if ints[i-1] > j:
                # if current element is greater than sum
                # that means too big of a number, so try
                # subsets without that number

                matrix[i][j] = matrix[i-1][j]
            else:
                # if current element is less than or equal to sum we
                # are looking for, then see if subsets with sum minus
                # the number we're at yields a subset that equals true
                # or if we exclude the number and the same sum yields
                # true.

                matrix[i][j] = matrix[i-1][j] or matrix[i-1][j - ints[i-1]]

    return matrix[n][target_sum]

# print subsetSumExists([3, 34, 4, 12, 5, 2], 9) # True
print isSubsetSum([3, 34, 4, 12, 5, 2], 6, 9) # True
