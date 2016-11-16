require "../data-structures/stack.rb"

def bracket_validator(string)
  openers = ["(", "{", "["]
  closers = [")", "}", "]"]
  matches = {
    "(" => ")",
    "{" => "}",
    "[" => "]"
  }
  stack = Stack.new
  (0..string.length-1).each do |i|
    if openers.include?(string[i])
      stack.push(string[i])
    elsif closers.include?(string[i])
      return false if stack.empty?
      popped = stack.pop
      return false if matches[popped] != string[i]
    end
  end
  true
end

case1 = "{ [ ] ( ) }"
case2 = "{ [ ( ] ) }"
case3 = "{ [ }"

puts bracket_validator(case1)
puts bracket_validator(case2)
puts bracket_validator(case3)
