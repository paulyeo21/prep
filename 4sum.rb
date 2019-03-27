# 18. 4Sum
#
# Given an array nums of n integers and an integer target, are there elements 
# a, b, c, and d in nums such that a + b + c + d = target? Find all unique 
# quadruplets in the array which gives the sum of target.
#
# Note:
# The solution set must not contain duplicate quadruplets.
#
# Example:
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

# Brute force method by checking all quadruplets is
# T: O(n**4)
# S: O(1)
#
# [-2, -1, 0, 0, 1, 2] Sort the array of numbers, take the first two elements and then
# use i and j as i = index after second element and j as last element and close in on
# target sum. If sum is > target then decrease j otherwise increase i. This should get
# us T: O(n**3) S: O()
def four_sum(nums, target)
  output = []
  nums.sort!
  (0..nums.length-4).each do |i|
    next if i > 0 and nums[i] == nums[i-1]
    (i+1..nums.length-3).each do |j|
      next if j-1 != i and nums[j] == nums[j-1]
      l = j+1
      r = nums.length-1
      while l < r
        s = nums[i] + nums[j] + nums[l] + nums[r]
        if s == target
          output.push([nums[i], nums[j], nums[l], nums[r]])
          l += 1
          r -= 1
          while nums[l] == nums[l-1]
            l += 1
          end
          while nums[r] == nums[r+1]
            r -= 1
          end
        elsif s < target
          l += 1
        else
          r -= 1
        end
      end
    end
  end
  return output
end

# [-2, -1, 0, 0, 1, 2]
puts four_sum([1, 0, -1, 0, -2, 2], 0).inspect # [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]
# [-4, -1, -1, 0, 1, 2]
puts four_sum([-1, 0, 1, 2, -1, -4], -1).inspect # [[-4, 0, 1, 2], [-1, -1, 0, 1]]

