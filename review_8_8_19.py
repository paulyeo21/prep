# 18. Compute the nth fibonacci number. Compute using memoization. Compute using bottom-up.
#
# Clarifications:
#   a) Fibonacci is the sequence of the numbers starting with 0 and 1 where you add the previous two numbers.
#   b) Use memoization means there will be duplicate work so cache that work.
#   c) Bottom-up means to work from the starting numbers to arrive at answer without doing extra work.
# Edge cases:
#   a) Given n = 0, return 1
#   b) Given n = 1, return 1
#   c) Given n = 2, return 2

def fib(n):
    print('*'),
    if n == 0:
        return 1
    if n == 1:
        return 1
    return fib(n-1) + fib(n-2)

class Fibonacci:
    def __init__(self):
        self.memo = {}

    def run(self, n):
        if n in self.memo:
            return self.memo[n]
        print('*'),
        if n == 0:
            return 1
        if n == 1:
            return 1
        output = self.run(n-1) + self.run(n-2)
        self.memo[n] = output
        return output

def fibBottomUp(n):
    prev1 = 1
    prev2 = 1
    for i in range(2, n+1):
        print('*'),
        prev1, prev2 = prev1 + prev2, prev1
    return prev1

# 1, 1, 2, 3, 5, 8, 13, 21
# assert(fib(0) == 1)
# assert(fib(1) == 1)
# assert(fib(2) == 2)

assert(fib(7) == 21)
print('')

fib = Fibonacci()
assert(fib.run(7) == 21)
print('')

assert(fibBottomUp(7) == 21)

# 19. Given a list of integers return the max sum using non-adjacent integers
# 
# Clarifications:
#   a) Given an array of integers, get the max sum by only using numbers that are 
#      not adjacent, meaning right after one another. For instance, given [1,10,11,1]
#      the max sum would be 12.
#   b) Can we be given negative numbers? Yes.
#   c) Can we be given zero? Yes.
#   d) Can we be given no numbers? Yes.
#   e) Can we be given None? Yes.
#
# Edge cases:
#   a) Given [] return 0
#   b) Given None return 0
#   c) Given [1,3,1] return 3
#   d) Given [2,3,2] return 4
#   e) Given [1,10,11,1] return 12
# 
# Algorithms:
#   a) At each element in the array, we store the non-adjacent max sum up to
#      that index. For instance given [1,3,1] we know at index 0, the non-adjacent
#      max sum is 1, at index 1, the non-adjacent max sum is 3, at index 2 the
#      non-adjacent max sum is current element + max sum of most recent non-adjacent
#      element which is at index 0, so 2. We return the max of all these which is 3.
#      T: O(n) S: O(n)

def maxNonAdjacentSum(integers):
    if not integers:
        return 0
    if len(integers) == 1:
        return integers[0]
    if len(integers) == 2:
        return max(integers[0], integers[1])

    maxNonAdjacentSums = [None] * len(integers)
    maxNonAdjacentSums[0] = integers[0]
    maxNonAdjacentSums[1] = integers[1]

    for i in range(2, len(integers)):
        maxNonAdjacentSums[i] = integers[i] + maxNonAdjacentSums[i-2]

    # find max
    output = maxNonAdjacentSums[0]
    for maxSum in maxNonAdjacentSums[1:]:
        output = max(maxSum, output)

    return output

assert(maxNonAdjacentSum([]) == 0)
assert(maxNonAdjacentSum(None) == 0)
assert(maxNonAdjacentSum([1]) == 1)
assert(maxNonAdjacentSum([1,2]) == 2)
assert(maxNonAdjacentSum([1,3,1]) == 3)
assert(maxNonAdjacentSum([2,3,2]) == 4)
assert(maxNonAdjacentSum([1,10,11,1]) == 12)
