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

def fibonacci_recursive(n):
    if n == 1 or n == 2:
        return 1
    fib1 = fibonacci_recursive(n - 1)
    fib2 = fibonacci_recursive(n - 2)
    return fib1 + fib2

fib5r = fibonacci_recursive(5)
print(fib5r)

n = 10
start_i = time.time()
fib5 = fibonacci_iterative(5)
end_i = time.time()
print("fibonacci_iterative took ", end_i - start_i)

start_r = time.time()
fib5r = fibonacci_recursive(5)
end_r = time.time()
print("fibonacci_recursiv took ", end_r - start_r)
