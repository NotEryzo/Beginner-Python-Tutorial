# Variables

name = "Sami"
age = 19

# Statements
print(f"My name is {name} and I am {age} years old")

# Datatypes

print(type(name), type(age))

# Checking correct datatype
print(isinstance(name, str))
print(isinstance(age, int))

# Typecasting - converting to different datatypes

age = float(age)
a = "20"
print(isinstance(int(a), int))

"""
Datatypes:

Strings - str
Integers - int
Floats - float
Booleans - bool
Lists - list
Tuples - tuple
ranges - range
dictionaries - dict
sets - set
complex numbers - complex

"""

# Example of complex numbers

num1 = 2 + 3j
num2 = complex(2, 3)

print(num2.real, num2.imag)

# Control statements

condition = True

if condition == True:
  print("The condition")
  print("was true")
elif name == "sami":
  print("hello")
else:
  print("The condition")
  print("was false")

