# [2, 3] meeting from 10:00 - 10:30 am
# [6, 9] meeting from 12:00 - 1:30 pm

# T: O(n lg n)
# S: O(n)
def merge_ranges(meeting_times)
  # 1. sort arrays by start time
  # 2. have two pointers, one to previous and one to current.
  #    merge if previous[1] >= current[0] else up to previous is independent
  meeting_times.sort!
  output = []
  previous = meeting_times[0]
  (1..meeting_times.length-1).each do |i|
    current = meeting_times[i]
    if previous[1] >= current[0]
      previous = [previous[0], [previous[1], current[1]].max]
    else
      output << previous
      previous = current
    end
  end
  output << previous # bc adding time only when current starting time is less 
                     # than previous ending time, we dont get to add the last 
                     # possible time, so we add it here
  output.inspect
end

puts merge_ranges([[0, 1], [3, 5], [4, 8], [10, 12], [9, 10]]) # [[0, 1], [3, 8], [9, 12]]
puts merge_ranges([[0, 2], [1, 10]]) # [[0, 10]]
puts merge_ranges([[0, 2], [3, 10]]) # [[0, 2], [3, 10]]
puts merge_ranges([[1, 5], [2, 3]]) # [[1, 5]]
