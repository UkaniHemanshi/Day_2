list = [1,1,2,'hello',3,2,2]
dict = {}
for i in range(len(list)):
      value_i = list.count(list[i])
      dict[list[i]] = value_i
print(f"dictionary with frequency of each element is: {dict}")


#without built in fuction
# count= 0
# check_list = []
# for i in range(len(list)):
#     if list[i] not in check_list:
#         count = 0
#         for j in range((i+1),len(list)):
#             if list[j] == list[i]:
#                 count = count + 1
#                 print(list[i])
#                 print(count)
#         dict[list[i]] = count
#         check_list.append(list[i])
# print(dict)


