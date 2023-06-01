# From Dhanshika

import random

answer = random.randint(1,100)

guess = int(input("Enter any Number:"))
    
while answer != guess:
    if answer<guess:
        print("Number too high! \U0001F446")
    elif answer>guess: 
        print("Number too low! \U0001F447")        

    guess = int(input("Enter a Guess"))

print("Good Job! \U0001f600")
