balance = int(input("Enter your account balance:"))
remain = 0
choice = "yes"
while(True):
    if choice == "yes":
        amount = int(input("Enter the amount you want to withdraw:"))
        if amount > balance:
            print("Insufficient Balance")
        elif amount <= balance:
            if amount % 10 == 0:
                print("proceed")
                remain = balance - amount
                print(f"Withdrawl is successful and your remaining balance is {remain}")
            else:
                print(f"amount  entered is not a multiple of 10")
    choice = input("want to withdraw more yes or no")
    if choice == "no":
        break




