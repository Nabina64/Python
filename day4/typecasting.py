# Typecasting: process of converting a datatype into another datatype.

a = 50
print(a + 3)
# convert into string ->str()
str_a = str(a)
print(type(str_a))
# print(str_a + 3)  #yo false hunxa kinavane duiota farak datatype harulai concat garna mildaina.

# convert into integers ->int()
b = "100"  #numeric value bahek aru vayo vane convert garna mildaina jastai b = "abc"
print(type(b))
int_b = int(b)
print(type(int_b))


# convert into float -> float()

float_b = float(b)
print(type(float_b))
print(float_b)

# convert into list -> list() 
a = "Mindrisers"
my_list = list(a)
print(my_list)


# convert into tuple -> tuple() 
my_tuple = tuple(my_list)
print(my_tuple)


# convert into set -> set() 
my_set = set(my_tuple)
print(my_set)   #asle duplicate data harulai hatayara print garxa: {'i', 'e', 'r', 'n', 's', 'd', 'M'}


# convert into dictionary -> dict() 
z = [('name','ram'),('age',35),('contact','12345')] #list of tuple //   asto khalko dataharulai matra dictionary ma convert garna milxa.
my_dict = dict(z)
print(my_dict)