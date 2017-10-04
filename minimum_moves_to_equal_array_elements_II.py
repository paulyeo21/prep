"""
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.
"""
def minMoves2(nums):
    moves = 0
    nums = sorted(nums)
    if len(nums) % 2 == 0:
        median = nums[(len(nums) / 2) - 1]
    else:
        median = nums[len(nums) / 2]
    for num in nums:
        moves += abs(median - num)
    return moves

print(minMoves2([1, 2, 3]))
