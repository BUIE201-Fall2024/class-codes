def my_function(name, last_name = ""):
    print("Hello " + name + " " + last_name + " from my_function()")

# positional parameters
my_function("caner", "taşkın")

# keyword parameters
my_function(last_name="taşkın", name="caner")

# default values
my_function("caner")

# non-default parameters must be set, otherwise we get an error
# my_function()
# my_function(last_name="taşkın")

def foo(name = "x", last_name = "y"):
    print("Hello " + name + " " + last_name + " from foo()")

foo()
foo(last_name="fsdfs")

def sum(a, b = 0, c = 0):
    return a + b + c

s = sum(3, 5)
print("sum(3, 5) = ", s)

s2 = sum(3)
print("sum(3) = ", s2)

s3 = sum(3, 5, 7)
print("sum(3, 5, 7) = ", s3)

# arbitrary arguments
def sum_all(*all):
    total = 0
    for i in all:
        total += i
    return total

s4 = sum_all()
print ("sum_all() = ", s4)

s5 = sum_all(4, 2, 6, 3, 67)
print ("sum_all(4, 2, 6, 3, 67) = ", s5)

def bar(x, y, *rest):
    pass

bar(10, 5, 35, 35, "fadfas", 3.24)
