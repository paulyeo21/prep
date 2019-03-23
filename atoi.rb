# Implement atoi which converts a string to an integer.

# The function first discards as many whitespace characters as necessary until the first non-whitespace character is found. Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

# The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

# If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

# If no valid conversion could be performed, a zero value is returned.

# Note:

# Only the space character ' ' is considered as whitespace character.
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. If the numerical value is out of the range of representable values, INT_MAX (231 − 1) or INT_MIN (−231) is returned.
# Example 1:

# Input: "42"
# Output: 42
# Example 2:

# Input: "   -42"
# Output: -42
# Explanation: The first non-whitespace character is '-', which is the minus sign.
#              Then take as many numerical digits as possible, which gets 42.
# Example 3:

# Input: "4193 with words"
# Output: 4193
# Explanation: Conversion stops at digit '3' as the next character is not a numerical digit.
# Example 4:

# Input: "words and 987"
# Output: 0
# Explanation: The first non-whitespace character is 'w', which is not a numerical 
#              digit or a +/- sign. Therefore no valid conversion could be performed.
# Example 5:

# Input: "-91283472332"
# Output: -2147483648
# Explanation: The number "-91283472332" is out of the range of a 32-bit signed integer.
#              Thefore INT_MIN (−231) is returned.

INT_MAX = 2**31 -1
INT_MIN = -2**31
DIGITS = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
SIGNS = ["-", "+"]

# if first non-whitespace character is not numerical or a +/- sign return 0
# if first non-whitespace character is - then take as many numerical digits
# if first non-whitespace character is numerical digit and then experience non-numerical digits, then return the consecutive numerical digits
# if consecutive numerical digits is greater than INT_MAX return INT_MAX or less than INT_MIN return INT_MIN.
# T: O(n)
# S: O(1)

def output(int, sign)
  int = (sign ? int : -int)
  return INT_MAX if int > INT_MAX
  return INT_MIN if int < INT_MIN
  return int
end

def my_atoi(str)
  str = str.strip
  sign_flag = false # flag to mark second occurrence of a sign
  positive_sign = true
  int = 0
  (0..str.length-1).each do |i|
    char = str[i]
    if DIGITS.include?(char)
      int = int * 10 + char.to_i
    elsif SIGNS.include?(char)
      if sign_flag or i != 0 # if second occurrence of a sign or sign occurs after numerical digit
        return output(int, positive_sign)
      else
        sign_flag = true
        positive_sign = (char == "-" ? false : true)
      end
    else
      return output(int, positive_sign)
    end
  end
  return output(int, positive_sign)
end

puts my_atoi("42") == 42
puts my_atoi("   -42") == -42
puts my_atoi("4193 with words") == 4193
puts my_atoi("-91283472332") == INT_MIN
puts my_atoi("+1") == 1
puts my_atoi("  0000000000012345678") == 12345678
puts my_atoi("+-2") == 0
puts my_atoi("  -0012a42") == -12
puts my_atoi("0-1") == 0
puts my_atoi("-5-") == -5
puts my_atoi("      -11919730356x") == INT_MIN

