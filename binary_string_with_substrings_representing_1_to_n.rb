# 1023. Binary String With Substrings Representing 1 To N
#
# Given a binary string S (a string consisting only of '0' and '1's) and a 
# positive integer N, return true if and only if for every integer X from 1 to N, 
# the binary representation of X is a substring of S.
#
# Example 1:
#
# Input: S = "0110", N = 3
# Output: true
# Example 2:
#
# Input: S = "0110", N = 4
# Output: false

# Brute force we try every integer from 1 to N
# O(n**2)
# O(1)

def binary_rep(n)
  output = 0
  while n != 0
    nth = Math.log2(n).floor
    output += 10 ** nth
    n -= 2 ** nth
  end
  return output.to_s
end

def query_string(s, n)
  (1..n).each do |i|
    string = binary_rep(i)
    return false if not s.include?(string)
  end
  return true
end

puts query_string("0110", 3) == true
puts query_string("0110", 4) == false
