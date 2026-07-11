class Person:   # parent class
    def walk(self):
        print("Person is walking")

    def sleep(self):
        print("Person is sleeping")

class Teacher(Person):  # child class
    def teach(self):
        print("Teacher is teaching")


class Student(Person):  # child class
    def study(self):
        print("Student is studying")


teacher = Teacher()     # object
teacher.walk()          # calling method from parent class
teacher.sleep()         # calling method from parent class
teacher.teach()         # calling method from child class

student = Student()     # object
student.walk()          # calling method from parent class
student.sleep()         # calling method from parent class
student.study()         # calling method from child class