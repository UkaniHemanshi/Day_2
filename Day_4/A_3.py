my_dict = {'India':'NewDelhi','USA':'Washington DC','UK':'London','Australia':'Melbourne','Germany':'Berlin'}
choice = 'yes'
score = 0
while(True):
    if choice == 'yes':
        question =int(input("Which question you want to attempt\n 1. What is the capital of India ? \n 2. What is the capital of USA ? \n "
              "3. What is the capital of UK ? \n 4. What is the capital of Australia ? \n 5. What is the capital of Germany ? \n"))

        for i 




        if question==1:
            ans = input(f"Enter your answer for 'India' :")
            if my_dict['India'] == ans:
                print('your answer is right')
                score = score + 1
            else:
                print("your answer is wrong")
        elif question==2:
            ans = input(f"Enter your answer for 'USA' :")
            if my_dict['USA'] == ans:
                print('your answer is right')
                score = score + 1
            else:
                print("your answer is wrong")

        elif question==3:
            ans = input(f"Enter your answer for 'UK' :")
            if my_dict['UK'] == ans:
                print('your answer is right')
                score = score + 1
            else:
                print("your answer is wrong")
        elif question==4:
            ans = input(f"Enter your answer for 'Australia' :")
            if my_dict['Australia'] == ans:
                print('your answer is right')
                score = score + 1
            else:
                print("your answer is wrong")
        elif question==5:
            ans = input(f"Enter your answer for 'Germany' :")
            if my_dict['Germany'] == ans:
                print('your answer is right')
                score = score + 1
            else:
                print("your answer is wrong")
    choice = input("want to attempt more yes or no")
    if choice == "no":
        break
print(f"Well Played your score is: {score}")