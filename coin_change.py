import sys

class Solution:
    def coinChange(self, coins, amount):
        changes = [sys.maxint] * (amount + 1)
        changes[0] = 0

        for change in range(1, amount + 1):
            for coin in coins:
                if coin > change:
                    continue

                # If there is a denomination for that change amount
                elif coin == change:
                    changes[change] = 1

                # Find the number of coins to make change of the 
                # current change amount - current coin then add
                # the current coin to make the number of coins
                elif (changes[change - coin] + 1) < changes[change]:
                    changes[change] = changes[change - coin] + 1

        if changes[amount] != sys.maxint:
            return changes[amount]
        else:
            return -1

solution = Solution()
print(solution.coinChange([1, 2, 5], 11))
print(solution.coinChange([2], 3))
print(solution.coinChange([1], 0))
print(solution.coinChange([186, 419, 83, 408], 6249))

