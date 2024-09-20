def check_int(num):
    if type(num) == "int":
        print(num)
    else:

try:
    check_int(input("Enter the number: "))
except ValueError:
    print(f'raised and caught exception: please enter correct integer value!!!')

