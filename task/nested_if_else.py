# Driving License Eligibility

age = int(input("Enter your age: "))

if age < 16:
    print("You are not eligible to drive.")

    choice = input("Do you want to get a driving license? (y/n): ")

    if choice == "y":
        print("You can apply for a driving license when you turn 16.")
    elif choice == "n":
        print("Okay, you don't want to get a driving license.")
    else:
        print("Invalid choice.")

else:
    print("You are eligible to drive.")

    license = input("Do you have a driving license? (y/n): ")

    if license == "y":
        print("You can drive legally.")
    elif license == "n":
        choice = input("Do you want to get a driving license? (y/n): ")

        if choice == "y":
            print("You can apply for a driving license.")
        elif choice == "n":
            print("Okay, you don't want to get a driving license.")
        else:
                print("Invalid choice.")
    else:
        print("invalid choice!")