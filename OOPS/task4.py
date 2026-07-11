class Car:
    company = "Toyota"

    
    @classmethod
    def change_company(cls,new_company):
        cls.company = new_company
        print("Company changed to",new_company)

    def show_company(self):
        print("Company: ",self.company)

car1 = Car()
car2 = Car()
car3 = Car()

car1.show_company()
car2.show_company()
car3.show_company()

Car.change_company("Honda")

car1.show_company()
car2.show_company()
car3.show_company()