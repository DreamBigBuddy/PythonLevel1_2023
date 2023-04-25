# Day 2 - Lists and Conditionals and Loops
import sys # ignore for now

# Lists
my_list = ["test", 4, "e"]

print(my_list)

my_list.append("Hi")

print(my_list)

my_list.append(1)

print(my_list)
print(len(my_list))

my_list.remove("Hi")

print(my_list)
print(len(my_list))

my_list.remove(1)

print(my_list[0])

my_list.insert(1, "blah")

print(my_list)

my_list[1] = 2

print(my_list)

# Simple conditional program
num = 1 # Change value of num to see different output

if num == 1:
    print("num equals 1")

elif num <= 5:
    print("num is less than 5")

else:
    print("num equals", num)

# Weather program
weather = input("What is the weather? ")

if weather == "rainy":
    print("Make sure you have an umbrella!")
	
elif weather == "sunny":
    print("Make sure you have ice cream!")
    	
else:
    print("Have a nice day!")

# Age Checker
age = int(input("Enter your age "))
          
if age <= 5: #if age younger than or equal to 5
    print("You’re very young!")
          
elif age == 6: #if age equals 6
    print("You are 6 years old!")
	
elif age >= 7: #if age older than or equal to 7
    print("You’re old!")

# Conditional Keywords
num = 45 # Change num to alter output

if num <= 0 or num > 100:
    print("num is either less than 0 or greater than 100")

elif num > 0 and num <= 10:
    print("num is between 0 and 10")

elif num > 10 and num < 50:
    print("num is between 10 and 50")

elif num >= 50 and num <= 100:
    print("num is between 50 and 100")

# For Loop
for i in range(0, 10, 1): # Change values to see how a for loop can be modified
    print(i)

# List and Range
my_list = list(range(10))
print(my_list)

# More For Loops
# Summing a range of numbers
total = 0
for i in range(10):
    total += i

print(total)

# Asking user to input items (user specifies amount ahead)
num_of_items = int(input("Enter how many items: "))
items = []

for i in range(num_of_items):
    item = input("Enter an item: ")
    items.append(item)

print("Here are the items you entered", ', '.join(items))

# While Loops
# Summing a range of numbers
total = 0
iterate = 0

while iterate < 10:
    total += iterate
    iterate += 1

print(iterate)

# Asking user to input items (unspecified amount of items)
items = []
item = input("Enter an item: ")
while item != "":
    items.append(item)
    item = input("Enter an item: ")

print("Here are the items you entered", ', '.join(items))
