class Animal:
  def walk(self):
    print("Walking...")

# Inheritance
class Dog(Animal):
  def __init__(self, name, age):
    self.name = name
    self.age = age
  
  def __gt__(self, other):
    return True if self.age > other.age else False

  def bark(self):
    print("woof!")

roger = Dog("Roger", 8)

print(type(roger))
print(roger.name)
print(roger.age)

roger.bark()
roger.walk()

"""
Modules

Importing functions from other libraries or files

math - math utilities
re - regular expression
json - JSON files
datatime - Work with Dates
sqlite3 - SQLite
os - operating system
random - random number generation
statistics - statistics utlilities
requests - HTTP network requests
http - to create HTTP servers
urllib - manage urls

"""

# Polymorphism - calling two of the same methods but they ouput different results

class Dog1:
  def eat(self):
    print("Eating dog food")

class Cat:
  def eat(self):
    print("Eating cat food")

animal1 = Dog1()
animal2 = Cat()

animal1.eat()
animal2.eat()

# Operator overloading

syd = Dog("Syd", 7)

print(roger > syd)

"""
__add__() - +
__sub__() - -
__mul__() - *
__truediv__() - /
__floordiv__() - //
__mod__() - %
__pow__() - **
__rshift__() - >>
__lshift__() - <<
__and__() - &
__or__() - |
__xor__() - ^

"""
