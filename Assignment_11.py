val = input("Enter your values")

tuple_list = tuple(int(x) for x in val.split(","))

print(tuple_list)