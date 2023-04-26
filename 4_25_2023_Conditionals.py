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
