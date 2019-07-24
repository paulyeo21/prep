# Get max profit from array of prices

def maxProfit(prices):
    if len(prices) < 2:
        return 0
    globalMax = prices[1] - prices[0]
    for i in range(len(prices)):
        localMax = 0 # come back to this
        for j in range(i + 1, len(prices)):
            localMax = max(localMax, prices[j] - prices[i])
        globalMax = max(localMax, globalMax)
    return globalMax

def maxProfit(prices):
    if len(prices) < 2:
        return 0
    minimum = prices[0]
    maxProfit = prices[1] - prices[0]
    for current in prices[1:]:
        maxProfit = max(current - minimum, maxProfit)
        minimum = min(minimum, current)
    return maxProfit

input1 = [7, 1, 5, 3, 6, 4]
input2 = [7, 6, 4, 3, 1]
assert maxProfit(input1) == 5
assert maxProfit(input2) == -1
assert maxProfit([]) == 0
