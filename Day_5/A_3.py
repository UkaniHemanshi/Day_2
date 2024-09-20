result_sum= 0
def add_1(*args):
    global result_sum
    print(f"Before modification: {result_sum}")

    result_sum = sum(args)
    print(f"After modification: {result_sum}")

print(f'Before calling fumction: {result_sum}')
add_1(1,2,3,4,5)
print(f'After calling fumction: {result_sum}')
