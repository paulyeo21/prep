# Given an array of unsorted scores and the highest possible
# score, return a sorted array of scores in less than O(n lg n)
#
# T: O(k+n)
# S: O(k+n)
def sort_scores(unsorted_scores, highest_possible_score)
  output = [nil] * unsorted_scores.length
  counts = [0] * (highest_possible_score+1)

  unsorted_scores.each {|score| counts[score-1] += 1}
  (1..counts.length-1).each {|i| counts[i] += counts[i-1]}
  unsorted_scores.each do |score|
    output[counts[score]-1] = score
    counts[score] -= 1
  end

  output.inspect
end

#def sort_scores(unsorted_scores, highest_possible_score)
#  score_counts = [0] * (highest_possible_score+1)

#  #populate score_counts
#  unsorted_scores.each do |score|
#    score_counts[score] += 1
#  end

#  #populate the final sorted array
#  sorted_scores = []

#  #for each item in score_counts
#  highest_possible_score.downto(0) do |score|
#    count = score_counts[score]

#    #for the number of times the item occurs
#    (0..count).each do |time|

#      #add it to the sorted array
#      sorted_scores.push(score)
#    end
#  end
  
#  return sorted_scores.inspect
#end

puts sort_scores([23, 11, 5], 25)
puts sort_scores([37, 89, 41, 65, 91, 53], 100)
puts sort_scores([65, 90, 90], 100)
