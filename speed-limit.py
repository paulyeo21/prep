"""
Given an array with tuple elements that represent the user's mph over a
number of miles and a similar array of tuple elements that represent the
legal mph over a number of miles, return whether the user has exceeded the
speed limit at any point in time.
"""

def exceededSpeedLimit(user_speeds, speed_limits):
    # Build data structure out of speed_limits
    total_miles = 0
    for mph, miles in speed_limits:
        total_miles += miles

    limits = [0 for i in range(total_miles)]
    prev_miles = 0
    for mph, miles in speed_limits:
        for mile in range(prev_miles, prev_miles + miles):
            limits[mile] = mph
        prev_miles += miles

    # print limits
    # Iterate over user speeds and check if exceeded at certain miles
    prev_mile = 0
    for mph, mile in user_speeds:
        # print mph
        # print prev_mile, limits[prev_mile]
        # print mile, limits[mile - 1]
        if mph > limits[prev_mile] or mph > limits[mile - 1]:
            return True
        else:
            prev_mile = mile

    return False

# assert exceededSpeedLimit([(30, 10)], [(35, 10)]) == False
# assert exceededSpeedLimit([(30, 10)], [(25, 10)]) == True
assert exceededSpeedLimit([(30, 10), (65, 25)], [(30, 15), (65, 25)]) == True
assert exceededSpeedLimit([(30, 20), (65, 25)], [(30, 15), (65, 30)]) == False
