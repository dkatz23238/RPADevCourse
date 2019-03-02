# Python RPA Developer Course

# List and Tuples

employee1 = "bob"
employee2 = "jack"
employee3 = "josh"

employees_tuple = (employee1, employee2, employee3)

print( type(employees_tuple) )

employees_tuple = ("bob", "jack", "josh")

# Just like strings tuples and lists can be sliced with brackets

employees_tuple[0]

# Tuples only have two methods

print(employees_tuple.count("jack"))
print(employees_tuple.index("jack"))

# Lets define a list
employees_l = [ employee1, employee2, employee3 ]

# Define a new variable called employee
employee4 = "stacy"

# we use the append method of the list data type to insert
# a piece of data to the end of a list
employees_l.append(employee4)

# Tuples can not be modified after created
# The following expression will result in a TypeError
employees_tuple[0] = 2

# Lists are mutable
employees_l[0] = "george"

# We can easily turn a tuple into a list using the list function
new_list = list(employees_tuple)

# Lets look at the pop method
print(employees_l)

# When you call pop on a list you remove the last item from that list
# At the same time python returns this last value for convenience
removed_employee =employees_l.pop()
print("removed employee is %s" % removed_employee)
print("Printing new list after pop method was used: ")
print(employees_l)