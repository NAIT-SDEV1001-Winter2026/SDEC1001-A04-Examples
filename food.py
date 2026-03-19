#Exercise:
#Using a new file called food.py write to a file called food_items.txt
#In a loop, ask for a food item and add to a list. Keep looping until the user enters "avacado"
#Add the items from the list to what is already on the file

from pathlib import Path

base_dir = Path(__file__).parent
file_path = base_dir/"food_items.txt"

food_items = []

while True:
    user_input = input("Enter a food item: ")
    if user_input.lower() =="avacodo":
        break
    food_items.append(user_input)

with open(file_path,"a") as f:
    for food in food_items:
        f.write(f"{food}\n") 