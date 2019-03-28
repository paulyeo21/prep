# 22. Generate Parentheses
#
# Given n pairs of parentheses, write a function to generate all combinations of 
# well-formed parentheses.

# For example, given n = 3, a solution set is:
# 
# [
#   "((()))",
#   "(()())",
#   "(())()",
#   "()(())",
#   "()()()"
# ]

# For every () you can add a permutation by adding a parenthese inside and one outside.
# For example for () with an additional parenthese possible permutations
# are (()) and ()(). For (()) permutations would be (()()), ((())) and for ()() would
# be (())() and ()(()).
# T: O(4**n/n*sqrt(n))
# S: O(4**n/n*sqrt(n))
def generate_parentheses(n)
  if n == 1
    return ["()"]
  else
    ps = []
    generate_parentheses(n-1).each do |p|
      (0..p.length-1).each do |i|
        if i > 0 and p[i-1] == "("
          if not ps.include?(p[0..i-1] + "()" + p[i..-1])
            ps.push(p[0..i-1] + "()" + p[i..-1])
          end
        end
      end
    end
    return ps + ["()"*n]
  end
end

puts generate_parentheses(4).inspect
