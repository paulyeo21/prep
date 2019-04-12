# 28. Implement strStr()
#
# Implement strStr().
#
# Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.
#
# Example 1:
# Input: haystack = "hello", needle = "ll"
# Output: 2
#
# Example 2:
# Input: haystack = "aaaaa", needle = "bba"
# Output: -1
#
# Clarification:
# What should we return when needle is an empty string? This is a great question to ask during an interview. For the purpose of this problem, we will return 0 when needle is an empty string. This is consistent to C's strstr() and Java's indexOf().

# Brute force is have two pointers. i will be when haystack[i] is equal to needle[i]. then
# increment second pointer until all chars match. If they dont then i += 1.
# T: O(n*m)
def str_str(haystack, needle)
  (0..haystack.length).each do |i|
    (0..needle.length).each do |j|
      return i if j == needle.length
      return -1 if i + j == haystack.length
      break if haystack[i + j] != needle[j]
    end
  end
end

puts str_str("hello", "ll") # 2
puts str_str("aaaaa", "bba") # -1
puts str_str("a", "a") # 0
puts str_str("a", "b") # -1
puts str_str("aaa", "aaa") # 0
puts str_str("mississippi", "issip") # 4
