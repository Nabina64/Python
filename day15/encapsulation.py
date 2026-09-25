# Encapsulation: wrapping attributes,methods in a single unit called class,while controlling direct access to data
#  keep the data protected and allow access through methods
# public,private,protected a
# public: accessible from anywhere
# private: accessible only within the class (using double underscore)
# protected: accessible within the class and its subclasses (using single underscore)
# private attributes and methods are defined using '__' followed by attributes and methods name

class Account:
    def login(self,email,password):
        self.__email = email
        self.__password = password

    def __show(self):
        print(self.__email)
        print(self.__password)

    def display(self):
        self.__show()

a = Account()
a.login("nabina@gmail.com","1234")
a.display()
# print(a.__email)