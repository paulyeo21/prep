# Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.
#
# '.' Matches any single character.
# '*' Matches zero or more of the preceding element.
# The matching should cover the entire input string (not partial).
#
# Note:
#
# s could be empty and contains only lowercase letters a-z.
# p could be empty and contains only lowercase letters a-z, and characters like . or *.
# Example 1:
#
# Input:
# s = "aa"
# p = "a"
# Output: false
# Explanation: "a" does not match the entire string "aa".
# Example 2:
#
# Input:
# s = "aa"
# p = "a*"
# Output: true
# Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
# Example 3:
#
# Input:
# s = "ab"
# p = ".*"
# Output: true
# Explanation: ".*" means "zero or more (*) of any character (.)".
# Example 4:
#
# Input:
# s = "aab"
# p = "c*a*b"
# Output: true
# Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
# Example 5:
#
# Input:
# s = "mississippi"
# p = "mis*is*p*."
# Output: false

# Hold two indices in memory, one will be when looping over regex; the other will be for 
# the given string. Loop over regex if not .  or *, then check regex char against string
# char. If . then matches any char so continue to next index. If *, need to hold in memory
# previous regex char so that we can check against what char for string.
# T: O(n)
# S: O(1)
def is_match(s, p)
  return false if s.empty? and not p.empty?
  return false if not s.empty? and p.empty?
  regex_index = 0
  string_index = 0
  while string_index < s.length
    # regex_index += 1 if p[regex_index+1] == "*"
    regex_char = p[regex_index]
    string_char = s[string_index]
    if regex_char == "."
      regex_index += 1
      string_index += 1
    elsif regex_char == "*"
      # if prev character in regex string is equal to string character
      # that means that continue to use * until we run into different char
      prev_char = p[regex_index - 1]
      if prev_char == string_char or prev_char == "."
        string_index += 1
      else
        regex_index += 1
      end
    elsif regex_char == string_char
      regex_index += 1
      string_index += 1
    else
      # if chars dont equal but next regex char is a *, then don't exit, because *
      # allows 0 or more.
      if p[regex_index + 1] == "*"
        regex_index += 1
      else
        return false
      end
    end
  end
  # return false if partial matches by checking where at regex stopped searching
  # if stopped searching at end with * then its ok otherwise fail
  return is_match(s[regex_index+1..-1], p[regex_index+1..-1]) if p[regex_index] == "*"
  return false if regex_index == p.length-1
  return true
end

puts is_match("aa", "a") == false
puts is_match("aa", "a.") == true
puts is_match("a", ".") == true
puts is_match("aa", "a*") == true
puts is_match("aab", "a*") == false
puts is_match("", "a*") == false
puts is_match("ab", "") == false
puts is_match("ab", ".*") == true
puts is_match("aab", "c*a*b") == true
puts is_match("mississippi", "mis*is*p*.") == false
puts is_match("ab", ".*c") == false
puts is_match("aaa", "aaaa") == false
puts is_match("aaa", "a*a") == true
