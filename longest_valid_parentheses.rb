# 32. Longest Valid Parentheses
#
# Given a string containing just the characters '(' and ')', 
# find the length of the longest valid (well-formed) parentheses 
# substring.
#
# Example 1:
#
# Input: "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()"
#
# Example 2:
#
# Input: ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()"

# For each char in string, check if it creates a valid parentheses,
# if it does, check last char up to current char to see if connecting
# valid parentheses.
# T: O(n**2)
# S: O(n)
require "pry"

def longest_valid_parentheses(s)
  return 0 if s.empty?
  longest = (0..s.length-1).map{0}
  stack = []
  (0..s.length-1).each do |i|
    if s[i] == "("
      stack.push(s[i])
    elsif s[i] == ")"
      popped = stack.pop
      if popped
        j, output = 2, 2
        neighbor = i - j
        while neighbor > 0 and j != 0
          # binding.pry
          # check j indices back to see if neighbor is connecting
          if longest[neighbor] >= longest[neighbor+1]
            j = longest[neighbor]
          else
            j = longest[neighbor+1]
          end
          neighbor -= j
          output += j
        end
        longest[i] = output
      end
    end
  end
  puts longest.inspect
  return longest.max
end

puts longest_valid_parentheses("(()())()") #8
puts longest_valid_parentheses(")()())()") #4
puts longest_valid_parentheses("(()") #2
puts longest_valid_parentheses(")()())") #4
puts longest_valid_parentheses(")()())((()))") #6
puts longest_valid_parentheses("()(()") #2
puts longest_valid_parentheses("()((())") #4
puts longest_valid_parentheses("(()(((())))()")#12
puts longest_valid_parentheses("")#0
puts longest_valid_parentheses("(())")#4
puts longest_valid_parentheses(")(((((()())()()))()(()))(")#22
puts longest_valid_parentheses("()(())")#6
