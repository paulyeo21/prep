# 20. Valid Parentheses
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
#
# An input string is valid if:
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Note that an empty string is also considered valid.
#
# Example 1:
#
# Input: "()"
# Output: true
# Example 2:
#
# Input: "()[]{}"
# Output: true
# Example 3:
#
# Input: "(]"
# Output: false
# Example 4:
#
# Input: "([)]"
# Output: false
# Example 5:
#
# Input: "{[]}"
# Output: true

# Use stack
# T: O(n)
# S: O(n/2)

$OPEN = {
 "(" => ")",
 "[" => "]",
 "{" => "}"
}

def is_valid(s)
  stack = []
  (0..s.length-1).each do |i|
    char = s[i]
    if $OPEN.keys.include?(char)
      stack.push(char)
    else
      popped = stack.pop
      return false if not $OPEN[popped] == char
    end
  end
  stack.empty? ? true : false
end

puts is_valid("()") # true
puts is_valid("()[]{}") # true
puts is_valid("(]") # false
puts is_valid("([)]") # false
puts is_valid("{[]}") # true
puts is_valid("[") # false
