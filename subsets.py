# 78 Subsets

# Given a set of distinct integers return all possible subsets.

def all_subsets(ints):
    # Backtracking to find all subsets
    # T: O(2**n), S: O(2**n)

    if len(ints) == 0:
        return [[]]

    num = ints[-1]
    subsets = all_subsets(ints[:-1])

    new_subsets = []
    for subset in subsets:
        new_subsets.append(subset + [num])
    subsets += new_subsets

    return subsets

print all_subsets([]) # [[]]
print all_subsets([1]) # [[],[1]]
print all_subsets([1,2]) # [[],[1],[2],[1,2]]
print all_subsets([1,2,3]) # [[],[1],[2],[3],[1,2],[1,3],[2,3],[1,2,3]]
