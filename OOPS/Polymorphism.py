class Animal:
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def speak(self):
        print("Dog is barking")

class Cat(Animal):
    def speak(self):
        print("Cat is meowing")

class Cow(Animal):
    def speak(self):
        print("Cow is mooing")

obj = Animal()    # object
obj.speak()    # calling method from Animal class

obj2 = Dog()   # object
obj2.speak()   # calling method from Dog class

obj3 = Cat()   # object
obj3.speak()   # calling method from Cat class

obj4 = Cow()   # object
obj4.speak()   # calling method from Cow class  



 