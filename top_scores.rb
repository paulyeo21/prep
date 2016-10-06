def top_scores(scores, highest_possible)
  # Counting sort: O(n)
  counts = Array.new(highest_possible, 0)

  # Count number of each score
  for score in scores
    counts[score] += 1
  end

  # Aggregate previous count to each count
  (1..counts.length-1).each do |i|
    counts[i] += counts[i - 1]
  end

  sorted_scores = Array.new(scores.length) 
  for score in scores
    sorted_scores[counts[score] - 1] = score
    counts[score] -= 1
  end 

  return sorted_scores.inspect
end

scores = [99, 8, 1, 3, 54, 34, 24, 2, 4, 2, 2]
puts top_scores(scores, 100)
