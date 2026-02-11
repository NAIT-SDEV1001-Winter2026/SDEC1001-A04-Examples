# Print a pyramid that is the number of rows entered by the user.  Remember:
# •	We can print a string a certain number of times
# •	We can concatenate strings together with +
# •	We can use a range loop to loop through the number of rows that must be printed

rows = int (input("Enter the number of rows: "))
   
for row in range(1, rows + 1):
    spaces = rows - row #Spaces before the *
    stars = 2 * row -1 #number of stars

    print (" " * spaces + "*" * stars)