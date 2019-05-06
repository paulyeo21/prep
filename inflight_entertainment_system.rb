# 60 and [5, 10, 30, 30] => true
# Given an integer and an array of integers, find a pair of integers
# in the array that equals the given integer.
# Do not use the exact integer twice and pick exactly two integers. 

# T: O(n)
# S: O(n)
def inflight_entertainment_system(flight_time, movie_times)
  # 1. iterate over movie times
  # 2. store in a hash the difference with index needed to sum to flight time
  # 3. iterate over movie times again
  # 4. check if any movie times are keys. return if key exists and index == value
  flight_time_differences = {}
  (0..movie_times.length-1).each do |i|
    flight_time_differences[flight_time - movie_times[i]] = i
  end
  (0..movie_times.length-1).each do |i|
    if flight_time_differences.key?(movie_times[i]) and
        flight_time_differences[movie_times[i]] != i
      return true
    end
  end
  false
end

def can_two_movies_fill_flight?(movie_lengths, flight_length)
  movie_lengths_seen = Set.new
  movie_lengths.any? do |first_movie_length|
    matching_second_movie_length = flight_length - first_movie_length
    if movie_lengths_seen.include?(matching_second_movie_length)
      true
    else
      movie_lengths_seen.add(first_movie_length)
      false
    end
  end
end

puts inflight_entertainment_system(60, [5, 10, 30]) # false
puts inflight_entertainment_system(60, [5, 10, 30, 30]) # true
puts inflight_entertainment_system(0, [5, 30]) # false
puts inflight_entertainment_system(30, [30]) # false
puts inflight_entertainment_system(30, []) # false
puts inflight_entertainment_system(10, [2, 4, 3]) # false
puts inflight_entertainment_system(10, [12, 4, 6]) # true
