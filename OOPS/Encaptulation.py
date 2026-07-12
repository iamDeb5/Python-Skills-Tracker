#Encaptulation :- Encaptulation is the mechanism where the data and functions that operate on the data are bundled together 
#in a single unit or class.

#encaptulation is also known as data hiding
#encaptulation can be achieved using private and public attributes


#private attribute:- (__name, __age, __marks) The attribute that is not accessible from outside the class is called private attribute.
#public attribute:- (name, age, marks) The attribute that is accessible from outside the class is called public attribute.  
#protected attribute:- (_name, _age, _marks) The attribute that is accessible from outside the class but its use to 
#indicate future developer that this attribute is a created for private use.


#getter and setter methods:- The method that is used to get and set the value of a private attribute is called getter and setter method.







class Student:
    def __init__(self,name,age,marks):
        self.__name = name   # private attribute
        self.__age = age     # private attribute
        self.__marks = marks   # private attribute

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_marks(self):
        return self.__marks

    def set_name(self,name):
        self.__name = name

    def set_age(self,age):
        self.__age = age

    def set_marks(self,marks):
        self.__marks = marks

obj = Student("John", 20, 80)   # object

print(obj.get_name())   # calling method from parent class
print(obj.get_age())    # calling method from parent class
print(obj.get_marks())   # calling method from parent class

obj.set_name("Jane")    # calling method from child class
obj.set_age(21)     # calling method from child class
obj.set_marks(85)    # calling method from child class

print(obj.get_name())    # calling method from parent class
print(obj.get_age())     # calling method from parent class
print(obj.get_marks())    # calling method from parent class