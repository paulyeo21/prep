# Median of Two Sorted Arrays
#
# nums1 = [1, 3]
# nums2 = [2]
#
# The median is 2.0
#
# nums1 = [1, 2]
# nums2 = [3, 4]
#
# The median is (2 + 3)/2 = 2.5

# Merge sort two arrays and return median
# T: O(2n + m)
# S: O(n + m)
def find_median_sorted_arrays(nums1, nums2)
  nums = []
  i = 0
  j = 0

  while i < nums1.length and j < nums2.length
    if nums1[i] < nums2[j]
      nums.push(nums1[i])
      i = i + 1
    else
      nums.push(nums2[j])
      j = j + 1
    end
  end

  while i < nums1.length
    nums.push(nums1[i])
    i = i + 1
  end

  while j < nums2.length
    nums.push(nums2[j])
    j = j + 1
  end

  if nums.length.even?
    return (nums[nums.length / 2] + nums[nums.length / 2 - 1]) / 2.0
  else
    return nums[nums.length / 2]
  end
end

# puts find_median_sorted_arrays([1,3], [2])
# puts find_median_sorted_arrays([1,2], [3,4])

# Early termination by only looking up to the median index
# T: O(n/2)
# S: O(1)
def find_median_sorted_arrays(nums1, nums2)
  total_length = nums1.length + nums2.length
  median_index = total_length.even? ? (total_length / 2) + 1 : total_length / 2
  # Get merged array up to median index
  k = 0
  i = 0
  j = 0
  loop do
    if nums1[i] < nums2[j]
      return nums1[i] if k == median_index
      i = i + 1
    else
      return nums2[j] if k == median_index
      j = j + 1
    end
    k = k + 1
  end 
end

# puts find_median_sorted_arrays([1,3], [2])
# puts find_median_sorted_arrays([1,2], [3,4])

# l = [2,4,5] r = [2,2,6,7] sum = [2,2,2,4,5,6,7] output = 4
# We need to find where max(l) <= min(r) with an index i for l and j
# for r where i + j = length of sum - (i + j) or i + j = 7 - i - j + 1.
# We can try different indices such as i = 1 and j = 3 which gets us
# l[1] = 4 and r[3] = 7 but these are not the max(l) <= min(r) because
# if we check r[3-1] = 6 which is > l[1] = 4 so we need to increase
# i until we find max(l) <= min(r) or i = 0, j = 0.
#
# T: O(log n)
# S: O(1)
def find_median_sorted_arrays(a, b)
  n, m = a.length, b.length
  if n > m
    a, b, n, m = b, a, m, n
  end
  imin, imax = 0, n
  while imin <= imax
    i = (imin + imax) / 2
    j = (n + m + 1) / 2 - i
    if i < n and a[i] < b[j-1]
      imin = i + 1
    elsif i > 0 and a[i-1] > b[j]
      imax = i - 1
    else
      if i == 0
        max_of_left = b[j-1]
      elsif j == 0
        max_of_left = a[i-1]
      else
        max_of_left = [a[i-1], b[j-1]].max
      end

      return max_of_left if (n + m) % 2 == 1

      if i == n
        min_of_right = b[j]
      elsif j == m
        min_of_right = a[i]
      else
        min_of_right = [a[i], b[j]].min
      end
      
      return (max_of_left + min_of_right) / 2.0
    end
  end
end

puts find_median_sorted_arrays([2,4,5], [2,2,6,7])
puts find_median_sorted_arrays([1,3], [2])
puts find_median_sorted_arrays([1], [1])
puts find_median_sorted_arrays([1, 2], [3, 4])
