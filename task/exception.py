# Review system, four seasons in the year, weight conversion program, simple calulator implement exception handling

# 1. Review system, the stars typically represent the different levels of satisfaction.
# Start by creating a rating variable and set it equal to a decimal number.
# Make a rating system using an if/elif/else statement:
# rating greater than 4.5, print 'Extraordinary'
# rating greater than 4, print 'Excellent'
# rating greater than 3, print 'Good'
# rating greater than 2, print 'Fair'
# Everything else, print 'Poor'

# try:
#   rating = float(input("Enter Your rating:"))
#   if (rating > 4.5):
#     print("Extraordinary. rating:",rating)
#   elif (rating > 4):
#     print("Excellent. rating:",rating)
#   elif (rating > 3):
#     print("Good. rating:",rating)
#   elif (rating > 2):
#     print("Fair. rating:",rating)
#   else:
#     print("poor")
# except ValueError:
#     print("you can enter only integer.")
# except Exception as e:
#     print("Something went wrong:", e)


# 2. Use the random module to create a number from 0 to 5.
# Then use an if/elif/else statement to print out one of these six random facts:
# 0 - 'Flamingos turn pink from eating shrimp.'
# 1 - 'The only food that doesn\'t spoil is honey.'
# 2 - 'Shrimp can only swim backwards.'
# 3 - 'A taste bud\'s life span is about 10 days.'
# 4 - 'It is impossible to sneeze while sleeping.'
# 5 - 'It is illegal to sing off-key in North Carolina.'

# import random

# try:
#     number = random.randint(0, 5)

#     if number == 0:
#         print("Flamingos turn pink from eating shrimp.")

#     elif number == 1:
#         print("The only food that doesn't spoil is honey.")

#     elif number == 2:
#         print("Shrimp can only swim backwards.")

#     elif number == 3:
#         print("A taste bud's life span is about 10 days.")

#     elif number == 4:
#         print("It is impossible to sneeze while sleeping.")

#     elif number == 5:
#         print("It is illegal to sing off-key in North Carolina.")

#     else:
#         raise ValueError("No fact found!")

# except ValueError:
#     print("Invalid number generated.")

# except Exception as e:
#     print("Something went wrong:", e)




# 4. Create a weight conversion program that:
# Asks the user what their Earth weight is (as a float).
# Asks the user for a planet number (as an int).
# Then, use an if/elif/else statement to calculate the user's weight on the destination planet.
# To calculate the user's weight:
# destination weight=Earth weight × relative gravity
# Number	Planet	Relative Gravity
# 1	Mercury	0.38
# 2	Venus	0.91
# 3	Mars	0.38
# 4	Jupiter	2.53
# 5	Saturn	1.07
# 6	Uranus	0.89
# 7	Neptune	1.14
# If the user enters a planet number outside of 1 - 7, print a message that says 'Invalid planet number'.




try:
    earth_weight = float(input("Enter weight:")) 
    weight = 0 
    print(" 1.mercury\n 2.veus \n 3.mars \n 4.jupiter \n 5.saturn \n 6.uranus \n 7.neptune") 
    number = int(input("choose a number:")) 

    if(number == 1): 
        weight = earth_weight * 0.38 
        print("weight in Mercury = ",weight) 
    elif (number == 2): 
        weight = earth_weight * 0.91 
        print("weight in Venus = ",weight) 
    elif (number == 3): 
        weight = earth_weight * 0.38 
        print("Weight in Mars = ",weight) 
    elif (number == 4): 
        weight = earth_weight * 2.53 
        print("Weight in Jupiter = ", weight) 
    elif (number == 5): 
        weight = earth_weight * 1.07 
        print("Weight of Saturn = ", weight) 
    elif (number == 6): 
        weight = earth_weight * 0.89 
        print("Weight of Uranus = ", weight) 
    elif (number == 7): 
        weight = earth_weight * 1.14 
        print("weight of Neptune = ",weight) 
    else: 
        print("Not a planet")

except ValueError as e:
    print("Invalid input:" , e)



# simple calculator implement exception handling

# try:
#     a = int(input("enter first number:"))
#     b = int(input("enter second number:"))

#     operator = input("choose operator(+,-,*,/)")

#     if operator == "+":
#         print(a+b)
#     elif operator == "-":
#         print(a-b)
#     elif operator == "*":
#         print(a*b)
#     elif operator == "/":
#         print(a/b)
#     else:
#         print("Invalid operator.")

# except ValueError:
#     print("Invalid input:")

# except ZeroDivisionError:
#     print("Cannot divide by zero:")