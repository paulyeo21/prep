# Clumsy Factorial
#
# Input: 4
# Output: 7
# Explanation: 7 = 4 * 3 / 2 + 1
#
# Input: 10
# Output: 12
# Explanation: 12 = 10 * 9 / 8 + 7 - 6 * 5 / 4 + 3 - 2 * 1

def clumsy(n)
    output = ""
    operations = ["*", "/", "+", "-"]
    (0..n-1).each do |i|
        output += (n - i).to_s + operations[i % 4]
    end
    eval output[0..-2]
end

puts clumsy(10)
