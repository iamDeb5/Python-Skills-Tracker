# Note: #basic definition of class and object & syntax

## Class: blueprint of an object #Class can be compared to a cookie cutter

## Object: instance of a class #Object can be compared to cookies made from the cookie cutter

## **init** is a constructor that is used to initialize the object

## self is a reference to the current instance of the class

## **init** is automatically called when an object is created

# In main.py

## SreeLeather = Factory("Leather", 2, 4, "Brown", 100) #here SreeLeather is an object of the class Factory

## methods (functions) are called using dot operator

## attributes are accessed using dot operator

## SreeLeather.make_item() #calling make_item() method

## SreeLeather.update_price(150) #calling update_price() method

## SreeLeather.update_pocket(5) #calling update_pocket() method

## SreeLeather.sell() #calling sell() method which is also a function

## CampusBags = Factory("Canvas", 2, 4, "Brown", 100) #here CampusBags is an object of the class Factory

## methods (functions) are called using dot operator

## attributes are accessed using dot operator

## CampusBags.make_item() #calling make_item() method

## CampusBags.update_price(150) #calling update_price() method

## CampusBags.update_pocket(5) #calling update_pocket() method

## CampusBags.sell() #calling sell() method which is also a function

# Output:

The item is made of Leather
The item has 2 zips
The item has 4 pockets
The item is Brown
The item costs 100
The item now costs 150
The item now has 5 pockets
The item is sold

The item is made of Canvas
The item has 2 zips
The item has 4 pockets
The item is Brown
The item costs 100
The item now costs 200
The item now has 10 pockets
The item is sold

# Note2: #Class Attribute and Instance Attribute

## Class Attribute: defined outside the **init** method and shared by all instances

## Instance Attribute: defined inside the **init** method and unique to each instance

## Class method: used to refer the class itself @classmethod is used to define a class method

## Static method: it is not related to the class or instance @staticmethod is used to define a static method
