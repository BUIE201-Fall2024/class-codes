import time

def check_duplicate(check):
    for i in range(len(check) - 1):
        for j in range(i + 1, len(check)):
            if check[i] == check[j]:
                return check[i]
    return None

check = [1, -5, 4, 7, -5, 5]
result1 = check_duplicate(check)
print(result1)

result2 = check_duplicate([])
print(result2)

check = [1, -2, 4, 7, -3, 5]
result3 = check_duplicate(check)
print(result3)

def check_set(check):
    already_seen = set()
    for number in check:
        if number in already_seen:
            return number
        else:
            already_seen.add(number)
    return None

check = [1, -5, 4, 7, -5, 5]
result1 = check_set(check)
print(result1)

result2 = check_set([])
print(result2)

check = [1, -2, 4, 7, -3, 5]
result3 = check_set(check)
print(result3)

n = 50000
check = list(range(n))

start = time.time()
result = check_set(check)
end = time.time()
print("check_set time: ", end - start)

start = time.time()
result = check_duplicate(check)
end = time.time()
print("check_duplicate time: ", end - start)

