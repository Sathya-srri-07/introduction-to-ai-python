# Lists in Python

# Creating a list
fruits = ["apple", "banana", "mango", "orange"]

print("Fruits:", fruits)

# Accessing list elements
print("First fruit:", fruits[0])
print("Second fruit:", fruits[1])

# Adding an element
fruits.append("grapes")
print("After append:", fruits)

# Removing an element
fruits.remove("banana")
print("After remove:", fruits)

# Length of the list
print("Number of fruits:", len(fruits))

# Loop through a list
print("All fruits:")
for fruit in fruits:
    print(fruit)
