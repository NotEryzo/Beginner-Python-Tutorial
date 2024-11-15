# Strings - A series of characters enclosed in quotations


# String concatenation
name = "Sami " + "Pokharel"
print(name)
name += " I am 19 years old"
print(name)

age = str(39)
print(isinstance(age, str))

# Multi-line string
print("""\nThis is
 
a Multi

-line string!
""")

# String methods 

name = "Sami"
last = "pokharel"

# These don't change the original string if printed, but they will change if we set it to change.

print(name.upper())  # Uppercase all letters
print(name.lower())  # Lowercase all letters
print((name + " " + last).title())
print(last.islower())  # Checks if the string is lowercase
print(name.isalpha())  # To check if a string contains only characters and is not empty
print(name.isalnum())  # To check if a string contains characters or digits and is not empty
print(name.isdecimal())  # To check if a string contains digits and is not empty
print(name.isupper())  # To check if a string is uppercase
print(name.startswith("S"))  # To check if the string starts with a specific substring
print(name.endswith("i"))  # To check if the string ends with a specific substring
print(name.replace(name, last))  # To replace a part of a string
print((name + " " + last).split())  # To split a string on a specific character seperator
print(name.strip())  # To trim the whitespace from a string
print(name.join("A"))  # To append new letters to a string
print(name.find("S"))  # To find the position of a substring

print(len(name))  # Will print the length of the argument, works on multiple datatypes
print("mi" in name)

# Escaping characters - \

print("He\"llo")
print("Hello\nMy name is\nSami")  # \n means new line

# String characters and Slicing

print(name[0], name[1])
print(name[-1])

# Slicing - Range
print(name[1:3])
print(name[:2])
print(name[::2]) # Skip

# Booleans - Useful for conditional statements
# 0 represents false, otherwise any other number represents true
# Empty strings represent false, otherwise any non-empty string represents true
# Same with lists, tuples, dicts, sets ^


done = True

if done:
  print("Yes")
else:
  print("No")

book_1_read = True
book_2_read = False

# The any function returns true if any of the values of a list is true. So it will return true. 
read_any_book = any([book_1_read, book_2_read])

# The all function returns true if all of the values are true. 
read_any_book = all([book_1_read, book_2_read])

# User input

age = input("What is your age?: ")
print(f"Your age is {age}")