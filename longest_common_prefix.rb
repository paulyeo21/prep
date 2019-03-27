# 14. Longest Common Prefix
#
# Write a function to find the longest common prefix string amongst an array of strings.
#
# If there is no common prefix, return an empty string "".
#
# Example 1:
#
# Input: ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.
# Note:
#
# All given inputs are in lowercase letters a-z.

# Take shortest length of strs and iterate from first to last until
# character does not equal.
# T: O(n**2)
# S: O(1)
def longest_common_prefix(strs)
  return "" if strs.empty?
  output = ""
  min_length = strs[0].length
  # get shortest length
  strs[1..-1].each do |str|
    min_length = [min_length, str.length].min
  end
  # check prefix of each str
  (0..min_length-1).each do |i|
    prefix = strs[0][0..i]
    strs[1..-1].each do |str|
      return output if str[0..i] != prefix
    end
    output = prefix
  end
  return output
end

puts longest_common_prefix(["flower", "flow", "flight"]) # "fl"
puts longest_common_prefix(["dog", "racecar", "car"]) # ""
