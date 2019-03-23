# The string "PAYPALISHIRING" is written in a zigzag pattern on a given number
# of rows like this: (you may want to display this pattern in a fixed font for
# better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R
# And then read line by line: "PAHNAPLSIIGYIR"
#
# Write the code that will take a string and make this conversion given a number of rows:
#
# string convert(string s, int numRows);
# Example 1:
#
# Input: s = "PAYPALISHIRING", numRows = 3
# Output: "PAHNAPLSIIGYIR"
# Example 2:
#
# Input: s = "PAYPALISHIRING", numRows = 4
# Output: "PINALSIGYAHRPI"
# Explanation:
#
# P     I    N
# A   L S  I G
# Y A   H R
# P     I

# if row = 2
# P Y A I H
# A P L S I
#
# if row = 5
# P      H
# A    S I
# Y   I  R
# P L    I G
# A      N
# 
# if row = 6
# P      R
# A    I I
# Y   H  N
# P  S   G
# A I
# L
#
# At first row = 1 and last row = number of rows, index increment is 2 * (n - 1)
# Lets define the start of a zigzag as a "pivot" if we know when the next pivot is
# and we know the current index of the char then we can determine how many indices to
# increment to get the next char in the row. 
def convert(s, num_rows)
  output = ""
  pivot_to_pivot = 2 * (num_rows - 1)
  (0..num_rows-1).each do |i|
    output += s[i]
    next_pivot = (num_rows - 1) * (((i + 1) / num_rows) + 1)
    index_incr = 2 * (next_pivot - ((i + 1) % num_rows))
    puts "i: #{i}"
    puts "next_pivot: #{next_pivot}"
    puts "index_incr: #{index_incr}"
    while i + index_incr < s.length
      output += s[i + index_incr]
      i += index_incr
    end 
    puts "Current:" + output
  end
  return output
end

puts "PAYPALISHIRING"
puts convert("PAYPALISHIRING", 2)
puts convert("PAYPALISHIRING", 3)
