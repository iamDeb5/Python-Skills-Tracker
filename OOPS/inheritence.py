class Vehicale:     #parent class           # inheritence mean parent to child class 
    def __init__(self,brand,model):     # constructor   # in constructor we initialize the attributes 
        self.brand = brand              # attribute
        self.model = model              # attribute

    def move(self):                    # method    
        print("The vehicale is moving")

class Car(Vehicale):                # child class inherit from Vehicale
    def honk(self):                 # method
        print("The car is honking")

class Bike(Vehicale):                # child class inherit from Vehicale
    def wheelie(self):                # method
        print("The bike is doing a wheelie")

class Plane(Vehicale):                # child class inherit from Vehicale
    def fly(self):                    # method
        print("The plane is flying")

car = Car("Toyota", "Corolla")          # object
bike = Bike("Honda", "CBR")             # object
plane = Plane("Boeing", "747")            # object

car.move()                              # calling method from parent class
car.honk()                              # calling method from child class

bike.move()                             # calling method from parent class
bike.wheelie()                          # calling method from child class

plane.move()                            # calling method from parent class
plane.fly()                             # calling method from child class
