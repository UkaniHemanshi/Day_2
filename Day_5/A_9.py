def res_file(filename,data):
    with open(filename,'a') as file:
        file.write(data)
    print(f"Data append success")

res_file("report.txt","Hello")