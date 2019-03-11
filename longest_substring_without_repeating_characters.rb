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

puts length_of_longest_substring("abcabcbb")
puts
puts length_of_longest_substring("bbb")
puts
puts length_of_longest_substring(" ")
puts
puts length_of_longest_substring("")
puts
puts length_of_longest_substring("au")
puts
