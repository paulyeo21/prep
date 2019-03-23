# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
# Input: 123
# Output: 321
# Example 2:
#
# Input: -123
# Output: -321
# Example 3:
#
# Input: 120
# Output: 21

# Pop last digit by % 10. Push by * 10 and adding popped
# T: O(log10 n)
# S: O(1)
MIN_INT = -2**31
MAX_INT = 2**31-1

def reverse(x)
  previous = 0
  while x != 0
    popped = x.remainder(10)
    current = previous * 10 + popped
    return 0 if current > MAX_INT or current < MIN_INT
    previous = current
    # for negative numbers -12.3 rounds down to -13, which we dont want
    x = (x / 10.0).to_int
  end
  previous
end

puts reverse(123)
puts reverse(-123)
