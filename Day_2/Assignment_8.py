num = int(input("Enter a positive integer"))
list = []
def prime(num):
    if num>1:
        for i in range(2,num+1):
            if num % i == 0:
              list.append(i)
            else:
                continue

prime(num)
print(list)