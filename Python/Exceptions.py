# Exceptions - Error handling

try:
  result = 2 / 0
except ZeroDivisionError:
  print("Cannot divide by zero!")
finally:
  result = 1

print(result)

try: 
  raise Exception('An error')
except Exception as error:
  print(error)

class DogNotFoundException(Exception):
  print("Inside")
  pass

try:
  raise DogNotFoundException()
except DogNotFoundException:
  print("Dog not found!")

"""

Working with files:

filename = "test.txt"

try:
  file = open(filename, 'r')
  content - file.read()
  print(content)
finally:
  file.close()

with open(filename, 'r') as file:
  content = file.read()
  print(content)

"""

