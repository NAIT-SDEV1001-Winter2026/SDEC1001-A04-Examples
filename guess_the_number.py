import random
play_again = "y"

while play_again == "y":
#Generate a random between 1 and 100
    random_number =  2#random.randint(1,100)
    is_done = False
    guesses = 0
    while not is_done:
        #get users guess
        guess = int (input("Enter a guess (1-100): "))
        guesses +=1
        #if not correct tell user if guess is too high or too low
        if guess == random_number:
            #win
            print("You win!")
            is_done = True
        elif guess < random_number:
            #too low
            print("Too low!")
        else:
            #too high
            print ("Too High!")
        #Keep guessing until number is guessed

    #print the number of guesses
    print(f"It took you {guesses} guesses")
    #Ask to play again validated
    is_valid = False
    play_again = input("Would you like to play again? (y/n): ")
    while not is_valid:
        if play_again == "y" or play_again =="n":
            is_valid = True
        else:
            play_again = input(f"Invalid entry!Cannot be {play_again}! Read the rules! Would you like to play again? (y/n): ")
        

print("Thanks for playing. Have a groovy day!") 

#Add to this solution the ability to play again if the user wants too after they win!
