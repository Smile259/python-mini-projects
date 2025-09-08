correct_password = "admin123"
attempts = 3

while attempts > 0:
    user_password = input("Enter Password:")

    if user_password == correct_password:
        print("Access Granted")
        break
    
    else:
        attempts -= 1
        if attempts > 0:
            print(f"Wrong Password {attempts} attempts left.")
        else:
            print("Access Denied! No Attempts left.")