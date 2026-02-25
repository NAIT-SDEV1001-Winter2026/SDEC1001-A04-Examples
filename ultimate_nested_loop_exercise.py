import random

numbers = []

while len(numbers) < 100:
    number = random.randint(1,1000)

    if number not in numbers:
        numbers.append(number)

print(f"Origional List: {numbers}")

#get length of list
length = len(numbers)
#compare last element in the range  to all previous elements
for end in range (length -1, 0, -1):#end is the position we are looking at in this pass
    for index in range(0,end):
        if numbers[index] > numbers[end]:
            #swap the numbers
            temp = numbers[index]
            numbers[index] = numbers[end]
            numbers[end] = temp

print (f"Sorterd: {numbers}")


