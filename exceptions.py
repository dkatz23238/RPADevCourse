# Python RPA Developer Course

# TypeError and IndexError

my_list = ["steven", 21, {"food":"pasta"}]

# 3 things that will cause exceptions

# this will return a TypeError
my_list[0] + 9

# this will also return a TypeError
len(my_list[1])

# this will produce a KeyError

# Python allows us to dynamically take care of errors

# The following syntax does this for us

try:

    my_list[0] + 9

except Exception as e:
    print("ERROR")
    print(e)

# if your try block does not cause error no other action will happen

try:

    print("hello")

except Exception as e:
    print("ERROR")
    print(e)
    