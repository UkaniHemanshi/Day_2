age = int(input("Enter your age"))

if age<5:
    print("you go free today")
elif age>=5 and age<=12:
    print("you are being charged 5rupees")
elif age >= 13 and age <= 60:
    print("you are being charged 10rupees")
elif age>60:
    print("you are being charged 7rupees")
