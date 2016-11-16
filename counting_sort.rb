def counting_sort(array)
  # 1. Create output array
  # 2. Create counting array initialized all to 0
  # 3. Store count of each element in array
  # 4. Modify counting array to store sum of previous counts
  # 5. Build output array

  output = Array.new(array.length)
  counts = Array.new(9, 0)

  for i in array
    counts[i] += 1
  end

  (1..counts.length-1).each do |i|
    counts[i] += counts[i - 1] 
  end
  
  (0..array.length-1).each do |i|
    output[counts[array[i]] - 1] = array[i]
    counts[array[i]] -= 1
  end

  return output.inspect
end

array = [1, 4, 1, 2, 7, 5, 2]
puts counting_sort(array)
