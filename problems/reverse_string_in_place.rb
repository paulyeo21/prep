def reverse_in_place(string)
  length = string.length
  (0..(length / 2)-1).each do |i|
    temp = string[i]
    string[i] = string[length - i - 1]
    string[length -i - 1] = temp
  end
  string
end

puts reverse_in_place("string")
puts reverse_in_place("dada")
