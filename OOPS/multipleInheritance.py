class Camera:
    def take_photo(self):
        print("Camera is taking a photo")

class Phone:
    def call(self):
        print("Phone is calling")

class SmartPhone(Camera, Phone):  # multiple inheritance
    def use_apps(self):
        print("SmartPhone is using apps")


obj = SmartPhone()  # object
obj.take_photo()  # calling method from Camera class
obj.call()  # calling method from Phone class
obj.use_apps()  # calling method from SmartPhone class