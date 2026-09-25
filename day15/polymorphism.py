# polymorphism: poly: multiple, morph: form
# same method, different behaviour depending on the object


# class int:
#     def __add__(self, other):
#         pass

# class str:
#     def __add__(self, other): 
#         pass

# a = 5
# b = 10

# x = "Hello"
# y = "World"

# print(a + b)  # addition of integers
# print(x + y)  # concatenation of strings

# print(a.__add__(b))  # addition of integers
# print(x.__add__(y))  # concatenation of strings


class Dog:
    def move(self):
        print("Dog move with legs.")

class Bird:
    def move(self):
        print("Bird move with wings.")

class Fish:
    def move(self):
        print("Fish move with fins.")

d = Dog()
b = Bird()
f = Fish()

d.move()
b.move()    
f.move()