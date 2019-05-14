# Write a function fib() that takes an integer n and returns the
# nth fibonacci number.

# Recursively
def fib(n):
    # Base case is when n == 0 and n == 1.
    # T: O(n)
    # S: O(n)
    if n == 0:
        return 0

    if n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

# Recursively with memoization
class Fibonacci:
    def __init__(self):
        self.memo = {}

    def fib(self, n):
        if n < 0:
            raise IndexError('Index was negative.')

        if n in [0, 1]:
            return n

        if n in self.memo:
            return self.memo[n]

        result = self.fib(n - 1) + self.fib(n - 2)
        self.memo[n] = result
        return result

# Iteratively
def fib(n):
    if n < 0:
        raise IndexError

    if n in [0, 1]:
        return n

    prev0 = 0
    prev1 = 1

    for i in xrange(2, n):
        temp = prev1
        prev1 = prev1 + prev0
        prev0 = temp

    return prev1 + prev0

print fib(0) # 0
print fib(1) # 1
print fib(2) # 1
print fib(3) # 2
print fib(4) # 3

f = Fibonacci()
print f.fib(0) # 0
print f.fib(1) # 1
print f.fib(2) # 1
print f.fib(3) # 2
print f.fib(4) # 3

