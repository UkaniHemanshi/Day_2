PAN = input("Enter your PAN: ")
count = 0

if len(PAN) == 10:
   first_five = PAN[:5]
   next_four = PAN[5:9]
   last_char = PAN[-1]
   if first_five.isupper():
       count += 1
   if next_four.isdigit():
       count += 1
   if last_char.isupper():
       count +=1


if count == 3:
    print("Your PAN is valid !!")
else:
    print("Invalid !!!")