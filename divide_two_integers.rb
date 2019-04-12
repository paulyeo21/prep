# 29. Divide Two Integers
#
# Given two integers dividend and divisor, divide two integers without using 
# multiplication, division and mod operator. Return the quotient after dividing 
# dividend by divisor. The integer division should truncate toward zero.
#
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
#
# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2

# Add absolute value of divisor with a counter until it reaches dividend. 
# T: O(n / m)
def signed_output(dividend, divisor, output)
  if divisor < 0 and dividend < 0
    return output
  elsif divisor < 0
    return -output
  elsif dividend < 0
    return -output
  else
    return output
  end
end

def divide(dividend, divisor)
  return 0 if dividend == 0
  return signed_output(dividend, divisor, 2**31-1) if dividend >= 2**31 - 1
  return signed_output(dividend, divisor, -2**31) if dividend <= -2**31
  counter = 0
  current = divisor.abs
  while current <= dividend.abs
    current += divisor.abs
    counter += 1
  end
  return signed_output(dividend, divisor, counter)
end

puts divide(10, 3) # 3
puts divide(7, -3) # -2
puts divide(0, 1) # 0
puts divide(-1, 1) # -1
puts divide(1, 2) # 0
puts divide(-2147483648, -1) # -2147483648
