# "asdf" => "fdsa"

# T: O(n)
# S: O(1)
def reverse_in_place(s)
  (0..s.length/2-1).each do |i|
    temp = s[i]
    s[i] = s[s.length-1-i]
    s[s.length-1-i] = temp
  end
  s.inspect
end

def reverse!(s)
  left, right = 0, s.length-1
  while left < right
    s[left], s[right] = s[right], s[left]
    left += 1
    right -= 1
  end
  s.inspect
end

puts reverse_in_place("ab") # "ba"
puts reverse_in_place("abc") # "cba"
puts reverse_in_place("asdf") # "fdsa"
puts reverse_in_place("") # ""

puts reverse!("ab") # "ba"
puts reverse!("abc") # "cba"
puts reverse!("asdf") # "fdsa"
puts reverse!("") # ""
