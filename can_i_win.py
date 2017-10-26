"""
In the "100 game," two players take turns adding, to a running total,
any integer from 1..10. The player who first causes the running total
to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of
numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal,
determine if the first player to move can force a win, assuming both
players play optimally.

You can always assume that maxChoosableInteger will not be larger than
20 and desiredTotal will not be larger than 300.


Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.
"""


class Solution(object):
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        if self.contiguousSum(maxChoosableInteger) < desiredTotal:
            return False

        self.memo = {}
        return self.canIWinUtil(range(1, maxChoosableInteger + 1), desiredTotal)

    def canIWinUtil(self, availableIntegers, desiredTotal):
        # print availableIntegers, desiredTotal

        if availableIntegers:
            hashString = str(availableIntegers)
            if hashString in self.memo:
                return self.memo[hashString]

            if availableIntegers[-1] >= desiredTotal:
                return True

            for i in range(len(availableIntegers)):
                if not self.canIWinUtil(availableIntegers[:i] + availableIntegers[i+1:], \
                        desiredTotal - availableIntegers[i]):
                    self.memo[hashString] = True
                    return True

            self.memo[hashString] = False
            return False
        return False

    def contiguousSum(self, n):
        return (n + 1) * (n) / 2


solution = Solution()
# print(canIWin(10, 11))
# print(canIWin(10, 20))
# print(solution.canIWin(10, 40))
# assert solution.canIWin(18, 188) == False
assert solution.canIWin(5, 50) == False
# print(canIWin(10, 12))
# print(canIWin(20, 19))
# print(canIWin(19, 20))
# print(canIWin(10, 100))

