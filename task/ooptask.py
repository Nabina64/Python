# create a method that takes window,room,door from user as argument ,assign it to the attributes


class House:
    def set_details(self, window, room, door):
        self.window = window
        self.room = room
        self.door = door

house1 = House()

house1.set_details(6, 3, 4)  

print(house1.window)
print(house1.room)
print(house1.door)  
