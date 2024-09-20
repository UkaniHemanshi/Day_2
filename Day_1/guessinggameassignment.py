x=5
y=1
while y<=10:
  num=int(input("Enter the correct number"))
  if num==x:
      print("wow correct")
      break
  else:
   y+=1
   print("try again")
print("you lost")