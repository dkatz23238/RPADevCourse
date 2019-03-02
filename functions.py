# Python RPA Developer Course

# Functions

def do_something():
    x = 2
    y = 3
    hello = "hello"
    return x * y * hello

print(do_something())

# We can assign the outputs of a function to a variable
mysomething = do_something()

print(mysomething)

# Functions can take in arguments. We can explicitly define them if the user chooses not to. 
# A predefined argument is like a place holder
def my_function(country = "Norway"):
  print("I am from %s" % country)

print(my_function())
print(my_function("Peru"))


# Note that we use return and not print.
# Calling this function will not return any data

# Not passing in an argument will result in a TypeError

# Calling help(function) will identify the arguments
def my_function_2(country):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function("Brazil")