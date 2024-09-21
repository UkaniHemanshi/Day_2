scores = input("Enter the scores:")
try :
    scores_list = [int(i) for i in scores.split(",")]
except ValueError as e:
    print("You have not entered proper string")
else:
    print(scores_list)
finally:
    print("end of program")
