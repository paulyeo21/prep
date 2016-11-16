"""
    Given a non-empty integer array of size n, find the minimum 
    number of moves required to make all array elements equal, 
    where a move is incrementing n - 1 elements by 1.
"""
def equal(nums):
    previous = nums[0]
    for current in nums[1:]:
        if previous != current:
            return False
    return True

def indexOfMax(nums):
    maximum = nums[0]
    index = 0 
    for i in range(1, len(nums)):
        if nums[i] > maximum:
            maximum = nums[i]
            index = i
    return index

# def minimumMoves(nums):
#     moves = 0
#     index_of_max = indexOfMax(nums)
#     while not equal(nums):
#         for i in range(len(nums)):
#             if i != index_of_max:
#                 nums[i] += 1
#         moves += 1
#         index_of_max = indexOfMax(nums)
#     return moves

def minimumMoves(nums):
    return sum(nums) - min(nums) * len(nums)

print(minimumMoves([1, 2, 3]))
