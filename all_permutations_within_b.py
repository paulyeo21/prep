# Given two strings, a and b, find all permutations of
# a within b.

def allPermutationsWithinB(a, b):
    # Get all permutations of a.
    # T: O(n!) n is length of a.
    # For each permutation check if exists in b.
    # T: O(n! * m) m is length of b.

print allPermutationsWithinB('abc', 'abcdefgbac')
