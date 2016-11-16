def crossedRiver(river, current, speed):
    if speed > 0:
        if current >= len(river):
            return True

        elif current > -1 and river[current] == False:
            return False

        else:
            return crossedRiver(river, current + speed, speed) \
                or crossedRiver(river, current + speed - 1, speed - 1) \
                or crossedRiver(river, current + speed + 1, speed + 1)

def memoizedCrossedRiverUtility(river, current, speed, memo):
    if speed > 0:
        if current >= len(river):
            return True

        elif current > -1 and river[current] == False:
            return False

        elif (current, speed) in memo:
            return memo[(current, speed)]

        else:
            isCrossed = memoizedCrossedRiverUtility(river, current + speed, speed, memo) \
                or memoizedCrossedRiverUtility(river, current + speed - 1, speed - 1, memo) \
                or memoizedCrossedRiverUtility(river, current + speed + 1, speed + 1, memo)
            
            memo[(current, speed)] = isCrossed
            return isCrossed

def memoizedCrossedRiver(river, current, speed):
    memo = {}
    return memoizedCrossedRiverUtility(river, current, speed, memo)

# print(crossedRiver([True, False], -1, 1))
# print(crossedRiver([True, False, False], -1, 1))
# print(crossedRiver([True, True, True, True, False, False, False, True, False, False, False, False, True], 0, 2))

print(memoizedCrossedRiver([True, False], -1, 1))
print(memoizedCrossedRiver([True, False, False], -1, 1))
print(memoizedCrossedRiver([True, True, True, True, False, False, False, True, False, False, False, False, True], 0, 2))

