list = [1,2,3,4,5,6,7,8,9,10]
final_list = [i**2 if i %2 == 0  else i**3 for i in list]
print(final_list)