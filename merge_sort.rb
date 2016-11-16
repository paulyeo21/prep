def merge_sort(list)
  # puts "Before sorting: #{list.inspect}"
  if list.length > 1
    mid = list.length / 2
    left = list[0, mid]
    right = list[mid, list.length - 1]

    merge_sort(left)
    merge_sort(right)

    # puts "Left: #{left}"
    # puts "Right: #{right}"

    i, j, k = 0, 0, 0
    while i < left.length and j < right.length
      if left[i] < right[j]
        list[k] = left[i]
        i += 1
      else
        list[k] = right[j]
        j += 1
      end
      k += 1
    end

    while i < left.length
      list[k] = left[i]
      i += 1
      k += 1
    end

    while j < right.length
      list[k] = right[j]
      j += 1
      k += 1
    end

    # puts "After sorting: #{list.inspect}"
  end

  return list.inspect
end

list = [54, 29, 91, 17, 77, 31]
list1 = [54, 29, 91, 17, 77]
puts merge_sort(list)
puts merge_sort(list1)
