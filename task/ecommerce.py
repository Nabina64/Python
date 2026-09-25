users = [
    {
        "username": "nabina",
        "password": "123",
        "usertype": "buyer"
    },
    {
        "username": "bilisha",
        "password": "456",
        "usertype": "seller"
    }
]


products = [
    {
        "name": "Laptop",
        "price": 80000,
        "seller_name": "sita"
    },
    {
        "name": "Phone",
        "price": 30000,
        "seller_name": "sita"
    }
]


username = input("Enter username: ")
password = input("Enter password: ")

login_success = False

for user in users:

    if user["username"] == username and user["password"] == password:

        login_success = True
        usertype = user["usertype"]
        break


if login_success:

    print("Login successful!")

    while True:

        if usertype == "buyer":

            print("\n1. View Products")
            print("2. Buy Product")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":

                for product in products:

                    print("Name:", product["name"])
                    print("Price:", product["price"])
                    print("Seller:", product["seller_name"])
                    print("--------------------")


            elif choice == "2":

                product_name = input("Enter product name: ")

                product_found = False

                for product in products:

                    if product["name"].lower() == product_name.lower():

                        print("Product found!")
                        print("Name:", product["name"])
                        print("Price:", product["price"])

                        quantity = int(input("Enter quantity: "))

                        total = product["price"] * quantity

                        print("Total price:", total)

                        product_found = True
                        break

                if not product_found:

                    print("Product not found.")


            elif choice == "3":

                print("Thank you!")
                break


            else:

                print("Invalid choice.")


        elif usertype == "seller":

            print("\n1. View My Products")
            print("2. Add Product")
            print("3. Exit")

            choice = input("Enter your choice: ")


            if choice == "1":

                product_found = False

                for product in products:

                    if product["seller_name"] == username:

                        print("Name:", product["name"])
                        print("Price:", product["price"])
                        print("--------------------")

                        product_found = True

                if not product_found:

                    print("You have no products.")


            elif choice == "2":

                product_name = input("Enter product name: ")
                product_price = float(input("Enter product price: "))

                new_product = {
                    "name": product_name,
                    "price": product_price,
                    "seller_name": username
                }

                products.append(new_product)

                print("Product added successfully.")


            elif choice == "3":

                print("Thank you!")
                break


            else:

                print("Invalid choice.")


else:

    print("Invalid username or password.")