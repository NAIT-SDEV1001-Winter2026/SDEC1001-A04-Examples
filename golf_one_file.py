def calculate_average(*args):
    #loop through the args tuple
    sum = 0
    for value in args:
        sum +=value
        
    average = sum/len(args)
    return average

def calculate_handicap(*args):
    if len(args) < 5:
        return "Need at least 5 scores to calculate a handicap"
    else:
        #some short cuts here
        #sort and slice
        top_five = sorted(args)[:5]
        return calculate_average(*top_five) - 72

print("Golf Score Calculator")
scores = []
playing = True
while playing:
    score_or_play_again = input("Enter another score (q to quit and calculate)?: ")
    if score_or_play_again == "q":
        break
    else:
        scores.append(int(score_or_play_again))


#We can pass a list to an arg parameter. Just need to put * in front of the name
#* unpacks the scores list into individual values to be passed into *args in the function
print(F"Your average golf score is {calculate_average(*scores)}")
print("Your handicap is:", calculate_handicap(*scores))