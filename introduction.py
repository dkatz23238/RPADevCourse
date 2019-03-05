# Python RPA Developer Course

# Introduction

# Let's write a few expressions. Lets remember our very first expression we wrote

print("Hello RPA developer!")


# Executing different expressions will result in the execution of them in the order you wrote them
print("A")
print("B")
print("C")

# Here is a simple mathematical expression

44 * 902 + 9

# Just like in algebra we can use parentheses to separate out terms that we want evaluated first
2 * 3 * (4 + 5)
# 54

# Let's write an expression that will produce an error
2 * 3 + "hello"
# TypeError: unsupported operand type(s) for +: 'int' and 'str'

# We can multiply a string by an int
2 * "hello"
# 'hellohello'

# What is a type
print(type("hello"))
# <type 'str'>
print(type(2019))
# <type 'int'>

# Basic data types in pyhon
print("hello")
print(23)
print(23.832)
print(True)

# Basic variable creation
greet = "hello"
print(greet)

# What is a variable?
some_number = 201.231
some_string = "hello"
some_number = 202.231
# We can assign expressions to variables
myexpression = (2*3*5)

# Other python functions
(len(some_string))
print(some_number)

# Comparison operators: >, <, =, and !=
the_number_one = 1
the_number_two = 2

# Is the number one equal to the number two?
print((the_number_one == the_number_two))

# Is the number one equal not equal the number two?
print((the_number_one != the_number_two))

# We can assign expression to variables
result_of_comparison = (the_number_one == the_number_two)

# The results of a comparison operator will always be a boolean value. 
# We can feed this boolean value into flow control statements.

if (result_of_comparison):
    print("Do this specific thing")
else:
    print("Do this other specific thing")


# Let's write a more complicated expression
some_value = 21.43

# Will not do anything because no condition was satisfied

if some_value < 10.0:
    print("Do something because some_value is less than 10")
elif some_value == 21.0:
    print("Doing something else becuase some_value is exactly equal to 21")
elif some_value > 22.0:
    print("Doing this becuase some_value is greater than 22")

some_value = 23

# Will not evaluate and resolve to last statement

if some_value < 10.0:
    print("Do something because some_value is less than 10")
elif some_value == 21.0:
    print("Doing something else becuase some_value is exactly equal to 21")
elif some_value > 22.0:
    print("Doing this becuase some_value is greater than 22")

employee1 = "bob"
employee2 = "steven"

# Logical Operators

# We can also use & , | for and , or
# Boolean operators: and and or
print(True and True)
print(False or True)
print(False and True)

if ( (employee1 == "bob") or  (employee2 == "bob")):
    print("Someone is called bob!")
else:
    print("Can somebody please get bob?")

