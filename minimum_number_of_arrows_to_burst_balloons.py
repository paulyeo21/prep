"""
    There are a number of spherical balloons spread in two-dimensional space.
    For each balloon, provided input is the start and end coordaintes of the
    horizontal diameter. Since it's horizontal, y-coordinates don't matter and
    hence the x-coordinates of start and end of the diameter suffice. Start
    is always smaller than end. There will be at most 10^4 balloons.

    An arrow can be shot up exactly vertically from different points along the
    x-axis. A balloon with x_start and x_end bursts by an arrow shot at x if
    x_start <= x <= x_end. There is no limit to the number of arrows that can be shot.
    An arrow once shot keeps traveling up infinitely. The problem is to find
    the minimum number of arrows that must be shot to burst all balloons.
"""
def findMinArrowShots(points):
    # Number of minimum arrows equals to the number of subsets
    # Find overlapping intervals using balloon coordinates
    # Return number of intervals

    if points:
        sortedPoints = sorted(points)
        balloonSubsets = []
        previous = sortedPoints[0]
        for current in sortedPoints[1:]:
            # print("previous")
            # print(previous)
            # print("current")
            # print(current)
            # print("subsets")
            # print(balloonSubsets)
            # print
            if current[0] <= previous[1]:
                overlap = [max(current[0], previous[0]), min(current[1], previous[1])]
                previous = overlap
            else:
                balloonSubsets.append(previous)
                previous = current

        balloonSubsets.append(previous)
        return len(balloonSubsets)
    else:
        return 0

print(findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(findMinArrowShots([]))
