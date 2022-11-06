# input in Python
# python uses the function input() to capture and store input in the application

print("User Profile Application")

first_name = input("First Name: ")
last_name = input("Last Name: ")
occupation = input("Your Job: ")

# print("Your first name is: " + first_name)
# print("Your last name is: " + last_name)
# print("Your occupation is: " + occupation)

# another way of outputting in python is through "condensing output" into a formatted string
print(f"Your first name is {first_name} and your job is {occupation}")

# Handling non-string input
# without "int()" - error: cannot concatenate int and string(25) ?:P
age = int(input("Please enter your age: "))

print(f"In two years, your age will be {age+2} ")
