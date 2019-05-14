# Given an input string, return all permutations as a set.

# Our approach is separately for each character, fill the length of
# the string with characters that haven't been used. So for instance,
# for input 'abc', we would start with 'a', 'b', and 'c'. Then for say
# 'a', we would want to append unused characters which are either
# 'b' or 'c', so we get 'ab' and 'ac'. Then for 'ab' we have 'c' left
# so we end up with 'abc' and similarly for 'ac' we have 'b' left so
# we get 'acb'. Do this for all bases and we get all permutations.
# T: O(n!)
# S: O(n!)

def all_permutations(s):
    # starting with 'a', given 'b' we want to put 'b' in every possible
    # index of 'a'. so we get 'ba' and 'ab'. For 'c' we do the same
    # for every permutation. we get 'cba', 'bca', and 'bac' for 'ba' and
    # 'cab', 'acb', and 'abc' for 'ab'.
    # T: O(n!)
    # S: O(n!)

    permutations = set()

    for char in s:
        if not permutations:
            permutations.add(char)
        else:
            new_permutations = set()
            for permutation in permutations:
                for i in xrange(len(permutation) + 1): # 'a' two spots
                                                       # 'ba' three spots
                    new_permutations.add(permutation[:i] + char \
                            + permutation[i:])
            permutations = new_permutations

    return permutations

# recursively
def all_permutations(s):
    # iterate over permutations and create new permutation by placing
    # current character on each possible 'spot'. at each recursion level 
    # return permutations.
    # T: O(n!)
    # S: O(n!)

    if not s:
        return ['']

    perms = all_permutations(s[1:])
    output = []
    for perm in perms:
        for i in xrange(len(perm) + 1):
            output.append(perm[:i] + s[0] + perm[i:])

    return output

print all_permutations('abc') # ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
print all_permutations('ab') # ['ab', 'ba']

