# #sorting
# numbers = [42,7,19,100,3]
# numbers.sort()#sorts ascending
# print (numbers)

# numbers.sort(reverse = True)#sort descending
# print(numbers)

# #add a single valuec#
courses = ["Python","SQL","C#", "Postgres"]
# courses.append("Baking")
# print(courses)
 
# #Insert a single value at a location
# courses.insert(2,"Cooking")
# print(courses)

# #Append a collection to a list
# courses.extend(["Metal work","Wood work"])
# print (courses)

# additional_courses = ["Teaching","Massage"]
# courses.extend(additional_courses)
# print (courses)

# #insert a collection (list) at a location
# #this inserts an entire list at one index (element)
# courses.insert(3,["Surveying","Drawing"])
# print (courses)

# #we must use slice assignment to insert the values
# courses [3:3] = ["Surveying","Drawing"]
# print (courses)

# #Removing values
# #pop removes by index and returns the value of that element
# #we do not need use the value returned

# courses.pop(4)
# print (courses)

# removed = courses.pop(3)
# print(courses)
# print(f"{removed} has been removed from the list")

# #remove by value
# courses.remove("C#")
# print(courses)

#is a value in the list?
check_course = input("Enter a course to search for: ")
result = check_course in courses
print (f"Is {check_course} in the list? {result}")

#index of a value
print(f"The index of C# is : {courses.index("C#")}")

#count the occurences of a value
courses.append("C#")
print(courses)

search_value = input("Enter a course name: ")
print (f"{search_value} is in the list {courses.count(search_value)} times")

#Clear the list
courses.clear()