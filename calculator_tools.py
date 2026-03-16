def add (number1,number2):
    answer = number1 + number2
    return answer

def subtract (number1,number2):
    answer = number1 - number2
    return answer

def divide (number1,number2):
    answer = number1 / number2
    return answer

def multiple (number1,number2):
    answer = number1 * number2
    return answer
#We only want this mainline code to execute if this py file is executed directly, not if it is imported from somewhere else.
#This is called a main guard

#__name__ is a dunder variable
#If this py file is run directly, __name__ contains "__main__"
#If this py file is NOT run directly(imported) it contains the name of the file it is in
print(__name__)
if __name__ == "__main__":
    #Demonstrate Functions
    print (add(6,3))
    print (subtract(6,3))
    print (divide(6,3))
    print (multiple(6,3))

#for the rest of the course, we will place the main guard before the mainline


