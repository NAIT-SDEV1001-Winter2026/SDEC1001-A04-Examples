#A Module is a py file that contains functions that can be imported by other files to be used

def get_and_calculate_average (sum,count):
    average = sum/count
    return average

def get_valid_positive_int(prompt):
    while True:
    #get user input
        user_input = input(prompt)
        try:                      
            user_input = int(user_input) 
            if user_input > 0:            
                break#if valid then break out of the input loop
            else:
                print("Please enter an integer greater than 0.\n")           
        except ValueError:
            print("That wasn't a valid integer. Please try again.\n")
    return user_input

def get_valid_positive_float(prompt):
    while True:
        user_input = input(prompt)
        try:
            user_input = float(user_input)
            if user_input > 0:                                                        
                break
            else: 
                print("Please enter a non-negative time in seconds.\n")
        except ValueError:
            print("That wasn't a valid number. Please try again.\n")
    return user_input