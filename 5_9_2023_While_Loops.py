# Basic while loop
i = 0

while i < 10:
    print(i)
    i += 1

print("done!")

# Previous getting items program with for loop
num_of_items = int(input("Enter how many items: "))
items = []

for i in range(num_of_items):
    item = input("Enter an item: ")
    items.append(item)

print(items)

# While Loop Input Program
# Get item input from user as many times as they want
# If they just hit enter for the item, making an empty
# string, then end the program and print the list

items = []
item = input("Enter an item: ")

while item != "":
    items.append(item)
    item = input("Enter an item: ")

print(items)
