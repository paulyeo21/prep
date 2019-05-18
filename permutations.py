# Get all permutations of a string

# def permutations(string):
#     permutations = [string[0]]
#     for char in string[1:]:
#         temp_permutations = []
#         for p in permutations:
#             for i in xrange(len(p) + 1):
#                 temp_permutations.append(p[:i] + char + p[i:])
#         permutations = temp_permutations
#     return permutations

# print permutations("ab")
# print permutations("abc")

##
# 46. Permutations

# Given a list of integers, return all possible permutations.

def permutations(ints):
    # T/S: O(n!)
    # Similar to getting the powerset of a given set, use backtracking,
    # but instead of combining the subsets found at each recursive level,
    # take each permutation and try current number at each possible position
    # left and right to existing numbers. For instance, if permutation is [1,2]
    # and current number is 3, we should get [3,1,2], [1,3,2], [1,2,3].

    # base case if len(ints) == 0 return [[]]
    # take current number and recurse over remaining

    if len(ints) == 0:
        return [[]]

    current_int = ints[-1]
    current_permutations = permutations(ints[:-1])

    new_permutations = []
    for permutation in current_permutations:
        for i in range(len(permutation)+1): # [1,2] should yield 3
            new_permutations.append(permutation[:i] + [current_int] + permutation[i:])

    return new_permutations

print permutations([1,2,3]) # [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
