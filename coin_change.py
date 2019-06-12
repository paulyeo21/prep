# Given an amount and a number of denomations, find the number of
# ways to make the amount using the denominations.

class Solution(object):
    def __init__(self):
        self.memo = {}

    def makeChange(self, amount, denominations, i=0):
        # 1. Sort in descending order.
        # 2. For each denomination in descending order try subtracting from
        #    amount until amount == 0 or amount < 0. If amount == 0 then
        #    increment number of ways, otherwise if amount < 0, don't increment.
        # 3. return counter

        print amount, denominations, i

        if amount == 0:
            return 1

        if amount < 0:
            return 0

        number_of_ways = 0

        for d in denominations[i:]:
            number_of_ways += self.makeChange(amount - d, denominations, i+1) \
                    + self.makeChange(amount - d, denominations, i)

        return number_of_ways

print Solution().makeChange(4, sorted([1,2,3], reverse=True)) # 4
