age = 8

print(age.real)
print(age.imag)
print(age.bit_length())  # Number of bits necessary to represent this number in binary notation

items = [1, 2]
items.append(3)
items.pop()

print(id(items))

# Loops

i = 0
while i < 2:
  print("The condition is true.")
  i += 1

for item in items:
  print(item)

for i in range(len(items)):
  print(items[i])

for i in range(5):
  print(i)

items = [1, 2, 3, 4]

for index, item in enumerate(items):  # Enumerate gets index and item
  print(index, item)

for item in items:
  if item == 2:
    continue
  print(item)

for item in items:
  if item == 2:
    break
  print(item)
