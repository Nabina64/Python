# for loop

# iterable: sequential data (group data,string)
a = [1,2,3,"hello",5]
# iteration: process of moving from 1st index to last index of iterable

# iterator: variable used to perform iteration in iterable
# for loop depends on the existing data in iterable

# syntax
# for iterator in iterable:
#   statement1
#   statement2


b = "loop"
for i in a:            #i is iterator and a is iterable
    print("hello world",i)
    for j in b:
        print(j)