def sum_numbers(*args):
    print(type(args))
    for i in range(0,len(args)):
        print(args[i])
        if i>0:
            return sum(args)
print(sum_numbers(1,-1,2))
print(sum_numbers(1,2,3,4,5,6,7,8))