#Create a list of numbers 1,2,3,4,5
#Create another list of the those numbers squared
#print the squared list
numbers = [1,2,3,4,5]
squares = []
for number in numbers:
    squares.append(number ** 2)

print (squares)
#Using list comprehension(short cut)
numbers = [1,2,3,4,5]
squares = [number ** 2 for number in numbers]
print(squares)

#Create a list of 3 names
#Use list comprehension to a create another list of those names all in upper case
#print new list
names = ["Homer", "Bart", "Lisa"]
upper_names = [name.upper() for name in names]
print(upper_names)


#Without list comprehension:
#Create a list of numbers 1-10
#Populate another list with only the even numbers
#print the even list
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = []

for number in numbers:
    if number % 2 == 0:
        even_numbers.append(number)

print(even_numbers)
#List comprehension with a condition:
#[new_value for item in collection if condition]
numbers = [1,2,3,4,5,6,7,8,9,10]
even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)
