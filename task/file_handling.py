# todo:

# ask user register or login
# if register: get username and save it in a file
# if login: get a username from user
# check if the entered username exist in the list of usernames
# if yes: print user exist
# if no: print user doesnot exist





# choice = input("Do you want to register or login? ")

# if choice == "register":
#     username = input("Enter username: ")

    
#     file = open("users.txt", "a")
#     file.write(username + "\n")
#     file.close()

#     print("Registration successful.")


# elif choice == "login":
#     username = input("Enter username: ")


#     file = open("users.txt", "r")
#     usernames = file.read().splitlines()
#     file.close()

#     if username in usernames:
#         print("User exists.")
#     else:
#         print("User does not exist.")

# else:
#     print("Invalid choice.")






# Accounting 
# ask user register or login
# if register: get username and password and save it in a file
# if login:  get username and password from user
# check if the entered username and password exists in the file 
# if no: print a statement
# if yes: print Login success
#     and show 3 option: 1. Show detail 2. Add balance 3. Withdraw
#     if choice is 1: print the userbalance of that user from the file
#     if choice is 2: get amount from user and store it to a file
#     if choice is 3: get amount from user , open the file, get the user ko balance from file, then if no user balance added yet print "Add amount first/ no Balance" if the amount is less than initial balance subtract the amount from initial balance and if amount is more than initial balance print a statement,




# choice = input("Do you want to register or login? ")

# if choice == "register":

#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     # save username and password in file
#     file = open("users.txt", "a")
#     file.write(username + "," + password + ",0\n")
#     file.close()

#     print("Registration successful.")

# elif choice == "login":

#     username = input("Enter username: ")
#     password = input("Enter password: ")

  
#     file = open("users.txt", "r")
#     users = file.readlines()
#     file.close()

#     login_success = False

#     for user in users:

#         data = user.strip().split(",")

#         saved_username = data[0]
#         saved_password = data[1]

#         if username == saved_username and password == saved_password:
#             login_success = True
#             balance = float(data[2])
#             break


#     if login_success:

#         print("Login success.")

#         print("\n1. Show detail")
#         print("2. Add balance")
#         print("3. Withdraw")

#         option = int(input("Choose an option: "))


#         if option == 1:

#             print("Username:", username)
#             print("Balance:", balance)

   
#         elif option == 2:

#             amount = float(input("Enter amount to add: "))

#             balance = balance + amount

#             # update file
#             file = open("users.txt", "a")

#             for user in users:

#                 data = user.strip().split(",")

#                 if data[0] == username:
#                     file.write(data[0] + "," + data[1] + "," + str(balance) + "\n")
#                 else:
#                     file.write(user)

#             file.close()

#             print("Balance added successfully.")
#             print("Current balance:", balance)

#         elif option == 3:

#             amount = float(input("Enter amount to withdraw: "))

#             if balance == 0:
#                 print("Add amount first / No Balance")

#             elif amount <= balance:

#                 balance = balance - amount

#                 # update file
#                 file = open("users.txt", "a")

#                 for user in users:

#                     data = user.strip().split(",")

#                     if data[0] == username:
#                         file.write(data[0] + "," + data[1] + "," + str(balance) + "\n")
#                     else:
#                         file.write(user)

#                 file.close()

#                 print("Withdrawal successful.")
#                 print("Remaining balance:", balance)

#             else:
#                 print("Insufficient balance.")

#         else:
#             print("Invalid option.")

#     else:
#         print("Invalid username or password.")


# else:
#     print("Invalid choice.")




# choice = input("enter you are login or register:")

# if choice == "register":
#     username = input("enter your username:")
#     password = input("enter your password:")
    
#     file = open("user.txt","a")
#     file.write(username+","+password)
#     file.close()

#     print("registration successful")

# elif choice == "login":
#     username = input("enter your username:")
#     password = input("enter your password:")

#     file = open("user.txt","r")
#     usernames = file.read().splitlines()
#     file.close()

#     if username +","+ password in usernames:
#         print("user exist")
#     else:
#         print("user does not exist")

# else:
#     print("invalid choice")



# choice = input("Do you want to register or login?")

# if choice == "register":
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     file = open("user.txt","a")
#     file.write(username + "," + password + ",0\n")
#     file.close()

#     print("Registration successful.")

# elif choice == "login":
#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     file = open("user.txt","r")
#     users = file.readlines()
#     file.close()

#     login_success = False

#     for user in users:
#         data = user.strip().split(",")

#         saved_username = data[0]
#         saved_password = data[1]

#         if username == saved_username and password == saved_password:
#             login_success = True
#             balance = float(data[2])
#             break


#     if login_success:
#         print("Login success.")
#         while True:
#          print("\n1. Show detail")
#          print("2. Add balance")
#          print("3. Withdraw")
#          print("4. Exit")

#          option = int(input("choose an option: "))

#          if option == 1:
#             print("Username:", username)
#             print("Balance:", balance)

#          elif option == 2:
#             amount = float(input("Enter amount to add: "))

#             balance = balance + amount

#             file = open("user.txt","w")

#             for user in users:
#                 data = user.strip().split(",")
#                 if data[0] == username:
#                     file.write(data[0] + "," + data[1] + "," + str(balance) + "\n")

#                 else:
#                     file.write(user)

#             file.close()

#             print("Balance added successfully. ")
#             print("current balance: ", balance)

#          elif option == 3:
#             amount = float(input("Enter amount to withdraw: "))

#             if balance == 0:
#                 print("Add amount first / No balance")
#             elif amount <= balance:
#                 balance = balance - amount

#                 file = open("user.txt", "w")

#                 for user in users:
#                     data = user.strip().split(",")

#                     if data[0] == username:
#                         file.write(data[0] + "," + data[1] + "," + str(balance) + "\n")
#                     else:
#                         file.write(user)
#                 file.close()

#                 print("withdrawal successful. ")
#                 print("Remaining balanca:", balance)
#             else:
#                 print("Insufficient balance.")
#          elif option == 4:
#             print("Thank you.")
#             break

#     else:
#         print("Invalid choice.")           

