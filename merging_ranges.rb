def merging_ranges(times)
  # Sort by start times
  times.sort!

  output = []
  previous = times[0]
  for current in times[1..-1]
    if previous[1] >= current[0]
      max = (previous[1] > current[1] ? previous[1] : current[1])
      current = previous[0], max
    else
      output << previous
    end
    previous = current
  end

  output << previous

  output.inspect
end

times = [ [0, 1], [3, 5], [4, 8], [10, 12], [9, 10] ]
times1 = [ [1, 2], [2, 3] ]
times2 = [ [1, 5], [2, 3] ]
times3 = [ [1, 10], [2, 6], [3, 5], [7, 9] ]
puts merging_ranges(times)
puts merging_ranges(times1)
puts merging_ranges(times2)
puts merging_ranges(times3)
