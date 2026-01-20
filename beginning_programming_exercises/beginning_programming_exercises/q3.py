# 3.	Ask the user for the width and height of a rectangle. There could be decimals. Calculate and display the width, height, area, and perimeter. Calculations print the results rounded to 3 decimal places.

#ask for height
height = float(input ("Height: "))
#ask for width
width = float(input ("Width: "))
#Calculate the Area
area = width * height
#Calculate the Perimiter
perimeter = 2 * (width + height)
#Display Area to 3 decimals
print (f"Area: {area:.3f}")
#Display Perimiter to 3 decimals
print (f"Permiter: {perimeter}")
