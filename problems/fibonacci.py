def fib(n):
    previous = 0
    current = 1
    while n > 0:
        temp = previous
        previous = current
        current += temp
        n -= 1
    return previous

print(fib(1))
print(fib(0))
print(fib(4))
print(fib(5))
print

def fib_recursion(n):
    if n == 0:
        return 0 
    elif n == 1:
        return 1 
    else:
        return fib_recursion(n-1) + fib_recursion(n-2)

print(fib_recursion(0))
print(fib_recursion(1))
print(fib_recursion(2))
print(fib_recursion(3))
print(fib_recursion(4))
print

def fib_dynamic(n):
    memo = {
        0: 0,
        1: 1
    }
    if n in memo:
        return memo[n]
    else:
        memo[n] = fib_dynamic(n-1) + fib_dynamic(n-2)
        return memo[n]

print(fib_dynamic(0))
print(fib_dynamic(1))
print(fib_dynamic(2))
print(fib_dynamic(3))
print(fib_dynamic(4))
