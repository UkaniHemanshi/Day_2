stu_name = input("Enter your name: ")

sc_hw = float(input("Enter your score in homework: "))
sc_quizz = float(input("Enter your score in quizz: "))
sc_midterm = float(input("Enter your score in midterm: "))
sc_finalex = float(input("Enter your score in final exam:"))

final_grade = ((sc_hw/100)*20 + (sc_quizz/100)*20 + (sc_midterm/100)*30 + (sc_finalex/100)*30) / 100
final_ptr = round(final_grade*100,2)
print("\n")
print(f"Student name is {stu_name}")
print(f"Final grade is {final_ptr} %")

if final_ptr >= 90:
    print(f"Your grade is A for {final_ptr} %")
elif final_ptr >= 70 and final_ptr < 90:
    print(f"Your grade is B for {final_ptr} %")
elif final_ptr >= 60 and final_ptr < 70:
    print(f"Your grade is C for {final_ptr} %")
elif final_ptr >= 50 and final_ptr < 60:
    print(f"Your grade is D for {final_ptr} %")
elif final_ptr <50:
    print(f"Your grade is F for {final_ptr} %")
