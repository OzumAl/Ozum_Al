# Below SafeBank app code assists the user to verify their username and password.
# It suggests some menu choices to complete tasks and returns the balance if needed. 

balance = 600
correct_password = 3455
correct_username = "Bankuser24"
not_logged_in = True

print("Welcome to Safebank")

def transfer_money(balance):
    acc_num = int(input("Please enter the account number: "))
    sort_cod = int(input("Please enter the sort code: "))
    transfer = int(input("How much would you like to transfer?: "))
    if transfer <= balance:
        print(f"\n *** Success! Your remaining balance is: {balance - transfer}***")
        return balance - transfer, True
    else:
        print("\n Sorry, you do not have enough funds in your account.")
        return balance, False

while not_logged_in:
    username = input("Please enter your username: ")
    password = int(input("Please enter your 4 digit password: "))

    if username == correct_username and password == correct_password:
        print(f"Hello {username}.To continue, please make a choice from the menu.")
        not_logged_in = False
    else:
        print("Your username or password is not correct. Please try again.")
 
while True:
    menu = int(input("""
1. Check Balance
2. Transfer Money
3. Withdraw Money
4. Exit
Enter your choice: """))
    

    if menu == 1:
        print(f"\n *** Your current balance is {balance}***")
    
    elif menu == 2:
        balance, success = transfer_money(balance)
        if not success:
            print("We cannot complete your request. Your account does not have enough funds.")

    elif menu == 3:
        withdraw = int(input("Please enter the amount you wish to withdraw: "))
        print(f"You are about to withdraw £{withdraw}")
        confirm_pin = int(input("Please confirm your password: "))
        if confirm_pin == correct_password and withdraw <= balance:
            print("The task is complete")
            balance -= withdraw
        elif confirm_pin != correct_password:
            print("You entered an invalid password.")
        elif withdraw > balance:
            print("We cannot complete your request. Your account does not have enough funds.")
    

    elif menu == 4:
        print("Thank you for using Safebank. Goodbye!")
        break

    else:
        print("Invalid choice. Please choose again.")
    

       
       
    