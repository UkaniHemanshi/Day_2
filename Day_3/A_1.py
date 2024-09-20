n = int(input("Enter the number you want add student details: "))
stu_tup = ()
stu_list = []
stu_avg_list = []
stu_avg_tup = ()

for i in range(n):
    name = input("Enter your name")
    age = int(input("Enter your age"))
    s1 = int(input("Enter your score1"))
    s2 = int(input("Enter your score2"))
    s3 = int(input("Enter your score3"))

    stu_list.append(stu_tup + (name,age,s1,s2,s3))

print(stu_list)


for stu_tuple in stu_list:
    name, age, s1, s2, s3 = stu_tuple

    avg = (s1 + s2 + s3)/3
    stu_avg_tup = name, age, s1, s2, s3, avg

    stu_avg_list.append(stu_avg_tup)

print(stu_avg_list)
highest_score = 0
topper = ""
for sta in stu_avg_list:
    name, age, s1, s2, s3, avg = sta
    if highest_score<avg:
        highest_score = avg
        topper = name
print(f"Name of the topper of the class {topper} and her/his avg is {highest_score} ")

min_score = int(input("Enter the minimum marks"))

for sta in stu_avg_list:
    name, age, s1, s2, s3, avg = sta
    if min_score<=avg:
       print(name)
