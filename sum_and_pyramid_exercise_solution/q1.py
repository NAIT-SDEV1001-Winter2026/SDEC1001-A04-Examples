# Find the sum of squares of the integers from 1 to my_square, where my_square is a variable that is input by the user. E.g. user enters 4 then return 1x1 + 2x2 + 3x3 + 4x4 = 30.

# The output should look like the following:

# Enter a number to sum the squares: 4
# The sum of squares is 30
sum = 0
my_square = int(input("Enter a number to sum the squares: "))

for number in range (1, my_square + 1):
    sum  += number ** 2

print (f"The sum of squares is {sum}")