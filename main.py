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
