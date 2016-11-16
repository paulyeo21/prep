def product_of_other_numbers(numbers)
  products = []
  (0..numbers.length-1).each do |i|
    product = 1
    (0..numbers.length-1).each do |j|
      if i != j
        product *= numbers[j]
      end
    end
    products[i] = product
  end

  return products.inspect
end

numbers = [1, 7, 3, 4]
numbers1 = [0, 7, 1, 4]
puts product_of_other_numbers(numbers)
puts product_of_other_numbers(numbers1)

def product_of_other_numbers_fast(numbers)
  output = []
  product = 1
  (0..numbers.length-1).each do |i|
    output[i] = product
    product *= numbers[i]
  end

  product = 1
  (0..numbers.length-1).each do |j|
    output[numbers.length-1-j] *= product
    product *= numbers[numbers.length-1-j]
  end

  return output.inspect
end

puts product_of_other_numbers_fast(numbers)
puts product_of_other_numbers_fast(numbers1)
