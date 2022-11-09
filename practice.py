# note = "The quick brown fox jumped over the lazy dog"
# print(note)
# print(note.count("dog"))


# # --------------------------FLOW CONTROL-------------------------
# # LOOPS
# print("Please enter your first name")
# fname = input("First name: ")
# for letter in fname:
#     print(letter)


# # End number in range (30) not included. If you want it included use 31.
# for number in range(0, 30, 3):
#     print(number)


# count = 10
# while (count >= 0):
#     print(f"The counter is currently on {count}")
#     if (count % 2 == 0):
#         print(f"{count} is even")
#     else:
#         print(f"{count} is odd")
#     count -= 1
# print("End of loop")

# # CONDITIONAL STATEMENTS
# print("Please enter your age")
# age = int(input("Age: "))
# if (age >= 21):                # # This line would throw a string-int error without "int" on previous line
#     print("You are eligible for a PSV driver's license")
# elif (age >= 18):
#     print("You are eligible for a driver's license but not for PSVs.")
# else:
#     print(f"You are not eligible for a driver's license until you are 18 years of age. Come back in {18-age} years")

# print("Please enter the mark")
# mark = int(input("Mark: "))
# if (mark >= 70):
#     print("Pass: Grade A")
# elif (mark >= 60):
#     print("Pass: Grade B")
# elif (mark >= 50):
#     print("Pass: Grade C")
# elif (mark >= 40):
#     print("Pass: Grade D")
# else:
#     print("Fail")
# ---------------------------------------------------------------


# #------------------------------DICTIONARIES---------------------------
# my_car = {
#     "Brand": "Volkswagen",
#     "Model": "Beetle",
#     "YoM": "1970",
# }

# print(f"Car specifications: {my_car}")

# my_phones = {
#     "phone_one": {
#         "Brand": "Apple",
#         "Model": "6s",
#         "YoM": "2018",
#     },
#     "phone_two": {
#         "Brand": "Samsung",
#         "Model": "s8",
#         "YoM": "2020",
#     },
#     "phone_three": {
#         "Brand": "Nokia",
#         "Model": "Lumia",
#         "YoM": "2022",
#     },
# }

# # print(f"Phone one specs: {my_phones['phone_one']}")
# print(my_phones["phone_one"])

# Just prints the "titles"
# for phone in my_phones:
#     print(phone)

# Prints all details
# for phone in my_phones:
#     print(my_phones[phone])

# Prints both title and details
# for phone in my_phones:
#     print(phone)
#     print(my_phones[phone])
# ---------------------------------------------------------------

# # ----------------------TUPLES---------------------------------
# cars = ("BMW", "Mercedes", "Honda")
# print(type(cars))
# print(len(cars))

# print(cars[1])
# print(cars[0])
# print(cars[-1])

# print(cars)

# for car in cars:
#     print(car)
# ---------------------------------------------------------------

# --------------------------SETS----------------------------------
# wa_countries = {"Sierra Leone", "Togo", "Benin", "The Gambia"}
# print(type(wa_countries))
# print(wa_countries)

# na_countries = {"Egypt", "Libya", "Algeria", "Tunisia"}
# print(na_countries)

# na_countries.add("Morocco")
# print(na_countries)

# africa = {"Kenya"}
# print(africa)

# africa.update(wa_countries)
# print(africa)

# africa.update(na_countries)
# print(africa)
# ---------------------------------------------------------------

# # ------------------------------------LISTS---------------------------------------
# fruits = ["Pineapple", "Peach", "Orange", "Mango", "Apple"]
# print(fruits)
# print(fruits[0])
# print(fruits[-1])
# print(f"The number of fruits in the list is {len(fruits)}")


# for fruit in fruits:
#     print(fruit)

# fruits.append("Lemon")
# print(fruits)
# print(f"The number of fruits in the list is {len(fruits)}")

# fruits.remove("Peach")
# print(fruits)

# fruits.pop(1)
# print(fruits)

# fruits.pop()
# print(fruits)

# fruits.insert(1, "Lemon")
# print(fruits)
# ---------------------------------------------------------------
