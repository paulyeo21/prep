# 27. Remove Element
#
# Given an array nums and a value val, remove all instances of that value in-place 
# and return the new length.
#
# Do not allocate extra space for another array, you must do this by modifying the 
# input array in-place with O(1) extra memory.
#
# The order of elements can be changed. It doesn't matter what you leave beyond the 
# new length.

def remove_element(nums, val)
  counter = 0
  nums.each do |num|
    if val != num
      nums[counter] = num
      counter += 1
    end
  end
  return counter
end

a = [3,2,2,3]
puts remove_element(a, 3) #2

b = [0,1,2,2,3,0,4,2]
puts remove_element(b, 2) #5
