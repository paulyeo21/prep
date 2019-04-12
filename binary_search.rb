# Binary Search
#
# Check mid point of input list if the element is equal to key. If not equal then 
# find whether mid point is less than or greater than key. If greater than key,
# then we know that key exists on left half, so repeat with left half of input. 
# Do this until we find key that matches or return nil for not found.
#
# Time complexity is log2 n, because worst case scenario we find key as last element
# when the half is length of 1, this requires cutting the input size in half each
# time until length of 1, which is (log2 n) + 1.
#
# T: O(log2 n)
# S: O(1)
def binary_search(key, list, left, right)
  index = (left + right) / 2
  mid = list[index]

  if key == mid
    return index
  elsif key < mid
    binary_search(key, list, 0, index)
  else
    binary_search(key, list, index + 1, list.length - 1)
  end
end

# l = [1, 2, 3, 4]
# j = [1, 2, 3]
# puts binary_search(2, l)
# puts binary_search(4, l)
# puts binary_search(3, l, 0, l.length - 1)
# puts binary_search(1, j, 0, j.length - 1)
# puts binary_search(2, j, 0, j.length - 1)
# puts binary_search(3, j, 0, j.length - 1)
