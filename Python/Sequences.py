# Lists - Allows us to group together multiple values

items = ["Roger", 1 , "Syd", True]

print("Roger" in items)

# List indexing 

print(items[1])
items[3] = "Apple"
print(items)
print(items[-1])  # Reverse order
print(items[2:4])  # Slicing

print(len(items))

# Ways to add items
items.append(True)
print(items)
items.extend(["Hello"])
print(items)
items += ["My name"]
print(items)

# Ways to remove items
items.remove("Roger")
print(items)
print(items.pop())  # Removes the last item and returns it.
print(items)

# Ways to insert into a certain index
items.insert(2, "Test")
print(items)

items[1:1] = ["Test1", "Test2"]
print(items)

# Sorting lists

names = ["Sami", "Samippya", "Pokharel", "Sami Pokharel", "Samippya Pokharel"]
age = [19, 18, 22, 20, 15, 17]

namecopy = names[:]
print(sorted(names, key=str.lower))  # Doesn't modify original
print(names)

names.sort(key=str.lower) # Makes it so that uppercase and lowercase doesn't matter when sorting
age.sort()
print(names)
print(namecopy)
print(age)

# Tuples - Allow us to create immutable groups of objects (cannot be modified once created)

names1 = ("Sami", "Samippya", "Pokharel")
print(names1[0])
print(names1.index("Samippya"))
print(names1[-1])
print(len(names1))
print("Sami" in names1)

names1[0:2]
print(sorted(names1, key=str.lower))

newTuple = names1 + ("Tina", "Quincy") # Cannot modify the original tuple  

# Dictionaries

# Keys have to be immutable and cannot be duplicated
dog = {"name": "Roger", "age": 8, "time": "3:45"}
print(dog["name"])
dog["name"] = "Syd"
print(dog)
print(dog.get("color", "brown"))  # If we find the key color then return it's value, otherwise return brown

# Removing from dictionaries
print(dog.pop("name"))
print(dog)
print(dog.popitem())
print(dog)

# Searching in dictionaries
print("color" in dog)
print(list(dog.keys()))
print(list(dog.values()))
print(list(dog.items()))
print(len(dog))

# Adding and deleting in dictionaries
dog["color"] = "Grey"
print(dog)
del dog["color"]
print(dog)
dogCopy = dog.copy()

# Sets - These are not ordered and mutable

set1 = {"Roger", "Syd", "Luna"}
set2 = {"Roger", "Syd"}

intersect = set1 & set2  # All items these have in common
print(intersect)

union = set1 | set2  # Union of two sets, all the values in both sets with no duplicates. 
print(union)

difference = set1 - set2  # What is different between the two sets 
print(difference)

mod = set1 > set2  # Does set1 have everything in set2, also works the other way around using <
print(mod)

print(len(union))

print(list[union])

# List compression

numbers = [1, 2, 3, 4, 5]

numbers_power_2 = [n**2 for n in numbers]

print(numbers_power_2)

num = []
for n in numbers:
  num.append(n**2)

print(num)

num1 = list(map(lambda n : n**2, numbers))

