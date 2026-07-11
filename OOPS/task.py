class Student:
    def __init__(self,name,age,course):
        self.name = name
        self.age = age
        self.course = course

    def introduce(self):
        print("My name is",self.name)
        print("My age is",self.age)
        print("My course is",self.course)

    def update_course(self, new_course):
        self.course = new_course
        print("My course has been updated to",self.course)


student1 = Student("Proloy",22,"MCA")
student2 = Student("Pranjali",21,"BCA")
student3 = Student("Sougata",23,"BBA")

student1.introduce()
student2.introduce()
student3.introduce()

student3.update_course("MCA")



        
        
   