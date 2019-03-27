# 1021. Best Sightseeing Pair
#
# Given an array A of positive integers, A[i] represents the value of the i-th sightseeing spot, and two sightseeing spots i and j have distance j - i between them.
#
# The score of a pair (i < j) of sightseeing spots is (A[i] + A[j] + i - j) : the sum of the values of the sightseeing spots, minus the distance between them.
#
# Return the maximum score of a pair of sightseeing spots.
# Example 1:
#
# Input: [8,1,5,2,6]
# Output: 11
# Explanation: i = 0, j = 2, A[i] + A[j] + i - j = 8 + 5 + 0 - 2 = 11

# Maximize for when a[i] + a[j] + i - j is greatest
# Brute force we can check all pairs
# T: O(n**2)
# S: O(1)
#
# We could experiment with sorting to optimize time complexity for O(n**2)
def max_score_sightseeing_pair(a)
  max_score = a[0] + a[1] + 0 - 1
  (0..a.length-2).each do |i|
    (i+1..a.length-1).each do |j|
      # puts "score: #{max_score}"
      # puts "#{i}: #{a[i]}"
      # puts "#{j}: #{a[j]}"
      score = a[i] + a[j] + i - j
      max_score = [max_score, score].max
    end
  end
  return max_score
end

# For a given index, we know that a[i] + i and a[j] - j. We can find the best pair
# in one iteration by seeing that as we increase the index we decrease i - j. So when we see
# new j's we can check if a[j] - j is greater than previous. If so we can log that. If
# we see a value a[i] + i thats greater than a[i] + i, then we log this index pair value
# and then start this index as the new a[i] and try the remaining js. We can be assured that
# this wont make us lose out on potential bests with the previous a[i] because if there is
# a j that is greater then that would be realized by the new a[i] since that is greater
# than previous a[i].
# T: O(n)
# S: O(1)
def score(a, i, j)
  return a[i] + a[j] + i - j
end

def max_score_sightseeing_pair(a)
  best_i = 0
  best_j = 1
  i = 0
  j = 1
  while j < a.length
    # puts "Best Pair: (#{best_i}, #{best_j}) #{score(a, best_i, best_j)}"
    # puts "i: #{i}"
    # puts "j: #{j}"
    # if we see a new j that creates a pair thats better val
    best_i, best_j = i, j if score(a, i, j) > score(a, best_i, best_j)
    # if we find a value that is greater than prev i, but cant
    # elect as best yet, because could end up not being best 
    # for example, if last element in array is huge number.
    i = j if a[j] + j > a[i] + i
    j += 1
  end
  return score(a, best_i, best_j)
end

puts max_score_sightseeing_pair([1,3,5]) == 7
puts max_score_sightseeing_pair([1,2,2]) == 3
puts max_score_sightseeing_pair([5,7,4,10,4]) == 15
puts max_score_sightseeing_pair([8,1,5,2,6]) == 11
puts max_score_sightseeing_pair([8,1,5,2,100]) == 104
