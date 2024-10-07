import time

def fibonacci_iterative(n):
    if n <= 2:
        return 1
    
    prevprev = 1
    prev = 1
    for i in range(n-2):
        current = prevprev + prev
        prevprev = prev
        prev = current
    return current
 
fib5 = fibonacci_iterative(5)
print(fib5)

fib2 = fibonacci_iterative(2)
print(fib2)
