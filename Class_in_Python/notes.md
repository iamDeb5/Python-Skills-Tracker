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

# In inheritence.py

## **Inheritance**:

It allows a child class (sub class) to inherit attributes and methods from a parent class (super class), promoting code reusability.

- **Parent Class / Super Class**: The class whose properties are inherited.
- **Child Class / Sub Class**: The class that inherits the properties.
- **Syntax**: `class ChildClass(ParentClass):`

## **Key Concepts Demonstrated**:

1. **Method Overriding**:
    - The child class `FactoryHowrah` defines its own `hello()` method.
    - When calling `fh.hello()`, it overrides the parent class's `hello()` method, printing `"Hello from class FactoryHowrah"` instead of `"Hello from class Factory"`.

2. **Constructor and Method Inheritance**:
    - `FactoryHowrah` does not define its own `__init__` constructor, so it inherits the constructor from `Factory` (it accepts the `brand` parameter).
    - `FactoryHowrah` inherits the `show_brand()` method from `Factory`. Hence, `fh.show_brand()` successfully prints the brand.

3. **Class Attribute Inheritance**:
    - The class attribute `a` (`"I am an attribute of class Factory"`) defined in `Factory` is inherited by `FactoryHowrah` and can be accessed via `fh.a`.

## **Code Walkthrough**:

```python
class Factory: # Parent Class / Super Class
    a = "I am an attribute of class Factory"

    def __init__(self, brand): # Constructor inherited by child
        self.brand = brand

    def show_brand(self): # Method inherited by child
        print(f"The brand is {self.brand}")

    def hello(self):
        print("Hello from class Factory")


class FactoryHowrah(Factory): # Child Class / Sub Class
    def hello(self): # Overridden method
        print("Hello from class FactoryHowrah")
```

## **Output**:

```text
Hello from class Factory
Hello from class FactoryHowrah
The brand is CampusBags
The brand is SreeLeather
I am an attribute of class Factory
I am an attribute of class Factory
```
