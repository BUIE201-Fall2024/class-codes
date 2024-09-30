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
