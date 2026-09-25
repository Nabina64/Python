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


def register():
    username = input("Enter username: ")
    password = input("Enter password: ")

    file = open("user.txt", "a")
    file.write(username + "," + password + ",0\n")
    file.close()

    print("Registration successful.")


def login():
    username = input("Enter username: ")
    password = input("Enter password: ")

    file = open("user.txt", "r")
    users = file.readlines()
    file.close()

    for user in users:
        data = user.strip().split(",")

        saved_username = data[0]
        saved_password = data[1]

        if username == saved_username and password == saved_password:
            balance = float(data[2])

            print("Login success.")

            menu(username, balance, users)
            return

    print("Invalid username or password.")


def show_detail(username, balance):
    print("Username:", username)
    print("Balance:", balance)


def add_balance(username, balance, users):
    amount = float(input("Enter amount to add: "))

    balance = balance + amount

    file = open("user.txt", "w")

    for user in users:
        data = user.strip().split(",")

        if data[0] == username:
            file.write(
                data[0] + "," + data[1] + "," + str(balance) + "\n"
            )
        else:
            file.write(user)

    file.close()

    print("Balance added successfully.")
    print("Current balance:", balance)

    return balance


def withdraw(username, balance, users):
    amount = float(input("Enter amount to withdraw: "))

    if balance == 0:
        print("Add amount first / No balance")

    elif amount <= balance:
        balance = balance - amount

        file = open("user.txt", "w")

        for user in users:
            data = user.strip().split(",")

            if data[0] == username:
                file.write(
                    data[0] + "," + data[1] + "," + str(balance) + "\n"
                )
            else:
                file.write(user)

        file.close()

        print("Withdrawal successful.")
        print("Remaining balance:", balance)

    else:
        print("Insufficient balance.")

    return balance


def menu(username, balance, users):

    while True:
        print("\n1. Show detail")
        print("2. Add balance")
        print("3. Withdraw")
        print("4. Exit")

        option = int(input("Choose an option: "))

        if option == 1:
            show_detail(username, balance)

        elif option == 2:
            balance = add_balance(username, balance, users)

        elif option == 3:
            balance = withdraw(username, balance, users)

        elif option == 4:
            print("Thank you.")
            break

        else:
            print("Invalid option.")


# Main program

choice = input("Do you want to register or login? ")

if choice == "register":
    register()

elif choice == "login":
    login()

else:
    print("Invalid choice.")