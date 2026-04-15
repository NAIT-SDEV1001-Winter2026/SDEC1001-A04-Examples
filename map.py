#seperates comma seperated string into seperate values, casts to ints and assigns to variables x,y, and z
user_input = input("Enter 3 numbers, seperated by a comma: ")

x,y,z = map(int,user_input.split(","))

print(x)
print(y)
print(z)

