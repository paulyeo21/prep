# Quicksort

def partition(arr, low, high)

end

def quicksort(arr, low, high)
  if low < high
    p = partition(arr, low, high)
    quicksort(arr, low, p - 1)
    quicksort(arr, p + 1, high)
  end
end

puts quicksort([10, 80, 30, 90, 40, 50, 70], 0, 6)
