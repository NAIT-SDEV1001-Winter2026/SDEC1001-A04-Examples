#Repeat a block of code while a condition is True
#Useful when you don't know how many times to loop

#Counter controlled loop
#Count up to 5
counter = 1

while counter <=5: #keep looping until this condition is True
    print(f"Number: {counter}")
    counter +=1
    
#User controlled loop
#Ask for numbers to add. Enter 'done' to print the sum

sum = 0
while True: #An endless loop unless break
    value = input("Enter a number: done to quit: ")
    if value.lower() == "done":
        break
    sum += int(value)
print (f"Sum: {sum}")

#Without break
sum = 0
value = input("Enter a number: done to quit: ") 
while  value !="done" : #An endless loop unless break
    
    value = input("Enter a number: done to quit: ")
print (f"Sum: {sum}")

#Using a boolean variable
sum = 0
is_continue = True 
while is_continue:
    value = input("Enter a number: done to quit: ")
    if value.lower() == "done":
        is_continue = False
    else:
        sum += int(value)
print (f"Sum: {sum}")

#Another Boolean Example
keep_going = True
while keep_going == True:
    #Cool code goes here
    answer = input("Would you like to continue? (y/n): ")
    if answer.lower() =="n":
        keep_going = False
print("Loop Over")
