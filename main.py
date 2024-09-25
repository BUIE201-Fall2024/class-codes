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
