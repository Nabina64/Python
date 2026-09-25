# global variable: it can be used anywhere in the program,
# local variable: DEFINED INSIDE THE FUNCTION AND FUNCTION and can only accessed inside the function, it is not accessible outside the function

z = 10 # global variable
def sum():
    global z
    a = 15
    print(z)
    print(a + z)
    z += 10
    print(z)

sum()
# print(z)
