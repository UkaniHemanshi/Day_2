import numpy as np
array_id = np.arange(10)
print("1D array:",array_id)

print(f"3rd element:",array_id[2])
print(f"2nd element using negative indexing:",array_id[-2])
print(array_id[:5])
print(array_id[::2])
print(array_id[::-1])

arry2 = np.arange(10,22).reshape(3,4)
print("2D array is:\n",arry2)

print(f"Entire 1st row:",arry2[0,:])
print(f"Entire 1st column:",arry2[ :,1])
subarray = arry2[1::2,::2]
print(subarray)







