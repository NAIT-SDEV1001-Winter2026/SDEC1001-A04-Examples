from pathlib import Path
from csv import DictReader,DictWriter

base_dir = Path(__file__).parent
file_path = base_dir/"movies.csv"

#Read a csv file 
with open(file_path,"r") as f:
    reader = DictReader(f)
    for row in reader:
        print(row)
        #print just the movie name of each movie
        print(row["Movie"])
#Print the name of the movies that have a budget over 20 000 000
print("Budgets over 20 000 000")
with open(file_path,"r") as f:
    reader = DictReader(f)
    for row in reader:
        if float(row["Budget"]) > 20000000:      
            print(row["Movie"])

#Read the csv file into a list of dictionaries
#movies = []
with open(file_path,"r") as f:
    reader = DictReader(f)
    movies = list(reader)
    # for row in reader:
    #     movies.append(row)
print(movies)
#Same as above but only add to the list the movies that have budgets over 20 000 000
# movies = []
# with open(file_path,"r") as f:
#     reader = DictReader(f)
#     for row in reader:
#         if float(row["Budget"]) > 20000000:  
#             movies.append(row)
# print(movies)

#Comment out the above example
#Loop through the list of dictionaries 
#print out each movie name: Budget
#at the end print the average budget
#format each budget/average to 2 decimal places
print("Movie Names, budgets and average budget")
sum = 0
for movie in movies:
    sum += float(movie["Budget"])
    print (f"{movie["Movie"]}: {float(movie["Budget"]):.2f}")
average = 4#sum/len(movies)
print(f"Average: {average:.2f}")


#Write to a csv file
movies = [
    {"Movie": "Star Wars","Rating":"5","Budget":"100"},
    {"Movie": "Star trek","Rating":"4","Budget":"200"}    
    ]
#We need to import writer
from csv import writer

#write a list of dictionaries to a file
with open(file_path,"w",newline="") as f:
    field_names = ["Movie","Rating","Budget"]
    writer = DictWriter(f,fieldnames = field_names)
    writer.writeheader()#write the header row to the file
    for movie in movies:
        writer.writerow(movie)