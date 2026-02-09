# #Quick Review
# #Strings are lists of single characters
# #Loop through a string and print each letter on it's own line
# word = "Have a Groovy day!"
# for letter in word:#each iteration of the loop gets the next letter
#     print (letter)

# #Ask the user for a string and print how many vowels are in the string
# #Enter a string: Happy Monday
# #There are 3 vowels in 'Happy Monday'
# string  = input("Enter a string: ")
# #Happy Monday
# vowels = ("aeiou")
# count = 0
# for letter in string:
#     if letter in vowels:    
#         count += 1
# print (f"There are {count} vowels in '{string}'")

#Range Loops
#Repeating code a certain number of times
#range() generates a sequence of numbers and can be used for a loop counter

#Syntax
#range (start,stop,step)
#start is inclusive, stop is exclusive

#print numbers 1 to 5
for number in range(1,6):
    print (f"Number: {number}")

#calculate and print the cubes of numbers from 0 to 4
#0 cubed is 0
#1 cubed is 1

for number in range (0,5):
    print (f"number {number} cubed is {number ** 3}")

#if your range starts at 0 you can omit the start value
for number in range (5):
    print (f"number {number} cubed is {number ** 3}")

#print the even numbers between 4 and 20
for number in range(4,21,2):
    print(number)

#ask the user how many "Hello Worlds" to print
how_many = int(input("How many 'Hello World' to print? "))
for count in range(how_many):
    print ("Hello World")

#Print a string a certain number of times
print ("Hello " * 3)#prints "Hello " 3 times


#Ask the user for how many rows to print like this (right angle triangle):
# *
# **
# ***
# ****

how_many = int(input("How many rows to print? "))
for count in range (1, how_many + 1):
    print("*" * count)

    



