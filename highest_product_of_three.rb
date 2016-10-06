def highest_product_of_three(numbers)
  highest = numbers[0]
  highest_product_of_two = numbers[0] * numbers[1]
  lowest_product_of_two = numbers[0] * numbers[1]
  highest_product_of_three = numbers[0] * numbers[1] * numbers[2]

  for number in numbers[3..-1]
    if highest_product_of_two * number > highest_product_of_three
      highest_product_of_three = highest_product_of_two * number
    elsif lowest_product_of_two * number > highest_product_of_three
      highest_product_of_three = lowest_product_of_two * number
    end

    if highest * number > highest_product_of_two
      highest_product_of_two = highest * number
    elsif highest * number < lowest_product_of_two
      lowest_product_of_two = highest * number
    end

    highest = number if number > highest
  end

  return highest_product_of_three
end

numbers = [1, 7, 3, 4]
numbers1 = [-1, -1, 10, 100, 0]
puts highest_product_of_three(numbers)
puts highest_product_of_three(numbers1)
