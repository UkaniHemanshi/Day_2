
choice = "y"
my_dict = {}
while(True):
    if choice == "y":
        item = input("Entr the item name")
        quantities = int(input("Entr the quantities "))
        prices = float(input("Entr the prices "))
        list = []
        list.append(quantities)
        list.append(prices)

        my_dict[item] = list

    print(my_dict)
    choice = input("Do you want to add more item y or n \n ")
    if choice == "n":
        break

#update
choice_update = input("which item you want to update: ")
for key in my_dict:
    if choice_update == key:
        l1 = my_dict[key]
        options = input("what you want to update price or quantity: ")
        if options == 'price':
            pr = float(input("Entr the new price "))
            l1[1] = pr
        elif options == 'quantity':
            qt = int(input("Entr the new quantity "))
            l1[0] = qt
        else:
            break

print(my_dict)

#total valu of inventory
for key in my_dict:
    l1 = my_dict[key]
    total_value = l1[0] * l1[1]
    print(f"The total value of {key} is {total_value}")


