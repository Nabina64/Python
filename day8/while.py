# break: loop end
# despite the the while condition being True, break end the loop
# if a is 2 then end the loop
# a = 0
# b = 5

# while a < b:  
#     print("Hello World")
#     if a == 2:
#         break
#     a += 1

# print("Line 30")



# complete loop: execution of all statements in while block
# incomplete loop: execution of statements half way

# continue: skip the current loop and starts new loop
a = 0
b = 5

while a < b:  
    a += 1
    if a == 2:
        continue
    print("Hello World", a)
print("Line 30")


# Nested while
a = 0
B = 5
c = 0
while a < b:  #parent while block 
    print("Parent block")
    if a == 2:
        break
    a += 1
    while c < b:
     print("Child block")   #child while block
     if a == 2:
        break
     c += 1

print("Line 30")

