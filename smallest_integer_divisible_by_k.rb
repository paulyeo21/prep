# 1022. Smallest Integer Divisible by K
#
# Given a positive integer K, you need to find the smallest positive integer N 
# such that N is divisible by K, and N only contains the digit 1.
#
# Return the length of N.  If there is no such N, return -1.
#
# Example 1:
#
# Input: 1
# Output: 1
# Explanation: The smallest answer is N = 1, which has length 1.
# Example 2:
#
# Input: 2
# Output: -1
# Explanation: There is no such positive integer N divisible by 2.
# Example 3:
#
# Input: 3
# Output: 3
# Explanation: The smallest answer is N = 111, which has length 3.
#
# 1 <= K <= 10**5

# return -1 if k can be divided by 2 or 5, because if N is made of only
# 1s then 2 cannot be a multiple because any number that is a multiple of
# 2 is even. same with 5.
#
# T: O(n)
# S: O(1)
def smallest_repunit_div_by_k(k)
  return -1 if k % 2 == 0 or k % 5 == 0
  r = 0
  (1..k).each do |i|
    r = (r * 10 + 1) % k
    if r == 0
      return i
    end
  end
end

puts smallest_repunit_div_by_k(1) == 1
puts smallest_repunit_div_by_k(2) == -1
puts smallest_repunit_div_by_k(3) == 3 # 111
puts smallest_repunit_div_by_k(9) == 9 # 111111111
puts smallest_repunit_div_by_k(6) == -1
puts smallest_repunit_div_by_k(7) == 6 # 111111
puts smallest_repunit_div_by_k(17) == 16 # 111111
