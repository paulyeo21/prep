def which_appears_twice(numbers, n)
  real_sum = (n*n + n) / 2 
  actual_sum = 0
  for number in numbers
    actual_sum += number
  end
  return actual_sum - real_sum
end

numbers = [1, 2, 3, 4, 4, 5]
puts which_appears_twice(numbers, 5)
