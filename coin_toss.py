#NO FUNCTIONS
#Randomly generate a coin toss
#Get the valid guess from the user
#Display if they are correct or not

#random.choice([True, False])

import random
# heads will be 0 and tails will be 1
toss = random.choice(["Heads","Tails"]).lower()

while True:
    user_guess = input("Guess the coin flip! Enter heads or tails (Heads/Tails): ").lower()
    if user_guess == "heads" or user_guess == "tails":            
            break
    else:
        print("You must enter Heads or Tails!")           
 
if toss == user_guess:
    print("you guessed correct!")    
else:
    print("you guessed wrong!")