# "civic" => true
# "ivicc" => true
# "civil" => false
# "livci" => false

# Not permutation palindrome if at least a character has odd number of
# occurrences, except if one character has one occurrence.
# T: O(n)
# S: O(n)
def any_permutation_palindrome?(s)
  # 1. use hash to get counts of all characters
  # 2. check all key, value pairs to see if any
  #    counts are odd and not one or more than
  #    one key, value pair is odd. 
  counts = {}
  (0..s.length-1).each do |i|
    if counts.key?(s[i])
      counts[s[i]] += 1
    else
      counts[s[i]] = 1
    end
  end

  odd_flag = false
  for k, v in counts
    if v % 2 != 0
      return false if odd_flag
      odd_flag = true
    end
  end

  true
end

# Use a set to keep track of unpaired characters. If
# the number of unpaired characters is less than 2, 
# that fits our criteria for a permutation palindrome, so true.
#
# Set efficiency O(1)
# Using a set to delete and add is O(1), because deleting
# we would hash the input and free up memory. Adding would
# hash the input and add the content. No need to shift like arrays.
def has_palindrome_permutation?(s)
  unpaired_characters = Set.new
  (0..s.length-1).each do |i|
    char = s[i]
    if unpaired_characters.include?(char)
      unpaired_characters.delete(char)
    else
      unpaired_characters.add(char)
    end
  end

  return unpaired_characters.length <= 1
end

puts any_permutation_palindrome?("civic") # true
puts any_permutation_palindrome?("ccvcc") # true
puts any_permutation_palindrome?("cvcc") # false
puts any_permutation_palindrome?("ivicc") # true
puts any_permutation_palindrome?("civil") # false
puts any_permutation_palindrome?("livci") # false
