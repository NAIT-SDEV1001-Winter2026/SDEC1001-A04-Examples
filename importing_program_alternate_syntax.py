#another way to import
#However, you need to reference the module before each function when you use a function
import calculator_tools

number1 = int(input("Enter number 1: "))
number2 = int(input("Enter number 2: "))

sum = calculator_tools.add(number1,number2)

print (f"The sum is: {sum}")
