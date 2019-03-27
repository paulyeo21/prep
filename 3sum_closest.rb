# 16. 3Sum Closest
#
# Given an array nums of n integers and an integer target, find three integers in 
# nums such that the sum is closest to target. Return the sum of the three integers. 
# You may assume that each input would have exactly one solution.
#
# Example:
# Given array nums = [-1, 2, 1, -4], and target = 1.
#
# The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

# Brute force yields T: O(n**3).
def three_sum_closest(nums, target)
  closest_s = nums[0] + nums[1] + nums[2]
  (0..nums.length-3).each do |i|
    (i+1..nums.length-2).each do |j|
      (j+1..nums.length-1).each do |k|
        s = nums[i] + nums[j] + nums[k]
        closest_s = s if (target - s).abs < (target - closest_s).abs
      end
    end
  end
  return closest_s
end

# [-4, -1, 1, 2] Sort input iterate over element lets call it a[i]. Check all pairs
# i+1 (we'll call l) to length of input (r). If s = a[i] + a[l] + a[r] < target,
# increase l otherwise decrease r. This will allow us to track all triplets to find closest
# sum in O(n**2)
# T: O(n**2)
# S: O(1)
def three_sum_closest(nums, t)
  nums.sort!
  closest = nums[0] + nums[1] + nums[2]
  (0..nums.length-3).each do |i|
    l = i+1
    r = nums.length-1
    while l < r
      s = nums[i] + nums[l] + nums[r]
      return t if s == t
      s < t ? l += 1 : r -= 1
      closest = s if (t - s).abs < (t - closest).abs
    end
  end
  return closest
end

puts three_sum_closest([-1,2,1,-4], 1) # 2
puts three_sum_closest([0,2,1,-3], 1) # 0
puts three_sum_closest([1,1,-1,-1,3], -1) # -1
puts three_sum_closest([-3,-2,-5,3,-4], -1) # -2 [-5, -4, -3, -2, 3]
