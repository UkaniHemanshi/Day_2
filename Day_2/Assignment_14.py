val = input("Enter your values seprated by commas")
thres = int(input("Enter your values seprated by commas"))
tup = tuple(int(x) for x in val.split(","))
s_tup =sorted(tup, reverse=False)
print("Sorted values are:",sorted(tup, reverse=False))

for x in range(len(s_tup)):
    if  x >= thres:


    else: