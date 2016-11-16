def reverse_words(words)
  words = words.split(" ")
  length = words.length
  (0..(length / 2)-1).each do |i|
    temp = words[i]
    words[i] = words[length - i - 1]
    words[length - i - 1] = temp
  end
  words.join(" ")
end

puts reverse_words("find will you one the")
