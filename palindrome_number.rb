# Determine whether an integer is a palindrome. An integer is a palindrome when it reads the same backward as forward.
#
# Example 1:
#
# Input: 121
# Output: true
# Example 2:
#
# Input: -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
# Example 3:
#
# Input: 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

# T: O(n / 2)
# S: O(1)
def is_palindrome(x)
  if x < 0
    return false
  else
    str = x.to_s
    (0..(str.length-1)/2).each do |i|
      return false if str[i] != str[str.length-1-i]
    end
    return true
  end
end

puts is_palindrome(121) == true
puts is_palindrome(-121) == false
puts is_palindrome(10) == false
