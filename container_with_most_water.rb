#11. Container With Most Water
#
#Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
#
#Note: You may not slant the container and n is at least 2.
#
#Input: [1,8,6,2,5,4,8,3,7]
#Output: 49

# Area = min(a[i], a[j]) * (j - i)
# Brute force check each pair and log max
# T: O(n**2)
# S: O(1)
def max_area(height)
  max_area = [height[0], height[1]].min
  (0..height.length-2).each do |i|
    (i+1..height.length-1).each do |j|
      area = [height[i], height[j]].min * (j-i)
      max_area = [max_area, area].max
    end
  end
  return max_area
end

# Given the formula Area = min(a[i], a[j]) * (j - i)
# We start at the ends, i = 0 j = length - 1. We know that
# the area is the min of a[i] a[j] so we compare a[i] and a[j]
# and move i or j depending on what is less. if a[i] is < a[j]
# move i += 1 otherwise j -= 1. This works because were checking
# the highest min(a[i], a[j]) for each pair at the max distance
# (j - i). 
# T: O(n)
# S: O(1)
def area(height, i, j)
  return [height[i], height[j]].min * (j-i)
end

def max_area(height)
  max_area = area(height, 0, height.length-1)
  left = 0
  right = height.length-1
  while left < right
    max_area = [max_area, area(height, left, right)].max
    if height[left] < height[right]
      left += 1
    else
      right -= 1
    end
  end
  return max_area
end

puts max_area([1,8,6,2,5,4,8,3,7]) == 49
puts max_area([2,3,9]) == 4

