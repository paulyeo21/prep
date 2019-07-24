
def maxProfit(prices):
    for i in range(len(prices)):
        print(prices[i])

input1 = [7, 1, 5, 3, 6, 4]
input2 = [7, 6, 4, 3, 1]
assert maxProfit(input1) == 5
assert maxProfit(input2) == 0
assert maxProfit([]) == 0
