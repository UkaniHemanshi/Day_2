keyword = "NM"
with open("report.txt","r") as file:
    line = file.readlines()
    print(type(line))
    for i in line:
        list_ofword = [i for i in i.split(" ")]
        for i in range(len(list_ofword)):
            if list_ofword[i] == "name":
                list_ofword[i] = keyword
        print(list_ofword)
    result_list =  " ".join(list_ofword)
with open("report.txt","w") as file:
    file.write(result_list)


