#List is a collection of values stored in a single variable
#Each value can be accessed from a zero based index
#Can hold multiple datatypes (including other lists!)

colors = ["red", "blue", "green","yellow"]
#Display the entire list
print (colors)

#access a single value by its index
print(colors[1])

#Access from the end of a list
print(colors[-1])

#change a value in a list
colors[2] = "purple"
print(f"green is now {colors[2]}")

#slicing lists
letters = ["a","b","c","d","e"]
print (f"First three letters: {letters[0:3]}")
#with slices, the lower boundary is inclusive, the upper boundary is exclusive

#length of a list
print (len(letters))

#Accessing a list outside its boundaries is an error
print (letters[12])









