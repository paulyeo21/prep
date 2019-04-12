# For each merge we look at two subarrays and check head of each until we form a 
# sorted array. The time complexity for this is the sum of the lengths of the two
# subarrays. T: O(i+j) or O(k). Depending on the size of the subarray we run this
# merge function x times, because say we are merging subarrays of size 1 then we know
# we are at the most broken up length of the input so we merge the subarrays of size 
# 1 x times. We also know that the subarray sizes will be n/x , because if input size
# n is 8 and we are merging subarrays of length 1, so we merge which is time complexity
# of O(n/x) x times which is O(n) for each subarray size. We know there are (log2 n) + 1
# subarray sizes, because we divide input length n half every time which is the height
# of a tree. so T: O(n * (log2 n) + 1) which is O(n log n). Space complexity is same
# because for every merge we create a merged array the size of the sum of two subarrays.
#
def merge_sort(list)
  return list if list.length == 1
  left = merge_sort(list[0..list.length/2-1])
  right = merge_sort(list[list.length/2..-1])
  # merge
  merged = []
  i, j, k = 0, 0, 0
  while i < left.length and j < right.length
    if left[i] < right[j]
      merged.push(left[i])
      i += 1
    else
      merged.push(right[j])
      j += 1
    end
    k += 1
  end
  while i < left.length
    merged.push(left[i])
    i += 1
    k += 1
  end
  while j < right.length
    merged.push(right[j])
    j += 1
    k += 1
  end
  return merged
end

list = [54, 29, 91, 17, 77, 31]
list1 = [54, 29, 91, 17, 77]
puts merge_sort(list).inspect
puts merge_sort(list1).inspect
