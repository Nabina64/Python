# file_handling: creation,editing,write,read of file progranatically

# open a file
# f = open('file.path', 'mode')

# close file
# f.close()

# read a file
f = open('C:\\Users\\acer\\OneDrive\\Desktop\\java\\file1.txt', 'r')
a = f.read()
print(a)
f.close()

# write a file:existing data is replaced by new data, if file in the path does not exist then a file is created

# f = open('C:\\Users\\acer\\OneDrive\\Desktop\\java\\file1.txt', 'w')   
# a = f.write("This is a new line.\n")
# print(a)
# f.close()

# append:new data is added to the existing data, if file in the path does not exist then a file is created
# f = open('C:\\Users\\acer\\OneDrive\\Desktop\\java\\file1.txt', 'a')
# f.write("This is an appended line.\n")
# f.close()


# 'r+'   ---> read and write
# 'w+'  ---> write and read
# 'a+'  ---> append and read


# todo:

# ask user register or login
# if register: get username and save it in a file
# if login: get a username from user
# check if the entered username exist in the list of usernames
# if yes: print user exist
# if no: print user doesnot exist

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