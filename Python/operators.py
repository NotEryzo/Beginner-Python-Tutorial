# Operators

# Assignment
age = 19  
fire = True
water = not fire

# Arithmetic operators

print(1 + 1)  # Addition, output = 2
print(2 - 1)  # Subtract, output = 1
print(2 * 2)  # Multiplication, output = 4
print(4 / 2)  # Division, output = 2.0
print(4 % 3)  # Modulus or Remainder, output = 1
print(4 ** 2) # Power, output = 16
print(5 // 2) # Integer division, output = 2 

print("Hello " + "My name is " + "Sami")

age += 1
print(age)  # Output = 20
# += -= *= /= 

# Comparison operators

a = 1
b = 2

a == b  # False
a != b  # True
a > b  # False
a < b  # True

# Boolean operators

condition1 = True
condition2 = False

not condition1  # False
condition1 and condition2  # False
condition1 or condition2  # True

# The or operator returns the first value that is not false (or true). 0 represents false so the output is 1
# If x is false then y else x

print(0 or 1)  # 1
print(False or 'hey')  # hey
print('hi' or 'hey')  # hi since both are not false
print([] or False)  # 'False' - Empty bracket means false
print(False or [])  # '[]'

# The and operator will only evaluate the second argument if the first one is true. If the first is false then it will return that argument.
# If x is false then x else y

print(0 and 1)  # 0
print(1 and 0)  # 0
print(False and 'hey')  # False
print('hi' and 'hey')  # 'hey'
print([] and False)  # []
print(False and [])  # False

"""
Bitwise operators

& performs binary AND
| performs binary OR
^ performs a binary XOR opertation - Exclusive or
~ performs a binary NOT operation - Negation
<< shift left operation
>> shift right operation

Is (Identity operator) and In (Membership operator)
- Is returns true if both objects being compared are the same. 
- In is used to tell if a value is contained in a list or another sequence. 

"""

# Ternary operator - Allows us to quickly define a conditional  

def is_adult(age):
  if age > 18:
    return True
  else:
    return False
  
def is_adult2(age): 
  return True if age > 18 else False

# Built-in functions

print(abs(-5.5))  # Absolute value
print(round(5.49))  # Round to the nearest integer
print(round(5.49, 1)) # Round to the nearest 10th place value integer

# Enums are readable names that are bound to a constant value
# Only way to create constants in Python

from enum import Enum

class State(Enum): 
  INACTIVE = 0
  ACTIVE = 1

print(State.ACTIVE.value)
print(State(1))
print(State['ACTIVE'])
print(list(State))
print(len(State))

