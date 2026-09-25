# OOP: Object oriented programming

# class: structure, blueprint
# object: a data created using a class is called an object,real world entity

# Syntax:
# class class_name:
#     attributes
#     methods
    
class House:      #class define
        window = 6
        room = 3
        door = 4

house1 = House()      #class call , house1 is an object of class House
print(house1.window)
print(house1.room)
print(house1.door)