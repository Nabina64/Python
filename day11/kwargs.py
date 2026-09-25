# kwargs: keyword arguments
#  ** is used to define kwargs
#  ** is folowed by the name of the argument
#  accepts multiple keyword arguments
# 
# gets the data in tuple

def intro(**kwargs):
    print(kwargs)
    print(kwargs.items())
    print(kwargs.keys())
    print(kwargs.values())
    for i,j in kwargs.items():
        # print("key:",i)
        # print("value:",j)
        print(f"{i} : {j}")

a = "Nabina"
b = 18
intro(name=a, age=b,address="Kathmandu") 
intro(name=a, age=b,address="Kathmandu",contact=9800000000)
intro(name=a, age=b,address="Kathmandu",contact=9800000000,email="nabina@example.com")


