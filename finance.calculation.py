import math

# menu display to explain the options.

menu = """
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
"""
while menu:
    print(menu) # prints the menu for the customer.

# asking for a choice between investment and bond. All answers printed in low case.
    choice = input("Please enter investment or bond to proceed: ").lower()
    print(choice)

# this will ask the customer to restart the task if they enter anything 
# other than 'investment' or 'bond'
    if (choice != "investment") and (choice != "bond"):
        print("Please restart and enter a valid choice.")

    elif choice == "investment":

# p outputs the initial deposit amount.
# r outputs the interest rate and divides the input by 100.
# t outputs the number of years that the customer invests in.
# asks for the interest type; simple or compund
        P = int(input("Please enter the amount you are depositing: "))
        r = int(input("Please enter the interest percentage rate as whole number: ")) / 100
        t = int(input("Please enter the number of years you wish to invest: "))
        interest = input("Please enter the type of interest you would like to choose. Simple or Compound: ").lower()

# gives the appropriate calculation for simple interest in investment
        simple_interest = P *(1 + r*t)

# gives the appropriate calculation for simple interest in investment
        compound_interest = P * math.pow((1+r),t)

        if  interest == "simple":
            print(round(simple_interest))

        elif interest == "compound":
            print(round(compound_interest))

    elif choice == "bond":
# p outputs the value of the house 
# i outouts the interest rate that is divided by 100 and then by 12. 
# n outputs the number of repayment months.
        p = int(input("Please enter the value of your house: "))
        i = int(input("Please enter the interest percentage rate as whole number: ")) / 100 / 12
        n = int(input("Please enter the number of months you plan to repay your bond: "))

# calculates the monthly repayments and rounds the amount to get rid off the decimal.
        repayment = (i * p)/(1 - (1 + i)**(-n))
        repayment = round(repayment)
        print(f"Your repayment will be {repayment} per month.")

