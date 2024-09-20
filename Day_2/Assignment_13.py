val = input("Enter your values seprated by commas")

tup = tuple(int(x) for x in val.split(","))

print("Sum of the values is:",sum(tup))
print("Average of the values is:",sum(tup)/len(tup))
print(f"Max and Min of the values is: {max(tup)} and {min(tup)}")
print("Number of elemets are:",len(tup))
