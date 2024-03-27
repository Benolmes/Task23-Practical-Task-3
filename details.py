#Need to use inputs to get the variable information.
#The information can then be printed using an f string to display it in a user friendly format.

name = input("Please enter your name: ")
age = input("Please enter your age: ")
street = input("Please enter the name of the street you live on: ")
house_number = input("Please enter your house number: ")

print(f"This is {name} who is {age} years old. They live at {house_number} {street}.")