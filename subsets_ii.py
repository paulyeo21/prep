# 90. Subsets II

# Given a list of integers that might contain duplicates, return
# the power set (all possible subsets).

def subsets(ints):
    # T/S: O(2**n)
    # Naive solution would be to produce all subsets given a list of integers
    # without considering duplicates, and check if subset exists before adding 
    # a subset.

    # base case is if len(ints) == 0 return [[]]
    # otherwise take one int and recursively take remaining

    ints = sorted(ints)

    if len(ints) == 0:
        return [[]]

    current_int = ints[-1]
    current_subsets = subsets(ints[:-1])

    new_subsets = []
    for subset in current_subsets:
        # new_subset = sorted(subset + [current_int])
        new_subset = subset + [current_int]
        if new_subset not in current_subsets:
            new_subsets.append(new_subset)
    current_subsets += new_subsets

    return current_subsets

print subsets([2]) # [[],[2]]
print subsets([2,2]) # [[],[2],[2,2]]
print subsets([1,2,2]) # [[],[1],[2],[1,2],[2,2],[1,2,2]]
print subsets([4,4,4,1,4])
