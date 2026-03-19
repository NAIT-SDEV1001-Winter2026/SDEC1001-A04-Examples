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
#Add the items from the list to what is already on the file

#Read from a file
#Use the mode "r"
#Read all the lines from a file into a list
try:
    with open(file_path,"r") as f:
        new_list = f.readlines()#reads all the lines from the file into a list
except FileNotFoundError:
    print("File not found")

print (new_list)

#Loop through and display the movies
for movie in new_list:
    print(movie.strip())#removes the \n from the row

# Functions for basic IO
#read from a file and return the list
def read_file(file_path):
    try:
        with open(file_path,"r") as f:
            new_list = f.readlines()#reads all the lines from the file into a list
    except FileNotFoundError:
        print("File not found")
    return new_list

#function to append text to a file
def add_to_file(file_path,text):
    with open(file_path,"a") as f:
        f.write(f"{text}\n")

#function to overwrite text on a file
def add_to_file(file_path,text):
    with open(file_path,"w") as f:
        f.write(f"{text}\n")
    

from_file = read_file(file_path)

print(from_file)
