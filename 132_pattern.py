"""
    Given a sequence of n integers a1, a2, ..., an, a 132 pattern is a subsequence ai, aj, ak 
    such that i < j < k and ai < ak < aj. Design an algorithm that takes a list of n 
    numbers as input and checks whether there is a 132 pattern in the list.
"""
def find132Pattern(nums):
    if len(nums) < 3:
        return False

    # Brute force: check each three numbers O(n^3)
    # for i in range(len(nums) - 2):
    #     ai = nums[i]
    #     for j in range(i + 1, len(nums) - 1):
    #         aj = nums[j]
    #         if aj <= ai: # aj must be greater than ai
    #             continue
    #         for k in range(j + 1, len(nums)):
    #             ak = nums[k]
    #             if ak <= ai:
    #                 continue
    #             if ak < aj:
    #                 return True
    # return False

    # Two pointers O(n^2)
    # for i in range(len(nums) - 2):
    #     ai = nums[i]
    #     aj = None
    #     flag = False
    #     for j in range(i + 1, len(nums)):
    #         current = nums[j]
    #         if aj and current < aj and current > ai and flag:
    #             return True
    #         if current > ai:
    #             flag = True
    #             aj = current
    # return False

    # O(n)

    # Forward scan get minimums
    minimums = nums
    for i in range(1, len(nums)):
        minimums[i] = min(minimums[i - 1], nums[i - 1])
    print minimums

# print find132Pattern([1, 2, 3, 4])
print find132Pattern([3, 1, 4, 2])
# print find132Pattern([-1, 3, 2, 0])
# print find132Pattern([1,0,1,-4,-3])
# print find132Pattern([-2, 1, -2])
