# OOPS is an programming paradigm based on the concept of "objects".
# OOPs has four pillars: 
# 1. Abstraction
# 2. Encapsulation
# 3. Inheritance
# 4. Polymorphism

# class -->  Blueprint of an object
# Object --> Instance of a class

class Car:                                      # class
    def __init__(self, make, model, year):      # constructor
        self.make = make                        # attribute
        self.model = model                      # attribute
        self.year = year                        # attribute

    def display_info(self): # method
        print(f"{self.make} {self.model} {self.year}") 

    def start_engine(self):     # method
        print("Engine started")

    def stop_engine(self):      # method
        print("Engine stopped")

# Car --> 

my_car = Car("Toyota", "Camry", 2022)          # object creation
my_car.display_info()                          # method calling
my_car.start_engine()                          # method calling
my_car.stop_engine()                           # method calling