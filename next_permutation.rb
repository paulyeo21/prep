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

# if all decreasing, return reversed
# if all increasing, switch last with second to last
# else find decreasing point and switch that with previous
def next_permutation(nums)
end

puts next_permutation([1,2,3]) #[1,3,2]
puts next_permutation([3,2,1]) #[1,2,3]
puts next_permutation([1,1,5]) #[1,5,1]
