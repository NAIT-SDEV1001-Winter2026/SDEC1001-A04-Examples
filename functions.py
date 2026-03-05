#functions are a bunch of code that is given a name
#they are called by name
#Can return a value
#values passed to functions when they are called are called arguments and the arguments are accepted into parameters
#Parameters values are not optional 
#Should perform a single task/operation
#Breaks down larger problems into smaller problems

# name1 = input("Enter your name: ")
# print(f"Welcome {name1}")

#using functions
#prompt for name and return the name
# def get_name(): 
#     name = input("Enter your name: ")
#     return name#returns a value from the function

# def display_name(name):
#     print(f"Welcome {name}!")
# #mainline/driver
# name = get_name()
# display_name(name)

# #Multiple parameters
def add_numbers(number1,number2):
    answer = number1 + number2
    return answer    

# print(add_numbers(5,3))

# print(add_numbers())

#default parameter values
def display_favorite_color (color = "Purple"):
    print (f"Your favorite color is {color}")
    
display_favorite_color("Blue")
