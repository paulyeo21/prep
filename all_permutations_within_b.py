# Given two strings, a and b, find all permutations of
# a within b.

def allPermutationsWithinB(a, b):
    # Get all permutations of a and for each permutation pattern match
    # with b to find all permutations of within b. To get all permutations of a,
    # T: O(n!) n is length of a. For each permutation check if exists in b.
    # T: O(n! * n * m) where n is length of a and m is length of b.

print allPermutationsWithinB('abc', 'abcdefgbac')
