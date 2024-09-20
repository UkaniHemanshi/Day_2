val_1 = input("Enter your values seprated by commas")
val_2 = input("Enter your values seprated by commas")

tup_1 = tuple(int(x) for x in val_1.split(","))
tup_2 = tuple(int(x) for x in val_2.split(","))

set_1 = set(tup_1)
set_2 = set(tup_2)

inter_set = set_1.intersection(set_2)
final_tup = tuple(inter_set)
print(final_tup)