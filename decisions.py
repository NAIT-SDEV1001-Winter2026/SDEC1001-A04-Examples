# #Decision making is the ability to control the flow of program based on conditions
# #In Python we will use if, elif, else statements

# #Sytnax of basic if
# #if condition:
#     #code to run if the condition is TRUE

# #Comparision operators: ==, !=, <, >, <=, >=

# age = 11

# if age >= 18:        
#     print("You are an adult")#only prints if >=18
#     print("Yay!")#only prints if >=18    

# print("Have groovy day!")# Always prints

# score = 100 #Assignment operator

# if score == 100: #Comparision Operator
#     print("perfect score!")

# print("Have a groovy day!")

# #Ask the user for their name. If it is your name print "Awesome name!"
# name = input("Enter your name: ")
# if name == "Shane":
#     print("Awesome Name!")

# #Remember, Python is case sensitive!
# #Shane is different than shane
# #In this course, it will be an expectation that user entered strings should be tested as case insensitive(user can enter any case)
# name = input("Enter your name: ")
# if name.upper() == "SHANE":
#     print(f"{name.capitalize()} is an awesome Name!")

# #Boolean
# #Use the word is in front of Boolean variable names
# is_awesome = True
# if is_awesome == True:
#     print("Awesome!")

# #Boolen decisions should be written as
# if is_awesome:
#     print("Awesome!")

# is_awesome = False
# if not is_awesome:#Checks for False
#     print ("NOT Awesome!")

#if else
# if condition: == True
    #True code
# else:
    #False code

# grade = int(input("Enter your grade: "))
# #With just if statements
# if grade >=50:
#     print("Pass")
# if grade <50:
#     print("Fail")

# print("Have a groovy day!")

# #inefficient as it checks grade <50 even if the grade was 80
# #Use else!
# if grade >=50:
#     print("Pass")
# else:
#     print("Fail")

# print("Have a groovy day!")

#if elif else
grade = int(input("Enter your grade: "))

if grade >=80:
    print("Honors!")
    print("You are smart!")
elif grade >=50:
    print("Pass")
elif grade == 0:
    print("Where were you?")
else:   #if no other conditions are True
    print ("Fail")















