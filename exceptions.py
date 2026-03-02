# try/except
#Handle unexpected situations gracefully and prevent the code from crashing
#try - if an exception occurs in the try block code will jump to the except block
#except - addresses the error and can perform clean up tasks and/or display nice error messages
# try:
#     numerator  = int(input("Enter a numerator: "))
#     denominator  = int(input("Enter a denominator: "))
#     quotient = numerator/denominator

#     print (f"The quotient is: {quotient}")

# except:
#     print("Something went BOOM! ERROR!")

# print("have a groovy day!")

#The above message is generic. Does not tell the user what they did wrong.

# try:
#     numerator  = int(input("Enter a numerator: "))
#     denominator  = int(input("Enter a denominator: "))
#     quotient = numerator/denominator

#     print (f"The quotient is: {quotient}")

# except ValueError:
#     print(f"You did not enter an integer! Try again!")
# except ZeroDivisionError:
#     print(f"Remember grade 3? Cannot divide by 0!")
# except:
#     print("Something went BOOM! ERROR!")

# print("have a groovy day!")

#Show nice exceptions messages and the Python one
# try:
#     numerator  = int(input("Enter a numerator: "))
#     denominator  = int(input("Enter a denominator: "))
#     quotient = numerator/denominator

#     print (f"The quotient is: {quotient}")

# except ValueError as error_message: #error_message is a variable holding the python error message
#     print(f"You did not enter an integer! Try again! If you do not understand send this to tech support: {error_message}")
# except ZeroDivisionError as error_message:
#     print(f"Remember grade 3? Cannot divide by 0! If you do not understand send this to tech support: {error_message}")
# except:
#     print("Something went BOOM! ERROR! ")
# finally: 
#     print("Always executes")#Executes if the try fails or succeeds

# print("have a groovy day!")

#Best practices
#Keep the try blocks small as possible
#provide nice error messages in the except
#Trap specific exceptions where possible

#ValueError - int("Turkey")
#TypeError - len(42) - len() is for strings not ints
#ZeroDivisionError
#NameError - print(abc) - There is no abc variable

#Using try/except
# while True:
#     try:
#         user_input = int(input("Enter an integer: "))
#         break
#     except ValueError:
#         print("That is not a valid integer! Try again!")

#User must enter an integer between 1 and 10. Loop until valid
# while True:
#     try:
#         number = int(input("Enter an integer between 1 and 10: "))
#         if number >=1 and number <=10:
#             break
#         else:
#             print("Must be between 1 and 10")
#     except ValueError:
#         print(f"That is not an integer! Try again!")
#how could we show the number in the error message?
while True:
    try:
        user_input = input("Enter an integer between 1 and 10: ")
        number = int(user_input)
        if number >=1 and number <=10:
            break
        else:
            print("Must be between 1 and 10")
    except ValueError:
        print(f"{user_input} is not an integer! Try again!")

#Summary
#Try the risky operation
#If it explodes, catch it in an except
#If it works, escape the loop

#For your lab you could use Try/except for (some could be handled other ways as well):
    #Catching casting errors from user input
    #Using remove() in a list to remove an item that is not there(ValueError)
    #Using a variable that has not been declared and assigned a value(NameError). Probably not an exception to catch... one to fix
    #Accessing an index that is not in the list(IndexError)





