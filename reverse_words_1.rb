# Reverse order of the words in place
# "cake pound steal" => "steal pound cake"

# T: O(n)
# S: O(1)
def reverse_words!(message)
  # 1. check if multiple words
  # 2. for whole message reverse chars
  # 3. for each word
  #    reverse chars
  def reverse!(s, left, right)
    while left < right
      s[left], s[right] = s[right], s[left]
      left += 1
      right -= 1
    end
  end

  reverse!(message, 0, message.length-1)

  i, j = 0, 1
  while i < message.length - 1
    if message[j] == " " or j == message.length
      reverse!(message, i, j-1)
      i = j + 1
    end
    j += 1
  end

  message.inspect
end

puts reverse_words!("cake") # "cake"
puts reverse_words!("cake steal") # "steal cake"
puts reverse_words!("cake pound steal") # "steal pound cake
puts reverse_words!("") # ""
