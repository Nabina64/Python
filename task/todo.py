# todo:
# create a list of usernames
# get a username from user
# check if the entered username exist in the list of usernames

# create a dictionary of userdetails with username as key and password as value  {'ram':10000, 'dia':20000}
# create a dictionary of userbalance with username as key and initial balance as value
# get username and password from user
# check if the entered username exists in the dictioanry userdetails and the entered password matches the value of that username
# if no: print a statement
# if yes: print Login success
#     and show 3 option: 1. Show detail 2. Add balance 3. Withdraw
#     if choice is 1: print the userbalance of that user
#     if choice is 2: get amount from user and add it to the initial balance 
#     if choice is 3: get amount from user then if the amount is less than iinitial balance subtract the amount from initial balance and if amount is more than initial balance print a statement



usernames = ["rita", "bina", "sita"]

userdetails = {
    "rita": "1234",
    "bina": "5678",
    "sita": "9999"
}

userbalance = {
    "rita": 10000,
    "bina": 20000,
    "sita": 15000
}

username = input("Enter username: ")
password = input("Enter password: ")

if username in userdetails and password == userdetails[username]:
    print("Login success")

    print("1. Show detail")
    print("2. Add balance")
    print("3. Withdraw")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        print("Your balance is:", userbalance[username])

    elif choice == 2:
        amount = int(input("Enter amount to add: "))
        userbalance[username] = userbalance[username] + amount
        print("Balance added successfully")
        print("Your new balance is:", userbalance[username])

    elif choice == 3:
        amount = int(input("Enter amount to withdraw: "))

        if amount <= userbalance[username]:
            userbalance[username] = userbalance[username] - amount
            print("Withdrawal successful")
            print("Your remaining balance is:", userbalance[username])
        else:
            print("Insufficient balance")

    else:
        print("Invalid choice")

else:
    print("Invalid username or password")