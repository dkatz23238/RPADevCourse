# Python RPA Developer Course

# For Loops

mylist = ["John", "Bob", "Julie", "Anne"]

for name in mylist:
    print("%s's is this long:" % name)
    print(len(name))


for n in mylist:
    for l in n:
        if (l == "A") or (l == "J") or (l == "D"):
            print(l)
            print("The condition has been satisfied")
    print("Going onto next item in list")

# While Loops

n = 0

while (n <= 5):
    print(n)
    n = n + 1

# Be careful because while loops can become infinite ig we dont terminate them
n = 0

while (n <= 5):
    print(n)


# We can programatically stop a loop by using the word break

# The range function returns an ordered series of intergers from 0 to the arguments passed -1

mylist = range(20)
for number in mylist:
    print(number)
    if number > 15:
        break

for number in range(20):
    print(number)
    if number > 15:
        break

# Hold control - c to interupt any python programming

