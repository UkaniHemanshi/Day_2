Income = float(input("Enter your monthly income"))
Rent = float(input("Enter your rent"))
Groceries = float(input("enter your groceries expenses"))
Total_expenses = Rent+Groceries

Total_Saving = Income-Total_expenses
print("your saving are",Total_Saving)

Percentage_Saved=(Total_Saving/Income)*100

print(Percentage_Saved)

Percentage_Spent=(Total_expenses/Income)*100

print(Percentage_Spent)

