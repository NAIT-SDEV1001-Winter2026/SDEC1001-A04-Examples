#Stores data in key-value pairs (like **kwargs)
#keys are unique and usually strings; values can be any datatype
#The value can be another dictionary, list, tuple
#dictionaries use {}

#Student
student = {"name": "Bob", "age": 5, "email": "Bob2021@gmail.com"}
#Create a dictionary in car variable with make, model, year.
car = {"make": "Jeep", "model":"TJ", "year":1999}

#accessing values
print(student["name"])
student["age"] = 6

#create a new key-value pair
student["grade"] = 95

#accessing a key that does not exist is an error
#print(student["shoe_size"])

#check if key exists:
if "shoe_size" in student:
    print(f"your shoe size is: {student['shoe_size']}")
else:
    print("We don't know your shoe size")

#return a default value for a non existent key
print (student.get("names","N/A"))

#inventory dictionary
inventory = {
            "apple":{"price": .50, "stock": 40},
            "dragonfruit":{"price": .80, "stock": 20}
}
#Accessing nested values
print(f"{inventory["apple"]["price"]:.2f}")

#Looping
#Show all the keys and values
for key in student:#loop through the keys. Could use student.keys()
    print(f"{key}: {student[key]}")
#OR
grades = {"Bart": 40, "Homer":20, "Lisa": 95}
for name,grade in grades.items():#items() returns the key AND value
    print(f"{name}:{grade}")

#print all the names in the grades dictionary
print("Names")
for name in grades.keys():
    print(f"{name}")

#print all the grades
print("Grades")
for grade in grades.values():
    print(grade)

#Exercise 
inventory = {"apples": 0, "bananas":0, "oranges": 0}
deliveries = ["apples","bananas", "apples", "oranges", "apples"]
#update the inventory
for item in deliveries:
    inventory[item] += 1
#print out the inventory
for fruit, count in inventory.items():
    print(f"{fruit}: {count}")

#Output
#apples: 3
#bananas: 1
#oranges: 1
