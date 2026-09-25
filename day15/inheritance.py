# Inheritance: it follows the concept of superclass and subclass,base class and derived class,parent class and child class

# child class can use the properties and methods  that exists in parent class

# child class can have new attributes and methods that are not present in parent class

# method overriding: parent class and child class both have method with same name but feature/functionality are different


class Car:
    color : None
    brand : None
    model : None

    def get_details(self,color,brand,model):
        self.color = color
        self.brand = brand
        self.model = model

    def show_details(self):
        print(f"""Color: {self.color}
     Brand: {self.brand}
     Model: {self.model}""")
        

class EV(Car):
    speed : None

    def get_speed(self,speed):
        self.speed = speed

    def show_details(self):   #method overriding
        print(f"""Color: {self.color}
    Brand: {self.brand}
    Model: {self.model}
    Speed: {self.speed}""")

        # super().show_details()  #calling parent class method
        # print(f"Speed: {self.speed}")  

ev = EV()
ev.get_details("Red","Tesla","XYZ")
ev.get_speed("120 km/h")
ev.show_details()
    