class Factory: # Parent Class / Super Class
    a = "I am an attribute of class Factory"

    def __init__(self, brand): # Instance attributes
        self.brand = brand

    def show_brand(self):
        print(f"The brand is {self.brand}")

    def hello(self):
        print("Hello from class Factory")


class FactoryHowrah(Factory): # Inheriting from Factory [Parent Class] to Child Class] / Sub Class
    def hello(self):
        print("Hello from class FactoryHowrah")
        

# Create objects of the classes 
f = Factory("CampusBags")
fh = FactoryHowrah("SreeLeather")       

# Access attributes and methods
f.hello() 
fh.hello() # [Note: It will not call the parent class method]
f.show_brand()
fh.show_brand() 
print(f.a) 
print(fh.a)




