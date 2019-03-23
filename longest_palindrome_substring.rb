# Longest Palindrome Substring
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.

# Input: "cbbd"
# Output: "bb"

# T: O(n/2) = O(n)
# S: O(1)
def palindrome?(string)
  length = string.length
  (0..length-1).each do |i|
    return false if string[i] != string[length-1-i]
  end
  true
end

# Brute force
# For each substring and check if palindrome.
# T: O(n^3)
# S: O(1)
def longest_palindrome_substring(s)
  longest = s[0]
  (0..s.length-1).each do |i|
    (i..s.length-1).each do |j|
      substring = s[i..j]
      is_palindrome = palindrome?(substring)
      if is_palindrome and longest.length < substring.length
        longest = substring
      end
    end
  end
  longest
end

# Improving palindrome calculation
# Given a substring i..j store the permutations of previous palindromes
# so that for substring i+1..j-1 we can confirm whether the palindrome
# and then if palindrome check char at i == char at j. Start by storing
# one and two character palindromes and moving to greater lengths.
# T: O(n^2)
# S: O(n^2)
def longest_palindrome_substring(s)
  palindromes = [""] + s.split("")
  (1..s.length-1).each do |k|
    (0..s.length-1).each do |i|
      if i + k < s.length
        substring = s[i..i+k]
        # If substring's inside substring (not including first and last characters)
        # are a palindrome and the first and last characters are identical
        if palindromes.include?(substring[1..-2]) and substring[0] == substring[-1]
          palindromes.push(substring)
        end
        # puts "Palindromes #{palindromes.inspect}"
        # puts "Substring #{substring}"
      end
    end
  end
  palindromes.pop
end

# Improving space complexity
# If we find every center of a string and check each center's surrounding characters
# and log the longest, we can achieve a better space complexity algorithm. The time
# complexity is still n^2, because for each center (2n-1) we check against the length
# of the string (n).
# T: O(n^2)
# S: O(1)
def longest_palindrome_substring(s)
  if s.length > 0
    output = s[0]
    centers = []
    # Get all centers including space between substrings with even characters
    (0..s.length-1).each do |i|
      centers.push(s[i])
      centers.push("") if i != s.length-1
    end
    # Starting on each center expand to boundaries to see if palindrome
    (0..centers.length-1).each do |i|
      (1..centers.length/2).each do |j|
        center = centers[i]
        if i - j > -1 and i + j < centers.length
          center = centers[i]
          if centers[i-j] == centers[i+j]
            substring = centers[i-j..i+j].join
            output = substring if substring.length > output.length
          else
            break
          end
        end
      end
    end
    return output
  else
    return s
  end
end

# Simpler variation
def longest_palindrome_substring(s)
  longest_start = 0
  longest_end = 0
  (0..s.length-1).each do |i|
    # odd
    _start, _end = i, i
    while _start > -1 and _end < s.length
      if s[_start] == s[_end]
        if longest_end - longest_start < _end - _start
          longest_end = _end
          longest_start = _start
        end
        _start -= 1
        _end += 1
      else
        break
      end
    end

    # even
    _start, _end = i, i+1
    while _start > -1 and _end < s.length
      if s[_start] == s[_end]
        if longest_end - longest_start < _end - _start
          longest_end = _end
          longest_start = _start
        end
        _start -= 1
        _end += 1
      else
        break
      end
    end
  end
  return s[longest_start..longest_end]
end

puts longest_palindrome_substring("babad")
puts longest_palindrome_substring("")
puts longest_palindrome_substring("cbbd")
puts longest_palindrome_substring("abcba")
puts longest_palindrome_substring("a")
