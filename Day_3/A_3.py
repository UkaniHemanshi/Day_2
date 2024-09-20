para = input("Enter a paragraph of text")
list_final = []

list_of_word = list(x for x in para.split(" "))
for word in list_of_word:
    for x in word:
        list_final.append(x)

set1 = set(list_final)
f_set = sorted(set1)
print(f_set)


num =