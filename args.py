def add_numbers(number1,number2):
    answer = number1 + number2
    return answer

# print (add_numbers(5,3))

#good, but you can only add 2 numbers
#*numbers is an arg (tuple)
def add_any_numbers(*numbers):
    sum = 0
    for number in numbers:
        sum += number
    return sum

# print(add_any_numbers(1,2,3,4,5,6))

#create a function that will be passed the name of a sport and displays it.
#pass in a number of scores as args
#pass in coaching staff as kwargs (Key - value pairs)

def sport_stuff(sport,*scores,**coaches):
    print (f"The sport is: {sport}")
    print("Scores: ")
    #Loop through all the scores
    for score in scores:
        print(score)
    #Loop through all the coaching staff
    for key, value in coaches.items():
        print(f"- {key}: {value} ")


sport_stuff("Soccer",3,5,2,7,4,coach = "Yoda", assistant_coach = "Luke Skywalker", water_boy = "Homer")


#Extra
#scores are passed into *scores
#technically, *scores "unpacks" the scores into a tuple
# * is called the unpacking operator. This concept can be used for other purposes since * will unpack any collection

grades = [60,80,55,77,99]
print (grades)#prints the list

print(*grades)

print(*"Shane")