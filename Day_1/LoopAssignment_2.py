password = input("Enter a password")
str='!@#$'
criteria=0

if len(password)>=8:
    criteria += 1
    print(len(password))

for char in password:
  print(char)
  if char.isupper() and char.islower():
    criteria += 1
  elif char in str:
    criteria += 1

if password.isdigit():
    criteria += 1
    print(password.isdigit())


if criteria==1:
    print("your password is weak")
elif criteria==2 or criteria==3:
    print("your password is moderate")
elif criteria==4:
    print("your password is very strong wow!")
else:
    print("your pwd is too short ")


