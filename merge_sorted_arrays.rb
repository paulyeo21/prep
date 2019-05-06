# Merge sorted arrays

# T: O(n+m) = O(n)
# S: O(n+m) = O(n)
def merge_arrays(a, b)
  output = []
  i, j = 0, 0
  while i < a.length and j < b.length
    if a[i] <= b[j]
      output << a[i]
      i += 1
    else
      output << b[j]
      j += 1
    end
  end

  while i < a.length
    output << a[i]
    i += 1
  end

  while j < b.length
    output << b[j]
    j += 1
  end

  output.inspect
end

puts merge_arrays([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19]) # [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
