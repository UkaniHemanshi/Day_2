list= []

choice = "yes"
while(True):
    if choice == "yes":
        operation = int(input("Enter your choice:\n 1:Add\n 2:remove\n 3:view\n 4:Exit\n"))
        if operation==1:
            value=int(input("Enter your value"))
            list.append(value)
        elif operation==2:
            index = int(input("Enter your index you want to delete"))
            del list[index]
        elif operation==3:
            print(list)
        elif operation==4:
            break
    print(list)
    choice = input("want to perform another action yes or no")
    if choice == "no":
        break


