# Functions - a set of instructions that we can run when needed
# Paramaters - The values accpeted by the function inside the function definetion
# Arguments - The values we pass to the function when we call it

def hello(name="my friend", age = 19):  # Optional / default argument
  print("Hello " + name + ", You are " + str(age) + " years old!")

hello("Sami", 18)
hello("Samippya", 20)
hello()

# The function does not change the value because parameters are passed by reference
# Since some of these are immutable, then if we modify it's value inside the function then it won't be modified outside.

def change(value):
  value = 2

val = 1
change(val)
print(val)

# Anything mutable can change inside a function which is then modified outside the function. 

def change1(value):
  value["name"] = 2

val1 = {"name": "Sami"}
change1(val1)

print(val1)

# Return statement

def hello1(name):
  print(f"Hello {name}!") 
  return name, "Sami", 19

print(hello1("Sami"))

# Variable scope

# Global variable - Can access both inside and outside functions.
# Local variables - Can access only inside of a function

age = 19

def test():
  age = 10
  print(age)

print(age) # 19
test() # 10 

# Nested functions - Functions only visable inside another function

def talk(phrase):
  def say(word):
    print(word)

  words = phrase.split(' ')
  for word in words:
    say(word)

talk("I am going to buy the milk")

def counter():
  count = 0

  def increment():
    nonlocal count  # To access variables defined in the outer function
    count = count + 1
    return count

  return increment

increment = counter()

print(increment())
print(increment())
print(increment())
