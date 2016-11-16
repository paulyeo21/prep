# T: O(n!n)
# S: O(n!)
def permutation_palindrome(string)
  # 1. Get all permutations of string:
  # 2. Analyze all permutations if there exists a palindrome
  permutations = permutations(string)
  for permutation in permutations
    return true if is_palindrome?(permutation)
  end
  return false
end

# T: O(n!)
# S: O(n!)
def permutations(string)
  permutations = [string[0]]

  (1..string.length-1).each do |i|
    # Holds new wave of permutations
    current_permutations = []

    # For each permuation accumulated previously
    for permutation in permutations

      # For each possible space in permutation
      (0..permutation.length).each do |j|
        new_permutation = "#{permutation[0, j]}#{string[i]}#{permutation[j, permutation.length]}"
        current_permutations << new_permutation
      end
    end

    # Set new wave as the next waves permutations
    permutations = current_permutations
  end

  permutations
end

# T: O(n/2)
# S: O(1)
def is_palindrome?(string)
  (0..(string.length/2)-1).each do |i|
    return false if string[i] != string[string.length - i - 1]
  end
  return true
end

# T: O(n)
# S: O(n)
def permutation_palindrome_fast(string)
  chars = {}
  (0..string.length-1).each do |i|
    if chars[string[i]].nil?
      chars[string[i]] = false
    else
      chars[string[i]] = !chars[string[i]]
    end
  end

  found_middle_char = false
  for k, v in chars
    if v == false
      if found_middle_char
        return false
      else
        found_middle_char = true
      end
    end
  end

  return true
end

# puts permutation_palindrome("civic")
# puts permutation_palindrome("ivicc")
# puts permutation_palindrome("civil")
# puts permutation_palindrome("livci")

puts permutation_palindrome_fast("civic")
puts permutation_palindrome_fast("ivicc")
puts permutation_palindrome_fast("civil")
puts permutation_palindrome_fast("livci")
