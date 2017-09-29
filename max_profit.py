# Say you have an array for which the ith element is the price of a given stock on day i.

# If you were only permitted to complete at most one transaction (ie, buy one and 
# sell one share of the stock), design an algorithm to find the maximum profit.

# Brute force
# T: O(n^2)
# S: O(1)
def maxProfit(stocks):
    maximum = 0
    for i in range(len(stocks) - 1):
        local_max = 0
        for j in range(i + 1, len(stocks)):
            if stocks[j] > stocks[i]:
                profit = stocks[j] - stocks[i]
                local_max = max(profit, local_max)
        maximum = max(local_max, maximum)
    return maximum

# T: O(n)
# S: O(1)
def maxProfit1(stocks):
    if not stocks: return 0
    minimum = stocks[0]
    max_profit = 0
    for current in stocks[1:]:
        max_profit = max(current - minimum, max_profit)
        minimum = min(current, minimum)
    return max_profit


input1 = [7, 1, 5, 3, 6, 4]
input2 = [7, 6, 4, 3, 1]
assert maxProfit1(input1) == 5
assert maxProfit1(input2) == 0
assert maxProfit1([]) == 0

