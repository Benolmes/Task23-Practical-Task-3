#Need to use inputs to get the variable information.
#The information can then be printed using an f string to display it in a user friendly format.

name = input("Name: ")
age = input("Age: ")
street = input("Street: ")
house_number = input("House number: ")

print(f"This is {name} who is {age} years old. They live at {house_number} {street}.")