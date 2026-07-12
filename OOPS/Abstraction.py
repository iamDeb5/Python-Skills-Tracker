#Abstraction:- Abstraction is the mechanism
#it is used to hide the implementation details and show only the essential features of an object
#it is achieved using abstract class and abstract method
#abstract class:- The class that contains one or more abstract methods is called abstract class.
#abstract method:- The method that is declared in an abstract class but not implemented is called abstract method.


from abc import ABC,abstractmethod

class Shape(ABC):  # parent class
    @abstractmethod
    def area(self):   # abstract method
        pass

class Circle(Shape):  # child class inherit from Shape
    def area(self,radius):   # method overriding   
        print(3.14*radius*radius)

class Square(Shape):  # child class inherit from Shape
    def area(self,side):   # method overriding   
        print(side*side)

obj = Circle(5)  # object
obj.area()  # calling method from parent class

obj2 = Square(5)  # object
obj2.area()  # calling method from child class  