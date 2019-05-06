# T: O(n)
# S: O(n)

def backspace_compare_helper(string)
  stack = []
  (0..string.length-1).each do |i|
    if string[i] == "#"
      stack.pop
    else
      stack.push(string[i])
    end
  end
  stack.join
end

def backspace_compare(s, t)
  backspace_compare_helper(s) == backspace_compare_helper(t)
end

puts backspace_compare("ab#c", "ad#c")
puts backspace_compare("ab##", "c#d#")
puts backspace_compare("a##c", "#a#c")
puts backspace_compare("a#c", "b")
