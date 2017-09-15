# Get all permutations of a string

def permutations(string):
    permutations = [string[0]]
    for char in string[1:]:
        temp_permutations = []
        for p in permutations:
            for i in xrange(len(p) + 1):
                temp_permutations.append(p[:i] + char + p[i:])
        permutations = temp_permutations
    return permutations

print permutations("ab")
print permutations("abc")
