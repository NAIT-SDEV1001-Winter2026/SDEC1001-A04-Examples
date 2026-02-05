#For loops allow us look at and use each value in a list

bands = ["ABBA", "Journey", "Styx", "The Beatles"]

#loop through the list

for band in bands:
    print(f"{band} is a great band!")

#Enumerate functions returns both the value AND the index

for index, band in enumerate(bands, start = 1):
    print(f"band number {index} is {band}")

#Create a list of 4 menu options ("add", "update", "delete",'quit)
#display all 4 menu optins as follows:
# 1. add
# 2. update
# 3. delete
# 4. quit

options = ("Add customer", "Edit customer", "Delete customer", "Exit")
for option_number,value in enumerate(options, start = 1):
    print (f"{option_number}. {value}")


names  = ["Han Solo", "Luke", "Darth Vader", "Yoda","Leia", "Boba Fett","Chewbacca"]
bad_names = ("Darth Vader", "Boba Fett")

#Only print the names that are not bad names
for name in names:
    if name not in bad_names:
        print(f"{name} is a good name!")

#Using continue
for name in names:
    if name in bad_names:
       continue#skips to the next name in the list. 
    print(f"{name} is a good name!") 

#Break 
#Exists a loop
#find the first even number in a list
numbers = [1,9,11,4,8,10]

for number in numbers:
    if number % 2 == 0:
        print(f"The first even number found is {number}")
        break
print("Have a groovy day!")

#print the numbers in the list until the sum of the numbers goes over 25
numbers = [5,8,12,20,7,12,14,55,22,54,543,123,543,154,23]
sum = 0
for number in numbers:
    sum += number
    if sum > 25:
        break        
    print (number)
        
        