list_int = [10,-5,0,7,-3,4,-2]
result = map(lambda x: "Positive" if x > 0 else('negative' if x < 0 else "zero"), list_int)
print(list(result))