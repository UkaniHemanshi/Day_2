file_1 = 'file.txt'
file_2 = 'report.txt'

list1 = []
with open(file_1,'r') as file1:
    for line in file1:
        list1.append(line)
list2 = []
with open(file_2,'r') as file2:
    for line in file2:
        list2.append(line)
merge_list = []
merge_list = list1+list2
print(f'Without duplicate line of list: {set(merge_list)}')

with open('merged_unique','w') as file:
    for i in set(merge_list):
        file.writelines(i)