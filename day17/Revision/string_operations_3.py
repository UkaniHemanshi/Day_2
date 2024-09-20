# days = int(input("Enter days in the month:"))
# week_day = int(input("Enter day of the week month begins 0 or 1:"))
#
# list = ['S',"M",'T',"W",'T',"F",'S']
#
# for i in list:
#     print(f"{i:<4}",end=" ")
# print()
#
# for i in range(1,days+1):
#     if i%len(list) == 0:
#         print(f"{i:<4}",end= " ")
#         print()
#     else:
#         print(f"{i:<4}",end=" ")

def calender(day,start_day):
    print("S\tM\tT\tW\tT\tF\tS")
    print("\t" * start_day,end="")
    for i in range(1,day+1):
        print(i, end='\t')
        if (i+start_day)%7==0:
            print()

calender(31,0)