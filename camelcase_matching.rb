# 1023. Camelcase Matching
#
# A query word matches a given pattern if we can insert lowercase letters to the 
# pattern word so that it equals the query. (We may insert each character at any 
# position, and may insert 0 characters.)
#
# Given a list of queries, and a pattern, return an answer list of booleans, where 
# answer[i] is true if and only if queries[i] matches the pattern.

# Have two pointers i and j. i tracks each query independently as j tracks the pattern.
# For each query if char at i equals char at j, increment both i and j. If we see a
# capitalized char, and that char does not exist at char at j, then false immediately,
# otherwise we can increment i if char at i and char at j are not equal and char at i
# is not a capitalized char.
# T: O(#queries * length of queries * length of pattern) = O(m * l * n)
# S: O(1)

CAPS = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

def camel_match(queries, pattern)
  (0..queries.length-1).each do |k|
    query = queries[k]
    i = 0
    j = 0
    while i < query.length
      if query[i] == pattern[j]
        j += 1
      else
        break if CAPS.include?(query[i])
      end
      i += 1
    end
    queries[k] = (i == query.length and j == pattern.length ? true : false)
  end
  return queries.inspect
end

puts camel_match(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FB") #[true,false,true,true,false]
puts camel_match(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBa") #[true,false,true,false,false]
puts camel_match(["FooBar","FooBarTest","FootBall","FrameBuffer","ForceFeedBack"], "FoBaT") #[false,true,false,false,false]
