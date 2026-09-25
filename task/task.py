# 1. Review system, the stars typically represent the different levels of satisfaction.
# Start by creating a rating variable and set it equal to a decimal number.
# Make a rating system using an if/elif/else statement:
# rating greater than 4.5, print 'Extraordinary'
# rating greater than 4, print 'Excellent'
# rating greater than 3, print 'Good'
# rating greater than 2, print 'Fair'
# Everything else, print 'Poor'

# rating = float(input("Enter Your rating:"))
# if (rating > 4.5):
#   print("Extraordinary. rating:",rating)
# elif (rating > 4):
#   print("Excellent. rating:",rating)
# elif (rating > 3):
#   print("Good. rating:",rating)
# elif (rating > 2):
#   print("Fair. rating:",rating)
# else:
#   print("poor")




# 2. Use the random module to create a number from 0 to 5.
# Then use an if/elif/else statement to print out one of these six random facts:
# 0 - 'Flamingos turn pink from eating shrimp.'
# 1 - 'The only food that doesn\'t spoil is honey.'
# 2 - 'Shrimp can only swim backwards.'
# 3 - 'A taste bud\'s life span is about 10 days.'
# 4 - 'It is impossible to sneeze while sleeping.'
# 5 - 'It is illegal to sing off-key in North Carolina.'

# import random
# number = random.randint(0,5)
# if (number == 0):
#   print("Flamingos turn pink from eating shrimp.")
# elif (number == 1):
#   print("The only food that doesn\'t spoil is honey.")
# elif (number == 2):
#   print("Shrimp can only swim backwards.")
# elif (number == 3):
#   print("A taste bud\'s life span is about 10 days.")
# elif (number == 4):
#   print("It is impossible to sneeze while sleeping.")
# elif (number == 5):
#   print("It is illegal to sing off-key in North Carolina.")
# else:
#   print("not any fact")

# 3. Instructions
# four seasons in the year — winter, spring, summer, or fall
# Ask the user the month number using the input() function.
# Check for the four seasons using an if/elif/else statement and logical operators:
# month is 1, 2, 3, print 'Winter'
# month is 4, 5, 6, print 'Spring'
# month is 7, 8, 9, print 'Summer'
# month is 10, 11, 12, print 'Autumn'
# Everything else is 'Invalid'

# month = int(input("Enter month:"))
# if (month == 1 or month == 2 or month == 3):
#   print("Winter")
# elif (month == 4 or month == 5 or month == 6):
#   print("Spring")
# elif (month == 7 or month == 8 or month == 9):
#   print("Autumn")
# else:
#   print("Everything else is invalid")


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

# earth_weight = float(input("Enter weight:"))
# weight = 0
# print(" 1.mercury\n 2.veus \n 3.mars \n 4.jupiter \n 5.saturn \n 6.uranus \n 7.neptune")
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
#   print("Not a planet")

  
  





# 6. a countdown from 10 to 1.
# Use a for loop that counts down by using the "step" value in range().
# Inside the loop, print the numbers from 10 to 1, each on its own line.
# When the loop finishes the countdown, print this exact string.

# number = range(10,0,-1)
# for i in number:
#   print(i)
# print("end of loop")


# 7. Suppose we have a pair of dice.
# First, use the random module to “roll” the two dice.
# Each die (named die1 and die2) should have an integer value from 1 to 6.
# Store the sum of the two random values in variable named total.
# Using a while loop, check if total is 2. If it isn't, print the string 'Nope' and keep "rerolling" the dice.
# Let the loop run until the total is 2, then print 'Snake eyes!

# import random

# die1 = random.randint(1, 6)
# die2 = random.randint(1, 6)
# total = die1 + die2

# while total != 2:
#     print("Nope")
#     die1 = random.randint(1, 6)
#     die2 = random.randint(1, 6)
#     total = die1 + die2

# print("Snake eyes!")


# For loop
# 8. Find the sum of numbers from 1 to 100 
# total = 0
# num = range(1,101)
# for i in num:
#   total += i
# print(total)


# 9. Find the sum of even numbers from 1 to 50
# sum = 0
# num = range(1,51)
# for i in num:
#   if i % 2 == 0:
#     sum = sum + i
# print(sum)
  

# 10. Find the sum of odd numbers from 1 to 50

# sum = 0
# num = range(1,50)
# for i in num:
#   if i % 2 != 0:
#     sum = sum + i
# print(sum)

# 11.  create a list of numbers. Find sum of all numbers in the list
# sum = 0
# list = [1,2,3,4,5]
# for i in list:
#   sum = sum + i
# print(sum)


# 12. define a word and print out each character
# char = "Nabina Magar"
# for letter in char:
#   print(letter)



# 13.  create a list of numbers. find the largest number
# list = [1,2,5,6,9,7,0]
# largest = list[0]
# for i in list:
#   if largest < i:
#     largest = i
# print(largest)


# 14. create a list of numbers and count how many even numbers exist
# list = [1,2,3,4,5,6,7,8,9]
# even = 0
# for nbr in list:
#   if nbr % 2 == 0:
#     even += 1
# print(even)

