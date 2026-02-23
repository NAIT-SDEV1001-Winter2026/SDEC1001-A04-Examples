print("Golf score calculator")

scores = [] 
sum = 0
top_5_sum = 0

while True:
    #get scores from user
    score = input("Enter another score (q to quit and calculate): ")
    #if q then quit
    if score == "q":
        break         
    #Add value to sum
    sum += int(score)       
    #Add the score to the list
    scores.append(int(score))

#Calculate the average
average = sum/len(scores)

#Display average
print (f"Your average golf score is {average}")

#Calculate the handicap
if len(scores) < 5:
    print("Your handicap is: Need at least 5 scores to calculate a handicap")
else:
    #Sort the list ascending
    scores.sort()
    #sum the first 5 scores
    #Loop through the first 5 elements in the list
    for score in scores[0:5]:
        #add the score of each element to top_5_sum
        top_5_sum += score
    #Calculate average of the 5 scores and subtract 72
    handicap = (top_5_sum/5) - 72
    #Display the handicap
    print (f"Your handicap is: {handicap:.2f}")
