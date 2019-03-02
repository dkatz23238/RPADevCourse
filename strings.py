# Python RPA Developer Course

# Strings

# Some common string methods

# The number 9 is not the same as the character "9"
print(9 == "9")

# Slicing a string using an index
print("hello"[0])
greet = "hello"
print(greet[0])

# For example calling the upper method on the variable hello will return 
# the same string in all capital letters.
hello = "hello"
print(hello.upper())

# If we do not close parenthesis after calling a method
# or a function Python will return the function itself and not be executed

print( hello.upper() )
# HELLO


print( hello.upper )
# <built-in method upper of str object at 0x00000000056CA698>

# Knowing the different methods a string can produce is usefull for our RPA development.

# Lets learn some

print(hello.count("h"))
print(hello.count("l"))
print(hello.replace("hello", "hellohellohellohello"))

# Although not a method, slicing is a way to return a specific part of a string
# Slicing in python is done with square brackets and you must use an index

print(hello[0])
print(hello[-1])
print(hello[3])
print(hello[3:2])

# Lets remember slicing as it is used with other data types we will learn later on in the book

# Operators on strings will have their own result.

# Using the plus (+) sing will concatenate strings together

name = "David"

print(hello + " " + name)

hello_to_strip = "     hello        "

print(hello_to_strip)
print(hello_to_strip.strip())

# For Example how to remove spaces from string and then add one space to each side
# We can overwrite variables by re declaring them

hello_to_strip = hello_to_strip.strip()
hello_to_strip = "  "+hello_to_strip+" "

# String insertions are awesome tools !
name = "David"
hello = "hello %s" % name
print(hello)
greeting = "Hor Are You Today?"
hello = "hello %s, %s" % (name, greeting)
print(hello)

# You can directly call methods on data without storing it in a variable too.
"hello".upper()

# If you need to define a long string you can use tripel quoates:

longstring = """
Hello,

My name is david.
Welcome to cross entropy.
"""
print(longstring)