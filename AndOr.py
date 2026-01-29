#And/Or
#T and T = T
#T and F = F
#T or T = T
#T or F = T

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

#And
#All conditions must be True for the entire condition to be True
if number1 == 5 and number2 == 8:
    print ("Number 1 is 5 and number 2 is 8")

#or 
#If any of the coniditions are true, the entire condition is True
if number1 == 5 or number2 == 8:
    print ("At least one of the conditions is True")

#And takes precedence over Or. Evaluate the And conditions FIRST
#Brackets take precedence ALWAYS