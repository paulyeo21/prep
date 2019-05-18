# 47. Permutations II

# Similar to finding all permutations, given a list of integers
# that may contain duplicates, return all possible unique permutations.

class Solution:
    def __init__(self):
        self.memo = {}

    def getDistinct(self, nums):
        distinct = {}
        repeats = []
        for num in nums:
            if num not in distinct:
                distinct[num] = True
            else:
                repeats.append(num)
        return (list(distinct.keys()), repeats)

    def permuteUnique(self, nums):
        # T/S: O(n!)

        # Get distinct integers and like finding all permutations without
        # duplicates, get all permutations with those integers. Use memoization
        # to not recompute duplicates. The memoization will take length of
        # permutation, index which is the insertion position, and the current integer.

        # base case if len(ints) == 0 return [[]]
        # take one number and recursively take remaining

        distincts, repeats = self.getDistinct(nums)
        current_permutations = self.permute(distincts)

        print repeats, current_permutations, self.memo

        for current_num in repeats:
            new_permutations = []
            for permutation in current_permutations:
                for i in range(len(permutation)+1):
                    print current_num, permutation, i, self.memo

                    if current_num not in self.memo or self.memo[current_num] != (permutation, i):
                        new_permutations.append(permutation[:i] + [current_num] + permutation[i:])
                        self.memo[current_num] = (permutation, i)
            current_permutations = new_permutations

        return current_permutations

    def permute(self, nums):
        if len(nums) == 0:
            return [[]]

        current_num = nums[0]
        current_permutations = self.permute(nums[1:])

        print self.memo

        new_permutations = []
        for permutation in current_permutations:
            for i in range(len(permutation)+1):
                if current_num not in self.memo or self.memo[current_num] != (permutation, i):
                    new_permutations.append(permutation[:i] + [current_num] + permutation[i:])
                    self.memo[current_num] = (permutation, i)

        return new_permutations

# s = Solution()
# print s.permuteUnique([1,2]) # [[1,2],[2,1]]
s = Solution()
print s.permuteUnique([1,1,2]) # [[1,1,2],[1,2,1],[2,1,1]]
# s = Solution()
# print permutationsUnique([1,1,2,2]) # [[2,1,1,2],[1,2,1,2],[1,1,2,2],[2,1,2,1],[1,2,2,1]]
