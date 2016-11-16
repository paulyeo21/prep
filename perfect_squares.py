import math

def isSquare(integer):
    isqrt = int(math.sqrt(integer))
    return isqrt ** 2 == integer

def getMinimumUniqueSum(arr):
    output = []
    for item in arr:
        if bool(item.strip()):
            interval = item.split()
            a = int(interval[0])
            b = int(interval[1])
            count = 0
            for i in range(a, b+1):
                if isSquare(i):
                    count += 1
            output.append(count)
    return output

print(getMinimumUniqueSum([]))
print(getMinimumUniqueSum([" "]))
print(getMinimumUniqueSum(["3 9", "2 27"]))
print(getMinimumUniqueSum(["3 9", "2 10000"]))
