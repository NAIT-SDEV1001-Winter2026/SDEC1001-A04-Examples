print ("variables, strings, input")
#Comment
#Use "" or '' for strings
print("Hello")
print('Hello')
#Print How's it going?
print ("How's it going?")
#print ('How's it going?')

#Escape Sequences - Allow us to place certain characters or behaviour in a string
#They us a \

print ('How\'s it going?')# \' prints a '
print ("You are \"Awesome\"!") # \" prints "
print ("Line 1\nLine 2") # \n goes to a new line
print ("Name: \tShane") # \t tab

#Concatonating Strings
print ("Hello"  + " World")

#Concatonating strings and numbers. Everything must be a string in the concatonation
print ("Score: " + str(55))#str(55) casts(converts) the 55 to a string

#in python we should use f strings
print (f"Score: {55}")

#Variables
#a named box that holds a value
#names can only contain letters, numbers and _
#use snake_case for variable names

#variables can hold different types of data
name = "Shane" #string
age = 53 # integer (do not use "" around numeric values)
price = 5.25 # float (floating point number (decimals))
is_valid = True # boolean (True/False)

#You can reassign variable values
score = 60
score = 600

#string data is case sensitive and so are variable names
a = "Hello World"
print (a)

age = 53
type = "Awesome" 
#GOOD
print (f"Shane is {age} years old and he is {type}")
#BAD 
print ("Shane is " + str(age) + " years old and he is " + type)  
 
#constants - like variables but do not change

GST_RATE = .05

#Input - returns a string
name = input("enter your name: ")
print (name)
print (f"Your name is {name}")

#ask the user for 2 integers
#Calculate the sum
#display the sum
number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2:` "))
#cast to an int after input OR at time of calculation
sum = int(number1) + int(number2)

print (sum)

#rounding
total = 124.4356

print (f"Total: {total:.2f}" )#returns a string
print (f"Total: {round(total,2)}" )# returns a float

print(round(2.4,2)) #2.4
print(f"{2.4:.2f}") #2.40

#Math Operators

print (2 + 4) #6
print (4 - 2) #2
print (2 * 4) #8
print (4 / 2) #2.0
print (9//4) #2 floor division
print (2**3) #8
print (9 % 4) #1

#Math Functions and constants
#import the math module to use more math stuff
import math
test_value = 5.245435
print (math.ceil(test_value))#ceiling (round up to whole number)
print (math.floor(test_value))#floor (round down to whole number)
print (math.pow(2,3))#power
print(math.sqrt(9))#sqrt
print(max(2,5,4,3,8,11,32,2))#highest value
print(min(2,5,4,3,8,11,32,2))#lowest value
print (math.pi)#pi 














 #TO DO WED
 #Constants
 #Input
 #casting to float/int with input for calculations
 #when to cast (input/calculation)
 #basic math operators
 






 
 
