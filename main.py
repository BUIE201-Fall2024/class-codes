import time

# iterative function
def factorial(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return result

five_fact = factorial(5)

def factorial_recursive(n):
    if n == 0:
        return 1
    return n * factorial_recursive(n - 1)

five_fact_recursive = factorial_recursive(5)
print(five_fact_recursive)

# be careful with max recursion depth in Python, which is 1000 by default
# for n in [5, 50, 250, 1000, 5000]:
for n in [5, 50, 250, 500, 750]:
    print ("calculating ", n, "!")
    start_i = time.time()
    result_i = factorial(n)
    end_i = time.time()
    print ("iterative result: ", result_i, " time: ", end_i - start_i)

    start_r = time.time()
    result_r = factorial_recursive(n)
    end_r = time.time()
    print ("recursive result: ", result_r, " time: ", end_r - start_r)
