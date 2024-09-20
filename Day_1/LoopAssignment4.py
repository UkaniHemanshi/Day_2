num = int(input("Enter the number"))
fact=1
if num==0:
    print("factorial is: 1")
while num>=1:
    fact = fact * num
    num -= 1
print("factorial of num is",fact)