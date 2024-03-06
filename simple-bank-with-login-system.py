wallet = 0

print("Create your account")
username = str(input("Username: "))
password = str(input("Password: "))
age = int(input("How old are you? "))

if age <= 18:
    print("You must be +18 years old!")
    username = str(input("Username: "))
    password = str(input("Password: "))
    age = int(input("How old are you? "))


print("Log In")
username_l = str(input("Username: "))
password_l = str(input("Password: "))

while True:
    if username_l == username and password_l == password:
        print("You're welcome! to our bank system!")
        menu = int(input("Select an option \n Wallet [1] \n Deposit[2] \n Pay [3] \n Exit [0] "))
        if menu == 1:
            print("You have $",wallet)
        elif menu == 2:
            deposit = int(input("Type the how much money do you wanna save: "))
            wallet = wallet + deposit
        elif menu == 3:
            pay = int(input("Type the value of the payment: "))
            if pay > wallet:
                print("You don't have money enough! try again another value: ")
                continue
            else:
                wallet = wallet - pay
        else:
            break
    else:
        print("Username or Password incorrect!")
        back = int(input("press 1 to try again: "))
        if back == 1:
            print("Log In")
            username_l = str(input("Username: "))
            password_l = str(input("Password: "))
