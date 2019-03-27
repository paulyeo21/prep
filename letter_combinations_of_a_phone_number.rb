# 17. Letter Combinations of a Phone Number
#
# Given a string containing digits from 2-9 inclusive, return all possible 
# letter combinations that the number could represent.
#
# A mapping of digit to letters (just like on the telephone buttons) is given 
# below. Note that 1 does not map to any letters.
#
# Example:
# Input: "23"
# Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

$DIGIT_TO_LETTERS = {
  "2" => "abc",
  "3" => "def",
  "4" => "ghi",
  "5" => "jkl",
  "6" => "mno",
  "7" => "pqrs",
  "8" => "tuv",
  "9" => "wxyz"
}

# For each digit get possible permutations. Add possible permutation to each previous 
# permutation to get all possible letter combinations. For example, given 23, if we look at
# 2 we get permutations ["a", "b", "c"] and then with 3 we have permutations ["d", "e", "f"]
# so we add those permutations to each of the previous permutations to get ["ad", "ae", "af",
# "bd", "be", "bf", "cd", "ce", "cf"]
# T: O(3**n * 4**m)
# S: O(3**n * 4**m)
def letter_combinations(digits)
  if digits.length == 0
    return []
  elsif digits.length == 1
    letters = $DIGIT_TO_LETTERS[digits]
    return (0..letters.length-1).map {|i| letters[i]}
  else
    permutations = []
    letter_combinations(digits[1..-1]).each do |g_permutation|
      letter_combinations(digits[0]).each do |permutation|
        permutations.push(permutation + g_permutation)
      end
    end
    return permutations
  end
end

puts letter_combinations("23").inspect # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]
puts letter_combinations("").inspect
