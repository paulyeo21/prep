# 31. Next Permutation
#
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
#
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
#
# The replacement must be in-place and use only constant extra memory.
#
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
#
# 1,2,3 → 1,3,2
# 3,2,1 → 1,2,3
# 1,1,5 → 1,5,1

# Find largest index i such that array[i − 1] < array[i].
# (If no such i exists, then this is already the last permutation.)
# Find largest index j such that j ≥ i and array[j] > array[i − 1].
# Swap array[j] and array[i − 1].
# Reverse the suffix starting at array[i].
# T: O(n)
# S: O(1)
def next_permutation(nums)
  i = nums.length-1
  i -= 1 while i > 0 and nums[i-1] >= nums[i]
  return nums.reverse! if i == 0
  j = nums.length-1
  # find largest index j such ath j >= i and array[j] > array[i-1]
  j -= 1 while nums[j] <= nums[i-1]
  # swap pivot
  temp = nums[j]
  nums[j] = nums[i-1]
  nums[i-1] = temp
  # reverse suffix
  j = nums.length-1
  while j > i
    temp = nums[j]
    nums[j] = nums[i]
    nums[i] = temp
    i += 1
    j -= 1
  end
  return nums
end

puts next_permutation([0,1,2,5,3,3,0]).inspect #[0,1,3,0,2,3,5]
puts next_permutation([1,2,3]).inspect #[1,3,2]
puts next_permutation([1,3,2]).inspect #[2,1,3]
puts next_permutation([3,2,1]).inspect #[1,2,3]
puts next_permutation([1,1,5]).inspect #[1,5,1]
puts next_permutation([1,5,1]).inspect #[5,1,1]
puts next_permutation([2,2,0,4,3,1]).inspect #[2,2,1,0,3,4]
puts next_permutation([1,2]).inspect #[2,1]
puts next_permutation([1,3,2]).inspect #[2,1,3]
