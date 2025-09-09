print("Welcome to Python ATM")

balance = 1000
pin = "1234"

entered_pin = input("Enter your PIN: ")

if entered_pin == pin:
    while True:
        print("\n____ATM Menu____")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            print("Your current balance is: Rs",balance)

        elif choice == "2":
            deposit = float(input("Enter amount to deposit: Rs"))
            balance += deposit
            print("Deposited successfully!",deposit)
            print("New balance: Rs",balance)

        elif choice == "3":
            withdraw = float(input("Enter amount to deposit: Rs"))
            if withdraw <= balance:
                balance -= withdraw
                print("Withdraw Successfully!")
                print("Remaining Balance: Rs",balance)
            else:
                print("Insufficient Balance!")

        elif choice == "4":
            print("Thank You for using Python ATM!")
            break

        else:
            print("Invalid choice! Please trt again.")
    else:
        print("Incorrect PIN! Access Denied")

        