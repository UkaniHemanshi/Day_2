str = input("Enter a string with commas: ")

tup_list1 = tuple(int(i) for i in str.split(","))

spec_itm = input("Enter the element you want to repeat: ")
spec_itm1  = tuple(int(j) for j in spec_itm.split(","))

spec_time = int(input("Enter the time you want to repeat: "))

tup_list2 = tup_list1 + tuple((spec_itm1)*spec_time)

print(f"Your original tuple is {tup_list1}\nYour new tuple is {tup_list2}")



