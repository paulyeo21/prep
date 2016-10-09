def merged_arrays(first, second)
  i, j, k = 0, 0, 0
  merged = []

  while i < first.length-1 and j < second.length-1
    if first[i] < second[j]
      merged[k] = first[i]
      i += 1
    else
      merged[k] = second[j]
      j += 1
    end
    k += 1
  end

  while i < first.length-1
    merged[k] = first[i]
    i += 1
    k += 1
  end

  while j < second.length-1
    merged[k] = second[j]
    j += 1
    k += 1
  end

  return merged.inspect
end

first = [3, 4, 6, 10, 11, 15]
second = [1, 5, 8, 12, 14, 19]
puts merged_arrays(first, second)
