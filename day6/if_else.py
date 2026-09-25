# if else : conditional statement
# syntax
# if condition:
#     statements
# elif condition:
#    statements
# elif condition:
#     statements
# else:
#     statements

# statements of if block is executed when the condition in if is true
#  statements of elif block is executed when the condition in elif is true 
#  statements of elif block is executed when the conditions defined above are all false
# else do not take conditions
# if and elif take conditions
# multiple of elif blocks can be defined
# else block is defined at the buttom/end 

# requirements:
a = 1
b = 1
# if a is greater than b print A is greater than B
# if a is less than b print B is greater than B

# condition = a is greater than b
# action = print A is greater than b

if a > b:
    print("A is greater than B")
elif a < b:
    print("B is greater than A.")   
else:
    print("A and B are equal.")  




# Nested if else statement: if else statement inside another if else statement
if a > 0:
    if b > 0:
        print("Both a and b are positive.")
    else:
        print("a is positive, but b is not.")
else:
    print("a is not positive.")


    # simple calculator
    # using input get two numbers from user
    # using input get a operators(+,-,*,/) from users
    # if operator is +,print the sum of two numbers  
    # if operator is -,print the subtract of two numbers  
    # if operator is *,print the multiple of two numbers  
    # if operator is /,print the divide of two numbers  