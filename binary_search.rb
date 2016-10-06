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
