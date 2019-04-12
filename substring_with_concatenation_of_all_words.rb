# 30. Substring with Concatenation of All Words
#
# You are given a string, s, and a list of words, words, that are all of the same length. Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.
#
# Example 1:
#
# Input:
#   s = "barfoothefoobarman",
#   words = ["foo","bar"]
#
# Output: [0,9]
# Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.
# The output order does not matter, returning [9,0] is fine too.
#
# Example 2:
#
# Input:
#   s = "wordgoodgoodgoodbestword",
#   words = ["word","good","best","word"]
# Output: []

# get a chunk of length m * # of words. get chunks of chunk to see if all chunks
# are all words against words_map. If so skip to end of the length of substring 
# otherwise, increment index.
# T: O(s * n * m)
# S: O(n)
def find_substring(s, words)
  return [] if words.length == 0
  n = words.length
  m = words[0].length
  output = []
  i = 0
  while i <= s.length-n*m
    substring = s[i..i+n*m-1]
    sub_substrings = []
    (0..n-1).each do |j|
      sub_substrings.push(substring[j*m..j*m+m-1])
    end
    # puts substring
    # puts sub_substrings.inspect
    if sub_substrings.sort == words.sort
      output.push(i)
    end
    i += 1
  end
  return output.inspect
end

puts find_substring("barfoothefoobarman", ["foo", "bar"]) # [0, 9]
puts find_substring("wordgoodgoodgoodbestword", ["word", "good", "best", "word"]) # []
puts find_substring("", []) # []
puts find_substring("barfoofoobarthefoobarman", ["foo", "bar", "the"]) # [6, 9, 12]
puts find_substring("wordgoodgoodgoodbestword", ["word", "good", "best", "good"]) # [8]
puts find_substring("aaaaaaaa", ["aa", "aa", "aa"]) # [0,1,2]
