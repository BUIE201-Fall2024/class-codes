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
