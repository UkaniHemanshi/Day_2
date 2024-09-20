list_of_tuple = [('mayura',30),("Pravin",25),("Reeya",35)]
age_list = []
for i in range(len(list_of_tuple)):
    age_list.append(list_of_tuple[i][1])

print(age_list)


sorted_age_list = sorted(age_list, key=lambda x: x)
print(sorted_age_list)
