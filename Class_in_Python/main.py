"""
Class is a blueprint for creating objects
Object is an instance of a class

"""
class Factory: #blueprint of an 
    #Class Attribute
    total_bags = 0
    total_price = 0

    
    def __init__(self, material, zips, pocket, color, price): #Instance attributes
        self.material = material #properties of the object
        self.zips = zips
        self.pocket = pocket
        self.color = color
        self.price = price

    def make_item(self): #methods(functions inside a class)
        print(f"The item is made of {self.material}") 
        print(f"The item has {self.zips} zips")
        print(f"The item has {self.pocket} pockets") #if any change happend to the attributes, it will reflect here
        print(f"The item is {self.color}")
        print(f"The item costs {self.price}")

    def update_price(self, new_price): #updation of attributes
        self.price = new_price 
        print(f"The item now costs {self.price}")

    def update_pocket(self, new_pocket): #updation of attributes
        self.pocket = new_pocket
        print(f"The item now has {self.pocket} pockets")

    def sell(self): #methods
        print("The item is sold")

    #cls - it is used to refer the class itself
    @classmethod
    def total_items(cls):
        return cls.total_bags

    @classmethod
    def total_price(cls):
        return cls.total_price

    #static method - it is not related to the class or instance
    @staticmethod
    def static_method():
        print("This is a static method")


#Creating an object 
SreeLeather = Factory("Leather", 2, 4, "Brown", 100) #here SreeLeather is an object
CampusBags = Factory("Canvas", 2, 4, "Brown", 100) #here CampusBags is an object



#Calling methods
SreeLeather.make_item() 
CampusBags.make_item()

SreeLeather.update_price(150)
CampusBags.update_price(200)

SreeLeather.update_pocket(5)
CampusBags.update_pocket(10)

SreeLeather.sell()
CampusBags.sell()
