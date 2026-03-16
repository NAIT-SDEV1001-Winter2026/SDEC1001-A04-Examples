while True:
    user_input = (input("Enter something. Cannot be nothing: "))
    if user_input.strip():#if a string has nothing in it, it is False when used in a condition, otherwise it is True
        break

#if "Hello":            TRUE
#if "":                 FALSE
