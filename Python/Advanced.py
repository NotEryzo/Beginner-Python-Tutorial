"""
import sys
import argparse

parser = argparse.ArgumentParser(
  description="This program prints the name of my dogs"
)

parser.add_argument('-c', '--color', metavar='color', required=True,choices={'red', 'yellow'}, help='the color to search for')

args = parser.parse_args()

print(args.color)

print(sys.argv)  # Printing the arguments 


This is all done in the powershell or terminal. We can run the code by typing python "name of file", then typing in the arguments

"""

# Lambda functions - Anonymous functions that only have one expression 

lambda num : num * 2

multiply = lambda a, b : a * b

print(multiply(2, 4))

# Map(), filter(), reduce()

# Map - Takes each element of a list and does something to it. Run a function on each item of a list.

numbers = [1, 2, 3, 4, 5, 6]

def double(a):
  return a * 2

result = map(lambda a : a * 2, numbers)

print(list(result))

# Filter - takes an iterable and returns a filter object which is another iterable without the original itemss

def isEven(n):
  return n % 2 == 0

result = filter(lambda n : n % 2 == 0, numbers)

print(list(result))

# Reduce - Calculate a value out of a sequence

expenses = [
  ('Dinner', 80), 
  ('Car repair', 120)
]

sum = 0
for expence in expenses:
  sum += expence[1]

print(sum)

from functools import reduce

sum1 = reduce(lambda a, b: a[1] + b[1], expenses)

print(sum1)

# Recursion

def factorial(n): 
  if n == 1: return 1  # Base case
  return n * factorial(n-1)  # Calling function again with a new argument

print(factorial(3))
print(factorial(4))
print(factorial(5))

# Decorators - Function that takes a function as a parameter, wraps the function in the inner function, and returns that inner function

def logtime(func):
  def wrapper():
    print("Before")
    val = func()
    print("After")
    return val
  return wrapper

@logtime

def hello():
  print("Hello")

hello()

# Annotations

def increment(n: int) -> int:
  return n + 1

count: int = 0
