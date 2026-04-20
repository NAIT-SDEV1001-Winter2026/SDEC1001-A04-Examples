class Vehicle:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    
    def move(self):
        print("moving from here to there")
    
    def __str__(self):
        return f"This is a {self.make}, {self.model}"
    
    

my_car = Vehicle("Ford","F150")

print(my_car)
my_car.move()

#Inherit from Vehicle for the Airplane class
class Airplane(Vehicle):
    #Override the constructor from the parent
    #long way (do not use)
    # def __init__(self,make,model,props):
    #     self.make = make
    #     self.model = model
    #     self.props = props    

    #DO IT THIS WAY
    def __init__(self,make,model,props,flaps):
        super().__init__(make,model)

        self.props = props
        self.flaps = flaps

    #you may want to override the __str__ for this class now
    def __str__(self):
        return f"This is a {self.make}, {self.model} with {self.props} props"     

    def move(self):
        print("Flies from here to there")

my_plane = Airplane("Cesna","A123",2,True)
print(my_plane)
my_plane.move()


class Motorcycle(Vehicle):
    def __init__(self,make, model, windsheild, sidecar):
        super().__init__(make, model)
        self.windsheild =  windsheild
        self.sidecare = sidecar

    def move(self):
        print("Roars from here to there")

my_motorcyle = Motorcycle("Harley", "Hog", True, False)
print (my_motorcyle)
my_motorcyle.move()
print("\n\n")
#Polymorphism
#Same method name on different classes with different behaviour
print ("Polymorphism")
my_car.move()
my_plane.move()
my_motorcyle.move()

for vehicle in (my_car, my_plane, my_motorcyle):
    print(vehicle)
    vehicle.move()





    

               


    