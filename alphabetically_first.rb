def alphabetically_first_recursive(array, low, high)
  index = (low + high) / 2

  if array[index] > array[index + 1]
    return index + 1
  elsif array[low] < array[high]
    alphabetically_first(array, low, index - 1)
  else
    alphabetically_first(array, index + 1, high)
  end
end

def alphabetically_first_iterative(array)
  low = 0
  high = array.length - 1
  index = (low + high) / 2

  while index > 0
    if array[index] > array[index + 1]
      return index + 1
    elsif array[low] < array[high]
      high = index - 1
    else
      low = index + 1
    end

    index = (low + high) /2
  end
end

words = [
  "retrograde",
  "supplant",
  "undulate",
  "xenoepist",
  "asymptote", # <-- rotates here!
  "babka",
]

puts alphabetically_first_recursive(words, 0, words.length - 1)
