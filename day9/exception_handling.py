# Exception handling : errors caused by wrong user interaction with the program are exeception 

# try and except block
# try: includes lines of that raises exceptions 
# try block is excute if no exception ,but if exception raises in try block then except block is executed instead 
#a try block can have a except block but multiple error specific  except block


try:
    b = int(input("Enter a number: "))
    print(a + 5)
except Exception as e:
    print(e)
    
# except ValueError:
#     print(" enter a valid integer.")
# except NameError:
#     print("a is not defined.")
# except:
#     print("Not value error or name error.")
