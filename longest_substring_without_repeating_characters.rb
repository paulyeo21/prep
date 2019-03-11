# Longest Substring Without Repeating Characters
#
# Input: "abcabcbb"
# Output: 3 
# Explanation: The answer is "abc", with the length of 3. 

# T: O(n^2)
# S: O(n)
def length_of_longest_substring(s)
  output = 0
  # Look at all substrings
  (0..s.length-1).each do |i|
    # Assume this is a real set and include? is O(1)
    set = []
    (i..s.length-1).each do |j|
      puts s[i..j]
      # if char is not unique move to next i
      if set.include?(s[j])
        output = [output, set.length].max
        break
      end
      set.push(s[j])
    end
    output = [output, set.length].max
  end
  output
end

# T: O(n)
# S: O(n)
require "set"

def length_of_longest_substring(s)
  set = Set.new
  i, j, output = 0, 0, 0
  while i <= s.length-1 and j <= s.length-1
    if set.include?(s[j])
      set.delete(s[i])
      i = i + 1
    else
      set.add(s[j])
      output = [output, j-i+1].max
      j = j + 1
    end
  end
  output
end

puts length_of_longest_substring("abcabcbb")
puts length_of_longest_substring("bacabc")
puts length_of_longest_substring("bbb")
puts length_of_longest_substring(" ")
puts length_of_longest_substring("")
puts length_of_longest_substring("au")
