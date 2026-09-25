# 1. Review system, thjupiter \n 5.saturn \n 6.uranus \n 7.neptune")
# number = int(input("choose a number:"))
# if(number == 1):
#   weight = earth_weight * 0.38
#   print("weight in Mercury = ",weight)
# elif (number == 2):
#   weight = earth_weight * 0.91
#   print("weight in Venus = ",weight)
# elif (number == 3):
#   weight = earth_weight * 0.38
#   print("Weight in Mars = ",weight)
# elif (number == 4):
#   weight = earth_weight * 2.53
#   print("Weight in Jupiter = ", weight)
# elif (number == 5):
#   weight = earth_weight * 1.07
#   print("Weight of Saturn = ", weight)
# elif (number == 6):
#   weight = earth_weight * 0.89
#   print("Weight of Uranus = ", weight)
# elif (number == 7):
#   weight = earth_weight * 1.14
#   print("weight of Neptune = ",weight)
# else:
#   print("Not a planet")e stars typically represent the different levels of satisfaction.
# Start by creating a rating variable and set it equal to a decimal number.
# Make a rating system using an if/elif/else statement:
# rating greater than 4.5, print 'Extraordinary'
# rating greater than 4, print 'Excellent'
# rating greater than 3, print 'Good'
# rating greater than 2, print 'Fair'
# Everything else, print 'Poor'


# def get_rating():
#     rating = float(input("Enter Your rating: "))
#     return rating


# def check_rating(rating):
#     if rating > 4.5:
#         return "Extraordinary"
#     elif rating > 4:
#         return "Excellent"
#     elif rating > 3:
#         return "Good"
#     elif rating > 2:
#         return "Fair"
#     else:
#         return "Poor"


# def display_result(rating, result):
#     print(result, "rating:", rating)


# rating = get_rating()
# result = check_rating(rating)
# display_result(rating, result)



# 3. Instructions
# four seasons in the year — winter, spring, summer, or fall
# Ask the user the month number using the input() function.
# Check for the four seasons using an if/elif/else statement and logical operators:
# month is 1, 2, 3, print 'Winter'
# month is 4, 5, 6, print 'Spring'
# month is 7, 8, 9, print 'Summer'
# month is 10, 11, 12, print 'Autumn'
# Everything else is 'Invalid'

# def get_month():
#     month = int(input("Enter month: "))
#     return month


# def check_season(month):
#     if month == 1 or month == 2 or month == 3:
#         return "Winter"
#     elif month == 4 or month == 5 or month == 6:
#         return "Spring"
#     elif month == 7 or month == 8 or month == 9:
#         return "Summer"
#     elif month == 10 or month == 11 or month == 12:
#         return "Autumn"
#     else:
#         return "Invalid"


# def display_result(season):
#     print(season)


# month = get_month()
# season = check_season(month)
# display_result(season)




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


# def get_earth_weight():
#     earth_weight = float(input("Enter weight: "))
#     return earth_weight

# def get_planet_number():
#     print(" 1.Mercury\n 2.Venus \n 3.Mars \n 4.Jupiter \n 5.Saturn \n 6.Uranus \n 7.Neptune")
#     number = int(input("Choose a number: "))
#     return number   

# def calculate_weight(earth_weight, number):
#     if number == 1:
#         weight = earth_weight * 0.38
#         return "Weight in Mercury = ", weight
#     elif number == 2:
#         weight = earth_weight * 0.91
#         return "Weight in Venus = ", weight
#     elif number == 3:
#         weight = earth_weight * 0.38
#         return "Weight in Mars = ", weight
#     elif number == 4:
#         weight = earth_weight * 2.53
#         return "Weight in Jupiter = ", weight
#     elif number == 5:
#         weight = earth_weight * 1.07
#         return "Weight in Saturn = ", weight
#     elif number == 6:
#         weight = earth_weight * 0.89
#         return "Weight in Uranus = ", weight
#     elif number == 7:
#         weight = earth_weight * 1.14
#         return "Weight in Neptune = ", weight
#     else:
#         return "Invalid planet number"

# earth_weight = get_earth_weight()
# planet_number = get_planet_number()
# result = calculate_weight(earth_weight, planet_number)
# print(result)




# simple calculator implement exception handling

def get_numbers():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    return a, b


def get_operator():
    operator = input("Choose operator (+, -, *, /): ")
    return operator


def calculate(a, b, operator):
    if operator == "+":
        return a + b
    elif operator == "-":
        return a - b
    elif operator == "*":
        return a * b
    elif operator == "/":
        return a / b
    else:
        return "Invalid operator."


def main():
    try:
        a, b = get_numbers()
        operator = get_operator()
        result = calculate(a, b, operator)
        print(result)

    except ValueError:
        print("Invalid input.")

    except ZeroDivisionError:
        print("Cannot divide by zero.")


main()