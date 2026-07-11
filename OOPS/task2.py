class Laptop:
    def __init__(self,brand,ram):
        self.brand = brand
        self.ram = ram

    def show_specs(self):
        print("Brand: ",self.brand)
        print("RAM: ",self.ram)

laptop1 = Laptop("Dell",8)
laptop2 = Laptop("Apple",16)
laptop3 = Laptop("HP",4)

laptop1.show_specs()
laptop2.show_specs()
laptop3.show_specs()

        
    