# Given an array of prices, find the max difference
# between two prices where a[i] - a[j] and i > j.

# T: O(n)
# S: O(1)
def max_profit(stocks):
    if len(stocks) < 2:
        raise ValueError('Getting a profit requires at least 2 prices')

    min_price = stocks[0]
    max_profit = stocks[1] - stocks[0]

    for current_time in xrange(1, len(stocks)):
        current_price = stocks[current_time]
        potential_profit = current_price - min_price
        max_profit = max(max_profit, potential_profit)
        min_price = min(min_price, current_price)
    return max_profit

print max_profit([10, 7, 5]) # -2
print max_profit([5, 7, 10]) # 5
print max_profit([-1, -2, -3]) # -1
print max_profit([20, 3]) # -17
print max_profit([1, 10, 0, 10]) # 10
