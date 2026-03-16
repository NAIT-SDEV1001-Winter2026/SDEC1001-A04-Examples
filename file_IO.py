#write to a file in the same folder as the py file
#basic steps to writing to a file:
    #Open the file
    #Write to the file
    #Close the file

from pathlib import Path#Importing the Path class

#Set the path to your text file to be the same folder as the py file (this file)
base_dir = Path(__file__).parent #What is the path to the folder this file is in now
file_path = base_dir/"movies.txt"#path to the text file we will create/use

#with will open the file (at the defined file_path) for appending and close it when done
#appending adds to the current content of the file
#if the file does not exist, it will be created

with open(file_path,"a") as f:
    f.write("Jurassic Park\n")#write to the file
    f.write("Event Horizon\n")

#Change a to w. 
#w means overwrite everything on the file
with open(file_path,"w") as f:
    f.write("Lord of the rings\n")#write to the file
    f.write("Star Trek\n")
    f.write("Annie\n")

#Exercise:
#Using a new file called food.py write to a file called food_items.txt
#In a loop, ask for a food item and add to a list. Keep looping until the user enters "avacado"
#Add the items to what is already on the list

