#Object Oriented Programming (OOP)
#where we model real world things using classes
#A class is a blueprint. We create objects from the class

#Example
#Class - Car
#Object - a specific car 

#Class  - Car 
class Car:
    #Constructor Method (always called __init__)
    #A method is a function that is in a class
    #Constructor runs when we create an object (instantiate) from the class
    #self refers to the current object being created. It is always the FIRST parameter
      
    def  __init__ (self, make, model, year):
        self.make = make#the make of this object will be the value of the parameter make
        self.model = model
        self.year = year
    #When you print an object __str__ is called. The default behavior of __str__ is to return the memory location.
    #We want to OVERRIDE that behavior to return a different string
    def __str__ (self):
        return f"{self.make}, {self.model}, {self.year}"
    
    #__repr__ is used by developers for testing in certain environments (Jupyter Notebook, command line, etc...)
    #It does nothing if you just run the py file
    #in this course we need to know how to write it, but we won't be "using" it
    def __repr__ (self):
        return f"{self.make}, {self.model}, {self.year}"
    
    #Define HOW objects should be compared
    #When someone uses ==, this is how to compare the objects
    def __eq__(self, other):
        return self.make == other.make and self.model == other.model and self.year == other.year
                
#Mainline
if __name__ == "__main__":
    car1 = Car("Ford","F150",2020)
    print (car1.make)  
    print (car1.model)
    print (car1.year)
    #Change the year
    car1.year = 2022
    print (car1.year)

    car2 = Car("Mercedes-Benz", "Gt63", 2019)
    print (car2.make)

    #list of my cars
    cars = [car1,car2]

    #print all the cars in the list
    for car in cars:
        print(f"{car.make}, {car.model}, {car.year}")

    #What happens if we just print an object
    #Not much. Just gives us the memory location. Unless you have changed (override) the __str__ method to return something else.    
    print(car1)
    print(car2)
    print("Loop through cars using __str__")
    for car in cars:
        print(car)

    #Comparing objects
    test_car1 = Car("Volkswagon","Beatle",1964)
    test_car2 = Car("Volkswagon","Beatle",1964)
    #Does not work because it is comparing memory locations, not the attributes in the objects (unless you have overwritten the __eq__ method to redefine what gets compared)
    if test_car1 == test_car2:
        print("Same")
    else:
        print("Not the same")

    


    
    


