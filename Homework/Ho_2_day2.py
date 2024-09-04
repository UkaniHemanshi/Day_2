num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

while (True):
    opt_choice = input("Enter operation choice: \n 1. Addition (+)\n 2. Subtraction (-)\n 3. Multiplication (*)\n 4. Division (/)\n 5. exit ? \n")

    match opt_choice:
        case "1":
            print(f"Your Addition of number {num1} + {num2} = {num1 + num2}")
        case "2":
            print(f"Your Subtraction of number {num1} - {num2} = {num1 - num2}")
        case "3":
            print(f"Your Multiplication of number {num1} * {num2} = {num1 * num2}")
        case "4":
            print(f"Your Division of number {num1} / { num2} = {num1 / num2}")
        case "5":
            print("Thank you! for using this calculator!")
            break
