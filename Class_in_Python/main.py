"""
Class is a blueprint for creating objects
Object is an instance of a class

"""
class Factory: #blueprint of an object
    def __init__(self, material, zips, pocket, color, price): #attributes
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

#Creating an object
SreeLeather = Factory("Leather", 2, 4, "Brown", 100) #here SreeLeather is an object

#Calling methods
SreeLeather.make_item()

SreeLeather.update_price(150)
SreeLeather.update_pocket(5)
SreeLeather.sell()
