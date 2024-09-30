import time

print("Hello, IE 201!")
print("Class of Fall 2024!")
print("How are you?")

# this is a comment
# answer = input()
# print("User answered:" + answer)

a = 5
print(type(a))

s = "this is a string"
print(type(s))

b = True
print(type(b))

f = 3.14
print(type(f))

# integer arithmetic is exact
a = 1
b = 2

if a + b == 3:
    print("a + b == 3")
else:
    print("a + b != 3")

# floating point arithmetic is approximate
x = 0.1
y = 0.2

if x + y == 0.3:
    print("x + y == 0.3")
else:
    print("x + y != 0.3")

t = x + y

print (t)

if abs(x + y - 0.3) <= 0.0000001:
    print ("x + y is approximately 0.3")
else:
    print ("x + y is not approximately 0.3")

# testing branch

# list
my_list = [3, 5, 7]
print(my_list)
my_list.append(9)
print(my_list)

my_list.append(4.15)
my_list.append("my string")
my_list[0] = 99
print(my_list)

my_tuple = (3, 5, 7)
print(my_tuple)
# no append function in tuples
# my_tuple.append(9)
# no item assignment in tuples
# tuples are immutable
# my_tuple[0] = 99

# dictionary keeps track of keys -> values
my_dict = {"IE 201": "Z. Caner Taşkın",
           "IE 202": "Tınaz Ekim",
           "IE 255": "Wolfgang Hormann"}

print(my_dict)

# lookup of existing keys
print ("IE 201 is taught by: " + my_dict["IE 201"])

# lookup of non-existing keys throw error
# print ("IE 203 is taught by: " + my_dict["IE 203"])

# list can have duplicate values of the same item
my_list.append(99)
print(my_list)

# eliminate duplicates in a list
my_list = list(set(my_list))
print(my_list)

my_set = {99, 5, 7, 9, 4.15, 'my string'}
print(my_set)
my_set.add(149)
print(my_set)

# no duplicates are allowed in set
my_set.add(99)
print(my_set)

# operators and keywords
a = 10
if a <= 15:
    print ("a <= 15")
elif a <= 25:
    print ("15 < a <= 25")
else:
    print ("25 < a")

m = "a"
if m == "a":
    pass
elif m == "b":
    pass
elif m == "c":
    pass
else:
    pass

# is equivalent to 
match m:
    case "a": pass
    case "b": pass
    case "c": pass
    case _: pass # default behavior corresponding to else

print ("while loop")
x = 0
while x < 10:
    print (x)
    x += 1  # x = x + 1

print ("for loop")
for i in range(10):
    print (i)

print ("for loop")
for i in range(10):
    if i == 6:
        break   #early termination of a loop
    if i == 3:
        continue    # skip the remainder of this iteration
    print (i)

print ("for loop with range(10, 20)")
for i in range(10, 20):
    print (i)

print ("for loop with range(10, 20, 3)")
for i in range(10, 20, 3):
    print (i)

# operators
# +
tuple1 = (4, 5)
tuple2 = (6, 15)
print(tuple1 + tuple2)
# print ("my_string" + 4)

# -, *, /, //
# float division
my_result = 15 / 2
print (type(my_result))
print(my_result)

# integer division
my_result2 = 15 // 2
print (type(my_result2))
print(my_result2)

# %
my_result3 = 15 % 2
print(my_result3)

# ** power operator
print (2 ** 5)

# =, ==, +=, -=, *=, /=

# !=, <, <=, >, >=

# and, or, not 
# is, is not

x = ["apple", "banana", "cherry"]
y = x
print(x is y)
print(x == y)

z = ["apple", "banana", "cherry"]
print(x is z)
print(x == z)

# in 
if "IE 201" in my_dict:
    print("IE 201 is taught by " + my_dict["IE 201"])
else:
    print("IE 201 is not taught this semester")

my_int_list = list(range(10))
print(my_int_list)

if 5 in my_int_list:
    print("5 is found in list")
else:
    print("5 is not found in list")

my_int_set = set(range(10))
print(my_int_set)

if 5 in my_int_set:
    print("5 is found in set")
else:
    print("5 is not found in set")

for r in [10, 500, 10000, 50000, 1000000, 10000000, 100000000]:
    print ("r = ", r)
    l = list(range(r))
    s = set(range(r))

    start_s = time.time()
    print (-1 in s)
    end_s = time.time()
    print ("set lookup took ", end_s - start_s)

    start_l = time.time()
    print (-1 in l)
    end_l = time.time()
    print ("list lookup took ", end_l - start_l)
