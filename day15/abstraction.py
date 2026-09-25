# Abstraction: data hiding-> hiding unnecessary details/events from user 

class Bike:
    acc = False
    key = False
    clutch = False
    gear = False

    def start(self):
        self.key = True
        self.clutch = True
        self.gear = True
        self.acc = True
        print("Bike started")

b1 = Bike()
b1.start()
