class Vehicle:              # parent class
    def __init__(self,brand):   # constructor
        self.brand = brand      # attribute

    def showBrand(self):        # method
        print("Brand: ",self.brand)

class Car(Vehicle):       # child class
    def __init__(self,brand,model):
        super().__init__(brand)   # calling parent class constructor
        self.model = model        # attribute

    def showModel(self):      # method
        print("Model: ",self.model)

car = Car("Toyota","Corolla")   # object
car.showBrand()                 # calling method from parent class
car.showModel()                 # calling method from child class