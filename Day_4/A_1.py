num = int(input("Enter the number you want:"))
list_tup = []
tup = ()
my_dict = {}

for i in range(0,num):
    key_i = input("Enter a key:")
    val_i = int(input("Enter a value:"))
    tup = (key_i,val_i)
    list_tup.append(tup)
print(list_tup)

for tup_1 in list_tup:
    key_i, val_i = tup_1
    my_dict[key_i] = val_i
print(my_dict)





