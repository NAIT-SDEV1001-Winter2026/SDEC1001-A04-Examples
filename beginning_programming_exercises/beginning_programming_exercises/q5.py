# 5.	Ask the user for a number of miles and print out how many kilometres it is. Display to 2 decimal places.
# The conversion rate is 1 mile = 1.609344 kilometers

#Ask for miles
miles = float(input("Enter the number of miles: "))
#Calculate km
km = miles * 1.609344
#display km
print (f"{miles} is {km:.2f} kilometers")