# Given an array A of integers, return true if and only if we can partition the array into three non-empty parts with equal sums.
#
# Formally, we can partition the array if we can find indexes i+1 < j with (A[0] + A[1] + ... + A[i] == A[i+1] + A[i+2] + ... + A[j-1] == A[j] + A[j-1] + ... + A[A.length - 1])
#
#  
#
#  Example 1:
#
#  Input: [0,2,1,-6,6,-7,9,1,2,0,1]
#  Output: true
#  Explanation: 0 + 2 + 1 = -6 + 6 - 7 + 9 + 1 = 2 + 0 + 1
#  Example 2:
#
#  Input: [0,2,1,-6,6,7,9,-1,2,0,1]
#  Output: false
#  Example 3:
#
#  Input: [3,3,6,5,-2,2,5,1,-9,4]
#  Output: true
#  Explanation: 3 + 3 = 6 = 5 - 2 + 2 + 5 + 1 - 9 + 4

# Greedy algo, sum until we get desired partition size, then reset until we hit all three
# partitions. if we have numbers left over then we return false. 
# T: O(n)
# S: O(1)
def can_three_parts_equal_sum(a)
  sum = a.reduce(0, :+)
  return false if sum % 3 != 0 # sum must be divisible by 3
  desired_partition = sum / 3
  current_partition = 0
  num_partitions = 0
  a.each do |num|
    current_partition += num
    if current_partition == desired_partition
      current_partition = 0
      num_partitions += 1
    end
  end
  return num_partitions == 3 ? true : false
end

puts can_three_parts_equal_sum([0,2,1,-6,6,-7,9,1,2,0,1]) == true
puts can_three_parts_equal_sum([3,3,6,5,-2,2,5,1,-9,4]) == true
puts can_three_parts_equal_sum([3, -3, 3, 3, 3]) == true
puts can_three_parts_equal_sum([0,2,1,-6,6,7,9,-1,2,0,1]) == false
