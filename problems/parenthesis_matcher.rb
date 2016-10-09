require "../data-structures/stack.rb"

def parenthesis_matcher(string, index_of_first_parenthesis)
  stack = Stack.new()
  (index_of_first_parenthesis..string.length-1).each do |index|
    if string[index] == ")"
      stack.pop
      return index if stack.empty?
    elsif string[index] == "("
      stack.push("(")
    end
  end 
end

message = "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."

puts parenthesis_matcher(message, 10)
