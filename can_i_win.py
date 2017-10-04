"""
In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.
"""
def canIWin(maxChoosableInteger, desiredTotal):
    if desiredTotal == 0:
        return True
    else:
        while desiredTotal > 0:
            desiredTotal -= maxChoosableInteger + 1
        return maxChoosableInteger >= desiredTotal and desiredTotal != 0

print(canIWin(10, 11))
print(canIWin(10, 0))
print(canIWin(10, 40))
# print(canIWin(10, 12))
# print(canIWin(20, 19))
# print(canIWin(19, 20))
# print(canIWin(10, 100))
