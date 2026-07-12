#Method Overriding

class Animal:                         # parent class
    def speak(self):                  # method
        print("Animal is speaking")

class Dog(Animal):                    # child class inherit from Animal
    def speak(self):                  # method overriding   
        print("Dog is barking")

obj = Animal()                        # object
obj.speak()                           # calling method from parent class

obj2 = Dog()                          # object
obj2.speak()                          # calling method from child class


# super() keyword in method overriding

class Car:                          # parent class  
    def __init__(self,brand,model):   # constructor
        self.brand = brand          # attribute
        self.model = model          # attribute

    def display_info(self):           # method
        print(f"{self.brand} {self.model}")      

class ElectricCar(Car):               # child class inherit from Car
    def __init__(self,brand,model,battery_size): 
        super().__init__(brand,model)     # calling parent class constructor
        self.battery_size = battery_size    # attribute

    def display_info(self):               # method overriding   
        print(f"{self.brand} {self.model} {self.battery_size}")    


car = Car("Toyota", "Camry")             # object
car.display_info()                       # calling method from parent class

electric_car = ElectricCar("Tesla", "Model S", 100)  # object
electric_car.display_info()              # calling method from child class


#polymorphism:- Polymorphism is the ability of an object to take on many forms.
# It allows you to write code that can work with objects of different classes.


class Shape:                # parent class
    def area(self):         # method
        print("Area of shape")

class Circle(Shape):        # child class inherit from Shape
    def area(self,radius):    # method overriding   
        print(3.14*radius*radius)

class Square(Shape):        # child class inherit from Shape
    def area(self,side):    # method overriding
        print(side*side)    

obj = Shape()             # object
obj.area()                # calling method from parent class

obj2 = Circle()           # object
obj2.area(5)              # calling method from child class

obj3 = Square()           # object
obj3.area(5)              # calling method from child class 


