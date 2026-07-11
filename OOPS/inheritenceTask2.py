class Animal:         # parent class
    def __init__(self,name):            # constructor
        self.name = name                # attribute
    def introduce(self):                # method
        print(f"Hello my name is {self.name}")

class Dog(Animal):    # child class inherit from Animal
    def bark(self):                     # method
        print("The dog is barking")

class Cat(Animal):    # child class
    def meow(self):
        print("The cat is meowing")

class Bird(Animal):
    def chirp(self):
        print("The bird is chirping")


obj = Dog("Buddy")                    # object
obj.introduce()                       # calling method from parent class
obj.bark()                            # calling method from child class

obj2 = Cat("Whiskers")                # object
obj2.introduce()                      # calling method from parent class
obj2.meow()                           # calling method from child class

obj3 = Bird("Tweety")                 # object
obj3.introduce()                      # calling method from parent class
obj3.chirp()                          # calling method from child class

    
        