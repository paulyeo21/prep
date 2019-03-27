# 15. 3Sum
#
# Given an array nums of n integers, are there elements a, b, c in nums 
# such that a + b + c = 0? Find all unique triplets in the array which 
# gives the sum of zero.
#
# Note:
# The solution set must not contain duplicate triplets.
#
# Example:
# Given array nums = [-1, 0, 1, 2, -1, -4],
#
# A solution set is:
# [
#   [-1, 0, 1],
#   [-1, -1, 2]
# ]

# Sort nums increasing order [-4, -1, -1, 0, 1, 2] 
# For each number say -4 look at subset [-1, -1, 0, 1, 2] and check starting from
# outside in i=0 j=length-1 if a sum exists that is = opposite of -4. If sum is
# less than what is needed then increase i otherwise decrease j.
# T: O(n**2)
# S: O(1)
require "set"
def three_sum(nums)
  nums.sort!
  output = []
  return output if nums.length < 3
  return output if nums[0] > 0
  return output if nums[nums.length-1] < 0
  (0..nums.length-3).each do |i|
    next if i > 0 and nums[i] == nums[i-1]
    left = i+1
    right = nums.length-1
    while left < right
      sum = nums[i] + nums[left] + nums[right]
      if sum == 0
        output.push([nums[i], nums[left], nums[right]])
        left += 1
        right -= 1
        while left < right and nums[left] == nums[left-1]
          left += 1
        end
        while left > right and nums[right] == nums[right+1]
          right -= 1
        end
      elsif sum < 0
        left += 1
      else
        right -= 1
      end
    end
  end
  return output
end

puts three_sum([-1, 0, 1, 2, -1, -4]).inspect # [[-1,0,1],[-1,-1,2]]
puts three_sum([0, 0, 0, 0]).inspect # [[0,0,0]]
puts three_sum([]).inspect # []
puts three_sum([0]).inspect # []
puts three_sum([1,-1,-1,0]).inspect # [[-1,0,1]]
puts three_sum([-1,0,1,0]).inspect # [[-1,0,1]]
