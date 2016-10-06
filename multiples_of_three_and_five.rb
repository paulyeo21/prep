def multiples_of_three_and_five(n)
  sum = 0

  (3..n-1).each do |i|
    if i % 3 == 0 || i % 5 == 0
      sum += i
    end
  end

  sum
end

puts multiples_of_three_and_five(100)
