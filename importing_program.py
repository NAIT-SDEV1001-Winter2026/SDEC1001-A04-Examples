#When we import like this (*) we import everything, including any mainline code that executes. To only import the functions we use a main guard (coded on the imported file) 
from calculator_tools import *

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

sum = add(number1,number2)

print (f"The sum is: {sum}")
